"""Base agent with canonical context loading and LLM call."""

from __future__ import annotations

import json
import re
from pathlib import Path

from bookharness.llm import LLMBackend, get_backend
from bookharness.memory.loader import MemoryLoader
from bookharness.utils.io import read_text
from bookharness.utils.yaml_utils import load_yaml


class BaseAgent:
    """Base class for all bookharness agents.

    Every agent calls the LLM backend. There is no template fallback.
    """

    def __init__(self, root: Path, backend: LLMBackend | None = None) -> None:
        self.root = root
        self.backend = backend or get_backend()
        self._loader = MemoryLoader(root)

    # --- LLM call ---

    def _call_llm(self, system: str, user: str, *, max_tokens: int | None = None) -> str:
        """Call the LLM backend. Always."""
        return self.backend.generate(system, user, max_tokens=max_tokens)

    def _parse_json_response(self, text: str) -> dict | None:
        """Extract JSON from LLM response (handles ```json fences)."""
        match = re.search(r"```json\s*\n(.*?)\n```", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                pass
        # Try parsing the whole thing as JSON
        try:
            return json.loads(text)
        except (json.JSONDecodeError, ValueError):
            return None

    # --- Context loading ---

    def load_project_context(self) -> dict[str, object]:
        return self._loader.load_project_context()

    def load_prior_summaries(self) -> dict[str, str]:
        return self._loader.load_prior_chapter_summaries()

    def load_chapter_brief(self, chapter_id: str) -> str:
        path = self.root / f"manuscript/{chapter_id}/brief.md"
        return read_text(path) if path.exists() else ""

    def load_chapter_outline(self, chapter_id: str) -> str:
        path = self.root / f"manuscript/{chapter_id}/outline.md"
        return read_text(path) if path.exists() else ""

    def load_chapter_source_notes(self, chapter_id: str) -> str:
        path = self.root / f"sources/chapter_packs/{chapter_id}/notes.md"
        return read_text(path) if path.exists() else ""

    def load_chapter_bundle(self, chapter_id: str) -> dict:
        path = self.root / f"sources/chapter_packs/{chapter_id}/bundle.yaml"
        return load_yaml(path) or {}

    def load_latest_draft(self, chapter_id: str) -> str:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        drafts = sorted(chapter_dir.glob("draft_v*.md"))
        return read_text(drafts[-1]) if drafts else ""

    def load_revision_plan(self, chapter_id: str) -> str:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        plans = sorted(chapter_dir.glob("revision_plan_v*.md"))
        return read_text(plans[-1]) if plans else ""

    def _build_context_block(self, ctx: dict[str, object]) -> str:
        """Build a project context block for insertion into prompts."""
        parts = []
        for key in ("blueprint", "tone_guide", "argument_map", "decisions_log", "writing_rules", "audience_profile"):
            value = ctx.get(key, "")
            if value:
                parts.append(f"### {key}\n\n{value}")
        concept_dict = ctx.get("concept_dictionary", {})
        if concept_dict and isinstance(concept_dict, dict):
            lines = []
            for term, info in concept_dict.items():
                if isinstance(info, dict):
                    korean = info.get("preferred_korean", term)
                    definition = info.get("definition", "")
                    lines.append(f"- **{term}** ({korean}): {definition}")
                else:
                    lines.append(f"- **{term}**: {info}")
            parts.append("### concept_dictionary\n\n" + "\n".join(lines))
        deps = ctx.get("chapter_dependencies", {})
        if deps and isinstance(deps, dict):
            dep_lines = []
            for ch, info in deps.items():
                if isinstance(info, dict):
                    introduces = ", ".join(info.get("introduces", []))
                    depends = ", ".join(info.get("depends_on", []))
                    dep_lines.append(f"- {ch}: introduces=[{introduces}], depends_on=[{depends}]")
                else:
                    dep_lines.append(f"- {ch}: {info}")
            parts.append("### chapter_dependencies\n\n" + "\n".join(dep_lines))
        return "\n\n".join(parts)
