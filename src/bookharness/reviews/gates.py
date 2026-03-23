from __future__ import annotations

from bookharness.models.review_report import ReviewReport


class AcceptanceGate:
    def __init__(self, threshold: int = 4) -> None:
        self.threshold = threshold

    def passes(self, reports: list[ReviewReport]) -> bool:
        for report in reports:
            if report.must_fix:
                return False
            for score in report.score.values():
                if score < self.threshold:
                    return False
        return True
