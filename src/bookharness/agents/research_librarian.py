from __future__ import annotations

import json
import re
from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import RESEARCH_LIBRARIAN
from bookharness.utils.io import read_text, write_text
from bookharness.utils.yaml_utils import dump_yaml, load_yaml


class ResearchLibrarianAgent(BaseAgent):
    """Source collector that uses local registry first, then web search for gaps."""

    def collect_sources(self, chapter_id: str) -> None:
        ctx = self.load_project_context()
        brief = self.load_chapter_brief(chapter_id)
        context_block = self._build_context_block(ctx)

        # Step 1: Gather local sources
        registry = self._load_registry()
        local_sources = self._filter_relevant_sources(registry, chapter_id)
        local_block = self._format_registry(local_sources) if local_sources else "등록된 로컬 source가 없다."

        # Step 2: Ask LLM what additional sources are needed
        gap_prompt = f"""다음 장의 brief를 읽고, 집필에 필요한 참고 자료의 검색 쿼리를 생성하라.

## 장 정보
- chapter_id: {chapter_id}

## Chapter Brief
{brief}

## 이미 확보된 로컬 Source
{local_block}

## 지시
1. 이미 확보된 source로 충분한 영역과 부족한 영역을 파악하라.
2. 부족한 영역에 대해 웹 검색 쿼리를 최대 5개 생성하라.
3. 각 쿼리는 학술 논문, 기술 블로그, 공식 문서 등을 찾을 수 있는 구체적인 영문 쿼리여야 한다.

## 출력 형식 (반드시 JSON)
```json
{{
  "sufficient_areas": ["이미 충분한 영역1", ...],
  "gap_areas": ["부족한 영역1", ...],
  "search_queries": ["query1", "query2", ...]
}}
```"""
        gap_result = self._call_llm(RESEARCH_LIBRARIAN, gap_prompt)
        queries = self._extract_search_queries(gap_result)

        # Step 3: Web search for each query
        web_sources = []
        web_raw_texts = []
        if queries and hasattr(self.backend, "search_web"):
            for query in queries[:5]:
                try:
                    raw_text, parsed = self._web_search(query, chapter_id, brief)
                    web_sources.extend(parsed)
                    if raw_text:
                        web_raw_texts.append(raw_text)
                except Exception:
                    continue  # Skip failed searches

        # Step 4: Build final bundle with local + web sources
        all_local_block = self._format_registry(local_sources) if local_sources else "없음"
        if web_sources:
            web_block = self._format_web_sources(web_sources)
        elif web_raw_texts:
            # Parsing failed but we have raw search results — pass them directly
            web_block = "\n\n---\n\n".join(web_raw_texts[:3000])
        else:
            web_block = "없음"

        bundle_prompt = f"""다음 장에 필요한 source bundle을 작성하라.

## 장 정보
- chapter_id: {chapter_id}

## Chapter Brief
{brief}

## 프로젝트 맥락
{context_block}

## 확보된 로컬 Source (registry에 등록된 것)
{all_local_block}

## 웹 검색으로 찾은 Source
{web_block}

## 중요 규칙
- core_sources와 supporting_sources에는 **위에 나열된 실제 source만** 포함하라.
- 존재하지 않는 source를 만들어내지 마라. 네가 알고있는 논문이라도 위 목록에 없으면 포함하지 마라.
- 로컬 source의 source_id는 registry의 id를 그대로 사용하라.
- 웹 검색 source의 source_id는 web_ 접두사를 붙여라 (예: web_01).
- 웹 검색으로 찾은 source가 있다면 **반드시** core_sources 또는 supporting_sources에 포함하라.

## 출력
1. bundle.yaml 내용을 ```yaml 코드 블록으로 출력하라.
2. 이어서 source pack notes를 Markdown으로 작성하라.
"""
        result = self._call_llm(RESEARCH_LIBRARIAN, bundle_prompt)

        pack_dir = self.root / f"sources/chapter_packs/{chapter_id}"
        pack_dir.mkdir(parents=True, exist_ok=True)
        self._parse_and_write(result, chapter_id, pack_dir)

    def _web_search(self, query: str, chapter_id: str, brief: str) -> tuple[str, list[dict]]:
        """Search the web and return (raw_text, parsed_entries)."""
        search_prompt = f"""다음 검색 쿼리에 대해 조사하고, 이 장의 집필에 참고할 만한 자료를 찾아 정리하라.

검색 쿼리: {query}

이 자료가 사용될 장의 brief (요약):
{brief[:500]}

## 출력 형식 (반드시 JSON)
찾은 자료를 다음 형식으로 정리하라. 실제로 존재하는 자료만 포함하라.
```json
[
  {{
    "title": "논문/글 제목",
    "authors": ["저자1"],
    "year": 2024,
    "type": "academic_paper | blog_post | documentation | industry_report",
    "url": "실제 URL",
    "summary": "이 장에서 어떻게 활용할 수 있는지 2-3문장",
    "key_claims": ["핵심 주장1", "핵심 주장2"]
  }}
]
```"""
        result = self.backend.search_web(search_prompt, max_tokens=4096)

        # Save raw search result
        search_dir = self.root / f"sources/raw/web_searches/{chapter_id}"
        search_dir.mkdir(parents=True, exist_ok=True)
        safe_query = re.sub(r'[^\w\s-]', '', query)[:50].strip().replace(' ', '_')
        write_text(search_dir / f"{safe_query}.md", f"# Search: {query}\n\n{result}")

        return result, self._parse_web_results(result)

    def _parse_web_results(self, text: str) -> list[dict]:
        """Extract structured source entries from web search results."""
        match = re.search(r"```json\s*\n(.*?)\n```", text, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                pass
        try:
            data = json.loads(text)
            if isinstance(data, list):
                return data
        except (json.JSONDecodeError, ValueError):
            pass
        return []

    def _extract_search_queries(self, text: str) -> list[str]:
        """Extract search queries from gap analysis result."""
        parsed = self._parse_json_response(text)
        if parsed and "search_queries" in parsed:
            return parsed["search_queries"]
        return []

    def _format_web_sources(self, sources: list[dict]) -> str:
        lines = []
        for i, s in enumerate(sources):
            title = s.get("title", "Unknown")
            url = s.get("url", "")
            authors = ", ".join(s.get("authors", []))
            year = s.get("year", "")
            summary = s.get("summary", "")
            lines.append(f"- web_{i+1:02d}: {title} ({year}, {authors})\n  URL: {url}\n  요약: {summary}")
        return "\n".join(lines)

    def _parse_and_write(self, result: str, chapter_id: str, pack_dir: Path) -> None:
        """Parse LLM output into bundle.yaml and notes.md."""
        import yaml as yaml_mod

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
            notes_content = result[yaml_match.end():].strip()
            if notes_content.startswith("```"):
                notes_content = notes_content[3:].strip()
        else:
            self._write_default_bundle(pack_dir, chapter_id)
            notes_content = result

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
            local_path = s.get("local_path", "")
            lines.append(f"- {sid}: {title} (authority={authority}, topics=[{topics}], path={local_path})")
        return "\n".join(lines)
