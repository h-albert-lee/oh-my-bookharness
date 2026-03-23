from __future__ import annotations

from pathlib import Path

from bookharness.orchestrator.runner import WorkflowRunner
from bookharness_api.services.audit_service import AuditService
from bookharness_api.services.job_service import JobService
from bookharness_api.services.metadata_index import MetadataIndex


class ChapterService:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.runner = WorkflowRunner(root)
        self.audit = AuditService(root)
        self.jobs = JobService(root)
        self.index = MetadataIndex(root)

    def create_chapter(self, chapter_id: str, title: str, dependencies: list[str], actor: str) -> dict:
        state = self.runner.initialize_chapter(chapter_id, title, dependencies)
        self.audit.record(
            "chapter_initialized",
            actor,
            {"chapter_id": chapter_id, "title": title, "dependencies": dependencies},
        )
        self.index.sync_all()
        return state.to_dict()

    def queue_stage(self, chapter_id: str, stage: str, actor: str) -> dict:
        self.audit.record("stage_requested", actor, {"chapter_id": chapter_id, "stage": stage})
        return self.jobs.queue_stage(chapter_id, stage, actor)

    def queue_mvp(self, chapter_id: str, title: str, dependencies: list[str], actor: str) -> dict:
        self.audit.record(
            "mvp_requested",
            actor,
            {"chapter_id": chapter_id, "title": title, "dependencies": dependencies},
        )
        return self.jobs.queue_mvp(chapter_id, title, dependencies, actor)

    def queue_approval(self, chapter_id: str, approval_key: str, result: str, notes: list[str], actor: str) -> dict:
        self.audit.record(
            "approval_requested",
            actor,
            {"chapter_id": chapter_id, "approval_key": approval_key, "result": result, "notes": notes},
        )
        return self.jobs.queue_approval(chapter_id, approval_key, result, notes, actor)
