from __future__ import annotations

import html
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def to_iso(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    html_lines: list[str] = []
    in_list = False
    in_code = False
    for line in lines:
        escaped = html.escape(line)
        if line.startswith("```"):
            if in_code:
                html_lines.append("</code></pre>")
            else:
                html_lines.append("<pre><code>")
            in_code = not in_code
            continue
        if in_code:
            html_lines.append(escaped)
            continue
        if line.startswith("### "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h3>{html.escape(line[4:])}</h3>")
        elif line.startswith("## "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("# "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{html.escape(line[2:])}</li>")
        elif not line.strip():
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<br />")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{escaped}</p>")
    if in_list:
        html_lines.append("</ul>")
    if in_code:
        html_lines.append("</code></pre>")
    return "\n".join(html_lines)


def ensure_within_root(root: Path, target: Path) -> Path:
    root = root.resolve()
    target = target.resolve()
    if root != target and root not in target.parents:
        raise ValueError(f"Path {target} is outside root {root}")
    return target
