"""Binary gate checker and review report I/O.

BinaryGateChecker performs cheap, deterministic checks that supplement
the LLM-based reviews. These are binary pass/fail signals, not the review itself.

ReviewIO handles reading/writing ReviewReport objects to disk.
"""

from __future__ import annotations

import re
from pathlib import Path

from bookharness.memory.loader import MemoryLoader
from bookharness.models.review_report import ReviewReport
from bookharness.utils.io import read_json, read_text, write_json, write_text
from bookharness.utils.yaml_utils import load_yaml


# Patterns for binary gate checks
ABSOLUTE_PATTERNS = [r"항상\s", r"절대\s", r"반드시\s", r"무조건\s", r"예외\s*없이\s"]
DECLARATIVE_PATTERNS = [r"혁명적", r"패러다임\s*시프트", r"게임\s*체인저"]
BLOG_PATTERNS = [r"오늘은\s", r"여러분[,!]", r"짜잔", r"놀랍게도"]


class BinaryGateChecker:
    """Deterministic binary checks that supplement LLM reviews."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self._loader = MemoryLoader(root)

    def check(self, chapter_id: str, review_type: str) -> dict[str, bool]:
        draft = self._read_latest_draft(chapter_id)
        if review_type == "technical":
            return self._check_technical(chapter_id, draft)
        elif review_type == "style":
            return self._check_style(draft)
        elif review_type == "continuity":
            return self._check_continuity(chapter_id, draft)
        return {}

    def _check_technical(self, chapter_id: str, draft: str) -> dict[str, bool]:
        has_unsupported = self._has_patterns_without_refs(draft, ABSOLUTE_PATTERNS)
        has_source_refs = bool(re.search(r"\[\^", draft))
        word_count = len(draft.split())

        # Citation verification: check if cited source_ids exist in the bundle
        citation_result = self._verify_citations(chapter_id, draft)

        return {
            "has_unsupported_claims": has_unsupported,
            "has_source_references": has_source_refs,
            "meets_minimum_length": word_count >= 500,
            "all_citations_valid": citation_result["all_valid"],
        }

    def _verify_citations(self, chapter_id: str, draft: str) -> dict:
        """Verify that all [^source_id] citations in the draft reference real sources."""
        # Extract all cited source IDs from the draft
        cited_ids = set(re.findall(r"\[\^(\w+)\]", draft))
        if not cited_ids:
            return {"all_valid": True, "details": "No citations found in draft."}

        # Load known source IDs from bundle + registry
        known_ids = set()

        # From chapter bundle
        bundle_path = self.root / f"sources/chapter_packs/{chapter_id}/bundle.yaml"
        if bundle_path.exists():
            bundle = load_yaml(bundle_path) or {}
            for key in ("core_sources", "supporting_sources"):
                for src in bundle.get(key, []):
                    sid = src.get("source_id") or src.get("id", "")
                    if sid:
                        known_ids.add(sid)

        # From global registry
        registry_path = self.root / "sources/metadata/registry.yaml"
        if registry_path.exists():
            registry = load_yaml(registry_path) or []
            if isinstance(registry, list):
                for src in registry:
                    sid = src.get("id", "")
                    if sid:
                        known_ids.add(sid)

        # Check for normalized source files
        norm_dir = self.root / "sources/normalized"
        if norm_dir.exists():
            for f in norm_dir.glob("*.md"):
                known_ids.add(f.stem)

        # Verify
        valid_ids = cited_ids & known_ids
        invalid_ids = cited_ids - known_ids

        details = f"Cited: {len(cited_ids)}, Valid: {len(valid_ids)}, Invalid: {len(invalid_ids)}"
        if invalid_ids:
            details += f"\nUnknown sources: {', '.join(sorted(invalid_ids))}"

        return {
            "all_valid": len(invalid_ids) == 0,
            "details": details,
        }

    def _check_style(self, draft: str) -> dict[str, bool]:
        has_declarative = self._has_patterns(draft, DECLARATIVE_PATTERNS)
        has_blog = self._has_patterns(draft, BLOG_PATTERNS)
        return {
            "tone_guide_violation": has_declarative,
            "blog_style_detected": has_blog,
        }

    def _check_continuity(self, chapter_id: str, draft: str) -> dict[str, bool]:
        ctx = self._loader.load_project_context()
        ch_deps = ctx.get("chapter_dependencies", {})
        ch_info = ch_deps.get(chapter_id, {}) if isinstance(ch_deps, dict) else {}
        depends_on = ch_info.get("depends_on", []) if isinstance(ch_info, dict) else []
        prior_summaries = self._loader.load_prior_chapter_summaries()

        deps_covered = all(
            c.lower().replace("_", " ") in draft.lower().replace("_", " ")
            for c in depends_on
        ) if depends_on else True

        has_prior_ref = any(
            kw in draft for kw in ["앞서", "이전 장", "앞 장", "살펴본 바와 같이"]
        ) if prior_summaries else True

        has_forward = any(kw in draft for kw in ["다음 장", "이후", "뒤에서"])

        return {
            "dependency_concepts_covered": deps_covered,
            "has_prior_chapter_reference": has_prior_ref,
            "has_forward_reference": has_forward,
        }

    def _read_latest_draft(self, chapter_id: str) -> str:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        drafts = sorted(chapter_dir.glob("draft_v*.md"))
        if not drafts:
            return ""
        return read_text(drafts[-1])

    def _has_patterns(self, text: str, patterns: list[str]) -> bool:
        for line in text.splitlines():
            if line.strip().startswith("#") or line.strip().startswith("```"):
                continue
            for p in patterns:
                if re.search(p, line, re.IGNORECASE):
                    return True
        return False

    def _has_patterns_without_refs(self, text: str, patterns: list[str]) -> bool:
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("#") or line.strip().startswith("```"):
                continue
            for p in patterns:
                if re.search(p, line, re.IGNORECASE):
                    context = "\n".join(lines[max(0, i - 1):i + 2])
                    if not re.search(r"\[\^", context):
                        return True
        return False


class ReviewIO:
    """Read/write ReviewReport objects to disk."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def write_report(self, chapter_id: str, report: ReviewReport) -> None:
        chapter_dir = self.root / f"manuscript/{chapter_id}"
        markdown_path = chapter_dir / f"review_{report.review_type}_v1.md"
        json_path = self.root / f"eval/reports/{chapter_id}_{report.review_type}_v1.json"

        score_lines = "\n".join(f"- {k}: **{v}/5**" for k, v in report.score.items())
        check_lines = "\n".join(
            f"- {k}: {'✓ Pass' if v else '✗ Fail'}" for k, v in report.binary_checks.items()
        ) if report.binary_checks else "- (binary checks 미실행)"

        body = f"""# {report.review_type.title()} Review: {chapter_id}

## Score

{score_lines}

## Must Fix

{self._fmt(report.must_fix)}

## Should Fix

{self._fmt(report.should_fix)}

## Nice to Have

{self._fmt(report.nice_to_have)}

## Binary Checks

{check_lines}
"""
        write_text(markdown_path, body)
        write_json(json_path, report.to_dict())

    def load_reports(self, chapter_id: str) -> list[ReviewReport]:
        reports = []
        for review_type in ("technical", "style", "continuity"):
            json_path = self.root / f"eval/reports/{chapter_id}_{review_type}_v1.json"
            if json_path.exists():
                data = read_json(json_path)
                reports.append(ReviewReport(**data))
        return reports

    @staticmethod
    def _fmt(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- 없음"
