"""Acceptance gate with configurable thresholds from rubric files."""

from __future__ import annotations

from pathlib import Path

from bookharness.models.review_report import ReviewReport
from bookharness.utils.yaml_utils import load_yaml


DEFAULT_THRESHOLD = 4


class AcceptanceGate:
    """Evaluates whether review reports pass acceptance criteria.

    Thresholds can be loaded from eval/rubrics/ YAML files or set manually.
    Default threshold: all scores >= 4 and must_fix count == 0.
    """

    def __init__(self, threshold: int = DEFAULT_THRESHOLD, thresholds: dict[str, int] | None = None) -> None:
        self.default_threshold = threshold
        self.thresholds = thresholds or {}

    @classmethod
    def from_rubrics(cls, root: Path, threshold: int = DEFAULT_THRESHOLD) -> "AcceptanceGate":
        """Load thresholds from eval/rubrics/*.yaml files."""
        thresholds: dict[str, int] = {}
        rubrics_dir = root / "eval/rubrics"
        if rubrics_dir.exists():
            for path in rubrics_dir.glob("*.yaml"):
                data = load_yaml(path)
                if isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, dict) and "scale" in value:
                            # Use the threshold as the minimum passing score
                            thresholds[key] = threshold
        return cls(threshold=threshold, thresholds=thresholds)

    def passes(self, reports: list[ReviewReport]) -> bool:
        """Check if all reports pass the acceptance gate."""
        for report in reports:
            if report.must_fix:
                return False
            for key, score in report.score.items():
                min_score = self.thresholds.get(key, self.default_threshold)
                if score < min_score:
                    return False
        return True

    def evaluate(self, reports: list[ReviewReport]) -> dict:
        """Return detailed gate evaluation results."""
        passed = True
        details = []
        total_must_fix = 0

        for report in reports:
            report_detail = {
                "review_type": report.review_type,
                "must_fix_count": len(report.must_fix),
                "score_checks": {},
                "passed": True,
            }
            if report.must_fix:
                report_detail["passed"] = False
                passed = False
            total_must_fix += len(report.must_fix)

            for key, score in report.score.items():
                min_score = self.thresholds.get(key, self.default_threshold)
                check_passed = score >= min_score
                report_detail["score_checks"][key] = {
                    "score": score,
                    "threshold": min_score,
                    "passed": check_passed,
                }
                if not check_passed:
                    report_detail["passed"] = False
                    passed = False

            details.append(report_detail)

        return {
            "passed": passed,
            "total_must_fix": total_must_fix,
            "details": details,
        }
