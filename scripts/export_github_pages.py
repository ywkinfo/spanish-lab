#!/usr/bin/env python3
"""Export Spanish Lab project content into a GitHub Pages-friendly docs tree.

This is intentionally small and conservative: it turns a finished project module
into a static lesson page plus a lightweight index page.
"""

from __future__ import annotations

import argparse
import importlib
import re
from pathlib import Path
from textwrap import dedent
from urllib.parse import urlparse, parse_qs
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
DEFAULT_SITE_DIR = ROOT / "docs"
DEFAULT_PROJECT = "frases_a1_50_utiles"
DEFAULT_TITLE = "Spanish Lab"


def md_escape(text: str) -> str:
    return (
        str(text)
        .replace("|", "\\|")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
    )


def quote_yaml(text: str) -> str:
    return str(text).replace("\"", "\\\"")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def youtube_id(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    if parsed.netloc in {"youtu.be"}:
        return parsed.path.lstrip("/")
    if "youtube.com" in parsed.netloc:
        qs = parse_qs(parsed.query)
        if "v" in qs and qs["v"]:
            return qs["v"][0]
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{6,})", url)
    return m.group(1) if m else ""


def get_module(project: str):
    return importlib.import_module(f"projects.{project}")


def lesson_slug(module, override: str | None = None) -> str:
    if override:
        return override
    return getattr(module, "PUBLIC_SLUG", getattr(module, "OUTPUT_NAME", "lesson"))


def build_phrase_table(phrases: list[tuple]) -> str:
    lines = [
        "| # | Español | Coreano | Ejemplo |",
        "|---:|---|---|---|",
    ]
    for number, text_es, text_ko, example_es in phrases:
        lines.append(
            f"| {number} | {md_escape(text_es)} | {md_escape(text_ko)} | {md_escape(example_es)} |"
        )
    return "\n".join(lines)


def build_block_list(blocks: list[dict]) -> str:
    lines = []
    for block in blocks:
        lines.append(
            f"- {block.get('block_id', ''):02d}. {block.get('title_es', '')} / {block.get('title_ko', '')}"
        )
    return "\n".join(lines)


def build_quiz(phrases: list[tuple]) -> str:
    quiz_items = [
        ("¿Cómo saludas por la mañana?", "Buenos días."),
        ("¿Cómo dices que hablas un poco de español?", "Hablo un poco de español."),
        ("¿Cómo preguntas el precio?", "¿Cuánto cuesta?"),
        ("¿Cómo pides la cuenta en un restaurante?", "La cuenta, por favor."),
        ("¿Cómo te despides?", "Hasta luego."),
    ]
    lines = []
    for i, (q, a) in enumerate(quiz_items, start=1):
        lines.append(f"{i}. {q}  ")
        lines.append(f"   - Respuesta: {a}")
    return "\n".join(lines)


def build_lesson_markdown(module, slug: str, youtube_url: str) -> str:
    title = getattr(module, "YOUTUBE_TITLE", slug.replace("-", " ").title())
    level = getattr(module, "LEVEL", "")
    series_title = getattr(module, "SERIES_TITLE", "Spanish Lab")
    episode = getattr(module, "EPISODE", "")
    intro = getattr(module, "DESCRIPTION_INTRO", "")
    outro = getattr(module, "DESCRIPTION_OUTRO", "")
    korean_teaser = getattr(module, "KOREAN_TEASER", "")
    phrases = list(getattr(module, "PHRASES", []))
    blocks = list(getattr(module, "BLOCKS", []))
    chapter_titles = [c.get("title", "") for c in getattr(module, "CHAPTERS", [])]
    video_id = youtube_id(youtube_url)
    thumbnail_md = ""
    if video_id:
        thumb_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        thumbnail_md = f"[![{title}]({thumb_url})]({youtube_url})"

    front_matter = dedent(
        f"""\
        ---
        title: \"{quote_yaml(title)}\"
        description: \"{quote_yaml(intro)}\"
        level: {level}
        episode: {episode}
        permalink: /lessons/{slug}/
        ---
        """
    ).strip()

    lines = [front_matter, "", f"# {title}", "", f"Nivel: {level} · Serie: {series_title} · Ep. {episode}"]
    if thumbnail_md:
        lines += ["", thumbnail_md, ""]
    lines += [
        "## Qué practicar",
        intro,
        "",
        "## Enlace del video",
        f"[Ver en YouTube]({youtube_url})",
        "",
        "## Bloques temáticos",
        build_block_list(blocks),
        "",
        "## Frases base",
        build_phrase_table(phrases),
        "",
        "## Repetición guiada",
        "Lee cada frase, escucha el audio y repite en voz alta. Intenta copiar ritmo, pausas y entonación.",
        "",
        "## Mini quiz",
        build_quiz(phrases),
        "",
        "## Teaser coreano",
        korean_teaser,
        "",
        "## Cierre",
        outro,
        "",
        "## Chapter map",
    ]
    for i, chapter in enumerate(chapter_titles, start=1):
        if chapter:
            lines.append(f"- {i}. {chapter}")
    return "\n".join(lines).rstrip() + "\n"


def build_index_markdown(lessons: list[dict]) -> str:
    lines = [
        "---",
        'title: "Spanish Lab"',
        'description: "Spanish Lab learning hub for Korean learners."',
        'permalink: /',
        "---",
        "",
        "# Spanish Lab",
        "",
        "YouTube is the discovery channel. GitHub Pages is the learning hub.",
        "",
        "## Lessons",
    ]
    for lesson in lessons:
        lines.append(
            f"- [{lesson['title']}](lessons/{lesson['slug']}/) — {lesson['level']} · Ep. {lesson['episode']}"
        )
    lines += [
        "",
        "## Channel strategy",
        "- YouTube: discovery and subscriber growth",
        "- GitHub Pages: structured lesson archive and reuse",
        "",
        "## Current focus",
        "Build one lesson page per finished episode, then expand only after the format is stable.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def write_text(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text, encoding="utf-8")


def read_lesson_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
    level = re.search(r'^level:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
    episode = re.search(r'^episode:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
    permalink = re.search(r'^permalink:\s*"?(.*?)"?\s*$', text, re.MULTILINE)
    slug = path.parent.name
    return {
        "title": title.group(1) if title else slug,
        "level": level.group(1) if level else "",
        "episode": episode.group(1) if episode else "",
        "slug": slug,
        "permalink": permalink.group(1) if permalink else f"/lessons/{slug}/",
    }


def collect_lessons(site_dir: Path) -> list[dict]:
    lessons = []
    lessons_root = site_dir / "lessons"
    if lessons_root.exists():
        for lesson_md in sorted(lessons_root.glob("*/index.md")):
            lessons.append(read_lesson_meta(lesson_md))
    return sorted(
        lessons,
        key=lambda item: (
            int(item["episode"]) if str(item["episode"]).isdigit() else 9999,
            item["slug"],
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export Spanish Lab lessons to a GitHub Pages docs tree.")
    parser.add_argument("--project", default=DEFAULT_PROJECT, help="Project module name under projects/.")
    parser.add_argument("--site-dir", default=str(DEFAULT_SITE_DIR), help="Target docs directory.")
    parser.add_argument("--youtube-url", default="", help="Video URL for the lesson page.")
    parser.add_argument("--slug", default="", help="Override the public lesson slug.")
    args = parser.parse_args()

    module = get_module(args.project)
    site_dir = Path(args.site_dir)
    slug = lesson_slug(module, args.slug or None)
    youtube_url = args.youtube_url or getattr(module, "YOUTUBE_URL", "")
    if not youtube_url and args.project == DEFAULT_PROJECT:
        youtube_url = "https://www.youtube.com/watch?v=2WrERE9LOyE"

    config = dedent(
        f"""\
        title: {DEFAULT_TITLE}
        description: Spanish Lab learning hub for Korean learners.
        theme: minima
        """
    ).lstrip()
    write_text(site_dir / "_config.yml", config)

    lesson_md = build_lesson_markdown(module, slug, youtube_url)
    write_text(site_dir / "lessons" / slug / "index.md", lesson_md)

    lessons = collect_lessons(site_dir)
    index_md = build_index_markdown(lessons)
    write_text(site_dir / "index.md", index_md)

    print(f"Wrote {site_dir / '_config.yml'}")
    print(f"Wrote {site_dir / 'index.md'}")
    print(f"Wrote {site_dir / 'lessons' / slug / 'index.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
