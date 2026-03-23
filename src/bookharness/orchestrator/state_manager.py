from __future__ import annotations

from pathlib import Path

from bookharness.models.chapter_state import ChapterState
from bookharness.utils.io import read_json, write_json


class StateManager:
    def __init__(self, root: Path) -> None:
        self.root = root

    def path_for(self, chapter_id: str) -> Path:
        return self.root / f"workflow/chapter_states/{chapter_id}_state.json"

    def save(self, state: ChapterState) -> None:
        write_json(self.path_for(state.chapter_id), state.to_dict())

    def load(self, chapter_id: str) -> ChapterState:
        return ChapterState.from_dict(read_json(self.path_for(chapter_id)))
