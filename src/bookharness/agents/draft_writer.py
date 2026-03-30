from __future__ import annotations

import re
from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import DRAFT_WRITER
from bookharness.manuscript.versioning import next_draft_path
from bookharness.utils.io import write_text


class DraftWriterAgent(BaseAgent):
    def _get_expected_pages(self, ctx: dict, chapter_id: str) -> int:
        ch_deps = ctx.get("chapter_dependencies", {})
        ch_info = ch_deps.get(chapter_id, {}) if isinstance(ch_deps, dict) else {}
        if isinstance(ch_info, dict):
            return ch_info.get("expected_pages", 20)
        return 20

    def _parse_sections_from_outline(self, outline: str) -> list[dict]:
        """Parse outline into a list of section dicts with title and full content."""
        sections: list[dict] = []
        # Split by ### Section headers
        parts = re.split(r"(?=^### Section \d+)", outline, flags=re.MULTILINE)
        for part in parts:
            part = part.strip()
            if not part.startswith("### Section"):
                continue
            # Extract section number and title from first line
            first_line = part.split("\n")[0]
            m = re.match(r"### Section (\d+)\.\s*(.*)", first_line)
            if m:
                sections.append({
                    "number": int(m.group(1)),
                    "title": m.group(2).strip(),
                    "outline_detail": part,
                })
        # Fallback: if no sections parsed, try ## level headings
        if not sections:
            parts = re.split(r"(?=^## )", outline, flags=re.MULTILINE)
            for i, part in enumerate(parts):
                part = part.strip()
                if not part.startswith("##"):
                    continue
                first_line = part.split("\n")[0].lstrip("# ").strip()
                sections.append({
                    "number": i,
                    "title": first_line,
                    "outline_detail": part,
                })
        return sections

    def _write_section(
        self,
        *,
        chapter_id: str,
        title: str,
        section: dict,
        section_index: int,
        total_sections: int,
        target_chars_per_section: int,
        brief: str,
        source_notes: str,
        context_block: str,
        summaries_block: str,
        previous_sections: str,
        next_section_title: str | None,
        revision_section: str,
    ) -> str:
        """Write a single section with full context of what came before."""
        position_guide = ""
        if section_index == 0:
            position_guide = (
                "이 섹션은 장의 **도입부**다. 독자에게 이 장에서 무엇을 다루는지 안내하라. "
                "선언문처럼 시작하지 말고, 질문이나 상황 묘사로 시작하라."
            )
        elif section_index == total_sections - 1:
            position_guide = (
                "이 섹션은 장의 **마무리**다. 핵심 내용을 정리하고 다음 장으로의 연결을 예고하라. "
                "새로운 개념을 도입하지 말고, 앞 내용을 통합적으로 정리하라."
            )
        else:
            position_guide = "이 섹션은 장의 **본론** 부분이다."

        transition_guide = ""
        if previous_sections:
            transition_guide = (
                "중요: 이 섹션의 시작부에서 직전 섹션 내용을 자연스럽게 받아 이어 써야 한다. "
                "갑자기 새로운 이야기가 시작되는 느낌이 들지 않도록 앞 내용과의 연결 문장을 넣어라. "
                "예: '앞에서 ~를 살펴보았다. 이제 ~로 넘어가자.', '~가 왜 필요한지 이해했으니, 이번에는 ~를 구체적으로 들여다보자.'"
            )
        if next_section_title:
            transition_guide += (
                f"\n이 섹션의 끝에서 다음 섹션('{next_section_title}')으로의 자연스러운 전환을 만들어라. "
                "다음 내용이 왜 필요한지를 독자가 느낄 수 있게 하라."
            )

        prev_context = ""
        if previous_sections:
            # Give the last ~3000 chars of previous sections for continuity
            prev_tail = previous_sections[-3000:] if len(previous_sections) > 3000 else previous_sections
            prev_context = f"""
## 이 섹션 직전까지 작성된 내용 (연결성 참고용)
{prev_tail}
"""

        user_prompt = f"""다음 장의 특정 섹션 하나를 작성하라.

## 장 정보
- chapter_id: {chapter_id}
- 장 제목: {title}
- 현재 작성할 섹션: Section {section['number']}. {section['title']} ({section_index + 1}/{total_sections})

## 위치 안내
{position_guide}

## 연결성 지침
{transition_guide}

## 이 섹션의 Outline
{section['outline_detail']}

## Chapter Brief (요약)
{brief[:1500]}

## Source Pack Notes
{source_notes[:2000]}

## 이전 장 요약
{summaries_block}

## 프로젝트 맥락 (핵심만)
{context_block[:2000]}
{prev_context}
{revision_section}

## 작성 규칙
1. 이 섹션의 outline 내용을 빠짐없이 작성한다.
2. 최소 3개 문단 이상으로 구성한다.
3. source pack에 있는 자료를 참조할 때는 [^source_id] 형식으로 각주를 단다.
4. concept_dictionary의 용어를 정확히 사용한다.
5. 첫 등장하는 전문 용어는 한국어 설명을 함께 제공한다.
6. 목표 분량: 이 섹션은 약 {target_chars_per_section}자 내외로 작성한다.
7. 분량이 부족하면 예시, 비유, 실무 사례를 추가하여 채운다.
8. ## 레벨 헤딩으로 섹션 제목을 시작한다.
9. 이 섹션만 출력하라. 다른 섹션의 내용은 작성하지 마라.
"""
        return self._call_llm(DRAFT_WRITER, user_prompt, max_tokens=8192)

    def write(self, chapter_id: str, title: str, revision_mode: bool = False) -> Path:
        ctx = self.load_project_context()
        brief = self.load_chapter_brief(chapter_id)
        outline = self.load_chapter_outline(chapter_id)
        source_notes = self.load_chapter_source_notes(chapter_id)
        prior_summaries = self.load_prior_summaries()
        context_block = self._build_context_block(ctx)
        expected_pages = self._get_expected_pages(ctx, chapter_id)
        target_chars = expected_pages * 1000

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
{revision_plan[:2000]}

## Previous Draft 해당 섹션 참고용
{previous_draft[:3000]}

중요: 위 revision plan의 must_fix 항목을 반드시 반영하라. should_fix도 가능하면 반영하라.
"""

        # Parse sections from outline
        sections = self._parse_sections_from_outline(outline)

        if not sections:
            # Fallback: single-shot writing for outlines without clear sections
            return self._write_single_shot(
                chapter_id, title, revision_mode,
                ctx, brief, outline, source_notes, prior_summaries,
                context_block, expected_pages, target_chars,
            )

        # Distribute target chars across sections
        target_per_section = target_chars // len(sections)

        # Write section by section
        completed_sections: list[str] = []
        for i, section in enumerate(sections):
            next_title = sections[i + 1]["title"] if i + 1 < len(sections) else None
            previous_text = "\n\n".join(completed_sections)

            section_content = self._write_section(
                chapter_id=chapter_id,
                title=title,
                section=section,
                section_index=i,
                total_sections=len(sections),
                target_chars_per_section=target_per_section,
                brief=brief,
                source_notes=source_notes,
                context_block=context_block,
                summaries_block=summaries_block,
                previous_sections=previous_text,
                next_section_title=next_title,
                revision_section=revision_section if revision_mode else "",
            )
            completed_sections.append(section_content)

        # Combine all sections into final draft
        full_draft = f"# {title}\n\n" + "\n\n".join(completed_sections)

        chapter_dir = self.root / f"manuscript/{chapter_id}"
        path = next_draft_path(chapter_dir)
        write_text(path, full_draft)
        return path

    def _write_single_shot(
        self,
        chapter_id: str, title: str, revision_mode: bool,
        ctx: dict, brief: str, outline: str, source_notes: str,
        prior_summaries: dict, context_block: str,
        expected_pages: int, target_chars: int,
    ) -> Path:
        """Fallback: write entire chapter in one LLM call (for short chapters or unparseable outlines)."""
        target_words = target_chars // 3
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
- 목표 분량: {expected_pages}쪽 (약 {target_chars}자, {target_words}단어 이상)

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
8. 목표 분량({expected_pages}쪽, 약 {target_chars}자)에 맞춰 작성한다. 최소 {target_words}단어 이상.
9. 분량이 부족하면 예시, 비유, 실무 사례를 추가하여 채운다.
"""
        adjusted_max_tokens = max(8192, expected_pages * 2000)
        content = self._call_llm(DRAFT_WRITER, user_prompt, max_tokens=adjusted_max_tokens)

        chapter_dir = self.root / f"manuscript/{chapter_id}"
        path = next_draft_path(chapter_dir)
        write_text(path, content)
        return path
