from __future__ import annotations

from pathlib import Path

from bookharness.manuscript.writer import DraftComposer


class DraftWriterAgent:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.composer = DraftComposer(root)

    def write(self, chapter_id: str, title: str, revision_mode: bool = False) -> Path:
        return self.composer.create_draft(chapter_id, title, revision_mode=revision_mode)
