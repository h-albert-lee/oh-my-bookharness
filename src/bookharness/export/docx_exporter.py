"""Export Markdown drafts to Word (.docx) using the publisher template.

Uses the 한빛미디어 template (1장_피드백 진행.docx) as a style source,
mapping Markdown elements to the publisher's custom Word styles.

Style mapping:
    # N장. 제목          → Heading 1
    ## N.M 절제목         → Heading 2
    ### N.M.K 중제목      → Heading 3
    #### 소제목           → Heading 4
    ##### 소소제목        → 소소제목 (custom)
    ::: box 제목 ... :::  → 박스 제목 + 박스_끝
    ::: note 제목 ... ::: → 노트
    ::: tip 제목 ... :::  → 노트 (same style as note)
    ```code```            → _코드 (custom paragraph style)
    `inline code`         → _코드_본문 (custom character style)
    **표 N-M. 제목**      → Caption
    **그림 N-M. 제목**    → Caption
    - list items          → List Paragraph
    영문(English)         → _병기 for the English part
    [^source_id]          → footnote reference
"""

from __future__ import annotations

import copy
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH


def _strip_heading_prefix(text: str) -> str:
    """Remove markdown # prefixes from heading text."""
    return text.lstrip("#").strip()


class DocxExporter:
    """Convert a Markdown draft to .docx using the publisher template."""

    def __init__(self, template_path: Path | str | None = None) -> None:
        self.template_path = Path(template_path) if template_path else None

    def export(self, markdown_path: Path | str, output_path: Path | str | None = None) -> Path:
        """Export a single Markdown file to .docx.

        Args:
            markdown_path: Path to the Markdown draft file.
            output_path: Path for the output .docx. Defaults to same dir with .docx extension.

        Returns:
            Path to the created .docx file.
        """
        markdown_path = Path(markdown_path)
        if output_path is None:
            output_path = markdown_path.with_suffix(".docx")
        else:
            output_path = Path(output_path)

        md_text = markdown_path.read_text(encoding="utf-8")

        # Create document from template or blank
        if self.template_path and self.template_path.exists():
            doc = Document(str(self.template_path))
            # Clear template content but keep styles
            self._clear_content(doc)
        else:
            doc = Document()

        # Parse and render
        lines = md_text.split("\n")
        self._render(doc, lines)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(output_path))
        return output_path

    def _clear_content(self, doc: Document) -> None:
        """Remove all paragraphs and tables from the template, keeping styles."""
        for _ in range(len(doc.paragraphs)):
            p = doc.paragraphs[0]._element
            p.getparent().remove(p)
        for _ in range(len(doc.tables)):
            t = doc.tables[0]._element
            t.getparent().remove(t)

    def _render(self, doc: Document, lines: list[str]) -> None:
        """Walk through Markdown lines and add them to the document."""
        i = 0
        footnotes: dict[str, str] = {}

        # First pass: collect footnote definitions
        for line in lines:
            m = re.match(r"^\[\^(\w+)\]:\s*(.+)$", line)
            if m:
                footnotes[m.group(1)] = m.group(2)

        while i < len(lines):
            line = lines[i]

            # Skip blank lines
            if not line.strip():
                i += 1
                continue

            # Skip footnote definitions (already collected)
            if re.match(r"^\[\^(\w+)\]:\s*", line):
                i += 1
                continue

            # Horizontal rule
            if re.match(r"^---+\s*$", line):
                i += 1
                continue

            # Fenced div: ::: box/note/tip
            m = re.match(r"^:::\s*(box|note|tip)\s*(.*)?$", line)
            if m:
                i = self._render_fenced_div(doc, lines, i, m.group(1), m.group(2) or "")
                continue

            # Code block
            if line.startswith("```"):
                i = self._render_code_block(doc, lines, i)
                continue

            # Headings
            if line.startswith("#"):
                self._render_heading(doc, line)
                i += 1
                continue

            # Table caption (**표 N-M.** or **그림 N-M.**)
            m = re.match(r"^\*\*(?:표|그림)\s+\d+-\d+\.\s*.+\*\*$", line.strip())
            if m:
                caption_text = line.strip().strip("*")
                self._add_para(doc, caption_text, "Caption")
                i += 1
                continue

            # Markdown table
            if "|" in line and i + 1 < len(lines) and re.match(r"^\|[-\s|:]+\|$", lines[i + 1].strip()):
                i = self._render_table(doc, lines, i)
                continue

            # List items
            if re.match(r"^[-*]\s+", line):
                text = re.sub(r"^[-*]\s+", "", line)
                para = self._add_para(doc, "", "List Paragraph")
                self._add_formatted_runs(para, text, footnotes)
                i += 1
                continue

            # Numbered list
            m = re.match(r"^(\d+)[.)]\s+", line)
            if m:
                text = line[m.end():]
                para = self._add_para(doc, "", "List Paragraph")
                self._add_formatted_runs(para, text, footnotes)
                i += 1
                continue

            # Normal paragraph
            para = self._add_para(doc, "", "Normal")
            self._add_formatted_runs(para, line, footnotes)
            i += 1

    def _render_heading(self, doc: Document, line: str) -> None:
        """Render a heading line."""
        level = 0
        for ch in line:
            if ch == "#":
                level += 1
            else:
                break

        text = line[level:].strip()

        if level == 1:
            self._add_para(doc, text, "Heading 1")
        elif level == 2:
            self._add_para(doc, text, "Heading 2")
        elif level == 3:
            self._add_para(doc, text, "Heading 3")
        elif level == 4:
            self._add_para(doc, text, "Heading 4")
        elif level >= 5:
            self._add_para(doc, text, "소소제목")

    def _render_fenced_div(self, doc: Document, lines: list[str], start: int, div_type: str, title: str) -> int:
        """Render ::: box/note/tip ... ::: blocks."""
        i = start + 1
        content_lines = []

        while i < len(lines):
            if lines[i].strip() == ":::":
                i += 1
                break
            content_lines.append(lines[i])
            i += 1

        title = title.strip()

        if div_type == "box":
            # Box: title in 박스 제목, content in 박스_끝
            if title:
                self._add_para(doc, title, "박스 제목")
            content = "\n".join(line for line in content_lines if line.strip())
            for para_text in self._split_paragraphs(content_lines):
                self._add_para(doc, para_text, "박스_끝")
        else:
            # Note/Tip: all in 노트 style
            if title:
                self._add_para(doc, title, "노트")
            for para_text in self._split_paragraphs(content_lines):
                self._add_para(doc, para_text, "노트")

        return i

    def _render_code_block(self, doc: Document, lines: list[str], start: int) -> int:
        """Render ``` code blocks."""
        i = start + 1
        code_lines = []

        while i < len(lines):
            if lines[i].startswith("```"):
                i += 1
                break
            code_lines.append(lines[i])
            i += 1

        # Use _코드 style if available, fall back to Normal
        style_name = "_코드"
        for code_line in code_lines:
            self._add_para(doc, code_line, style_name)

        return i

    def _render_table(self, doc: Document, lines: list[str], start: int) -> int:
        """Render a Markdown table."""
        i = start
        rows_data = []

        while i < len(lines) and "|" in lines[i]:
            row_text = lines[i].strip()
            # Skip separator row
            if re.match(r"^\|[-\s|:]+\|$", row_text):
                i += 1
                continue
            cells = [c.strip() for c in row_text.split("|")[1:-1]]
            rows_data.append(cells)
            i += 1

        if not rows_data:
            return i

        num_cols = max(len(row) for row in rows_data)
        table = doc.add_table(rows=len(rows_data), cols=num_cols)
        table.style = "Table Grid"

        for ri, row in enumerate(rows_data):
            for ci, cell_text in enumerate(row):
                if ci < num_cols:
                    # Strip bold markers from cell text
                    cell_text = cell_text.strip("*")
                    table.rows[ri].cells[ci].text = cell_text

        return i

    def _split_paragraphs(self, lines: list[str]) -> list[str]:
        """Split lines into paragraph groups (separated by blank lines)."""
        paragraphs = []
        current = []
        for line in lines:
            if not line.strip():
                if current:
                    paragraphs.append(" ".join(current))
                    current = []
            else:
                current.append(line.strip())
        if current:
            paragraphs.append(" ".join(current))
        return paragraphs

    def _add_para(self, doc: Document, text: str, style_name: str) -> "Paragraph":
        """Add a paragraph with the given style. Falls back to Normal if style not found."""
        try:
            para = doc.add_paragraph(style=style_name)
        except KeyError:
            para = doc.add_paragraph()
        if text:
            para.add_run(text)
        return para

    def _add_formatted_runs(self, para, text: str, footnotes: dict[str, str]) -> None:
        """Parse inline formatting and add runs with appropriate styles."""
        # Process inline elements: **bold**, `code`, [^footnote], 영문(English)
        pattern = re.compile(
            r"(\*\*(.+?)\*\*)"       # bold
            r"|(`([^`]+)`)"           # inline code
            r"|(\[\^(\w+)\])"         # footnote reference
        )

        pos = 0
        for m in pattern.finditer(text):
            # Add text before match
            if m.start() > pos:
                para.add_run(text[pos:m.start()])

            if m.group(2):  # bold
                run = para.add_run(m.group(2))
                run.bold = True
            elif m.group(4):  # inline code
                run = para.add_run(m.group(4))
                try:
                    run.style = para.part.document.styles["_코드_본문"]
                except KeyError:
                    run.font.name = "Consolas"
            elif m.group(6):  # footnote ref
                ref_id = m.group(6)
                fn_text = footnotes.get(ref_id, ref_id)
                # Add as superscript reference for now
                run = para.add_run(f"[{ref_id}]")
                run.font.superscript = True
                run.font.size = None  # inherit

            pos = m.end()

        # Add remaining text
        if pos < len(text):
            para.add_run(text[pos:])


def export_chapter(
    project_root: Path,
    chapter_id: str,
    template_path: Path | str | None = None,
    output_dir: Path | str | None = None,
) -> Path:
    """Export the latest draft of a chapter to .docx.

    Args:
        project_root: Project root directory.
        chapter_id: Chapter ID (e.g., "ch01").
        template_path: Path to the publisher template .docx.
        output_dir: Output directory. Defaults to project_root/export/.

    Returns:
        Path to the created .docx file.
    """
    chapter_dir = project_root / f"manuscript/{chapter_id}"
    drafts = sorted(chapter_dir.glob("draft_v*.md"))
    if not drafts:
        raise FileNotFoundError(f"No drafts found for {chapter_id}")

    latest_draft = drafts[-1]

    if output_dir is None:
        output_dir = project_root / "export"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{chapter_id}_{latest_draft.stem}.docx"

    exporter = DocxExporter(template_path)
    return exporter.export(latest_draft, output_path)
