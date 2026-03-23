from __future__ import annotations

from pathlib import Path

from bookharness.utils.io import write_text


def ensure_memory_files(root: Path) -> None:
    defaults = {
        "memory/global_summary.md": "# Global Summary\n\n- 승인된 장이 아직 없습니다.",
        "memory/unresolved_questions.md": "# Unresolved Questions\n\n- 아직 기록된 질문이 없습니다.",
        "memory/recurring_examples.md": "# Recurring Examples\n\n- 아직 등록된 반복 사례가 없습니다.",
    }
    for relative_path, content in defaults.items():
        path = root / relative_path
        if not path.exists():
            write_text(path, content)
