from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from bookharness.memory.loader import MemoryLoader
from bookharness.orchestrator.state_manager import StateManager
from bookharness.utils.io import read_text
from bookharness.utils.yaml_utils import load_yaml


class MetadataIndex:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.db_path = root / "workflow/metadata.db"
        self.loader = MemoryLoader(root)
        self.state_manager = StateManager(root)
        self._ensure_schema()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _ensure_schema(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS chapters (
                    chapter_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    current_stage TEXT NOT NULL,
                    approved INTEGER NOT NULL,
                    latest_draft TEXT,
                    source_pack_ready INTEGER NOT NULL,
                    outline_ready INTEGER NOT NULL,
                    updated_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS workflow_runs (
                    job_id TEXT PRIMARY KEY,
                    chapter_id TEXT NOT NULL,
                    job_type TEXT NOT NULL,
                    status TEXT NOT NULL,
                    actor TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    finished_at TEXT,
                    error TEXT
                );
                CREATE TABLE IF NOT EXISTS approvals (
                    chapter_id TEXT NOT NULL,
                    approval_key TEXT NOT NULL,
                    result TEXT NOT NULL,
                    notes_json TEXT NOT NULL,
                    PRIMARY KEY (chapter_id, approval_key)
                );
                CREATE TABLE IF NOT EXISTS artifacts (
                    chapter_id TEXT NOT NULL,
                    artifact_key TEXT NOT NULL,
                    relative_path TEXT NOT NULL,
                    PRIMARY KEY (chapter_id, artifact_key)
                );
                CREATE TABLE IF NOT EXISTS review_scores (
                    chapter_id TEXT NOT NULL,
                    review_type TEXT NOT NULL,
                    score_json TEXT NOT NULL,
                    PRIMARY KEY (chapter_id, review_type)
                );
                CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    actor TEXT NOT NULL,
                    details_json TEXT NOT NULL
                );
                """
            )

    def sync_all(self) -> None:
        self.sync_chapters()
        self.sync_approvals()
        self.sync_runs()
        self.sync_audit_log()

    def sync_chapters(self) -> None:
        states_dir = self.root / "workflow/chapter_states"
        with self._connect() as conn:
            for path in sorted(states_dir.glob("*_state.json")):
                state = self.state_manager.load(path.stem.replace("_state", ""))
                conn.execute(
                    """
                    INSERT INTO chapters(chapter_id, title, status, current_stage, approved, latest_draft, source_pack_ready, outline_ready, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(chapter_id) DO UPDATE SET
                        title=excluded.title,
                        status=excluded.status,
                        current_stage=excluded.current_stage,
                        approved=excluded.approved,
                        latest_draft=excluded.latest_draft,
                        source_pack_ready=excluded.source_pack_ready,
                        outline_ready=excluded.outline_ready,
                        updated_at=excluded.updated_at
                    """,
                    (
                        state.chapter_id,
                        state.title,
                        state.status,
                        state.current_stage,
                        int(state.approved),
                        state.latest_draft,
                        int(state.source_pack_ready),
                        int(state.outline_ready),
                        state.last_updated,
                    ),
                )
                conn.execute("DELETE FROM artifacts WHERE chapter_id = ?", (state.chapter_id,))
                for artifact_key, relative_path in state.artifacts.items():
                    conn.execute(
                        "INSERT OR REPLACE INTO artifacts(chapter_id, artifact_key, relative_path) VALUES (?, ?, ?)",
                        (state.chapter_id, artifact_key, relative_path),
                    )
                reports_dir = self.root / "eval/reports"
                for report_path in reports_dir.glob(f"{state.chapter_id}_*_v1.json"):
                    review_type = report_path.stem.replace(f"{state.chapter_id}_", "").replace("_v1", "")
                    conn.execute(
                        "INSERT OR REPLACE INTO review_scores(chapter_id, review_type, score_json) VALUES (?, ?, ?)",
                        (state.chapter_id, review_type, read_text(report_path)),
                    )
            conn.commit()

    def sync_approvals(self) -> None:
        approvals = load_yaml(self.root / "workflow/approvals/approvals.yaml") or {}
        with self._connect() as conn:
            conn.execute("DELETE FROM approvals")
            for chapter_id, entries in approvals.items():
                for approval_key, payload in entries.items():
                    conn.execute(
                        "INSERT INTO approvals(chapter_id, approval_key, result, notes_json) VALUES (?, ?, ?, ?)",
                        (chapter_id, approval_key, payload.get("result", ""), json_dumps(payload.get("notes", []))),
                    )
            conn.commit()

    def sync_runs(self) -> None:
        runs_dir = self.root / "workflow/runs"
        with self._connect() as conn:
            for path in sorted(runs_dir.glob("*.json")):
                payload = load_yaml(path) or {}
                conn.execute(
                    """
                    INSERT OR REPLACE INTO workflow_runs(job_id, chapter_id, job_type, status, actor, created_at, started_at, finished_at, error)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        payload.get("job_id"),
                        payload.get("chapter_id", ""),
                        payload.get("job_type", ""),
                        payload.get("status", ""),
                        payload.get("actor", "system"),
                        payload.get("created_at", ""),
                        payload.get("started_at"),
                        payload.get("finished_at"),
                        payload.get("error"),
                    ),
                )
            conn.commit()

    def sync_audit_log(self) -> None:
        audit_path = self.root / "workflow/audit_log.jsonl"
        with self._connect() as conn:
            conn.execute("DELETE FROM audit_log")
            if audit_path.exists():
                for line in audit_path.read_text(encoding="utf-8").splitlines():
                    if not line.strip():
                        continue
                    payload = load_yaml_from_json_line(line)
                    conn.execute(
                        "INSERT INTO audit_log(timestamp, event_type, actor, details_json) VALUES (?, ?, ?, ?)",
                        (
                            payload.get("timestamp", ""),
                            payload.get("event_type", ""),
                            payload.get("actor", "system"),
                            json_dumps(payload.get("details", {})),
                        ),
                    )
            conn.commit()

    def list_chapters(self) -> list[dict[str, Any]]:
        self.sync_all()
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM chapters ORDER BY chapter_id").fetchall()
            return [dict(row) for row in rows]

    def list_runs(self, limit: int = 20) -> list[dict[str, Any]]:
        self.sync_all()
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM workflow_runs ORDER BY created_at DESC LIMIT ?", (limit,)).fetchall()
            return [dict(row) for row in rows]

    def list_pending_approvals(self) -> list[dict[str, Any]]:
        self.sync_all()
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT c.chapter_id, c.title, c.status, a.approval_key, a.result, a.notes_json
                FROM chapters c
                LEFT JOIN approvals a ON a.chapter_id = c.chapter_id
                WHERE c.status IN ('awaiting_human_outline_approval', 'awaiting_human_draft_approval')
                ORDER BY c.chapter_id
                """
            ).fetchall()
            return [dict(row) for row in rows]


def json_dumps(payload: Any) -> str:
    import json

    return json.dumps(payload, ensure_ascii=False)


def load_yaml_from_json_line(line: str) -> dict[str, Any]:
    import json

    return json.loads(line)
