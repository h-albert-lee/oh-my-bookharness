from __future__ import annotations

from pathlib import Path

from bookharness.models.schemas import REQUIRED_BOOK_DOCS
from bookharness.utils.io import read_text
from bookharness.utils.yaml_utils import load_yaml


class MissingCanonicalDocumentError(FileNotFoundError):
    """Raised when required canonical book files are missing."""


class MemoryLoader:
    def __init__(self, root: Path) -> None:
        self.root = root

    def validate_required_documents(self) -> None:
        missing = [doc for doc in REQUIRED_BOOK_DOCS if not (self.root / doc).exists()]
        if missing:
            raise MissingCanonicalDocumentError(
                "Missing required canonical documents: " + ", ".join(missing)
            )

    def load_project_context(self) -> dict[str, object]:
        self.validate_required_documents()
        return {
            "blueprint": read_text(self.root / "book/blueprint.md"),
            "tone_guide": read_text(self.root / "book/tone_guide.md"),
            "argument_map": read_text(self.root / "book/argument_map.md"),
            "concept_dictionary": load_yaml(self.root / "book/concept_dictionary.yaml") or {},
            "chapter_dependencies": load_yaml(self.root / "book/chapter_dependencies.yaml") or {},
            "decisions_log": read_text(self.root / "book/decisions_log.md"),
            "global_summary": read_text(self.root / "memory/global_summary.md")
            if (self.root / "memory/global_summary.md").exists()
            else "",
        }

    def load_prior_chapter_summaries(self) -> dict[str, str]:
        summaries_dir = self.root / "memory/chapter_summaries"
        if not summaries_dir.exists():
            return {}
        return {
            path.stem: read_text(path)
            for path in sorted(summaries_dir.glob("*.md"))
        }
