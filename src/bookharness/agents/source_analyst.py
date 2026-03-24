from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import SOURCE_ANALYST
from bookharness.utils.io import read_text, write_text
from bookharness.utils.yaml_utils import load_yaml


class SourceAnalystAgent(BaseAgent):
    def analyze(self, chapter_id: str) -> None:
        ctx = self.load_project_context()
        brief = self.load_chapter_brief(chapter_id)
        bundle = self.load_chapter_bundle(chapter_id)
        context_block = self._build_context_block(ctx)

        all_sources = []
        for key in ("core_sources", "supporting_sources"):
            all_sources.extend(bundle.get(key, []))

        for item in all_sources:
            sid = item.get("source_id", "")
            raw_content = self._load_raw_source(sid)
            self._create_note(sid, chapter_id, item, raw_content, brief, context_block)

        pack_dir = self.root / f"sources/chapter_packs/{chapter_id}"
        self._write_must_cite(pack_dir, chapter_id, bundle, brief, context_block)
        self._write_counterpoints(pack_dir, chapter_id, brief, context_block)

    def _load_raw_source(self, source_id: str) -> str:
        for raw_dir in ("papers", "blogs", "talks", "docs", "interviews"):
            for ext in (".md", ".txt"):
                path = self.root / f"sources/raw/{raw_dir}/{source_id}{ext}"
                if path.exists():
                    return read_text(path)[:3000]
        norm_path = self.root / f"sources/normalized/{source_id}.md"
        if norm_path.exists():
            return read_text(norm_path)[:3000]
        return ""

    def _create_note(
        self, source_id: str, chapter_id: str, item: dict,
        raw_content: str, brief: str, context_block: str,
    ) -> Path:
        user_prompt = f"""다음 source를 분석하고 장 집필용 note를 작성하라.

## Source 정보
- source_id: {source_id}
- title: {item.get('title', source_id)}
- authority: {item.get('authority', 'unknown')}
- 활용 방향: {item.get('why_it_matters', '')}
- 예상 사용처: {item.get('expected_usage', '')}

## Source 원문 (발췌)
{raw_content if raw_content else '(원문이 등록되지 않았다. metadata 기반으로 분석하라.)'}

## Chapter Brief
{brief[:1500]}

## 프로젝트 맥락
{context_block[:2000]}

## 출력 형식
다음 섹션을 포함하는 Markdown을 작성하라:
1. 핵심 주장
2. 책에 활용 가능한 포인트
3. 이 장과의 관련성
4. 주의할 점 / 한계
5. 인용 시 주의 표현
"""
        content = self._call_llm(SOURCE_ANALYST, user_prompt)
        path = self.root / f"sources/normalized/{source_id}.md"
        write_text(path, content)
        return path

    def _write_must_cite(self, pack_dir: Path, chapter_id: str, bundle: dict, brief: str, context_block: str) -> None:
        core = bundle.get("core_sources", [])
        core_info = "\n".join(
            f"- {s.get('source_id', '')}: {s.get('title', '')} — {s.get('why_it_matters', '')}"
            for s in core
        )
        user_prompt = f"""다음 core source 목록에서 반드시 인용해야 할 항목을 정리하라.

## Core Sources
{core_info}

## Chapter Brief
{brief[:1000]}

## 출력 형식
# Must Cite 형태의 Markdown을 작성하라. 각 source에 대해 인용 이유를 포함한다.
"""
        content = self._call_llm(SOURCE_ANALYST, user_prompt)
        write_text(pack_dir / "must_cite.md", content)

    def _write_counterpoints(self, pack_dir: Path, chapter_id: str, brief: str, context_block: str) -> None:
        user_prompt = f"""이 장의 논지에 대한 반론, 한계, 과장 가능성을 정리하라.

## Chapter Brief
{brief[:1000]}

## 프로젝트 맥락
{context_block[:1500]}

## 출력 형식
# Counterpoints 형태의 Markdown을 작성하라.
- 예상 반론
- 과장 가능성
- 미해결 쟁점
"""
        content = self._call_llm(SOURCE_ANALYST, user_prompt)
        write_text(pack_dir / "counterpoints.md", content)
