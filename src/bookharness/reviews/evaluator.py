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

    def _get_page_targets(self, chapter_id: str) -> dict:
        """Load expected_pages from chapter_dependencies.yaml."""
        deps_path = self.root / "book/chapter_dependencies.yaml"
        if deps_path.exists():
            deps = load_yaml(deps_path) or {}
            ch_info = deps.get(chapter_id, {})
            if isinstance(ch_info, dict):
                expected = ch_info.get("expected_pages", 20)
                return {
                    "expected_pages": expected,
                    "target_chars": expected * 1000,
                    "min_chars": int(expected * 1000 * 0.7),  # 70% 이상이면 통과
                    "max_chars": int(expected * 1000 * 1.5),  # 150% 이하이면 통과
                }
        return {"expected_pages": 20, "target_chars": 20000, "min_chars": 14000, "max_chars": 30000}

    def _check_technical(self, chapter_id: str, draft: str) -> dict[str, bool]:
        has_unsupported = self._has_patterns_without_refs(draft, ABSOLUTE_PATTERNS)
        has_source_refs = bool(re.search(r"\[\^", draft))
        word_count = len(draft.split())
        char_count = len(draft)

        # Page target check
        targets = self._get_page_targets(chapter_id)
        meets_min_length = char_count >= targets["min_chars"]
        within_max_length = char_count <= targets["max_chars"]

        # Citation verification: check if cited source_ids exist in the bundle
        citation_result = self._verify_citations(chapter_id, draft)

        return {
            "has_unsupported_claims": has_unsupported,
            "has_source_references": has_source_refs,
            "meets_minimum_length": meets_min_length,
            "within_maximum_length": within_max_length,
            "all_citations_valid": citation_result["all_valid"],
            "page_check_detail": f"{char_count}자 (목표: {targets['target_chars']}자 = {targets['expected_pages']}쪽, 허용: {targets['min_chars']}~{targets['max_chars']}자)",
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
        hierarchy = self._check_heading_hierarchy(draft)
        return {
            "tone_guide_violation": has_declarative,
            "blog_style_detected": has_blog,
            **hierarchy,
        }

    def _check_heading_hierarchy(self, draft: str) -> dict[str, bool | str]:
        """Check that headings follow the N.M / N.M.K numbering convention."""
        headings = []
        for line in draft.splitlines():
            if line.startswith("#"):
                headings.append(line)

        if not headings:
            return {"heading_hierarchy_valid": False, "heading_detail": "No headings found"}

        # Check ## headings have N.M numbering
        unnumbered_sections = []
        # Check ### headings have N.M.K numbering
        unnumbered_subsections = []
        # Check for legacy blockquote-as-structure patterns
        has_blockquote_structures = bool(re.search(
            r"^>\s*\*\*\[(?:참고|용어 정의|참고사항)\]",
            draft, re.MULTILINE,
        ))

        for h in headings:
            if h.startswith("## ") and not h.startswith("### "):
                # Should match ## N.M title
                text = h[3:].strip()
                if not re.match(r"\d+\.\d+\s", text):
                    unnumbered_sections.append(text[:40])
            elif h.startswith("### ") and not h.startswith("#### "):
                # Should match ### N.M.K title
                text = h[4:].strip()
                if not re.match(r"\d+\.\d+\.\d+\s", text):
                    unnumbered_subsections.append(text[:40])

        all_numbered = len(unnumbered_sections) == 0 and len(unnumbered_subsections) == 0
        detail_parts = []
        if unnumbered_sections:
            detail_parts.append(f"넘버링 없는 절({len(unnumbered_sections)}개): {', '.join(unnumbered_sections[:3])}")
        if unnumbered_subsections:
            detail_parts.append(f"넘버링 없는 중제목({len(unnumbered_subsections)}개): {', '.join(unnumbered_subsections[:3])}")
        if has_blockquote_structures:
            detail_parts.append("blockquote 구조물 사용 감지 (:::box/note/tip 형식 권장)")

        return {
            "heading_hierarchy_valid": all_numbered,
            "no_blockquote_structures": not has_blockquote_structures,
            "heading_detail": "; ".join(detail_parts) if detail_parts else "All headings properly numbered",
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
        if report.binary_checks:
            check_parts = []
            for k, v in report.binary_checks.items():
                if isinstance(v, bool):
                    check_parts.append(f"- {k}: {'✓ Pass' if v else '✗ Fail'}")
                else:
                    check_parts.append(f"- {k}: {v}")
            check_lines = "\n".join(check_parts)
        else:
            check_lines = "- (binary checks 미실행)"

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
