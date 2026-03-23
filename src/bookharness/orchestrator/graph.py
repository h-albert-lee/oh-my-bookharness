from __future__ import annotations

STAGE_ORDER = [
    "chapter_initialization",
    "brief_generation",
    "source_collection",
    "source_analysis",
    "outline_design",
    "human_approval_a",
    "draft_writing",
    "automated_review",
    "revision_plan_synthesis",
    "draft_revision",
    "human_approval_b",
]

TERMINAL_STAGES = {"human_approval_a", "human_approval_b"}
