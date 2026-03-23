from __future__ import annotations

from pathlib import Path

from bookharness.sources.normalizer import SourceNormalizer
from bookharness.utils.io import write_text
from bookharness.utils.yaml_utils import load_yaml


class SourceAnalystAgent:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.normalizer = SourceNormalizer(root)

    def analyze(self, chapter_id: str) -> None:
        bundle = load_yaml(self.root / f"sources/chapter_packs/{chapter_id}/bundle.yaml") or {}
        all_sources = []
        for key in ("core_sources", "supporting_sources"):
            all_sources.extend(bundle.get(key, []))
        for item in all_sources:
            source_id = item["source_id"]
            self.normalizer.create_note(source_id, chapter_id)
        pack_dir = self.root / f"sources/chapter_packs/{chapter_id}"
        write_text(
            pack_dir / "must_cite.md",
            "# Must Cite\n\n- 핵심 정의와 역사적 흐름을 지지하는 source를 여기에 기록한다.",
        )
        write_text(
            pack_dir / "counterpoints.md",
            "# Counterpoints\n\n- 반론, 한계, 과장 가능성을 여기에 기록한다.",
        )
