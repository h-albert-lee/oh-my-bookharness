from __future__ import annotations

from fastapi import APIRouter, Request

router = APIRouter(prefix="/api/approvals", tags=["approvals"])


@router.get("/pending")
def pending_approvals(request: Request):
    return request.app.state.project_service.pending_approvals()


@router.get("/{chapter_id}")
def chapter_approvals(chapter_id: str, request: Request):
    detail = request.app.state.project_service.chapter_detail(chapter_id)
    return detail["approvals"]
