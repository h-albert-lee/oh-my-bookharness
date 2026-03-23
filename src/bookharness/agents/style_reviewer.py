from __future__ import annotations

from pathlib import Path

from bookharness.reviews.evaluator import ReviewEvaluator


class StyleReviewerAgent:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.evaluator = ReviewEvaluator(root)

    def review(self, chapter_id: str):
        return self.evaluator.evaluate(chapter_id, "style")
