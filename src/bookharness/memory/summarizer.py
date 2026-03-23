from __future__ import annotations

from pathlib import Path

from bookharness.utils.io import read_text, write_text


class SummaryBuilder:
    def build_chapter_summary(self, chapter_id: str, final_candidate_path: Path) -> str:
        content = read_text(final_candidate_path)
        preview = "\n".join(content.splitlines()[:12]).strip()
        return (
            f"# {chapter_id} Summary\n\n"
            "## 핵심 개념\n\n"
            f"- 승인된 초안 기준 요약을 갱신한다.\n\n"
            "## 승인 초안 미리보기\n\n"
            f"```markdown\n{preview}\n```\n"
        )

    def refresh_global_summary(self, root: Path) -> str:
        summaries_dir = root / "memory/chapter_summaries"
        chunks: list[str] = ["# Global Summary", ""]
        for path in sorted(summaries_dir.glob("*.md")):
            chunks.append(f"## {path.stem}")
            chunks.append(read_text(path).strip())
            chunks.append("")
        return "\n".join(chunks).strip() + "\n"

    def write_summary_files(self, root: Path, chapter_id: str, final_candidate_path: Path) -> None:
        summary = self.build_chapter_summary(chapter_id, final_candidate_path)
        write_text(root / f"memory/chapter_summaries/{chapter_id}.md", summary)
        write_text(root / "memory/global_summary.md", self.refresh_global_summary(root))
