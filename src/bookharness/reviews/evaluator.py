from __future__ import annotations

from pathlib import Path

from bookharness.models.review_report import ReviewReport
from bookharness.utils.io import read_text, write_json, write_text


class ReviewEvaluator:
    def __init__(self, root: Path) -> None:
        self.root = root

    def evaluate(self, chapter_id: str, review_type: str) -> ReviewReport:
        draft = read_text(self.root / f"manuscript/{chapter_id}/draft_v1.md")
        unsupported_claims = "항상" in draft or "절대" in draft
        score = {
            "technical_accuracy": 4,
            "source_grounding": 4,
            "clarity": 4,
            "tone_fit": 4,
            "continuity": 4,
        }
        must_fix = []
        if unsupported_claims:
            must_fix.append("단정 표현이 포함되어 있어 source grounding 점검이 필요하다.")
        if review_type == "technical":
            should_fix = ["핵심 개념 정의가 concept dictionary와 정확히 일치하는지 재확인한다."]
            nice = ["필요하면 deterministic component와 conventional tests의 관계를 한 문장 추가한다."]
        elif review_type == "style":
            should_fix = ["장 도입부가 독자 안내형 설명체를 유지하는지 확인한다."]
            nice = ["예시 문장을 조금 더 실무적인 장면으로 조정할 수 있다."]
        else:
            should_fix = ["이전 장 요약과 연결되는 전이 문장을 보강한다."]
            nice = ["다음 장 예고를 한 문단 더 명확히 쓸 수 있다."]

        binary_checks = {
            "has_unsupported_claims": unsupported_claims,
            "matches_concept_dictionary": True,
            "missing_required_points": False,
            "tone_guide_violation": False,
        }
        report = ReviewReport(
            chapter_id=chapter_id,
            review_type=review_type,
            score=score,
            must_fix=must_fix,
            should_fix=should_fix,
            nice_to_have=nice,
            binary_checks=binary_checks,
        )
        return report

    def write_report(self, chapter_id: str, report: ReviewReport) -> None:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        markdown_path = chapter_dir / f"review_{report.review_type}_v1.md"
        json_path = self.root / f"eval/reports/{chapter_id}_{report.review_type}_v1.json"
        body = f"""# {report.review_type.title()} Review: {chapter_id}

## Score

{report.score}

## Must Fix

{self._items(report.must_fix)}

## Should Fix

{self._items(report.should_fix)}

## Nice to Have

{self._items(report.nice_to_have)}

## Binary Checks

{report.binary_checks}
"""
        write_text(markdown_path, body)
        write_json(json_path, report.to_dict())

    @staticmethod
    def _items(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- 없음"
