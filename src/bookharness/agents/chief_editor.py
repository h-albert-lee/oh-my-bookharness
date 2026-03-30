from __future__ import annotations

from pathlib import Path

from bookharness.agents.base import BaseAgent
from bookharness.agents.prompts import CHIEF_EDITOR
from bookharness.utils.io import write_text


class ChiefEditorAgent(BaseAgent):
    def generate_brief(
        self,
        chapter_id: str,
        title: str,
        dependencies: list[str],
        prior_summaries: list[str],
    ) -> Path:
        ctx = self.load_project_context()
        context_block = self._build_context_block(ctx)
        deps_block = "\n".join(f"- {d}" for d in dependencies) if dependencies else "- 없음"
        summaries_block = "\n".join(f"- {s}" for s in prior_summaries) if prior_summaries else "- 아직 승인된 이전 장 요약이 없다."

        ch_deps = ctx.get("chapter_dependencies", {})
        ch_info = ch_deps.get(chapter_id, {}) if isinstance(ch_deps, dict) else {}
        if isinstance(ch_info, dict):
            introduces = ch_info.get("introduces", [])
            depends_on = ch_info.get("depends_on", [])
            required_by = ch_info.get("required_by", [])
            expected_pages = ch_info.get("expected_pages", 20)
            ch_note = ch_info.get("note", "")
        else:
            introduces, depends_on, required_by = [], [], []
            expected_pages = 20
            ch_note = ""

        user_prompt = f"""다음 장에 대한 chapter brief를 작성하라.

## 장 정보
- chapter_id: {chapter_id}
- 제목: {title}
- 예상 분량: {expected_pages}쪽 (46배변형판 기준, 쪽당 약 1000자)
- 총 예상 글자 수: 약 {expected_pages * 1000}자
- 장 메모: {ch_note}
- 의존 장: {deps_block}
- 이 장이 도입하는 개념: {', '.join(introduces) if introduces else '미정'}
- 이 장이 의존하는 개념: {', '.join(depends_on) if depends_on else '없음'}
- 이 장을 필요로 하는 후속 장: {', '.join(required_by) if required_by else '미정'}

## 프로젝트 맥락
{context_block}

## 이전 장 요약
{summaries_block}

## 출력 형식
다음 섹션을 반드시 포함하는 Markdown을 작성하라:
1. 이 장의 목표
2. 독자가 얻을 것
3. 장의 핵심 질문
4. 반드시 들어갈 개념
5. 피해야 할 오해
6. 앞 장과의 연결
7. 뒤 장으로의 연결
8. 원하는 톤 메모
9. 참고할 이전 장 요약
"""
        content = self._call_llm(CHIEF_EDITOR, user_prompt)
        path = self.root / f"manuscript/{chapter_id}/brief.md"
        write_text(path, content)
        return path
