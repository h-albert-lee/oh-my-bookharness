from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass(slots=True)
class ChapterState:
    chapter_id: str
    title: str
    status: str = "not_started"
    current_stage: str = "chapter_initialization"
    approved: bool = False
    source_pack_ready: bool = False
    outline_ready: bool = False
    draft_versions: list[str] = field(default_factory=list)
    latest_draft: str | None = None
    review_reports: list[str] = field(default_factory=list)
    revision_plan: str | None = None
    human_feedback: list[dict[str, Any]] = field(default_factory=list)
    gate_passed: bool | None = None
    gate_details: dict[str, Any] | None = None
    open_issues: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    artifacts: dict[str, str] = field(default_factory=dict)
    last_updated: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["last_updated"] = utc_now()
        return payload

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ChapterState":
        import dataclasses

        valid_fields = {f.name for f in dataclasses.fields(cls)}
        filtered = {k: v for k, v in payload.items() if k in valid_fields}
        return cls(**filtered)
