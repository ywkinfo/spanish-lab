"""Small text adapters for project render variants."""

from __future__ import annotations

from typing import Any

RENDER_TYPE_KENBURNS = "kenburns"
RENDER_TYPE_CARDS = "cards"
RENDER_TYPE_DIARY = "diary"


def get_render_type(project_module: Any) -> str:
    """Return a normalized render type for a loaded project module."""
    render_type = getattr(project_module, "RENDER_TYPE", RENDER_TYPE_KENBURNS) or RENDER_TYPE_KENBURNS
    return str(render_type).strip().lower()


def narration_text(segment: dict, render_type: str) -> str:
    """Return the text that should be synthesized by TTS."""
    if render_type == RENDER_TYPE_CARDS:
        segment_type = segment.get("type")
        if segment_type == "phrase":
            number = int(segment["frase_num"])
            text_es = str(segment["text_es"]).strip()
            return f"Frase número {number}. {text_es} Repite conmigo. {text_es}"
        if segment_type == "dialogue":
            return str(segment["text_es"]).strip()
        if segment_type == "block_header":
            return str(segment["title_es"]).strip()
        if segment_type in {"intro", "outro"}:
            return str(segment["text_es"]).strip()
        return ""
    elif render_type == RENDER_TYPE_DIARY:
        segment_type = segment.get("type")
        if segment_type == "diary_line":
            return str(segment.get("text_es", "")).strip()
        if segment_type == "scene_header":
            return str(segment.get("title_es", "")).strip()
        if segment_type in {"intro", "outro"}:
            return str(segment.get("text_es", "")).strip()
        return ""
    return str(segment["text"]).strip()


def description_text(segment: dict, render_type: str) -> str:
    """Return the human-facing text used in the published description."""
    if render_type == RENDER_TYPE_CARDS:
        segment_type = segment.get("type")
        if segment_type == "phrase":
            number = int(segment["frase_num"])
            return f"{number:02d}. {segment['text_es']} — {segment['text_ko']}"
        if segment_type == "dialogue":
            number = int(segment["line_num"])
            speaker = str(segment.get("speaker", "")).strip()
            text_ko = str(segment.get("text_ko", "")).strip()
            suffix = f" — {text_ko}" if text_ko else ""
            return f"{number:02d}. {speaker}: {segment['text_es']}{suffix}"
        if segment_type == "block_header":
            return f"[{segment['title_es']}]"
        return str(segment.get("text_es", "")).strip()
    elif render_type == RENDER_TYPE_DIARY:
        segment_type = segment.get("type")
        if segment_type == "diary_line":
            speaker = str(segment.get("speaker", "")).strip()
            text_es = str(segment.get("text_es", "")).strip()
            text_ko = str(segment.get("text_ko", "")).strip()
            if speaker:
                return f"{speaker}: {text_es} — {text_ko}"
            return f"{text_es} — {text_ko}"
        if segment_type == "scene_header":
            return f"[{segment.get('title_es', '')}]"
        if segment_type in {"intro", "outro"}:
            return str(segment.get("text_es", "")).strip()
        return ""
    return str(segment["text"]).strip()


def display_text(segment: dict, render_type: str) -> str:
    """Return a compact text summary for preview QA/debug payloads."""
    if render_type == RENDER_TYPE_CARDS:
        segment_type = segment.get("type")
        if segment_type == "phrase":
            return f"#{int(segment['frase_num']):02d} {segment['text_es']} / {segment['text_ko']}"
        if segment_type == "dialogue":
            return f"#{int(segment['line_num']):02d} {segment.get('speaker', '')}: {segment['text_es']} / {segment.get('text_ko', '')}"
        if segment_type == "block_header":
            return f"BLOCK {segment.get('block_id', '?')}: {segment['title_es']}"
        return str(segment.get("text_es", segment_type or "")).strip()
    elif render_type == RENDER_TYPE_DIARY:
        segment_type = segment.get("type")
        if segment_type == "diary_line":
            scene_id = segment.get("scene_id", "?")
            speaker = str(segment.get("speaker", "")).strip()
            text_es = str(segment.get("text_es", "")).strip()
            text_ko = str(segment.get("text_ko", "")).strip()
            sp_prefix = f"{speaker}: " if speaker else ""
            return f"[Scene {scene_id}] {sp_prefix}{text_es} / {text_ko}"
        if segment_type == "scene_header":
            return f"SCENE {segment.get('scene_id', '?')}: {segment.get('title_es', '')}"
        if segment_type == "pause":
            return f"PAUSE {segment.get('duration_s', 0)}s"
        return str(segment.get("text_es", segment_type or "")).strip()
    return str(segment.get("text", "")).strip()
