from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import CHAPTER_ARCHITECT
from bookharness.utils.io import write_text


class ChapterArchitectAgent(BaseAgent):
    def build_outline(self, chapter_id: str, title: str) -> Path:
        ctx = self.load_project_context()
        brief = self.load_chapter_brief(chapter_id)
        source_notes = self.load_chapter_source_notes(chapter_id)
        bundle = self.load_chapter_bundle(chapter_id)
        prior_summaries = self.load_prior_summaries()
        context_block = self._build_context_block(ctx)

        summaries_block = "\n\n".join(
            f"### {ch}\n{summary[:300]}" for ch, summary in prior_summaries.items()
        ) if prior_summaries else "없음"

        source_list = "\n".join(
            f"- {s.get('source_id', 'unknown')}: {s.get('why_it_matters', '')}"
            for s in bundle.get("core_sources", []) + bundle.get("supporting_sources", [])
        )

        user_prompt = f"""다음 장의 outline을 설계하라.

## 장 정보
- chapter_id: {chapter_id}
- 제목: {title}

## Chapter Brief
{brief}

## Source Pack
{source_list}

## Source Notes
{source_notes[:2000]}

## 이전 장 요약
{summaries_block}

## 프로젝트 맥락
{context_block}

## 출력 형식
다음을 포함하는 outline.md를 작성하라:
1. 장 제목
2. 장 전체 argument flow (한 문단)
3. 각 Section: 제목, 목적, 사용 source, 포함 예시, 핵심 요점, 앞뒤 연결 아이디어
"""
        content = self._call_llm(CHAPTER_ARCHITECT, user_prompt)
        path = self.root / f"manuscript/{chapter_id}/outline.md"
        write_text(path, content)
        return path
