from __future__ import annotations

from pathlib import Path

from bookharness.models.source_metadata import SourceMetadata
from bookharness.utils.yaml_utils import dump_yaml, load_yaml


class SourceRegistry:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.path = root / "sources/metadata/registry.yaml"

    def load(self) -> list[dict]:
        data = load_yaml(self.path)
        return data if isinstance(data, list) else []

    def save(self, entries: list[dict]) -> None:
        dump_yaml(self.path, entries)

    def register(self, source: SourceMetadata) -> None:
        entries = self.load()
        entries = [entry for entry in entries if entry.get("id") != source.id]
        entries.append(source.to_dict())
        entries.sort(key=lambda item: item["id"])
        self.save(entries)
