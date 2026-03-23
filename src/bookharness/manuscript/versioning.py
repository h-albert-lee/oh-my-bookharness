from __future__ import annotations

from pathlib import Path


def next_draft_path(chapter_dir: Path) -> Path:
    existing = sorted(chapter_dir.glob("draft_v*.md"))
    version = len(existing) + 1
    return chapter_dir / f"draft_v{version}.md"
