"""Static validation for segment data."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.camera import DEFAULT_OUTPUT_SIZE, TARGET_ASPECT, output_size_for_design  # noqa: E402
from build.subtitles import layout_subtitle  # noqa: E402
from build.timeline import duration_for_text, expected_total_duration, transition_s  # noqa: E402
from segments import (  # noqa: E402
    AUDIO, DESCRIP_PATH, DESIGN, IMAGE_PATH, RENDER_TYPE, SEGMENTS,
    SERIES, SERIES_TITLE, OUTPUT_NAME, YOUTUBE_TITLE, DESCRIPTION_INTRO,
    DESCRIPTION_OUTRO, KOREAN_TEASER, EPISODE, RENDER_VERSION,
    PHRASES, BLOCKS, CHAPTERS, MINI_QUIZ, BASE_TAGS, EXTRA_TAGS,
    BASE_HASHTAGS, EXTRA_HASHTAGS, PUBLIC_SLUG, LANGUAGE,
    STORY_SCENES, SFX_MANIFEST, SEGMENT_SFX
)

BASE_MIN_W = 360
BASE_MIN_H = 203
ASPECT_TOLERANCE = 0.02


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def source_sentences() -> list[str]:
    text = (ROOT / DESCRIP_PATH).read_text(encoding="utf-8")
    body = re.sub(r"^#.*\n+", "", text).strip()
    return [normalize_text(sentence) for sentence in re.split(r"(?<=[.!?])\s+", body) if sentence.strip()]


def min_frame_size() -> tuple[int, int]:
    output_w, _ = output_size_for_design(DESIGN)
    scale = output_w / DEFAULT_OUTPUT_SIZE[0]
    return int(BASE_MIN_W * scale), int(BASE_MIN_H * scale)


def suggest_16x9(frame: dict[str, int], image_w: int, image_h: int) -> dict[str, int]:
    min_w, min_h = min_frame_size()
    center_x = frame["x"] + frame["w"] / 2
    center_y = frame["y"] + frame["h"] / 2
    width = max(min_w, frame["w"])
    height = round(width / TARGET_ASPECT)
    if height < min_h:
        height = min_h
        width = round(height * TARGET_ASPECT)
    if width > image_w:
        width = image_w
        height = round(width / TARGET_ASPECT)
    if height > image_h:
        height = image_h
        width = round(height * TARGET_ASPECT)
    x = round(max(0, min(image_w - width, center_x - width / 2)))
    y = round(max(0, min(image_h - height, center_y - height / 2)))
    return {"x": x, "y": y, "w": width, "h": height}


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    image_path = ROOT / IMAGE_PATH
    if not image_path.exists():
        errors.append(f"image not found: {IMAGE_PATH}")
        return errors, warnings, {}

    image_w, image_h = Image.open(image_path).size
    output_size = output_size_for_design(DESIGN)
    min_w, min_h = min_frame_size()
    required_segment_fields = {"text", "frame"}
    required_frame_fields = {"x", "y", "w", "h"}
    duration_sum = 0.0

    for index, segment in enumerate(SEGMENTS, start=1):
        missing = required_segment_fields - segment.keys()
        if missing:
            errors.append(f"seg #{index}: missing fields {sorted(missing)}")
            continue
        frame = segment["frame"]
        missing_frame = required_frame_fields - frame.keys()
        if missing_frame:
            errors.append(f"seg #{index}: missing frame fields {sorted(missing_frame)}")
            continue

        for key in required_frame_fields:
            if not isinstance(frame[key], int):
                errors.append(f"seg #{index}: frame.{key} must be int, got {type(frame[key]).__name__}")

        x, y, w, h = frame["x"], frame["y"], frame["w"], frame["h"]
        if x < 0 or y < 0 or x + w > image_w or y + h > image_h:
            errors.append(
                f"seg #{index}: frame out of image bounds ({x},{y},{w},{h}); "
                f"image={image_w}x{image_h}, suggested={suggest_16x9(frame, image_w, image_h)}"
            )
        if w < min_w:
            errors.append(f"seg #{index}: w={w} < {min_w}, suggested={suggest_16x9(frame, image_w, image_h)}")
        if h < min_h:
            errors.append(f"seg #{index}: h={h} < {min_h}, suggested={suggest_16x9(frame, image_w, image_h)}")

        ratio = w / h
        if abs(ratio - TARGET_ASPECT) / TARGET_ASPECT > ASPECT_TOLERANCE:
            errors.append(
                f"seg #{index}: aspect={ratio:.3f} not within ±2% of 16:9; "
                f"suggested={suggest_16x9(frame, image_w, image_h)}"
            )

        text = segment["text"]
        formula_duration = duration_for_text(text)
        duration = float(segment.get("duration_s", formula_duration))
        duration_sum += duration
        if "duration_s" in segment and duration <= 0:
            errors.append(f"seg #{index}: duration_s must be positive")
        if "duration_s" in segment and abs(duration - formula_duration) > 0.01:
            warnings.append(
                f"seg #{index}: duration_s override {duration:.2f}s differs from formula {formula_duration:.2f}s"
            )

        layout = layout_subtitle(text, video_size=output_size, design=DESIGN)
        if len(layout.lines) > 2:
            errors.append(
                f"seg #{index}: subtitle wraps to {len(layout.lines)} lines at min font {layout.font_size}; "
                "shorten text or allow smaller font"
            )

    combined_segments = normalize_text(" ".join(segment.get("text", "") for segment in SEGMENTS))
    for sentence_index, sentence in enumerate(source_sentences(), start=1):
        if sentence not in combined_segments:
            errors.append(f"source sentence #{sentence_index} is not covered by segment text: {sentence}")

    summary = {
        "segments": len(SEGMENTS),
        "source_sentences": len(source_sentences()),
        "output_size": output_size,
        "min_frame_size": [min_w, min_h],
        "duration_sum_s": round(duration_sum, 3),
        "transition_s": transition_s(DESIGN),
        "expected_total_s": round(expected_total_duration(SEGMENTS, design=DESIGN), 3),
        "warnings": warnings,
        "errors": errors,
    }
    return errors, warnings, summary


def validate_metadata() -> list[str]:
    errors: list[str] = []

    # Series subject to full metadata validation. Diary-format series built on the
    # historia-a1 rules (same required fields, MINI_QUIZ, slug/DESCRIP_PATH matching)
    # opt in here so they cannot silently bypass validate_metadata().
    if SERIES not in ("historia-a1", "diario-a2", "camino-a2"):
        return errors

    # Check RENDER_TYPE and LANGUAGE
    if RENDER_TYPE not in ("cards", "diary"):
        errors.append(f"{SERIES} validation: RENDER_TYPE must be 'cards' or 'diary', got {RENDER_TYPE!r}")
    if LANGUAGE != "es":
        errors.append(f"{SERIES} validation: LANGUAGE must be 'es', got {LANGUAGE!r}")

    # Required string fields
    required_strings = {
        "PUBLIC_SLUG": PUBLIC_SLUG,
        "OUTPUT_NAME": OUTPUT_NAME,
        "SERIES_TITLE": SERIES_TITLE,
        "YOUTUBE_TITLE": YOUTUBE_TITLE,
        "DESCRIPTION_INTRO": DESCRIPTION_INTRO,
        "DESCRIPTION_OUTRO": DESCRIPTION_OUTRO,
        "KOREAN_TEASER": KOREAN_TEASER,
    }
    for field_name, field_val in required_strings.items():
        if not field_val or not isinstance(field_val, str) or not field_val.strip():
            errors.append(f"{SERIES} validation: missing or empty required string field {field_name!r}")

    # Required numeric fields
    required_numbers = {
        "EPISODE": EPISODE,
        "RENDER_VERSION": RENDER_VERSION,
    }
    for field_name, field_val in required_numbers.items():
        if field_val is None or isinstance(field_val, bool) or not isinstance(field_val, (int, float)):
            errors.append(f"{SERIES} validation: missing or invalid numeric field {field_name!r}")

    # Required structures (list/dict/tuple)
    required_structures = {
        "CHAPTERS": CHAPTERS,
        "MINI_QUIZ": MINI_QUIZ,
        "BASE_TAGS": BASE_TAGS,
        "EXTRA_TAGS": EXTRA_TAGS,
        "BASE_HASHTAGS": BASE_HASHTAGS,
        "EXTRA_HASHTAGS": EXTRA_HASHTAGS,
    }
    if RENDER_TYPE == "cards":
        required_structures["PHRASES"] = PHRASES
        required_structures["BLOCKS"] = BLOCKS
    elif RENDER_TYPE == "diary":
        required_structures["STORY_SCENES"] = STORY_SCENES

    for field_name, field_val in required_structures.items():
        if field_val is None or not isinstance(field_val, (list, tuple, dict)):
            errors.append(f"{SERIES} validation: missing or invalid structure field {field_name!r}")

    # PUBLIC_SLUG directory matching DESCRIP_PATH folder
    if DESCRIP_PATH and PUBLIC_SLUG:
        try:
            folder_name = Path(DESCRIP_PATH).parent.name
        except Exception:
            folder_name = ""
        if folder_name != PUBLIC_SLUG:
            errors.append(
                f"{SERIES} validation: PUBLIC_SLUG {PUBLIC_SLUG!r} must match DESCRIP_PATH directory {folder_name!r}"
            )

    # MINI_QUIZ count must be exactly 5
    if MINI_QUIZ is not None:
        if not isinstance(MINI_QUIZ, (list, tuple)) or len(MINI_QUIZ) != 5:
            errors.append(
                f"{SERIES} validation: MINI_QUIZ must have exactly 5 questions, "
                f"got {len(MINI_QUIZ) if isinstance(MINI_QUIZ, (list, tuple)) else type(MINI_QUIZ).__name__}"
            )

    return errors


def main() -> int:
    if RENDER_TYPE == "cards":
        from checks.validate_cards import validate as validate_cards

        errors, warnings, summary = validate_cards(SEGMENTS, DESIGN, DESCRIP_PATH, AUDIO)
    elif RENDER_TYPE == "diary":
        from checks.validate_diary import validate as validate_diary
        from build.diary_timeline import expected_diary_total_duration

        errors, warnings, summary = validate_diary(STORY_SCENES, SFX_MANIFEST, DESIGN, DESCRIP_PATH, SEGMENT_SFX)
        summary["render_estimate_s"] = round(expected_diary_total_duration(SEGMENTS, audio_cfg=AUDIO), 3)
    else:
        errors, warnings, summary = validate()

    meta_errors = validate_metadata()
    errors.extend(meta_errors)
    if "errors" in summary:
        summary["errors"].extend(meta_errors)

    print(json.dumps({"ok": not errors, **summary}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

