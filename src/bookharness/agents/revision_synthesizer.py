from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import REVISION_SYNTHESIZER
from bookharness.models.review_report import ReviewReport
from bookharness.utils.io import write_text


class RevisionSynthesizerAgent(BaseAgent):
    def synthesize(self, chapter_id: str, reports: list[ReviewReport]) -> Path:
        must_fix = list(dict.fromkeys(item for r in reports for item in r.must_fix))
        should_fix = list(dict.fromkeys(item for r in reports for item in r.should_fix))
        optional = list(dict.fromkeys(item for r in reports for item in r.nice_to_have))
        score_summary = self._build_score_summary(reports)

        brief = self.load_chapter_brief(chapter_id)
        draft = self.load_latest_draft(chapter_id)

        user_prompt = f"""다음 리뷰 결과를 통합하여 revision plan을 작성하라.

## Must Fix
{self._items(must_fix)}

## Should Fix
{self._items(should_fix)}

## Optional
{self._items(optional)}

## Score Summary
{score_summary}

## Chapter Brief (참고)
{brief[:1500]}

## 현재 Draft (참고)
{draft[:3000]}

## 출력 형식
다음 구조의 Markdown을 작성하라:
1. Score Summary
2. Must Fix (반드시 수정)
3. Should Fix (권장 수정)
4. Optional Improvements (선택적 개선)
5. Contradictory Comments (상충 의견)
6. Rewrite Instructions for Writer (구체적 수정 지시)
"""
        content = self._call_llm(REVISION_SYNTHESIZER, user_prompt)

        path = self._next_plan_path(chapter_id)
        write_text(path, content)
        return path

    def _build_score_summary(self, reports: list[ReviewReport]) -> str:
        lines = []
        for report in reports:
            lines.append(f"### {report.review_type}")
            for key, value in report.score.items():
                status = "✓" if value >= 4 else "△" if value >= 3 else "✗"
                lines.append(f"- {key}: {value}/5 {status}")
            lines.append(f"- must_fix: {len(report.must_fix)}건")
            lines.append(f"- should_fix: {len(report.should_fix)}건")
        return "\n".join(lines)

    def _next_plan_path(self, chapter_id: str) -> Path:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        existing = sorted(chapter_dir.glob("revision_plan_v*.md"))
        version = len(existing) + 1
        return chapter_dir / f"revision_plan_v{version}.md"

    @staticmethod
    def _items(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- 없음"
