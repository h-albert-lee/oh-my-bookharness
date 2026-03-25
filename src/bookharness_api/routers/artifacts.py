from __future__ import annotations

from fastapi import APIRouter, Query, Request

from bookharness_api.schemas import ArtifactResponse, ArtifactSaveRequest, DiffResponse

router = APIRouter(prefix="/api/artifacts", tags=["artifacts"])


@router.get("", response_model=ArtifactResponse)
def get_artifact(path: str = Query(...), request: Request = None):
    return request.app.state.artifact_service.read_artifact(path)


@router.put("", response_model=ArtifactResponse)
def save_artifact(body: ArtifactSaveRequest, request: Request = None):
    return request.app.state.artifact_service.save_artifact(body.path, body.content)


@router.get("/diff", response_model=DiffResponse)
def get_diff(left: str = Query(...), right: str = Query(...), request: Request = None):
    return request.app.state.artifact_service.diff(left, right)
