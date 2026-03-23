from __future__ import annotations

from fastapi import APIRouter, Query, Request

from bookharness_api.schemas import ArtifactResponse, DiffResponse

router = APIRouter(prefix="/api/artifacts", tags=["artifacts"])


@router.get("", response_model=ArtifactResponse)
def get_artifact(path: str = Query(...), request: Request = None):
    return request.app.state.artifact_service.read_artifact(path)


@router.get("/diff", response_model=DiffResponse)
def get_diff(left: str = Query(...), right: str = Query(...), request: Request = None):
    return request.app.state.artifact_service.diff(left, right)
