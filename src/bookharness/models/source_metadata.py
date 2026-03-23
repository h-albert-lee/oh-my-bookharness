from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class SourceMetadata:
    id: str
    title: str
    type: str
    author: str
    published_at: str
    authority: str
    source_kind: str
    topic_tags: list[str]
    relevance_tags: list[str]
    status: str
    url: str | None = None
    local_path: str | None = None
    citation_priority: str | None = None
    claims_supported: list[str] = field(default_factory=list)
    caution_notes: list[str] = field(default_factory=list)
    review_status: str | None = None
    normalized_note_path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
