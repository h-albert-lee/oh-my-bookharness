"""Tests for agent LLM integration and output quality."""

from __future__ import annotations

from pathlib import Path

from bookharness.cli import scaffold_project
from bookharness.orchestrator.runner import WorkflowRunner
from bookharness.utils.io import read_text
from bookharness.utils.yaml_utils import dump_yaml, load_yaml


def test_all_stages_call_llm(tmp_path: Path, mock_llm) -> None:
    """Every agent stage should result in LLM calls."""
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    # Should have calls for: brief, source_collection, source_analysis (multiple),
    # outline, draft, 3x review, revision_plan, revision_draft
    assert len(mock_llm.calls) >= 10, f"Expected >= 10 LLM calls, got {len(mock_llm.calls)}"


def test_brief_generation_calls_chief_editor(tmp_path: Path, mock_llm) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.initialize_chapter("ch01", "테스트 장")
    runner.run_stage("ch01", "brief_generation")

    brief = read_text(tmp_path / "manuscript/ch01/brief.md")
    assert "Chapter Brief" in brief

    # Verify chief editor was called
    editor_calls = [(s, u) for s, u in mock_llm.calls if "편집장" in s or "Chief Editor" in s]
    assert len(editor_calls) == 1


def test_outline_calls_architect(tmp_path: Path, mock_llm) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.initialize_chapter("ch01", "테스트 장")
    runner.run_stage("ch01", "brief_generation")
    runner.run_stage("ch01", "source_collection")
    runner.run_stage("ch01", "source_analysis")
    runner.run_stage("ch01", "outline_design")

    outline = read_text(tmp_path / "manuscript/ch01/outline.md")
    assert "Outline" in outline or "Section" in outline

    architect_calls = [(s, u) for s, u in mock_llm.calls if "장 설계자" in s or "Chapter Architect" in s]
    assert len(architect_calls) == 1


def test_draft_calls_writer(tmp_path: Path, mock_llm) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    draft = read_text(tmp_path / "manuscript/ch01/draft_v1.md")
    assert len(draft) > 100

    writer_calls = [(s, u) for s, u in mock_llm.calls if "집필자" in s or "Draft Writer" in s]
    assert len(writer_calls) >= 1


def test_source_bundle_uses_registry(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    dump_yaml(tmp_path / "sources/metadata/registry.yaml", [
        {
            "id": "anthropic_eval_2024",
            "title": "Anthropic Evaluation Guide",
            "type": "blog",
            "author": "Anthropic",
            "published_at": "2024-06-01",
            "authority": "high",
            "source_kind": "official_company_blog",
            "topic_tags": ["evaluation"],
            "relevance_tags": ["ch01"],
            "status": "done",
        },
    ])

    runner = WorkflowRunner(tmp_path)
    runner.initialize_chapter("ch01", "테스트 장")
    runner.run_stage("ch01", "brief_generation")
    runner.run_stage("ch01", "source_collection")

    # Bundle should exist (written by LLM via mock)
    assert (tmp_path / "sources/chapter_packs/ch01/bundle.yaml").exists()
    assert (tmp_path / "sources/chapter_packs/ch01/notes.md").exists()


def test_multi_chapter_continuity(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    dump_yaml(tmp_path / "book/chapter_dependencies.yaml", {
        "ch01": {"introduces": ["system_vs_model"], "required_by": ["ch02"]},
        "ch02": {"depends_on": ["system_vs_model"], "introduces": ["evaluation"]},
    })

    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "시스템 대 모델")
    runner.approve("ch01", "approval_b", "approved")

    # Memory should be updated
    assert (tmp_path / "memory/chapter_summaries/ch01.md").exists()

    runner.run_mvp("ch02", "평가 체계", ["ch01"])

    # ch02 brief should have been generated (via LLM)
    brief = read_text(tmp_path / "manuscript/ch02/brief.md")
    assert len(brief) > 50


def test_revision_mode_calls_llm_with_plan(tmp_path: Path, mock_llm) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)
    runner.run_mvp("ch01", "테스트 장")

    # Check that revision draft call included revision plan context
    writer_calls = [(s, u) for s, u in mock_llm.calls if "집필자" in s or "Draft Writer" in s]
    # Should have at least 2 calls: initial draft + revision draft
    assert len(writer_calls) >= 2
    # The last writer call should contain revision-related context
    last_user_prompt = writer_calls[-1][1]
    assert "Revision Plan" in last_user_prompt or "수정" in last_user_prompt
