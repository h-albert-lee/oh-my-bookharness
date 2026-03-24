"""Rich summary builder for approved chapters.

Extracts structured information from final candidates:
- Key concepts and definitions
- Important examples
- Cross-chapter connection points
- Reusable phrases/analogies
"""

from __future__ import annotations

import re
from pathlib import Path

from bookharness.utils.io import read_text, write_text
from bookharness.utils.yaml_utils import load_yaml


class SummaryBuilder:
    def build_chapter_summary(self, chapter_id: str, final_candidate_path: Path, root: Path | None = None) -> str:
        content = read_text(final_candidate_path)

        # Extract title
        title = self._extract_title(content)

        # Extract section headings
        sections = self._extract_sections(content)

        # Extract key concepts (bold terms)
        concepts = self._extract_concepts(content)

        # Extract examples (lines mentioning 예, 사례, etc.)
        examples = self._extract_examples(content)

        # Extract source references
        source_refs = self._extract_source_refs(content)

        # Extract key definitions (concept_dictionary terms mentioned)
        definitions = []
        if root:
            concept_dict = load_yaml(root / "book/concept_dictionary.yaml") or {}
            if isinstance(concept_dict, dict):
                for term, info in concept_dict.items():
                    if term in content.lower() or (isinstance(info, dict) and info.get("preferred_korean", "") in content):
                        defn = info.get("definition", "") if isinstance(info, dict) else str(info)
                        definitions.append(f"{term}: {defn}")

        # Build structured summary
        parts = [f"# {chapter_id} Summary\n"]

        if title:
            parts.append(f"## 장 제목\n\n{title}\n")

        parts.append("## 핵심 개념\n")
        if concepts:
            for concept in concepts[:10]:
                parts.append(f"- {concept}")
        else:
            parts.append("- (추출된 핵심 개념 없음)")
        parts.append("")

        if definitions:
            parts.append("## 용어 정의\n")
            for defn in definitions[:10]:
                parts.append(f"- {defn}")
            parts.append("")

        parts.append("## 섹션 구조\n")
        if sections:
            for level, heading in sections:
                indent = "  " * (level - 2) if level > 2 else ""
                parts.append(f"{indent}- {heading}")
        else:
            parts.append("- (섹션 정보 없음)")
        parts.append("")

        if examples:
            parts.append("## 주요 예시\n")
            for example in examples[:5]:
                parts.append(f"- {example}")
            parts.append("")

        if source_refs:
            parts.append("## 참조된 Source\n")
            for ref in source_refs[:10]:
                parts.append(f"- {ref}")
            parts.append("")

        # Connection points for next chapters
        parts.append("## 다음 장과 연결되는 포인트\n")
        forward_refs = self._extract_forward_references(content)
        if forward_refs:
            for ref in forward_refs:
                parts.append(f"- {ref}")
        else:
            parts.append("- (명시적 다음 장 예고를 추출하지 못함. 본문 마지막 섹션을 확인할 것.)")
        parts.append("")

        # Content preview
        parts.append("## 승인 초안 미리보기\n")
        preview = "\n".join(content.splitlines()[:15]).strip()
        parts.append(f"```markdown\n{preview}\n```")

        return "\n".join(parts)

    def refresh_global_summary(self, root: Path) -> str:
        summaries_dir = root / "memory/chapter_summaries"
        chunks: list[str] = ["# Global Summary\n"]

        # Add overall statistics
        summary_files = sorted(summaries_dir.glob("*.md"))
        chunks.append(f"승인된 장 수: {len(summary_files)}\n")

        # Collect all concepts across chapters for cross-reference
        all_concepts: dict[str, list[str]] = {}

        for path in summary_files:
            content = read_text(path)
            ch_id = path.stem
            chunks.append(f"## {ch_id}\n")

            # Extract just the key sections for the global summary
            title = self._extract_title(content)
            if title:
                chunks.append(f"제목: {title}\n")

            # Extract concepts and map to chapters
            concepts = self._extract_concepts(content)
            if concepts:
                chunks.append("핵심 개념: " + ", ".join(concepts[:5]))
                for concept in concepts:
                    all_concepts.setdefault(concept, []).append(ch_id)

            chunks.append(content.strip())
            chunks.append("")

        # Add cross-reference section
        if all_concepts:
            chunks.append("## 장 간 개념 교차 참조\n")
            shared_concepts = {k: v for k, v in all_concepts.items() if len(v) > 1}
            if shared_concepts:
                for concept, chapters in sorted(shared_concepts.items()):
                    chunks.append(f"- {concept}: {', '.join(chapters)}")
            else:
                chunks.append("- (아직 장 간 공유 개념이 없다.)")
            chunks.append("")

        return "\n".join(chunks).strip() + "\n"

    def update_recurring_examples(self, root: Path) -> None:
        """Update recurring_examples.md from approved chapter summaries."""
        summaries_dir = root / "memory/chapter_summaries"
        all_examples: list[tuple[str, str]] = []

        for path in sorted(summaries_dir.glob("*.md")):
            content = read_text(path)
            ch_id = path.stem
            examples = self._extract_examples(content)
            for ex in examples:
                all_examples.append((ch_id, ex))

        if all_examples:
            lines = ["# Recurring Examples\n"]
            lines.append("장별로 등장한 주요 예시 목록. 동일 예시가 과도하게 반복되지 않도록 관리한다.\n")
            for ch_id, example in all_examples:
                lines.append(f"- [{ch_id}] {example}")
            write_text(root / "memory/recurring_examples.md", "\n".join(lines))

    def write_summary_files(self, root: Path, chapter_id: str, final_candidate_path: Path) -> None:
        summary = self.build_chapter_summary(chapter_id, final_candidate_path, root)
        write_text(root / f"memory/chapter_summaries/{chapter_id}.md", summary)
        write_text(root / "memory/global_summary.md", self.refresh_global_summary(root))
        self.update_recurring_examples(root)

    # --- Extraction helpers ---

    @staticmethod
    def _extract_title(content: str) -> str:
        for line in content.splitlines():
            if line.startswith("# ") and not line.startswith("## "):
                return line.lstrip("# ").strip()
        return ""

    @staticmethod
    def _extract_sections(content: str) -> list[tuple[int, str]]:
        sections = []
        for line in content.splitlines():
            match = re.match(r"^(#{2,4})\s+(.+)$", line)
            if match:
                level = len(match.group(1))
                heading = match.group(2).strip()
                sections.append((level, heading))
        return sections

    @staticmethod
    def _extract_concepts(content: str) -> list[str]:
        """Extract bold-formatted terms as key concepts."""
        concepts = re.findall(r"\*\*([^*]+)\*\*", content)
        # Deduplicate while preserving order
        seen = set()
        unique = []
        for c in concepts:
            if c.lower() not in seen and len(c) < 50:
                seen.add(c.lower())
                unique.append(c)
        return unique

    @staticmethod
    def _extract_examples(content: str) -> list[str]:
        """Extract lines that mention examples or cases."""
        keywords = ["예를 들", "사례", "예시", "경우를 생각", "구체적으로"]
        examples = []
        for line in content.splitlines():
            stripped = line.strip()
            if any(kw in stripped for kw in keywords) and len(stripped) > 20:
                examples.append(stripped[:100])
        return examples

    @staticmethod
    def _extract_source_refs(content: str) -> list[str]:
        return list(dict.fromkeys(re.findall(r"\[\^([^\]]+)\]", content)))

    @staticmethod
    def _extract_forward_references(content: str) -> list[str]:
        keywords = ["다음 장", "이후", "뒤에서", "이어서 살펴"]
        refs = []
        for line in content.splitlines():
            stripped = line.strip()
            if any(kw in stripped for kw in keywords) and len(stripped) > 10:
                refs.append(stripped[:100])
        return refs
