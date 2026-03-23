from __future__ import annotations

CHAPTER_STATUSES = {
    "not_started",
    "brief_generated",
    "source_collection_done",
    "source_analysis_done",
    "outline_ready",
    "awaiting_human_outline_approval",
    "draft_generated",
    "auto_review_done",
    "revision_ready",
    "awaiting_human_draft_approval",
    "chapter_approved",
    "locked",
}

APPROVAL_RESULTS = {
    "approved",
    "approved_with_notes",
    "revision_requested",
    "rejected",
}

REQUIRED_BOOK_DOCS = [
    "book/blueprint.md",
    "book/tone_guide.md",
    "book/argument_map.md",
    "book/concept_dictionary.yaml",
    "book/chapter_dependencies.yaml",
    "book/decisions_log.md",
]
