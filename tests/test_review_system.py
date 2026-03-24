"""Tests for the review system: LLM-based reviews + binary gate checks."""

from __future__ import annotations

import json
from pathlib import Path

from bookharness.cli import scaffold_project
from bookharness.orchestrator.runner import WorkflowRunner
from bookharness.reviews.evaluator import BinaryGateChecker, ReviewIO
from bookharness.reviews.gates import AcceptanceGate
from bookharness.utils.io import write_text


# --- Binary gate checker tests ---

def test_binary_gate_detects_absolute_claims(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    draft_path = tmp_path / "manuscript/ch01/draft_v2.md"
    write_text(draft_path, "# 테스트\n\n이 시스템은 항상 정확한 결과를 반환한다.\n\n모든 경우에 성공한다.\n")

    checker = BinaryGateChecker(tmp_path)
    checks = checker.check("ch01", "technical")

    assert checks["has_unsupported_claims"] is True


def test_binary_gate_detects_blog_patterns(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    draft_path = tmp_path / "manuscript/ch01/draft_v2.md"
    write_text(draft_path, "# 테스트\n\n오늘은 여러분에게 AI에 대해 이야기하겠습니다. 짜잔!\n")

    checker = BinaryGateChecker(tmp_path)
    checks = checker.check("ch01", "style")

    assert checks["blog_style_detected"] is True


def test_binary_gate_detects_declarative_patterns(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    draft_path = tmp_path / "manuscript/ch01/draft_v2.md"
    write_text(draft_path, "# 테스트\n\n이것은 혁명적인 패러다임 시프트이다.\n")

    checker = BinaryGateChecker(tmp_path)
    checks = checker.check("ch01", "style")

    assert checks["tone_guide_violation"] is True


def test_binary_gate_checks_dependency_coverage(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    from bookharness.utils.yaml_utils import dump_yaml
    dump_yaml(tmp_path / "book/chapter_dependencies.yaml", {
        "ch01": {"introduces": ["system_vs_model"], "required_by": ["ch02"]},
        "ch02": {"depends_on": ["system_vs_model"], "introduces": ["evaluation"]},
    })

    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "첫 번째 장")
    runner.approve("ch01", "approval_b", "approved")
    runner.run_mvp("ch02", "두 번째 장", ["ch01"])

    # Draft that doesn't mention dependency concept
    draft_path = tmp_path / "manuscript/ch02/draft_v2.md"
    write_text(draft_path, "# 두 번째 장\n\n완전히 새로운 주제만 다룬다.\n")

    checker = BinaryGateChecker(tmp_path)
    checks = checker.check("ch02", "continuity")

    assert checks["dependency_concepts_covered"] is False


# --- LLM-based review tests (via mock) ---

def test_reviewer_agents_call_llm(tmp_path: Path, mock_llm) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    # Verify LLM was called for reviews
    review_calls = [
        (s, u) for s, u in mock_llm.calls
        if "리뷰" in s or "Reviewer" in s
    ]
    assert len(review_calls) >= 3, "Should have at least 3 review LLM calls"


def test_review_reports_have_scores(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    io = ReviewIO(tmp_path)
    reports = io.load_reports("ch01")
    assert len(reports) == 3

    for report in reports:
        assert report.score, f"Report {report.review_type} has no scores"
        for key, value in report.score.items():
            assert 1 <= value <= 5, f"Score {key}={value} out of range"


def test_review_reports_have_binary_checks(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    io = ReviewIO(tmp_path)
    reports = io.load_reports("ch01")

    for report in reports:
        assert report.binary_checks, f"Report {report.review_type} has no binary_checks"


# --- Acceptance gate tests ---

def test_acceptance_gate_checks_must_fix(tmp_path: Path) -> None:
    from bookharness.models.review_report import ReviewReport
    from tests.mock_backend import TECHNICAL_REVIEW_RESPONSE

    # Mock report with must_fix
    report_with_issues = ReviewReport(
        chapter_id="ch01",
        review_type="technical",
        score={"technical_accuracy": 4, "source_grounding": 4, "clarity": 4},
        must_fix=["critical issue"],
    )
    gate = AcceptanceGate()
    assert not gate.passes([report_with_issues])


def test_acceptance_gate_passes_clean_reports(tmp_path: Path) -> None:
    from bookharness.models.review_report import ReviewReport

    clean_report = ReviewReport(
        chapter_id="ch01",
        review_type="technical",
        score={"technical_accuracy": 4, "source_grounding": 4, "clarity": 4},
        must_fix=[],
    )
    gate = AcceptanceGate()
    assert gate.passes([clean_report])


def test_gate_details_in_chapter_state(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    state_data = json.loads(
        (tmp_path / "workflow/chapter_states/ch01_state.json").read_text(encoding="utf-8")
    )
    assert "gate_passed" in state_data
    assert isinstance(state_data["gate_passed"], bool)
    assert "gate_details" in state_data
