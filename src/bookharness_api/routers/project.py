from __future__ import annotations

from fastapi import APIRouter, Request

from bookharness_api.schemas import ProjectSummaryResponse

router = APIRouter(prefix="/api/project", tags=["project"])


@router.get("", response_model=ProjectSummaryResponse)
def get_project_summary(request: Request):
    return request.app.state.project_service.project_summary()


@router.get("/chapters")
def get_chapters(request: Request):
    return request.app.state.project_service.list_chapters()
