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
        bundle = read_text(self.root / f"sources/chapter_packs/{chapter_id}/notes.md")
        revision_plan = ""
        if revision_mode and (chapter_dir / "revision_plan_v1.md").exists():
            revision_plan = read_text(chapter_dir / "revision_plan_v1.md")
        path = next_draft_path(chapter_dir)
        body = f"""# {title}

이 장은 독자에게 무엇을 다루는지 먼저 설명하고, 왜 AI 시스템 집필 자동화가 상태 기반 워크플로를 필요로 하는지 단계적으로 안내한다.

## 문제 설정

초안 생성만으로는 책 전체의 품질을 유지하기 어렵다. 장기 집필에서는 장별 상태, 승인 여부, 참고문헌 묶음, 리뷰 이력이 모두 추적 가능해야 한다. 따라서 이 시스템은 자유로운 대화형 협업보다 재현 가능한 단계 중심 워크플로를 우선한다.

## 상태 기반 워크플로

각 장은 brief, source collection, source analysis, outline, draft, review, revision, approval 단계를 거친다. 각 단계는 입력 문서와 출력 산출물이 명확해야 하며, 실패 시 해당 단계만 다시 실행할 수 있어야 한다. 인간 승인 게이트는 outline과 revised draft 이후에 명시적으로 배치한다.

## 문서 중심 메모리

긴 문맥을 모델의 암묵적 기억에 맡기지 않고, blueprint, tone guide, argument map, concept dictionary, chapter summaries 같은 canonical 문서를 읽어 작업한다. 승인된 장만 global summary에 반영하고, draft 상태의 내용은 canonical memory로 승격하지 않는다.

## 리뷰와 수정

초안 뒤에는 기술 리뷰, 스타일 리뷰, 연속성 리뷰를 분리해 수행한다. 이후 revision synthesizer가 must-fix와 should-fix를 정리하고, writer는 그 계획에 따라 다음 버전을 만든다. 이렇게 하면 생성보다 리뷰와 승인 구조가 더 엄격한 편집 시스템을 구현할 수 있다.

## 입력 문서 발췌

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
