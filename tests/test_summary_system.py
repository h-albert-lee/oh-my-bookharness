"""Tests for the summary/memory system."""

from __future__ import annotations

from pathlib import Path

from bookharness.cli import scaffold_project
from bookharness.memory.summarizer import SummaryBuilder
from bookharness.orchestrator.runner import WorkflowRunner
from bookharness.utils.io import read_text, write_text


def test_chapter_summary_extracts_structure(tmp_path: Path) -> None:
    scaffold_project(tmp_path)

    content = """# AI 시스템의 운영 과제

이 장에서는 AI 시스템의 운영 과제를 살펴본다.

## 문제 설정

**데모-운영 격차**(demo-production gap)는 AI 시스템에서 자주 관찰되는 현상이다.

## 핵심 개념

**평가 하네스**(evaluation harness)는 반복 가능하게 실행과 평가를 수행하는 외부 구조다.[^anthropic_eval_2024]

## 정리

다음 장에서는 평가 체계를 더 깊이 살펴본다.
"""
    final_path = tmp_path / "manuscript/ch01/final_candidate.md"
    write_text(final_path, content)

    builder = SummaryBuilder()
    summary = builder.build_chapter_summary("ch01", final_path, tmp_path)

    assert "핵심 개념" in summary
    assert "섹션 구조" in summary
    assert "anthropic_eval_2024" in summary
    assert "다음 장" in summary


def test_global_summary_includes_cross_references(tmp_path: Path) -> None:
    scaffold_project(tmp_path)

    write_text(tmp_path / "memory/chapter_summaries/ch01.md", "# ch01 Summary\n\n## 핵심 개념\n\n- **평가 하네스**\n")
    write_text(tmp_path / "memory/chapter_summaries/ch02.md", "# ch02 Summary\n\n## 핵심 개념\n\n- **평가 하네스**\n")

    builder = SummaryBuilder()
    global_summary = builder.refresh_global_summary(tmp_path)

    assert "ch01" in global_summary
    assert "ch02" in global_summary
    assert "승인된 장 수: 2" in global_summary


def test_full_approval_flow_updates_memory(tmp_path: Path) -> None:
    scaffold_project(tmp_path)
    runner = WorkflowRunner(tmp_path)

    runner.run_mvp("ch01", "첫 번째 장")
    runner.approve("ch01", "approval_b", "approved")

    assert (tmp_path / "memory/chapter_summaries/ch01.md").exists()

    global_summary = read_text(tmp_path / "memory/global_summary.md")
    assert "ch01" in global_summary
