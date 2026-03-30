from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import TECHNICAL_REVIEWER
from bookharness.models.review_report import ReviewReport
from bookharness.reviews.evaluator import BinaryGateChecker


class TechnicalReviewerAgent(BaseAgent):
    def __init__(self, root: Path, backend=None) -> None:
        super().__init__(root, backend)
        self.gate_checker = BinaryGateChecker(root)

    def review(self, chapter_id: str) -> ReviewReport:
        ctx = self.load_project_context()
        draft = self.load_latest_draft(chapter_id)
        brief = self.load_chapter_brief(chapter_id)
        source_notes = self.load_chapter_source_notes(chapter_id)
        context_block = self._build_context_block(ctx)

        user_prompt = f"""다음 초안의 기술 리뷰를 수행하라.

## Chapter Brief
{brief[:2000]}

## Source Pack Notes
{source_notes[:2000]}

## 초안
{draft[:8000]}

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
    "technical_accuracy": 1-5,
    "source_grounding": 1-5,
    "clarity": 1-5
  }}
}}
```
"""
        result = self._call_llm(TECHNICAL_REVIEWER, user_prompt)
        report = self._parse_review_result(chapter_id, "technical", result)
        binary = self.gate_checker.check(chapter_id, "technical")
        report.binary_checks = binary

        # Auto-add must_fix if page target is not met
        if not binary.get("meets_minimum_length", True):
            detail = binary.get("page_check_detail", "")
            report.must_fix.append(f"[분량 미달] 목표 분량의 70% 미만입니다. {detail}")
        if not binary.get("within_maximum_length", True):
            detail = binary.get("page_check_detail", "")
            report.must_fix.append(f"[분량 초과] 목표 분량의 150%를 초과합니다. {detail}")

        return report

    def _parse_review_result(self, chapter_id: str, review_type: str, result: str) -> ReviewReport:
        data = self._parse_json_response(result)
        if data:
            return ReviewReport(
                chapter_id=chapter_id,
                review_type=review_type,
                score=data.get("score", {"technical_accuracy": 3, "source_grounding": 3, "clarity": 3}),
                must_fix=data.get("must_fix", []),
                should_fix=data.get("should_fix", []),
                nice_to_have=data.get("nice_to_have", []),
            )
        return ReviewReport(
            chapter_id=chapter_id,
            review_type=review_type,
            score={"technical_accuracy": 3, "source_grounding": 3, "clarity": 3},
            must_fix=[f"LLM 리뷰 결과 파싱 실패. 원문: {result[:200]}"],
        )
