"""Static validation for card-based lesson projects."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw

from build.audio import text_hash, voice_for_segment
from build.segment_adapter import RENDER_TYPE_CARDS, narration_text
from build.subtitles import find_font_path, wrap_text_pixels

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "output" / "audio" / "tts" / "manifest.json"


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_descrip(path: str) -> tuple[list[tuple[int, str, str, str]], list[str]]:
    errors: list[str] = []
    rows: list[tuple[int, str, str, str]] = []
    source = ROOT / path
    if not source.exists():
        return rows, [f"descrip not found: {path}"]
    for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 4:
            errors.append(f"descrip line {line_no}: expected 4 pipe columns, got {len(parts)}")
            continue
        try:
            number = int(parts[0])
        except ValueError:
            errors.append(f"descrip line {line_no}: phrase number must be numeric: {parts[0]!r}")
            continue
        rows.append((number, parts[1], parts[2], parts[3]))
    return rows, errors


def _font(path: str | None, size: int, index: int = 0):
    found = find_font_path(path)
    if not found:
        return None
    from PIL import ImageFont

    return ImageFont.truetype(found, size=size, index=index)


def text_fits(
    text: str,
    *,
    font_path: str | None,
    font_index: int,
    start_size: int,
    min_size: int,
    max_width: int,
    max_lines: int,
) -> bool:
    scratch = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
    draw = ImageDraw.Draw(scratch)
    for size in range(start_size, min_size - 1, -2):
        font = _font(font_path, size, font_index)
        if font is None:
            return False
        lines = wrap_text_pixels(text, font, max_width, draw, stroke_width=0)
        if len(lines) > max_lines:
            continue
        if all(draw.textbbox((0, 0), line, font=font)[2] <= max_width for line in lines):
            return True
    return False


def load_manifest() -> dict[str, Any] | None:
    if not MANIFEST_PATH.exists():
        return None
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def validate_tts_fit(segments: list[dict], audio_cfg: dict | None, errors: list[str], warnings: list[str]) -> None:
    manifest = load_manifest()
    if not manifest:
        warnings.append("TTS manifest not found; run `make tts` then `make check` for TTS fit validation")
        return
    manifest_segments = manifest.get("segments")
    if not isinstance(manifest_segments, list) or len(manifest_segments) != len(segments):
        warnings.append("TTS manifest does not match segment count; skipping TTS fit validation")
        return

    cfg = audio_cfg or {}
    rate_wpm = int(cfg.get("rate_wpm", manifest.get("rate_wpm", 145)))
    expected = [
        text_hash(narration_text(segment, RENDER_TYPE_CARDS), voice_for_segment(segment, cfg), rate_wpm)
        for segment in segments
    ]
    actual = [str(segment.get("text_hash", "")) for segment in manifest_segments]
    if expected != actual:
        warnings.append("TTS manifest hashes do not match current card text; skipping TTS fit validation")
        return

    lead = float(cfg.get("lead_padding_s", 0.25))
    tolerance = float(cfg.get("tts_overlap_tolerance_s", 0.05))
    by_index = {int(segment["index"]): segment for segment in manifest_segments}
    for index, segment in enumerate(segments, start=1):
        tts_duration = float(by_index[index]["tts_duration_s"])
        repeat_pause = float(segment.get("repeat_pause_s", 0.0)) if segment.get("type") == "phrase" else 0.0
        duration = float(segment["duration_s"])
        required = tts_duration + lead + repeat_pause
        if required > duration + tolerance:
            pause_note = f" + pause {repeat_pause:.2f}s" if repeat_pause else ""
            errors.append(
                f"seg #{index}: TTS {tts_duration:.2f}s + lead {lead:.2f}s{pause_note} "
                f"exceeds duration {duration:.2f}s and would overlap the next slide"
            )


def validate(
    segments: list[dict],
    design: dict,
    descrip_path: str,
    audio_cfg: dict | None = None,
) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    output_w, output_h = tuple(design.get("output_size", (1280, 720)))
    font_path = design.get("font_path")
    font_path_ko = design.get("font_path_ko")
    font_index = int(design.get("font_index", 0))
    font_index_ko = int(design.get("font_index_ko", 0))

    if not font_path or not Path(font_path).exists():
        errors.append(f"font_path not found: {font_path}")
    if not font_path_ko or not Path(font_path_ko).exists():
        errors.append(f"font_path_ko not found: {font_path_ko}")

    required_by_type = {
        "intro": {"type", "text_es", "duration_s"},
        "outro": {"type", "text_es", "duration_s"},
        "block_header": {"type", "block_id", "title_es", "title_ko", "color_block", "duration_s"},
        "dialogue": {"type", "line_num", "speaker", "text_es", "text_ko", "color_block", "duration_s"},
        "phrase": {
            "type",
            "frase_num",
            "text_es",
            "text_ko",
            "example_es",
            "block_id",
            "color_block",
            "duration_s",
            "repeat_pause_s",
        },
    }

    phrase_segments = []
    dialogue_segments = []
    block_headers = []
    total_duration = 0.0
    for index, segment in enumerate(segments, start=1):
        segment_type = segment.get("type")
        if segment_type not in required_by_type:
            errors.append(f"seg #{index}: unknown card type {segment_type!r}")
            continue
        missing = required_by_type[segment_type] - segment.keys()
        if missing:
            errors.append(f"seg #{index}: missing fields {sorted(missing)}")
            continue
        duration = float(segment["duration_s"])
        total_duration += duration
        if duration <= 0:
            errors.append(f"seg #{index}: duration_s must be positive")

        if segment_type == "phrase":
            phrase_segments.append(segment)
            if not 8.0 <= duration <= 12.0:
                errors.append(f"seg #{index}: phrase duration_s {duration:.2f}s is outside 8-12s")
            if "|" in segment["text_es"] or "|" in segment["text_ko"] or "|" in segment["example_es"]:
                errors.append(f"seg #{index}: pipe character is not allowed in card text")
            if not text_fits(
                str(segment["text_es"]),
                font_path=font_path,
                font_index=font_index,
                start_size=int(design.get("font_size_es", 88)),
                min_size=int(design.get("min_font_size_es", 54)),
                max_width=int(output_w * 0.82),
                max_lines=2,
            ):
                errors.append(f"seg #{index}: Spanish phrase does not fit card area")
            if not text_fits(
                str(segment["text_ko"]),
                font_path=font_path_ko,
                font_index=font_index_ko,
                start_size=int(design.get("font_size_ko", 36)),
                min_size=28,
                max_width=int(output_w * 0.76),
                max_lines=2,
            ):
                errors.append(f"seg #{index}: Korean translation does not fit card area")
        elif segment_type == "dialogue":
            dialogue_segments.append(segment)
            if not 5.0 <= duration <= 14.0:
                errors.append(f"seg #{index}: dialogue duration_s {duration:.2f}s is outside 5-14s")
            if "|" in segment["text_es"] or "|" in segment["text_ko"]:
                errors.append(f"seg #{index}: pipe character is not allowed in dialogue text")
            if not text_fits(
                str(segment["text_es"]),
                font_path=font_path,
                font_index=font_index,
                start_size=int(design.get("font_size_es", 72)),
                min_size=int(design.get("min_font_size_es", 42)),
                max_width=int(output_w * 0.70),
                max_lines=3,
            ):
                errors.append(f"seg #{index}: Spanish dialogue does not fit card area")
            if not text_fits(
                str(segment["text_ko"]),
                font_path=font_path_ko,
                font_index=font_index_ko,
                start_size=int(design.get("font_size_ko", 34)),
                min_size=26,
                max_width=int(output_w * 0.70),
                max_lines=2,
            ):
                errors.append(f"seg #{index}: Korean dialogue translation does not fit card area")
        elif segment_type == "block_header":
            block_headers.append(segment)

    rows, descrip_errors = parse_descrip(descrip_path)
    errors.extend(descrip_errors)
    expected_phrase_nums = [number for number, *_ in rows]
    numbered_segments = phrase_segments + dialogue_segments
    segment_nums = [int(segment.get("frase_num", segment.get("line_num"))) for segment in numbered_segments]
    if expected_phrase_nums and segment_nums != expected_phrase_nums:
        errors.append(f"numbered segments must match descrip order {expected_phrase_nums}, got {segment_nums}")
    if not expected_phrase_nums and segment_nums:
        errors.append(f"descrip has no numbered rows, but SEGMENTS has numbered entries {segment_nums}")
    if not 1 <= len(block_headers) <= 10:
        errors.append(f"expected 1-10 block headers, got {len(block_headers)}")

    segment_by_num = {int(segment.get("frase_num", segment.get("line_num"))): segment for segment in numbered_segments}
    for number, text_es, text_ko, example_es in rows:
        segment = segment_by_num.get(number)
        if not segment:
            errors.append(f"descrip row #{number:02d} is missing from SEGMENTS")
            continue
        if normalize(segment["text_es"]) != normalize(text_es):
            errors.append(f"row #{number:02d}: text_es differs from descrip")
        if normalize(segment["text_ko"]) != normalize(text_ko):
            errors.append(f"row #{number:02d}: text_ko differs from descrip")
        if segment.get("type") == "phrase" and normalize(segment["example_es"]) != normalize(example_es):
            errors.append(f"phrase #{number:02d}: example_es differs from descrip")

    validate_tts_fit(segments, audio_cfg, errors, warnings)

    summary = {
        "segments": len(segments),
        "phrases": len(phrase_segments),
        "dialogue": len(dialogue_segments),
        "block_headers": len(block_headers),
        "output_size": [output_w, output_h],
        "duration_sum_s": round(total_duration, 3),
        "warnings": warnings,
        "errors": errors,
    }
    return errors, warnings, summary
