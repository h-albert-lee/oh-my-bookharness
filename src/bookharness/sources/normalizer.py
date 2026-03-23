from __future__ import annotations

from pathlib import Path

from bookharness.utils.io import write_text


class SourceNormalizer:
    def __init__(self, root: Path) -> None:
        self.root = root

    def create_note(self, source_id: str, chapter_id: str) -> Path:
        path = self.root / f"sources/normalized/{source_id}.md"
        body = f"""# Source Note: {source_id}

## 핵심 주장

- TODO: source의 핵심 주장을 요약한다.

## 책에 활용 가능한 포인트

- TODO: 책의 논지와 연결되는 활용 포인트를 적는다.

## 이 장과의 관련성

- 대상 장: {chapter_id}

## 주의할 점 / 한계

- TODO: 자료의 한계나 과장 가능성을 적는다.

## 인용 시 주의 표현

- TODO: 단정 표현을 피해야 하는 지점을 적는다.
"""
        write_text(path, body)
        return path
