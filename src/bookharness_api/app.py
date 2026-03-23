from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from bookharness.cli import scaffold_project
from bookharness_api.routers import approvals, artifacts, chapters, project, runs
from bookharness_api.services.artifact_service import ArtifactService
from bookharness_api.services.audit_service import AuditService
from bookharness_api.services.chapter_service import ChapterService
from bookharness_api.services.job_service import JobService
from bookharness_api.services.metadata_index import MetadataIndex
from bookharness_api.services.project_service import ProjectService


def create_app(root: str | Path = ".") -> FastAPI:
    project_root = Path(root).resolve()
    scaffold_project(project_root)

    app = FastAPI(title="bookharness api", version="0.2.0")
    app.state.project_root = project_root
    app.state.artifact_service = ArtifactService(project_root)
    app.state.audit_service = AuditService(project_root)
    app.state.index = MetadataIndex(project_root)
    app.state.job_service = JobService(project_root)
    app.state.project_service = ProjectService(project_root)
    app.state.chapter_service = ChapterService(project_root)
    app.state.index.sync_all()

    app.include_router(project.router)
    app.include_router(chapters.router)
    app.include_router(artifacts.router)
    app.include_router(approvals.router)
    app.include_router(runs.router)

    static_dir = Path(__file__).resolve().parent / "static"
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/")
    def index() -> FileResponse:
        return FileResponse(static_dir / "index.html")

    return app
