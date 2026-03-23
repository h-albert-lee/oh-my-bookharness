from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bookharness.utils.io import ensure_parent
from bookharness_api.services.helpers import utc_now


class AuditService:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.path = root / "workflow/audit_log.jsonl"

    def record(self, event_type: str, actor: str, details: dict[str, Any]) -> None:
        ensure_parent(self.path)
        payload = {
            "timestamp": utc_now(),
            "event_type": event_type,
            "actor": actor,
            "details": details,
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines[-limit:]][::-1]
