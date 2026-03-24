"""Draft composition utilities.

The DraftComposer is kept for backward compatibility but the primary
draft generation now happens in DraftWriterAgent.
"""

from __future__ import annotations

from pathlib import Path

from bookharness.manuscript.versioning import next_draft_path
from bookharness.utils.io import read_text, write_text


class DraftComposer:
    def __init__(self, root: Path) -> None:
        self.root = root

    def create_draft(self, chapter_id: str, title: str, revision_mode: bool = False) -> Path:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        brief = read_text(chapter_dir / "brief.md")
        outline = read_text(chapter_dir / "outline.md")
        bundle_path = self.root / f"sources/chapter_packs/{chapter_id}/notes.md"
        bundle = read_text(bundle_path) if bundle_path.exists() else ""

        revision_plan = ""
        if revision_mode:
            plan_files = sorted(chapter_dir.glob("revision_plan_v*.md"))
            if plan_files:
                revision_plan = read_text(plan_files[-1])

        path = next_draft_path(chapter_dir)
        body = f"""# {title}

이 장은 독자에게 무엇을 다루는지 먼저 설명하고, 핵심 개념을 단계적으로 안내한다.

## 문제 설정

{self._extract_section_from_brief(brief, "핵심 질문")}

## 핵심 개념

{self._extract_section_from_brief(brief, "반드시 들어갈 개념")}

## 분석과 사례

source pack의 근거를 바탕으로 핵심 개념을 분석하고 사례를 제시한다.

## 정리

이 장에서 다룬 핵심 메시지를 정리하고 다음 장을 예고한다.

---

### Brief Reference

{brief}

### Source Pack Notes

{bundle}

### Outline Reference

{outline}
"""
        if revision_plan:
            body += f"""

### Revision Plan Applied

{revision_plan}
"""
        write_text(path, body)
        return path

    @staticmethod
    def _extract_section_from_brief(brief: str, section_name: str) -> str:
        items = []
        in_section = False
        for line in brief.splitlines():
            if section_name in line:
                in_section = True
                continue
            if in_section and line.strip().startswith("##"):
                break
            if in_section and line.strip():
                items.append(line)
        return "\n".join(items) if items else f"(brief에서 '{section_name}' 섹션을 확인하라)"
