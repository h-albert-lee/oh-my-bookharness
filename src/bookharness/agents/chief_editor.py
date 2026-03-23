from __future__ import annotations

from pathlib import Path

from bookharness.manuscript.formatter import MarkdownFormatter
from bookharness.utils.io import write_text


class ChiefEditorAgent:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.formatter = MarkdownFormatter()

    def generate_brief(
        self,
        chapter_id: str,
        title: str,
        dependencies: list[str],
        prior_summaries: list[str],
    ) -> Path:
        content = self.formatter.chapter_brief(chapter_id, title, dependencies, prior_summaries)
        path = self.root / f"manuscript/{chapter_id}/brief.md"
        write_text(path, content)
        return path
