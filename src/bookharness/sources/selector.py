from __future__ import annotations

from pathlib import Path

from bookharness.utils.io import write_text
from bookharness.utils.yaml_utils import dump_yaml


class ChapterSourceSelector:
    def __init__(self, root: Path) -> None:
        self.root = root

    def create_placeholder_bundle(self, chapter_id: str, chapter_brief: str) -> None:
        pack_dir = self.root / f"sources/chapter_packs/{chapter_id}"
        pack_dir.mkdir(parents=True, exist_ok=True)
        bundle = {
            "chapter_id": chapter_id,
            "core_sources": [
                {
                    "source_id": "replace_with_core_source_id",
                    "why_it_matters": "핵심 논지를 직접 지지하는 자료를 선택한다.",
                    "expected_usage": "정의, 비교, 사례, 역사적 흐름 중 최소 하나를 담당한다.",
                    "quality_score": 5,
                }
            ],
            "supporting_sources": [
                {
                    "source_id": "replace_with_supporting_source_id",
                    "why_it_matters": "핵심 설명을 보완하거나 반례를 제공한다.",
                    "expected_usage": "보조 사례 또는 한계 설명에 사용한다.",
                    "quality_score": 3,
                }
            ],
        }
        dump_yaml(pack_dir / "bundle.yaml", bundle)
        write_text(
            pack_dir / "notes.md",
            f"# {chapter_id} Source Pack Notes\n\n## Brief Reference\n\n{chapter_brief}\n",
        )
