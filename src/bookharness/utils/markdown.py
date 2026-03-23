from __future__ import annotations


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- 없음"


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body.strip()}\n"
