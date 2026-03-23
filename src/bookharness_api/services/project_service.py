from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bookharness.memory.loader import MemoryLoader
from bookharness.orchestrator.state_manager import StateManager
from bookharness.utils.io import read_text
from bookharness.utils.yaml_utils import load_yaml
from bookharness_api.services.artifact_service import ArtifactService
from bookharness_api.services.audit_service import AuditService
from bookharness_api.services.metadata_index import MetadataIndex


class ProjectService:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.loader = MemoryLoader(root)
        self.state_manager = StateManager(root)
        self.index = MetadataIndex(root)
        self.artifacts = ArtifactService(root)
        self.audit = AuditService(root)

    def project_summary(self) -> dict[str, Any]:
        self.index.sync_all()
        context = self.loader.load_project_context()
        chapters = [self._normalize_chapter(row) for row in self.index.list_chapters()]
        pending = self.pending_approvals()
        recent_runs = self.index.list_runs(limit=10)
        blueprint = context["blueprint"]
        first_nonempty = next((line.strip("# ").strip() for line in blueprint.splitlines() if line.strip()), "Untitled Project")
        return {
            "title": first_nonempty,
            "blueprint_preview": "\n".join(blueprint.splitlines()[:8]),
            "chapters": chapters,
            "pending_approvals": pending,
            "recent_runs": recent_runs,
            "metrics": {
                "chapter_count": len(chapters),
                "approved_count": len([chapter for chapter in chapters if chapter["approved"]]),
                "pending_approval_count": len(pending),
                "recent_run_count": len(recent_runs),
            },
        }

    def list_chapters(self) -> list[dict[str, Any]]:
        return [self._normalize_chapter(row) for row in self.index.list_chapters()]

    def chapter_detail(self, chapter_id: str) -> dict[str, Any]:
        self.index.sync_all()
        state = self.state_manager.load(chapter_id)
        approvals = load_yaml(self.root / "workflow/approvals/approvals.yaml") or {}
        review_reports = []
        for report_name in state.review_reports:
            report_path = self.root / f"manuscript/{chapter_id}/{report_name}"
            if report_path.exists():
                review_reports.append({
                    "path": str(report_path.relative_to(self.root)),
                    "content": read_text(report_path),
                })
        return {
            "state": state.to_dict(),
            "artifacts": self.artifacts.list_chapter_artifacts(chapter_id),
            "approvals": approvals.get(chapter_id, {}),
            "review_reports": review_reports,
            "runs": [run for run in self.index.list_runs(limit=50) if run.get("chapter_id") == chapter_id],
            "audit": [item for item in self.audit.recent(limit=50) if item.get("details", {}).get("chapter_id") == chapter_id],
        }

    def pending_approvals(self) -> list[dict[str, Any]]:
        rows = self.index.list_pending_approvals()
        pending = []
        for row in rows:
            pending.append({
                "chapter_id": row["chapter_id"],
                "title": row["title"],
                "status": row["status"],
                "approval_key": self._expected_approval_key(row["status"]),
                "existing_result": row.get("result"),
                "notes": json.loads(row.get("notes_json") or "[]"),
            })
        return pending

    @staticmethod
    def _expected_approval_key(status: str) -> str:
        if status == "awaiting_human_outline_approval":
            return "approval_a"
        return "approval_b"

    @staticmethod
    def _normalize_chapter(row: dict[str, Any]) -> dict[str, Any]:
        return {
            "chapter_id": row["chapter_id"],
            "title": row["title"],
            "status": row["status"],
            "current_stage": row["current_stage"],
            "approved": bool(row["approved"]),
            "latest_draft": row["latest_draft"],
            "source_pack_ready": bool(row["source_pack_ready"]),
            "outline_ready": bool(row["outline_ready"]),
        }
