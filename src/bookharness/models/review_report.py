from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class ReviewReport:
    chapter_id: str
    review_type: str
    score: dict[str, int]
    must_fix: list[str] = field(default_factory=list)
    should_fix: list[str] = field(default_factory=list)
    nice_to_have: list[str] = field(default_factory=list)
    binary_checks: dict[str, bool] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
