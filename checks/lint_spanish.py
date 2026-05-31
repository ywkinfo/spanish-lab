"""Deterministic Spanish-facing text lint for Spanish Lab episodes."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.camera import output_size_for_design  # noqa: E402
from build.subtitles import layout_subtitle  # noqa: E402
from segments import (  # noqa: E402
    CHAPTERS,
    DESCRIPTION_INTRO,
    DESCRIPTION_OUTRO,
    DESIGN,
    RENDER_TYPE,
    SEGMENTS,
    YOUTUBE_TITLE,
)

FALSE_FRIENDS = {
    "actual": "Use `actual` only for `current`; not English `actual`.",
    "asistir": "Use `asistir` for attending, not helping.",
    "embarazada": "Means pregnant, not embarrassed.",
    "constipado": "Means having a cold, not constipated.",
    "sensible": "Means sensitive, not sensible.",
    "realizar": "Can mean carry out; avoid as a lazy translation of `realize`.",
}
ENGLISH_LEAKAGE = {
    "actually",
    "current",
    "assist",
    "embarrassed",
    "meeting",
    "team",
    "market",
    "train",
    "kitchen",
}
SUBJUNCTIVE_TRIGGERS = ("quizá", "quizás", "tal vez", "ojalá", "ojalá que", "puede que")
INDICATIVE_AFTER_TRIGGER = re.compile(
    r"\b(?:quiz[aá]s?|tal vez|ojal[aá](?: que)?|puede que)\s+"
    r"(?:est[aá]|es|son|tiene|tienen|hay|va|van|puede|pueden|parece|parecen)\b",
    re.IGNORECASE,
)


def text_sources() -> list[tuple[str, str]]:
    sources: list[tuple[str, str]] = []
    if RENDER_TYPE == "cards":
        for index, segment in enumerate(SEGMENTS, start=1):
            segment_type = segment.get("type")
            if segment_type == "phrase":
                sources.append((f"segment:{index:02d}:text_es", str(segment.get("text_es", ""))))
                sources.append((f"segment:{index:02d}:example_es", str(segment.get("example_es", ""))))
            elif segment_type == "block_header":
                sources.append((f"segment:{index:02d}:title_es", str(segment.get("title_es", ""))))
            elif segment_type in {"intro", "outro"}:
                sources.append((f"segment:{index:02d}:text_es", str(segment.get("text_es", ""))))
    else:
        sources = [(f"segment:{index:02d}", str(segment.get("text", ""))) for index, segment in enumerate(SEGMENTS, start=1)]
    if YOUTUBE_TITLE:
        sources.append(("youtube_title", str(YOUTUBE_TITLE)))
    if DESCRIPTION_INTRO:
        sources.append(("description_intro", str(DESCRIPTION_INTRO)))
    if DESCRIPTION_OUTRO:
        sources.append(("description_outro", str(DESCRIPTION_OUTRO)))
    for index, chapter in enumerate(CHAPTERS or [], start=1):
        sources.append((f"chapter:{index:02d}", str(chapter.get("title", ""))))
    return sources


def find_false_friends(label: str, text: str) -> list[dict[str, str]]:
    findings = []
    lowered = text.lower()
    for word, message in FALSE_FRIENDS.items():
        if re.search(rf"\b{re.escape(word)}(?:s|es|a|as|o|os)?\b", lowered):
            findings.append({"level": "warning", "source": label, "rule": "false_friend", "term": word, "message": message})
    return findings


def find_english_leakage(label: str, text: str) -> list[dict[str, str]]:
    findings = []
    lowered = text.lower()
    for word in ENGLISH_LEAKAGE:
        if re.search(rf"\b{re.escape(word)}\b", lowered):
            findings.append(
                {
                    "level": "error",
                    "source": label,
                    "rule": "english_leakage",
                    "term": word,
                    "message": "English token found in Spanish-facing copy.",
                }
            )
    return findings


def find_subjunctive_trigger_warnings(label: str, text: str) -> list[dict[str, str]]:
    if not any(trigger in text.lower() for trigger in SUBJUNCTIVE_TRIGGERS):
        return []
    if not INDICATIVE_AFTER_TRIGGER.search(text):
        return []
    return [
        {
            "level": "warning",
            "source": label,
            "rule": "subjunctive_trigger",
            "message": "Potential indicative after a subjunctive trigger; linguist should verify.",
        }
    ]


def find_subtitle_length_warnings(label: str, text: str) -> list[dict[str, Any]]:
    if RENDER_TYPE == "cards":
        return []
    if not label.startswith("segment:"):
        return []
    layout = layout_subtitle(text, video_size=output_size_for_design(DESIGN), design=DESIGN)
    if len(layout.lines) <= 2:
        return []
    return [
        {
            "level": "warning",
            "source": label,
            "rule": "subtitle_length",
            "lines": len(layout.lines),
            "message": "Subtitle may exceed the two-line target.",
        }
    ]


def lint() -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for label, text in text_sources():
        findings.extend(find_false_friends(label, text))
        findings.extend(find_english_leakage(label, text))
        findings.extend(find_subjunctive_trigger_warnings(label, text))
        findings.extend(find_subtitle_length_warnings(label, text))

    errors = [finding for finding in findings if finding["level"] == "error"]
    warnings = [finding for finding in findings if finding["level"] == "warning"]
    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "summary": {"sources": len(text_sources()), "errors": len(errors), "warnings": len(warnings)},
    }


def main() -> int:
    result = lint()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
