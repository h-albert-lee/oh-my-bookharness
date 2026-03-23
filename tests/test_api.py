from __future__ import annotations

import time
from pathlib import Path

from fastapi.testclient import TestClient

from bookharness_api.app import create_app


def wait_for_job(client: TestClient, job_id: str, timeout: float = 5.0) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        payload = client.get(f"/api/runs/{job_id}").json()
        if payload["status"] in {"succeeded", "failed", "waiting_for_approval"}:
            return payload
        time.sleep(0.05)
    raise AssertionError(f"Job {job_id} did not finish in time")


def test_project_dashboard_and_chapter_workflow(tmp_path: Path) -> None:
    app = create_app(tmp_path)
    client = TestClient(app)

    summary = client.get("/api/project").json()
    assert summary["metrics"]["chapter_count"] == 0

    created = client.post(
        "/api/chapters",
        json={
            "chapter_id": "ch01",
            "title": "데모는 되는데 왜 운영은 어려울까",
            "dependencies": ["ch00_blueprint"],
            "actor": "tester",
        },
    ).json()
    assert created["chapter_id"] == "ch01"

    run_job = client.post(
        "/api/chapters/ch01/run-stage",
        json={"stage": "brief_generation", "actor": "tester"},
    ).json()
    completed = wait_for_job(client, run_job["job_id"])
    assert completed["status"] == "succeeded"

    detail = client.get("/api/chapters/ch01").json()
    assert detail["state"]["status"] == "brief_generated"
    assert any(item["path"].endswith("brief.md") for item in detail["artifacts"])

    artifact = client.get("/api/artifacts", params={"path": "manuscript/ch01/brief.md"}).json()
    assert artifact["kind"] == "markdown"
    assert "Chapter Brief" in artifact["content"]


def test_run_mvp_updates_jobs_and_approval_flow(tmp_path: Path) -> None:
    app = create_app(tmp_path)
    client = TestClient(app)

    job = client.post(
        "/api/chapters/ch01/run-mvp",
        json={
            "title": "데모는 되는데 왜 운영은 어려울까",
            "dependencies": [],
            "actor": "tester",
        },
    ).json()
    completed = wait_for_job(client, job["job_id"], timeout=8.0)
    assert completed["status"] == "waiting_for_approval"

    pending = client.get("/api/approvals/pending").json()
    assert pending[0]["chapter_id"] == "ch01"
    assert pending[0]["approval_key"] == "approval_b"

    approval_job = client.post(
        "/api/chapters/ch01/approve",
        json={
            "approval_key": "approval_b",
            "result": "approved",
            "notes": ["looks good"],
            "actor": "chief-editor",
        },
    ).json()
    approval_completed = wait_for_job(client, approval_job["job_id"], timeout=8.0)
    assert approval_completed["status"] == "succeeded"

    detail = client.get("/api/chapters/ch01").json()
    assert detail["state"]["status"] == "chapter_approved"

    diff = client.get(
        "/api/artifacts/diff",
        params={
            "left": "manuscript/ch01/draft_v1.md",
            "right": "manuscript/ch01/draft_v2.md",
        },
    ).json()
    assert diff["left_path"].endswith("draft_v1.md")

    runs = client.get("/api/runs").json()
    assert len(runs) >= 2
