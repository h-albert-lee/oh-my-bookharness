from __future__ import annotations

from fastapi import APIRouter, Request

from bookharness_api.schemas import ApprovalRequest, ChapterCreateRequest, RunMVPRequest, RunStageRequest

router = APIRouter(prefix="/api/chapters", tags=["chapters"])


@router.post("")
def create_chapter(payload: ChapterCreateRequest, request: Request):
    return request.app.state.chapter_service.create_chapter(
        payload.chapter_id,
        payload.title,
        payload.dependencies,
        payload.actor,
    )


@router.get("/{chapter_id}")
def get_chapter_detail(chapter_id: str, request: Request):
    return request.app.state.project_service.chapter_detail(chapter_id)


@router.get("/{chapter_id}/artifacts")
def get_chapter_artifacts(chapter_id: str, request: Request):
    return request.app.state.artifact_service.list_chapter_artifacts(chapter_id)


@router.post("/{chapter_id}/run-stage")
def run_stage(chapter_id: str, payload: RunStageRequest, request: Request):
    return request.app.state.chapter_service.queue_stage(chapter_id, payload.stage, payload.actor)


@router.post("/{chapter_id}/run-mvp")
def run_mvp(chapter_id: str, payload: RunMVPRequest, request: Request):
    return request.app.state.chapter_service.queue_mvp(chapter_id, payload.title, payload.dependencies, payload.actor)


@router.post("/{chapter_id}/approve")
def approve(chapter_id: str, payload: ApprovalRequest, request: Request):
    return request.app.state.chapter_service.queue_approval(
        chapter_id,
        payload.approval_key,
        payload.result,
        payload.notes,
        payload.actor,
    )
