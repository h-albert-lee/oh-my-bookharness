from __future__ import annotations

from pathlib import Path

from bookharness.models.review_report import ReviewReport
from bookharness.utils.io import write_text


class RevisionSynthesizerAgent:
    def __init__(self, root: Path) -> None:
        self.root = root

    def synthesize(self, chapter_id: str, reports: list[ReviewReport]) -> Path:
        must_fix = [item for report in reports for item in report.must_fix]
        should_fix = [item for report in reports for item in report.should_fix]
        optional = [item for report in reports for item in report.nice_to_have]
        body = f"""# Revision Plan: {chapter_id}

## Must Fix

{self._items(must_fix)}

## Should Fix

{self._items(should_fix)}

## Optional Improvements

{self._items(optional)}

## Contradictory Comments

- 현재 자동 리뷰에서는 상충 코멘트가 감지되지 않았다.

## Rewrite Instructions for Writer

- must-fix를 먼저 해결한다.
- source grounding이 약한 단정 표현은 완곡하게 수정한다.
- 독자 안내형 설명체와 장 간 연결 문장을 유지한다.
"""
        path = self.root / f"manuscript/{chapter_id}/revision_plan_v1.md"
        write_text(path, body)
        return path

    @staticmethod
    def _items(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- 없음"
