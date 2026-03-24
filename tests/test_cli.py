from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def run_cli(tmp_path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "bookharness.cli", *args, "--root", str(tmp_path)],
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "PYTHONPATH": "src", "BOOKHARNESS_MOCK": "1"},
    )


def test_init_project_creates_required_structure(tmp_path: Path) -> None:
    run_cli(tmp_path, "init-project")

    assert (tmp_path / "book/blueprint.md").exists()
    assert (tmp_path / "sources/metadata/registry.yaml").exists()
    assert (tmp_path / "eval/rubrics/chapter_quality.yaml").exists()
    assert (tmp_path / "workflow/approvals/approvals.yaml").exists()


def test_run_mvp_creates_expected_artifacts(tmp_path: Path) -> None:
    run_cli(tmp_path, "init-project")
    run_cli(tmp_path, "run-mvp", "ch01", "데모는 되는데 왜 운영은 어려울까")

    chapter_dir = tmp_path / "manuscript/ch01"
    assert (chapter_dir / "brief.md").exists()
    assert (chapter_dir / "outline.md").exists()
    assert (chapter_dir / "draft_v1.md").exists()
    assert (chapter_dir / "draft_v2.md").exists()
    assert (chapter_dir / "revision_plan_v1.md").exists()
    assert (tmp_path / "sources/chapter_packs/ch01/bundle.yaml").exists()
    assert (tmp_path / "eval/reports/ch01_technical_v1.json").exists()

    state = json.loads((tmp_path / "workflow/chapter_states/ch01_state.json").read_text(encoding="utf-8"))
    assert state["status"] == "awaiting_human_draft_approval"
    assert state["latest_draft"] == "draft_v2.md"


def test_approval_a_advances_state(tmp_path: Path) -> None:
    run_cli(tmp_path, "init-project")
    run_cli(tmp_path, "init-chapter", "ch01", "테스트 장")
    run_cli(tmp_path, "run-stage", "ch01", "brief_generation")
    run_cli(tmp_path, "run-stage", "ch01", "source_collection")
    run_cli(tmp_path, "run-stage", "ch01", "source_analysis")
    run_cli(tmp_path, "run-stage", "ch01", "outline_design")
    run_cli(tmp_path, "approve", "ch01", "approval_a", "approved")

    state = json.loads((tmp_path / "workflow/chapter_states/ch01_state.json").read_text(encoding="utf-8"))
    assert state["status"] == "outline_ready"
    assert state["current_stage"] == "human_approval_a"


def test_approval_a_revision_requested_resets_stage(tmp_path: Path) -> None:
    run_cli(tmp_path, "init-project")
    run_cli(tmp_path, "init-chapter", "ch01", "테스트 장")
    run_cli(tmp_path, "run-stage", "ch01", "brief_generation")
    run_cli(tmp_path, "run-stage", "ch01", "source_collection")
    run_cli(tmp_path, "run-stage", "ch01", "source_analysis")
    run_cli(tmp_path, "run-stage", "ch01", "outline_design")
    run_cli(tmp_path, "approve", "ch01", "approval_a", "revision_requested", "--note", "도입부 수정 필요")

    state = json.loads((tmp_path / "workflow/chapter_states/ch01_state.json").read_text(encoding="utf-8"))
    assert state["current_stage"] == "outline_design"


def test_gate_passed_recorded_in_state(tmp_path: Path) -> None:
    run_cli(tmp_path, "init-project")
    run_cli(tmp_path, "run-mvp", "ch01", "테스트 장")

    state = json.loads((tmp_path / "workflow/chapter_states/ch01_state.json").read_text(encoding="utf-8"))
    assert "gate_passed" in state
    assert isinstance(state["gate_passed"], bool)


def test_approval_b_creates_final_candidate_and_updates_memory(tmp_path: Path) -> None:
    run_cli(tmp_path, "init-project")
    run_cli(tmp_path, "run-mvp", "ch01", "데모는 되는데 왜 운영은 어려울까")
    run_cli(tmp_path, "approve", "ch01", "approval_b", "approved")

    assert (tmp_path / "manuscript/ch01/final_candidate.md").exists()
    assert (tmp_path / "memory/chapter_summaries/ch01.md").exists()
    global_summary = (tmp_path / "memory/global_summary.md").read_text(encoding="utf-8")
    assert "ch01" in global_summary
