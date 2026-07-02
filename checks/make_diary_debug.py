"""Generate diary debug frames without requiring a single IMAGE_PATH."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.camera import output_size_for_design  # noqa: E402
from build.diary_timeline import build_diary_timings  # noqa: E402
from build.render_diary import render_diary_background, render_diary_caption  # noqa: E402
from build.segment_adapter import RENDER_TYPE_DIARY, display_text  # noqa: E402
from build.subtitles import load_font  # noqa: E402
from segments import AUDIO, DESIGN, OUTPUT_NAME, SEGMENTS  # noqa: E402

OUTPUT_PATH = ROOT / "output" / "debug" / "diary_contact_sheet.jpg"
SUMMARY_PATH = ROOT / "output" / "debug" / "diary_debug_summary.json"


def crop_scene_image(path: str, design: dict) -> Image.Image | None:
    full_path = ROOT / path
    if not full_path.exists():
        return None

    output_w, output_h = output_size_for_design(design)
    aspect = output_w / output_h
    with Image.open(full_path) as source:
        image = source.convert("RGB")
    source_w, source_h = image.size
    if source_w / source_h > aspect:
        crop_h = source_h
        crop_w = crop_h * aspect
        crop_x = (source_w - crop_w) / 2
        crop_y = 0
    else:
        crop_w = source_w
        crop_h = crop_w / aspect
        crop_x = 0
        y_ratio = float(design.get("diary_crop_y_ratio", 0.5)) if design else 0.5
        crop_y = (source_h - crop_h) * y_ratio
    cropped = image.crop((int(crop_x), int(crop_y), int(crop_x + crop_w), int(crop_y + crop_h)))
    return cropped.resize((output_w, output_h), Image.Resampling.LANCZOS)


def render_debug_frame(segment: dict, timing, design: dict) -> Image.Image:
    scene_image = None
    if timing.type in ("diary_line", "pause"):
        image_path = str(segment.get("image_path", "")).strip()
        if image_path:
            scene_image = crop_scene_image(image_path, design)

    frame = scene_image or render_diary_background(segment, timing, design)
    if timing.type == "diary_line":
        caption = render_diary_caption(timing, design)
        if caption:
            frame.paste(caption, (0, 0), caption)
    return frame.convert("RGB")


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    timings = build_diary_timings(SEGMENTS, design=DESIGN, tts_durations=None, audio_cfg=AUDIO)

    cell_w, cell_h = 320, 180
    label_h = 34
    cols = 4
    rows = math.ceil(len(SEGMENTS) / cols)
    sheet = Image.new("RGB", (cols * cell_w, rows * (cell_h + label_h)), (24, 24, 24))
    draw = ImageDraw.Draw(sheet)
    font = load_font(15)

    entries = []
    for index, (segment, timing) in enumerate(zip(SEGMENTS, timings), start=1):
        row = (index - 1) // cols
        col = (index - 1) % cols
        x = col * cell_w
        y = row * (cell_h + label_h)
        frame = render_debug_frame(segment, timing, DESIGN).resize((cell_w, cell_h), Image.Resampling.LANCZOS)
        sheet.paste(frame, (x, y + label_h))
        draw.rectangle((x, y, x + cell_w, y + label_h), fill=(0, 0, 0))
        label = f"{index:02d} {segment.get('type', '')}"
        if timing.scene_id is not None:
            label += f" s{timing.scene_id}"
        draw.text((x + 8, y + 8), label, font=font, fill=(255, 255, 255))
        entries.append(
            {
                "index": index,
                "type": segment.get("type"),
                "scene_id": timing.scene_id,
                "start_s": round(timing.start_s, 3),
                "duration_s": round(timing.duration_s, 3),
                "text": display_text(segment, RENDER_TYPE_DIARY),
            }
        )

    sheet.save(OUTPUT_PATH, quality=92)
    SUMMARY_PATH.write_text(
        json.dumps(
            {
                "ok": True,
                "project": OUTPUT_NAME,
                "contact_sheet": OUTPUT_PATH.relative_to(ROOT).as_posix(),
                "segments": entries,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "ok": True,
                "output": OUTPUT_PATH.relative_to(ROOT).as_posix(),
                "summary": SUMMARY_PATH.relative_to(ROOT).as_posix(),
                "segments": len(entries),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
