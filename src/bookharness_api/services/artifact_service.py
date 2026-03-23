from __future__ import annotations

import difflib
import json
from pathlib import Path
from typing import Any

from bookharness.utils.io import read_text
from bookharness_api.services.helpers import ensure_within_root, markdown_to_html, to_iso


class ArtifactService:
    def __init__(self, root: Path) -> None:
        self.root = root

    def read_artifact(self, relative_path: str) -> dict[str, Any]:
        path = ensure_within_root(self.root, self.root / relative_path)
        content = read_text(path)
        suffix = path.suffix.lower()
        kind = {
            ".md": "markdown",
            ".json": "json",
            ".yaml": "yaml",
            ".yml": "yaml",
        }.get(suffix, "text")
        rendered_html = markdown_to_html(content) if kind == "markdown" else None
        return {
            "path": str(path.relative_to(self.root)),
            "kind": kind,
            "content": content,
            "rendered_html": rendered_html,
            "modified_at": to_iso(path.stat().st_mtime),
        }

    def diff(self, left_path: str, right_path: str) -> dict[str, Any]:
        left = self.read_artifact(left_path)
        right = self.read_artifact(right_path)
        left_lines = left["content"].splitlines()
        right_lines = right["content"].splitlines()
        changed: list[dict[str, Any]] = []
        for line in difflib.ndiff(left_lines, right_lines):
            if line.startswith("- "):
                changed.append({"type": "removed", "line": line[2:]})
            elif line.startswith("+ "):
                changed.append({"type": "added", "line": line[2:]})
        left_only = sorted(set(left_lines) - set(right_lines))
        right_only = sorted(set(right_lines) - set(left_lines))
        return {
            "left_path": left["path"],
            "right_path": right["path"],
            "left_only": left_only,
            "right_only": right_only,
            "changed": changed,
        }

    def list_chapter_artifacts(self, chapter_id: str) -> list[dict[str, str]]:
        candidates = []
        for base in [
            self.root / f"manuscript/{chapter_id}",
            self.root / f"sources/chapter_packs/{chapter_id}",
        ]:
            if base.exists():
                for path in sorted(base.glob("*")):
                    if path.is_file():
                        candidates.append({"path": str(path.relative_to(self.root)), "name": path.name})
        for pattern in [f"eval/reports/{chapter_id}_*.json", f"workflow/chapter_states/{chapter_id}_state.json"]:
            for path in sorted(self.root.glob(pattern)):
                candidates.append({"path": str(path.relative_to(self.root)), "name": path.name})
        return candidates
