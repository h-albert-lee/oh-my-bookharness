from __future__ import annotations

from pathlib import Path

from bookharness.manuscript.formatter import MarkdownFormatter
from bookharness.utils.io import write_text


class ChapterArchitectAgent:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.formatter = MarkdownFormatter()

    def build_outline(self, chapter_id: str, title: str) -> Path:
        path = self.root / f"manuscript/{chapter_id}/outline.md"
        write_text(path, self.formatter.outline(chapter_id, title))
        return path
