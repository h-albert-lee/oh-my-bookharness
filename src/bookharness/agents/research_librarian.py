from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import RESEARCH_LIBRARIAN
from bookharness.utils.io import write_text
from bookharness.utils.yaml_utils import dump_yaml, load_yaml


class ResearchLibrarianAgent(BaseAgent):
    def collect_sources(self, chapter_id: str) -> None:
        ctx = self.load_project_context()
        brief = self.load_chapter_brief(chapter_id)
        registry = self._load_registry()
        context_block = self._build_context_block(ctx)

        relevant_sources = self._filter_relevant_sources(registry, chapter_id)
        registry_block = self._format_registry(relevant_sources) if relevant_sources else "등록된 source가 없다."

        user_prompt = f"""다음 장에 필요한 source를 선별하고 bundle을 작성하라.

## 장 정보
- chapter_id: {chapter_id}

## Chapter Brief
{brief}

## 프로젝트 맥락
{context_block}

## 등록된 Source Registry
{registry_block}

## 출력
1. bundle.yaml 내용 (core_sources, supporting_sources)을 ```yaml 코드 블록으로 출력하라.
2. 이어서 source pack notes를 Markdown으로 작성하라.
"""
        result = self._call_llm(RESEARCH_LIBRARIAN, user_prompt)

        pack_dir = self.root / f"sources/chapter_packs/{chapter_id}"
        pack_dir.mkdir(parents=True, exist_ok=True)
        self._parse_and_write(result, chapter_id, pack_dir)

    def _parse_and_write(self, result: str, chapter_id: str, pack_dir: Path) -> None:
        """Parse LLM output into bundle.yaml and notes.md."""
        import re
        import yaml as yaml_mod

        # Try to extract YAML block
        yaml_match = re.search(r"```yaml\s*\n(.*?)\n```", result, re.DOTALL)
        if yaml_match:
            try:
                bundle_data = yaml_mod.safe_load(yaml_match.group(1))
                if isinstance(bundle_data, dict):
                    if "chapter_id" not in bundle_data:
                        bundle_data["chapter_id"] = chapter_id
                    dump_yaml(pack_dir / "bundle.yaml", bundle_data)
                else:
                    self._write_default_bundle(pack_dir, chapter_id)
            except Exception:
                self._write_default_bundle(pack_dir, chapter_id)
            # Everything after the YAML block is notes
            yaml_end = result.find("```", yaml_match.end())
            notes_content = result[yaml_match.end():].strip()
            # Remove leading ``` if present
            if notes_content.startswith("```"):
                notes_content = notes_content[3:].strip()
        else:
            self._write_default_bundle(pack_dir, chapter_id)
            notes_content = result

        # Write notes
        if not notes_content.strip().startswith("#"):
            notes_content = f"# {chapter_id} Source Pack Notes\n\n{notes_content}"
        write_text(pack_dir / "notes.md", notes_content)

    def _write_default_bundle(self, pack_dir: Path, chapter_id: str) -> None:
        dump_yaml(pack_dir / "bundle.yaml", {
            "chapter_id": chapter_id,
            "core_sources": [],
            "supporting_sources": [],
        })

    def _load_registry(self) -> list[dict]:
        path = self.root / "sources/metadata/registry.yaml"
        data = load_yaml(path)
        return data if isinstance(data, list) else []

    def _filter_relevant_sources(self, registry: list[dict], chapter_id: str) -> list[dict]:
        return [s for s in registry if chapter_id in s.get("relevance_tags", []) or not s.get("relevance_tags")]

    def _format_registry(self, sources: list[dict]) -> str:
        lines = []
        for s in sources:
            sid = s.get("id", "unknown")
            title = s.get("title", "")
            authority = s.get("authority", "unknown")
            topics = ", ".join(s.get("topic_tags", []))
            lines.append(f"- {sid}: {title} (authority={authority}, topics=[{topics}])")
        return "\n".join(lines)
