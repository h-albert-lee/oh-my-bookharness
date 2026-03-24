from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import CONTINUITY_REVIEWER
from bookharness.models.review_report import ReviewReport
from bookharness.reviews.evaluator import BinaryGateChecker


class ContinuityReviewerAgent(BaseAgent):
    def __init__(self, root: Path, backend=None) -> None:
        super().__init__(root, backend)
        self.gate_checker = BinaryGateChecker(root)

    def review(self, chapter_id: str) -> ReviewReport:
        ctx = self.load_project_context()
        draft = self.load_latest_draft(chapter_id)
        prior_summaries = self.load_prior_summaries()
        context_block = self._build_context_block(ctx)

        summaries_block = "\n\n".join(
            f"### {ch}\n{summary[:500]}" for ch, summary in prior_summaries.items()
        ) if prior_summaries else "없음"

        user_prompt = f"""다음 초안의 연속성 리뷰를 수행하라.

## 초안
{draft[:8000]}

## 이전 장 요약
{summaries_block}

## 프로젝트 맥락
{context_block[:2000]}

## 출력 형식
반드시 다음 JSON을 ```json 코드 블록으로 출력하라:
```json
{{
  "must_fix": ["수정 필수 항목..."],
  "should_fix": ["권장 수정 항목..."],
  "nice_to_have": ["선택적 개선..."],
  "score": {{
    "continuity": 1-5,
    "dependency_coverage": 1-5
  }}
}}
```
"""
        result = self._call_llm(CONTINUITY_REVIEWER, user_prompt)
        report = self._parse_review_result(chapter_id, "continuity", result)
        report.binary_checks = self.gate_checker.check(chapter_id, "continuity")
        return report

    def _parse_review_result(self, chapter_id: str, review_type: str, result: str) -> ReviewReport:
        data = self._parse_json_response(result)
        if data:
            return ReviewReport(
                chapter_id=chapter_id,
                review_type=review_type,
                score=data.get("score", {"continuity": 3, "dependency_coverage": 3}),
                must_fix=data.get("must_fix", []),
                should_fix=data.get("should_fix", []),
                nice_to_have=data.get("nice_to_have", []),
            )
        return ReviewReport(
            chapter_id=chapter_id,
            review_type=review_type,
            score={"continuity": 3, "dependency_coverage": 3},
        )
