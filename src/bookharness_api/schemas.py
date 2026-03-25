from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ChapterCreateRequest(BaseModel):
    chapter_id: str
    title: str
    dependencies: list[str] = Field(default_factory=list)
    actor: str = "api"


class RunStageRequest(BaseModel):
    stage: str
    actor: str = "api"


class RunMVPRequest(BaseModel):
    title: str
    dependencies: list[str] = Field(default_factory=list)
    actor: str = "api"


class ApprovalRequest(BaseModel):
    approval_key: Literal["approval_a", "approval_b"]
    result: Literal["approved", "approved_with_notes", "revision_requested", "rejected"]
    notes: list[str] = Field(default_factory=list)
    actor: str = "api"


class ArtifactSaveRequest(BaseModel):
    path: str
    content: str
    actor: str = "ui-editor"


class JobResponse(BaseModel):
    job_id: str
    chapter_id: str
    job_type: str
    status: str
    actor: str
    created_at: str
    started_at: str | None = None
    finished_at: str | None = None
    error: str | None = None
    log: list[str] = Field(default_factory=list)


class ArtifactResponse(BaseModel):
    path: str
    kind: str
    content: str
    rendered_html: str | None = None
    modified_at: str


class DiffResponse(BaseModel):
    left_path: str
    right_path: str
    left_only: list[str]
    right_only: list[str]
    changed: list[dict[str, Any]]


class ChapterSummaryResponse(BaseModel):
    chapter_id: str
    title: str
    status: str
    current_stage: str
    approved: bool
    latest_draft: str | None = None
    source_pack_ready: bool = False
    outline_ready: bool = False


class ProjectSummaryResponse(BaseModel):
    title: str
    blueprint_preview: str
    chapters: list[ChapterSummaryResponse]
    pending_approvals: list[dict[str, Any]]
    recent_runs: list[dict[str, Any]]
    metrics: dict[str, int]
