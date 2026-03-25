from __future__ import annotations

import threading
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable

from bookharness.orchestrator.runner import ApprovalRequiredError, WorkflowRunner
from bookharness.utils.io import read_json, write_json
from bookharness_api.services.audit_service import AuditService
from bookharness_api.services.helpers import utc_now
from bookharness_api.services.metadata_index import MetadataIndex


class JobService:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.runner = WorkflowRunner(root)
        self.audit = AuditService(root)
        self.index = MetadataIndex(root)
        self.executor = ThreadPoolExecutor(max_workers=4)
        self._lock = threading.Lock()
        self._chapter_locks: dict[str, threading.Lock] = {}
        self._chapter_locks_guard = threading.Lock()

    def _get_chapter_lock(self, chapter_id: str) -> threading.Lock:
        """Get or create a per-chapter lock to prevent concurrent operations."""
        with self._chapter_locks_guard:
            if chapter_id not in self._chapter_locks:
                self._chapter_locks[chapter_id] = threading.Lock()
            return self._chapter_locks[chapter_id]

    def create_job(self, chapter_id: str, job_type: str, actor: str, payload: dict[str, Any]) -> dict[str, Any]:
        job = {
            "job_id": uuid.uuid4().hex,
            "chapter_id": chapter_id,
            "job_type": job_type,
            "status": "queued",
            "actor": actor,
            "payload": payload,
            "created_at": utc_now(),
            "started_at": None,
            "finished_at": None,
            "error": None,
            "log": [f"Queued {job_type}"],
        }
        self._write_job(job)
        self.audit.record("job_queued", actor, {"job_id": job["job_id"], "chapter_id": chapter_id, "job_type": job_type})
        return job

    def queue_stage(self, chapter_id: str, stage: str, actor: str) -> dict[str, Any]:
        job = self.create_job(chapter_id, "run_stage", actor, {"stage": stage})
        self.executor.submit(self._execute_job, job["job_id"], lambda: self.runner.run_stage(chapter_id, stage))
        return job

    def queue_mvp(self, chapter_id: str, title: str, dependencies: list[str], actor: str) -> dict[str, Any]:
        job = self.create_job(chapter_id, "run_mvp", actor, {"title": title, "dependencies": dependencies})
        self.executor.submit(self._execute_job, job["job_id"], lambda: self.runner.run_mvp(chapter_id, title, dependencies))
        return job

    def queue_approval(self, chapter_id: str, approval_key: str, result: str, notes: list[str], actor: str) -> dict[str, Any]:
        job = self.create_job(chapter_id, "approve", actor, {"approval_key": approval_key, "result": result, "notes": notes})
        self.executor.submit(
            self._execute_job,
            job["job_id"],
            lambda: self.runner.approve(chapter_id, approval_key, result, notes),
        )
        return job

    def _execute_job(self, job_id: str, operation: Callable[[], Any]) -> None:
        with self._lock:
            job = self.get_job(job_id)
            chapter_id = job.get("chapter_id", "")

        chapter_lock = self._get_chapter_lock(chapter_id)
        if not chapter_lock.acquire(blocking=False):
            # Another job is already running for this chapter
            with self._lock:
                job = self.get_job(job_id)
                job["status"] = "failed"
                job["finished_at"] = utc_now()
                job["error"] = f"Chapter {chapter_id} already has a running job. Wait for it to finish."
                job["log"].append(job["error"])
                self._write_job(job)
                self.audit.record("job_failed", job["actor"], {"job_id": job_id, "chapter_id": chapter_id, "error": job["error"]})
            return

        try:
            with self._lock:
                job = self.get_job(job_id)
                job["status"] = "running"
                job["started_at"] = utc_now()
                job["log"].append("Started execution")
                self._write_job(job)
            result = operation()
            with self._lock:
                job = self.get_job(job_id)
                job["status"] = "waiting_for_approval" if getattr(result, "status", "") in {
                    "awaiting_human_outline_approval",
                    "awaiting_human_draft_approval",
                } else "succeeded"
                job["finished_at"] = utc_now()
                job["log"].append(f"Completed with state {getattr(result, 'status', 'n/a')}")
                self._write_job(job)
                self.audit.record(
                    "job_completed",
                    job["actor"],
                    {"job_id": job_id, "chapter_id": job["chapter_id"], "status": job["status"]},
                )
                if job["job_type"] == "approve" and job["payload"].get("approval_key") == "approval_b" and job["payload"].get("result") in {"approved", "approved_with_notes"}:
                    self.audit.record(
                        "final_candidate_generated",
                        job["actor"],
                        {"chapter_id": job["chapter_id"], "job_id": job_id},
                    )
                self.index.sync_all()
        except ApprovalRequiredError as exc:
            with self._lock:
                job = self.get_job(job_id)
                job["status"] = "waiting_for_approval"
                job["finished_at"] = utc_now()
                job["log"].append(str(exc))
                self._write_job(job)
                self.audit.record(
                    "job_waiting_for_approval",
                    job["actor"],
                    {"job_id": job_id, "chapter_id": job["chapter_id"], "reason": str(exc)},
                )
                self.index.sync_all()
        except Exception as exc:  # pragma: no cover - defensive branch
            with self._lock:
                job = self.get_job(job_id)
                job["status"] = "failed"
                job["finished_at"] = utc_now()
                job["error"] = str(exc)
                job["log"].append(str(exc))
                self._write_job(job)
                self.audit.record(
                    "job_failed",
                    job["actor"],
                    {"job_id": job_id, "chapter_id": job["chapter_id"], "error": str(exc)},
                )
                self.index.sync_all()
        finally:
            chapter_lock.release()

    def get_job(self, job_id: str) -> dict[str, Any]:
        path = self.root / f"workflow/runs/{job_id}.json"
        if not path.exists():
            return {}
        return read_json(path)

    def list_jobs(self, limit: int = 20) -> list[dict[str, Any]]:
        self.index.sync_runs()
        runs_dir = self.root / "workflow/runs"
        jobs = [read_json(path) for path in sorted(runs_dir.glob("*.json"), reverse=True) if path.exists()]
        jobs.sort(key=lambda item: item.get("created_at", ""), reverse=True)
        return jobs[:limit]

    def _write_job(self, payload: dict[str, Any]) -> None:
        write_json(self.root / f"workflow/runs/{payload['job_id']}.json", payload)
