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
        ctx: dict[str, object] = {
            "blueprint": read_text(self.root / "book/blueprint.md"),
            "tone_guide": read_text(self.root / "book/tone_guide.md"),
            "argument_map": read_text(self.root / "book/argument_map.md"),
            "concept_dictionary": load_yaml(self.root / "book/concept_dictionary.yaml") or {},
            "chapter_dependencies": load_yaml(self.root / "book/chapter_dependencies.yaml") or {},
            "decisions_log": read_text(self.root / "book/decisions_log.md"),
        }
        for doc in ("audience_profile", "writing_rules"):
            path = self.root / f"book/{doc}.md"
            ctx[doc] = read_text(path) if path.exists() else ""
        ctx["global_summary"] = self._read_if_exists("memory/global_summary.md")
        ctx["unresolved_questions"] = self._read_if_exists("memory/unresolved_questions.md")
        ctx["recurring_examples"] = self._read_if_exists("memory/recurring_examples.md")
        return ctx

    def load_prior_chapter_summaries(self) -> dict[str, str]:
        summaries_dir = self.root / "memory/chapter_summaries"
        if not summaries_dir.exists():
            return {}
        return {
            path.stem: read_text(path)
            for path in sorted(summaries_dir.glob("*.md"))
        }

    def load_rubric(self, rubric_name: str) -> dict:
        path = self.root / f"eval/rubrics/{rubric_name}.yaml"
        return load_yaml(path) or {}

    def _read_if_exists(self, relative: str) -> str:
        path = self.root / relative
        return read_text(path) if path.exists() else ""
