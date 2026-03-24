from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import DRAFT_WRITER
from bookharness.manuscript.versioning import next_draft_path
from bookharness.utils.io import write_text


class DraftWriterAgent(BaseAgent):
    def write(self, chapter_id: str, title: str, revision_mode: bool = False) -> Path:
        ctx = self.load_project_context()
        brief = self.load_chapter_brief(chapter_id)
        outline = self.load_chapter_outline(chapter_id)
        source_notes = self.load_chapter_source_notes(chapter_id)
        prior_summaries = self.load_prior_summaries()
        context_block = self._build_context_block(ctx)

        summaries_block = "\n\n".join(
            f"### {ch}\n{summary[:300]}" for ch, summary in prior_summaries.items()
        ) if prior_summaries else "없음"

        revision_section = ""
        if revision_mode:
            revision_plan = self.load_revision_plan(chapter_id)
            previous_draft = self.load_latest_draft(chapter_id)
            if revision_plan:
                revision_section = f"""
## Revision Plan (수정 지시)
{revision_plan}

## Previous Draft (이전 초안)
{previous_draft[:4000]}

중요: 위 revision plan의 must_fix 항목을 반드시 반영하라. should_fix도 가능하면 반영하라.
"""

        user_prompt = f"""다음 장의 {'수정된 ' if revision_mode else ''}초안을 작성하라.

## 장 정보
- chapter_id: {chapter_id}
- 제목: {title}

## Chapter Brief
{brief}

## Outline
{outline}

## Source Pack Notes
{source_notes[:3000]}

## 이전 장 요약
{summaries_block}

## 프로젝트 맥락
{context_block}
{revision_section}

## 작성 규칙
1. outline의 각 Section을 빠짐없이 작성한다.
2. 각 섹션은 최소 3개 문단으로 구성한다.
3. source pack에 있는 자료를 참조할 때는 [^source_id] 형식으로 각주를 단다.
4. concept_dictionary의 용어를 정확히 사용한다.
5. 첫 등장하는 전문 용어는 한국어 설명을 함께 제공한다.
6. 장 도입부에서 독자에게 이 장에서 다루는 내용을 안내한다.
7. 각 섹션 전환부에서 앞 내용을 간략히 요약하고 다음 내용을 예고한다.
8. 최소 2000단어 이상 작성한다.
"""
        content = self._call_llm(DRAFT_WRITER, user_prompt, max_tokens=16384)

        chapter_dir = self.root / f"manuscript/{chapter_id}"
        path = next_draft_path(chapter_dir)
        write_text(path, content)
        return path
