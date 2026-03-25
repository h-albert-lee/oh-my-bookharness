from __future__ import annotations

import json
from pathlib import Path

from fastapi import APIRouter, Query, Request

router = APIRouter(prefix="/api/agent-logs", tags=["agent-logs"])


@router.get("")
def get_agent_logs(
    request: Request,
    agent: str | None = Query(None),
    limit: int = Query(100, ge=1, le=1000),
):
    root: Path = request.app.state.project_root
    log_path = root / "workflow/agent_logs.jsonl"
    if not log_path.exists():
        return []

    entries = []
    for line in log_path.read_text(encoding="utf-8").strip().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if agent and entry.get("agent") != agent:
            continue
        entries.append(entry)

    # Return most recent first
    entries.reverse()
    return entries[:limit]


@router.get("/agents")
def list_agents(request: Request):
    """Return distinct agent names from the log."""
    root: Path = request.app.state.project_root
    log_path = root / "workflow/agent_logs.jsonl"
    if not log_path.exists():
        return []

    agents = set()
    for line in log_path.read_text(encoding="utf-8").strip().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            agents.add(entry.get("agent", "unknown"))
        except json.JSONDecodeError:
            continue
    return sorted(agents)
