from __future__ import annotations

from fastapi import APIRouter, Request

router = APIRouter(prefix="/api/runs", tags=["runs"])


@router.get("")
def list_runs(request: Request):
    return request.app.state.job_service.list_jobs(limit=50)


@router.get("/{job_id}")
def get_run(job_id: str, request: Request):
    return request.app.state.job_service.get_job(job_id)
