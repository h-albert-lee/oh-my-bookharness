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


@router.get("/activity")
def get_activity(request: Request):
    """Return recent activity summary — is something running, what was the last call, etc."""
    from datetime import datetime, timezone

    root: Path = request.app.state.project_root
    log_path = root / "workflow/agent_logs.jsonl"
    if not log_path.exists():
        return {"active": False, "last_agent": None, "last_timestamp": None, "recent_count": 0}

    entries = []
    for line in log_path.read_text(encoding="utf-8").strip().splitlines():
        if not line.strip():
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    if not entries:
        return {"active": False, "last_agent": None, "last_timestamp": None, "recent_count": 0}

    last = entries[-1]
    last_ts = last.get("timestamp", "")

    # Check if last activity was within 120 seconds
    active = False
    recent_count = 0
    try:
        last_dt = datetime.fromisoformat(last_ts.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        age_sec = (now - last_dt).total_seconds()
        active = age_sec < 120

        # Count entries in last 5 minutes
        for e in reversed(entries):
            ts = e.get("timestamp", "")
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                if (now - dt).total_seconds() < 300:
                    recent_count += 1
                else:
                    break
            except (ValueError, TypeError):
                break
    except (ValueError, TypeError):
        pass

    return {
        "active": active,
        "last_agent": last.get("agent"),
        "last_timestamp": last_ts,
        "last_elapsed": last.get("elapsed_sec"),
        "last_error": last.get("error"),
        "recent_count": recent_count,
    }
