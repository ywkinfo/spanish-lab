#!/usr/bin/env python3
"""Generate the produced-episode inventory for docs/content-roadmap.md (single source of truth).

The authoritative episode record is the ``EPISODE``/``SERIES`` fields inside each
``projects/*.py`` module. This tool reads them via ``importlib`` -- the same pattern as
``scripts/export_github_pages.py`` (get_module/youtube_id) -- so the roadmap inventory can
never drift from what was actually produced. Read-only scan, stdlib only.

Usage:
    python3 scripts/build_episode_index.py            # print the table to stdout
    python3 scripts/build_episode_index.py --write     # replace ONLY the marked region
                                                       # in docs/content-roadmap.md
"""

from __future__ import annotations

import argparse
import importlib
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"
ROADMAP = ROOT / "docs" / "content-roadmap.md"

BEGIN_MARKER = "<!-- BEGIN:generated -->"
END_MARKER = "<!-- END:generated -->"

# Fields read off each project module (authoritative).
FIELDS = (
    "SERIES",
    "EPISODE",
    "LEVEL",
    "OUTPUT_NAME",
    "PUBLIC_SLUG",
    "YOUTUBE_TITLE",
    "YOUTUBE_URL",
)


def md_escape(text: object) -> str:
    """Collapse newlines and escape the pipe so a value is safe inside a table cell."""
    return (
        str(text)
        .replace("|", "\\|")
        .replace("\r\n", " ")
        .replace("\r", " ")
        .replace("\n", " ")
    )


def youtube_id(url: str) -> str:
    """Extract a YouTube video id from a watch/short URL (mirrors export_github_pages.py)."""
    if not url:
        return ""
    parsed = urlparse(url)
    if parsed.netloc == "youtu.be":
        return parsed.path.lstrip("/")
    if "youtube.com" in parsed.netloc:
        qs = parse_qs(parsed.query)
        if qs.get("v"):
            return qs["v"][0]
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{6,})", url)
    return m.group(1) if m else ""


def discover_rows() -> list[dict]:
    """Import every projects/*.py (except __init__) and read its authoritative fields."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    rows: list[dict] = []
    for path in sorted(PROJECTS_DIR.glob("*.py")):
        if path.stem == "__init__":
            continue
        try:
            module = importlib.import_module(f"projects.{path.stem}")
        except Exception as exc:  # scan boundary: one broken module must not kill the index
            rows.append({"module": path.stem, "SERIES": "(import-error)", "EPISODE": "", "_error": str(exc)})
            continue
        row = {"module": path.stem}
        for field in FIELDS:
            row[field] = getattr(module, field, "")
        rows.append(row)
    return rows


def url_status(row: dict) -> str:
    """A present URL is published; an empty one is merely *not recorded in the repo*."""
    vid = youtube_id(str(row.get("YOUTUBE_URL", "") or ""))
    return f"발행({vid})" if vid else "URL 미기록"


def _sort_key(row: dict):
    episode = row.get("EPISODE", "")
    return (str(row.get("SERIES", "")), episode if isinstance(episode, int) else 9999, row["module"])


def build_table(rows: list[dict]) -> str:
    by_series: dict[str, list[dict]] = {}
    for row in rows:
        series = str(row.get("SERIES", "") or "(none)")
        by_series.setdefault(series, []).append(row)

    lines: list[str] = []
    for series in sorted(by_series):
        lines.append(f"### {series}")
        lines.append("")
        lines.append("| Ep | module | slug | 레벨 | 학습 포인트 (YOUTUBE_TITLE) | URL 상태 |")
        lines.append("|---:|---|---|---|---|---|")
        for row in sorted(by_series[series], key=_sort_key):
            episode = row.get("EPISODE", "")
            if row.get("_error"):
                lines.append(f"| ? | `{row['module']}` | (import-error) | | {md_escape(row['_error'])} | - |")
                continue
            lines.append(
                f"| {episode} | `{row['module']}` | `{md_escape(row.get('PUBLIC_SLUG', ''))}` | "
                f"{md_escape(row.get('LEVEL', ''))} | {md_escape(row.get('YOUTUBE_TITLE', ''))} | "
                f"{url_status(row)} |"
            )
        lines.append("")

    lines.append(_summary_line(rows))
    return "\n".join(lines).rstrip() + "\n"


def _summary_line(rows: list[dict]) -> str:
    counts: dict[str, int] = {}
    max_ep: dict[str, int] = {}
    for row in rows:
        series = str(row.get("SERIES", "") or "(none)")
        counts[series] = counts.get(series, 0) + 1
        episode = row.get("EPISODE", "")
        if isinstance(episode, int):
            max_ep[series] = episode if series not in max_ep else max(max_ep[series], episode)

    parts = [f"{series}: {counts[series]}모듈(최대 Ep.{max_ep.get(series, '-')})" for series in sorted(counts)]
    frases_eps = [max_ep[s] for s in max_ep if s.startswith("frases-")]
    frases_max = max(frases_eps) if frases_eps else 0
    return (
        "> 요약: "
        + " · ".join(parts)
        + f" — 학습 채널 타임라인(frases-*) 최대 Ep.{frases_max} → **다음 = Ep.{frases_max + 1}**. "
        + "주의: frases-a1 모듈 수 ≠ 도달 Ep번호 (Ep.0×2 · Ep.2 remake 포함, Ep.24/25는 frases-a2, "
        + "descripcion은 독립 번호 Ep.1–6)."
    )


def write_region(rows: list[dict]) -> int:
    if not ROADMAP.exists():
        sys.stderr.write(
            f"error: {ROADMAP} 가 없습니다. 먼저 마커({BEGIN_MARKER} / {END_MARKER})를 포함한 "
            "스캐폴드 문서를 만든 뒤 --write 하세요.\n"
        )
        return 2
    text = ROADMAP.read_text(encoding="utf-8")
    if BEGIN_MARKER not in text or END_MARKER not in text:
        sys.stderr.write(
            f"error: {ROADMAP} 에 마커({BEGIN_MARKER} / {END_MARKER})가 없어 안전하게 갱신할 수 "
            "없습니다. 전체 덮어쓰기를 거부합니다 (SoT 신뢰성 보호).\n"
        )
        return 2
    head, rest = text.split(BEGIN_MARKER, 1)
    _, tail = rest.split(END_MARKER, 1)
    new_text = f"{head}{BEGIN_MARKER}\n\n{build_table(rows)}\n{END_MARKER}{tail}"
    if new_text == text:
        print(f"no change: {ROADMAP}")
        return 0
    ROADMAP.write_text(new_text, encoding="utf-8")
    print(f"updated: {ROADMAP}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Spanish Lab produced-episode index generator (SoT).")
    parser.add_argument(
        "--write",
        action="store_true",
        help="docs/content-roadmap.md 의 마커 구역만 치환 (마커 없으면 에러).",
    )
    args = parser.parse_args()

    rows = discover_rows()
    if args.write:
        return write_region(rows)
    sys.stdout.write(build_table(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
