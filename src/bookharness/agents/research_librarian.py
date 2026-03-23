from __future__ import annotations

from pathlib import Path

from bookharness.sources.selector import ChapterSourceSelector
from bookharness.utils.io import read_text


class ResearchLibrarianAgent:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.selector = ChapterSourceSelector(root)

    def collect_sources(self, chapter_id: str) -> None:
        brief = read_text(self.root / f"manuscript/{chapter_id}/brief.md")
        self.selector.create_placeholder_bundle(chapter_id, brief)
