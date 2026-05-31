"""Render static card-based Spanish-learning videos."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from build.audio import (
    assert_tts_fits_timeline,
    build_narration_wav,
    mix_with_bgm,
    mux_into_video,
    synthesize_segments,
    write_manifest,
)
from build.card_timeline import CardTiming, build_card_timings
from build.camera import output_size_for_design
from build.segment_adapter import RENDER_TYPE_CARDS
from build.subtitles import find_font_path, wrap_text_pixels

OUTPUT_DIR = Path("output")

DEFAULT_COLORS = {
    "coral": (224, 91, 76),
    "amber": (230, 158, 62),
    "teal": (44, 150, 142),
    "blue": (70, 120, 196),
    "green": (92, 148, 86),
    "violet": (138, 104, 190),
    "rose": (199, 90, 126),
    "indigo": (87, 98, 174),
    "red": (207, 72, 72),
    "slate": (87, 99, 115),
    "neutral": (42, 48, 57),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a card-based Spanish-learning video.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preview", action="store_true", help="Render a fast 12 fps preview.")
    mode.add_argument("--final", action="store_true", help="Render the final 30 fps MP4.")
    return parser.parse_args()


def _color(name: str | None, design: dict | None = None) -> tuple[int, int, int]:
    palette = dict(DEFAULT_COLORS)
    if design:
        palette.update({key: tuple(value) for key, value in design.get("color_blocks", {}).items()})
    return tuple(palette.get(str(name or "neutral"), DEFAULT_COLORS["neutral"]))


def _font(path: str | None, size: int, index: int = 0) -> ImageFont.ImageFont:
    found = find_font_path(path)
    if found:
        return ImageFont.truetype(found, size=size, index=index)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def _measure(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text or "Ag", font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def _fit_lines(
    text: str,
    *,
    draw: ImageDraw.ImageDraw,
    font_path: str | None,
    font_index: int,
    start_size: int,
    min_size: int,
    max_width: int,
    max_lines: int,
    max_height: int | None = None,
    spacing: int = 10,
) -> tuple[list[str], ImageFont.ImageFont, int]:
    for size in range(start_size, min_size - 1, -2):
        font = _font(font_path, size, font_index)
        lines = wrap_text_pixels(text, font, max_width, draw, stroke_width=0)
        if len(lines) <= max_lines:
            too_wide = any(_measure(draw, line, font)[0] > max_width for line in lines)
            if not too_wide:
                if max_height is not None:
                    total_height = sum(_measure(draw, line, font)[1] for line in lines) + spacing * (len(lines) - 1)
                    if total_height > max_height:
                        continue
                return lines, font, size
    font = _font(font_path, min_size, font_index)
    return wrap_text_pixels(text, font, max_width, draw, stroke_width=0), font, min_size


def _draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: Iterable[str],
    font: ImageFont.ImageFont,
    y: int,
    width: int,
    fill: tuple[int, int, int],
    spacing: int,
) -> int:
    current_y = y
    for line in lines:
        line_w, line_h = _measure(draw, line, font)
        draw.text(((width - line_w) // 2, current_y), line, font=font, fill=fill)
        current_y += line_h + spacing
    return current_y


def _draw_centered_lines_in_box(
    draw: ImageDraw.ImageDraw,
    lines: Iterable[str],
    font: ImageFont.ImageFont,
    y: int,
    box: tuple[int, int],
    fill: tuple[int, int, int],
    spacing: int,
) -> int:
    left, right = box
    current_y = y
    for line in lines:
        line_w, line_h = _measure(draw, line, font)
        draw.text((left + (right - left - line_w) // 2, current_y), line, font=font, fill=fill)
        current_y += line_h + spacing
    return current_y


def _draw_pill(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    outline: tuple[int, int, int],
) -> None:
    draw.rounded_rectangle(box, radius=(box[3] - box[1]) // 2, fill=fill, outline=outline, width=2)
    text_w, text_h = _measure(draw, text, font)
    draw.text(
        ((box[0] + box[2] - text_w) // 2, (box[1] + box[3] - text_h) // 2 - 1),
        text,
        font=font,
        fill=outline,
    )


def _character_path(name: str | None, design: dict | None) -> str | None:
    if not name or not design:
        return None
    images = design.get("character_images", {})
    if not isinstance(images, dict):
        return None
    path = images.get(str(name))
    return str(path) if path else None


def _load_character_portrait(name: str | None, design: dict | None, size: int) -> Image.Image | None:
    path = _character_path(name, design)
    if not path:
        return None
    portrait_path = Path(path)
    if not portrait_path.exists():
        return None
    try:
        portrait = Image.open(portrait_path).convert("RGB")
    except OSError:
        return None
    portrait = portrait.resize((size, size), Image.Resampling.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, size - 1, size - 1), fill=255)
    framed = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    framed.paste(portrait, (0, 0), mask)
    return framed


def _draw_character_portrait(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    name: str | None,
    design: dict | None,
    *,
    center: tuple[int, int],
    size: int,
    accent: tuple[int, int, int],
    label_font: ImageFont.ImageFont | None = None,
) -> None:
    portrait = _load_character_portrait(name, design, size)
    if portrait is None:
        return
    x = center[0] - size // 2
    y = center[1] - size // 2
    draw.ellipse((x - 6, y - 6, x + size + 6, y + size + 6), fill=(255, 255, 255), outline=accent, width=5)
    image.paste(portrait, (x, y), portrait)
    if name and label_font:
        text_w, text_h = _measure(draw, str(name), label_font)
        box = (center[0] - text_w // 2 - 18, y + size + 13, center[0] + text_w // 2 + 18, y + size + text_h + 29)
        draw.rounded_rectangle(box, radius=18, fill=(255, 255, 255), outline=accent, width=2)
        draw.text((center[0] - text_w // 2, y + size + 20), str(name), font=label_font, fill=accent)


def _draw_character_lineup(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    names: list[str],
    design: dict | None,
    *,
    y: int,
    size: int,
    accent: tuple[int, int, int],
    width: int,
    label_font: ImageFont.ImageFont,
) -> None:
    if not names:
        return
    spacing = size + 42
    total = spacing * (len(names) - 1) + size
    start_x = width // 2 - total // 2
    for i, name in enumerate(names):
        _draw_character_portrait(image, draw, name, design, center=(start_x + spacing * i, y), size=size, accent=accent, label_font=label_font)


def _clothing_asset_path(item: str, design: dict | None) -> str | None:
    if not item or not design:
        return None
    assets = design.get("clothing_images", {})
    if not isinstance(assets, dict):
        return None
    path = assets.get(str(item))
    return str(path) if path else None


def _load_clothing_asset(item: str, design: dict | None, size: int) -> Image.Image | None:
    path = _clothing_asset_path(item, design)
    if not path:
        return None
    try:
        source = Image.open(Path(path)).convert("RGBA")
    except FileNotFoundError:
        return None
    source.thumbnail((size, size), Image.LANCZOS)
    tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    tile.paste(source, ((size - source.width) // 2, (size - source.height) // 2), source)
    return tile


def _draw_clothing_cards(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    items: list[str] | tuple[str, ...] | None,
    design: dict | None,
    *,
    origin: tuple[int, int],
    card_size: int,
    accent: tuple[int, int, int],
    label_font: ImageFont.ImageFont,
) -> None:
    if not items:
        return
    spacing = card_size + 18
    for index, item in enumerate([str(v) for v in items if str(v).strip()]):
        x = origin[0] + index * spacing
        y = origin[1]
        draw.rounded_rectangle(
            (x + 5, y + 7, x + card_size + 5, y + card_size + 7),
            radius=20,
            fill=(0, 0, 0, 30),
        )
        draw.rounded_rectangle(
            (x, y, x + card_size, y + card_size),
            radius=20,
            fill=(255, 255, 255),
            outline=accent,
            width=4,
        )
        asset = _load_clothing_asset(item, design, card_size - 28)
        if asset:
            image.paste(asset, (x + 14, y + 10), asset)
        label = item.replace("_", " ")
        text_w, text_h = _measure(draw, label, label_font)
        draw.text((x + (card_size - text_w) // 2, y + card_size - text_h - 9), label, font=label_font, fill=accent)


def _cover_crop(source: Image.Image, size: tuple[int, int]) -> Image.Image:

    target_w, target_h = size
    scale = max(target_w / source.width, target_h / source.height)
    resized = source.resize((int(source.width * scale + 0.5), int(source.height * scale + 0.5)), Image.Resampling.LANCZOS)
    left = max(0, (resized.width - target_w) // 2)
    top = max(0, (resized.height - target_h) // 2)
    return resized.crop((left, top, left + target_w, top + target_h))


def _contain_resize(source: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize an image to fit fully inside ``size`` without cropping."""
    target_w, target_h = size
    scale = min(target_w / source.width, target_h / source.height)
    return source.resize((int(source.width * scale + 0.5), int(source.height * scale + 0.5)), Image.Resampling.LANCZOS)


def _load_design_image(path_value: str | None) -> Image.Image | None:
    if not path_value:
        return None
    path = Path(path_value)
    if not path.exists():
        return None
    try:
        return Image.open(path).convert("RGB")
    except Exception:
        return None


def render_card_image(segment: dict, timing: CardTiming | None, design: dict | None = None) -> Image.Image:
    """Render one card as a full-size RGB PIL image."""
    width, height = output_size_for_design(design)
    image = Image.new("RGB", (width, height), tuple(design.get("background_color", (248, 247, 242))) if design else (248, 247, 242))
    draw = ImageDraw.Draw(image)
    accent = _color(segment.get("color_block"), design)
    ink = tuple(design.get("text_color", (31, 35, 40))) if design else (31, 35, 40)
    muted = tuple(design.get("muted_text_color", (96, 101, 109))) if design else (96, 101, 109)
    font_path = design.get("font_path") if design else None
    font_path_ko = design.get("font_path_ko") if design else None
    font_index = int(design.get("font_index", 0)) if design else 0
    font_index_ko = int(design.get("font_index_ko", 0)) if design else 0
    segment_type = segment.get("type")

    draw.rectangle((0, 0, width, 18), fill=accent)
    draw.rectangle((0, height - 18, width, height), fill=accent)

    if segment_type == "intro":
        scene = _load_design_image(str(design.get("intro_scene_image_path", "")) if design else "")
        if scene is not None:
            scene_w = int(width * 0.48)
            scene_h = height - 36
            if str(design.get("intro_scene_fit", "cover")) == "contain":
                scene_panel = _cover_crop(scene, (scene_w, scene_h)).filter(ImageFilter.GaussianBlur(14))
                wash = Image.new("RGB", scene_panel.size, (255, 250, 238))
                scene_panel = Image.blend(scene_panel, wash, 0.32)
                foreground = _contain_resize(scene, (scene_w - 34, scene_h - 60))
                fx = max(0, (scene_w - foreground.width) // 2)
                fy = max(0, (scene_h - foreground.height) // 2)
                scene_panel.paste(foreground, (fx, fy))
            else:
                scene_panel = _cover_crop(scene, (scene_w, scene_h))
            image.paste(scene_panel, (0, 18))
            draw.rectangle((scene_w - 12, 18, scene_w, height - 18), fill=accent)
            draw.rectangle((scene_w, 18, width, height - 18), fill=tuple(design.get("background_color", (248, 247, 242))))
            draw = ImageDraw.Draw(image)
            title_font = _font(font_path, min(64, int(design.get("font_size_title", 82))), font_index)
            sub_font = _font(font_path, int(design.get("font_size_example", 34)), font_index)
            ko_font = _font(font_path_ko, int(design.get("font_size_ko", 36)), font_index_ko)
            label_font = _font(font_path, 24, font_index)
            box = (scene_w + 44, width - 48)
            title_lines, title_font, _ = _fit_lines(
                str(design.get("intro_title", "Mira la imagen")),
                draw=draw,
                font_path=font_path,
                font_index=font_index,
                start_size=min(64, int(design.get("font_size_title", 82))),
                min_size=48,
                max_width=box[1] - box[0],
                max_lines=2,
            )
            title_end_y = _draw_centered_lines_in_box(draw, title_lines, title_font, 82, box, ink, 8)
            draw.text((box[0], max(172, title_end_y + 26)), str(design.get("intro_subtitle", "Español A1")), font=sub_font, fill=accent)
            lines, font, _ = _fit_lines(
                str(segment["text_es"]),
                draw=draw,
                font_path=font_path,
                font_index=font_index,
                start_size=34,
                min_size=25,
                max_width=box[1] - box[0],
                max_lines=5,
            )
            _draw_centered_lines_in_box(draw, lines, font, 275, box, ink, 12)
            _draw_centered_lines_in_box(draw, [str(design.get("intro_ko", "읽고 듣고 따라 말해 보세요"))], ko_font, 610, box, muted, 10)
            _draw_clothing_cards(
                image,
                draw,
                segment.get("clothing_items"),
                design,
                origin=(760, 520),
                card_size=112,
                accent=accent,
                label_font=_font(font_path, 18, font_index),
            )
            return image

        title_font = _font(font_path, int(design.get("font_size_title", 82)), font_index)
        sub_font = _font(font_path, int(design.get("font_size_example", 34)), font_index)
        ko_font = _font(font_path_ko, int(design.get("font_size_ko", 36)), font_index_ko)
        label_font = _font(font_path, 24, font_index)
        _draw_centered_lines(draw, [str(design.get("intro_title", "50 frases útiles"))], title_font, 82, width, ink, 16)
        _draw_centered_lines(draw, [str(design.get("intro_subtitle", "Español A1"))], sub_font, 193, width, accent, 12)
        characters = [str(name) for name in segment.get("characters", [])]
        if design.get("show_character_portraits") and characters:
            _draw_character_lineup(image, draw, characters, design, y=330, size=132, accent=accent, width=width, label_font=label_font)
        lines, font, _ = _fit_lines(
            str(segment["text_es"]),
            draw=draw,
            font_path=font_path,
            font_index=font_index,
            start_size=30,
            min_size=24,
            max_width=int(width * 0.72),
            max_lines=3,
        )
        _draw_centered_lines(draw, lines, font, 490, width, muted, 10)
        _draw_centered_lines(draw, [str(design.get("intro_ko", "읽고 듣고 따라 말해 보세요"))], ko_font, 615, width, ink, 10)
        _draw_clothing_cards(
            image,
            draw,
            segment.get("clothing_items"),
            design,
            origin=(width - 380, 500),
            card_size=104,
            accent=accent,
            label_font=_font(font_path, 17, font_index),
        )
        return image

    if segment_type == "outro":
        title_font = _font(font_path, 58, font_index)
        ko_font = _font(font_path_ko, int(design.get("font_size_ko", 36)) if design else 36, font_index_ko)
        label_font = _font(font_path, 22, font_index)
        _draw_centered_lines(draw, ["Muy bien"], title_font, 80, width, accent, 16)
        characters = [str(name) for name in segment.get("characters", [])]
        if design.get("show_character_portraits") and characters:
            _draw_character_lineup(image, draw, characters, design, y=245, size=118, accent=accent, width=width, label_font=label_font)
        outro_y = int(design.get("outro_text_y", 425)) if design else 425
        outro_ko_y = int(design.get("outro_ko_y", 590)) if design else 590
        max_h = max(48, outro_ko_y - outro_y - 20)
        lines, font, _ = _fit_lines(
            str(segment["text_es"]),
            draw=draw,
            font_path=font_path,
            font_index=font_index,
            start_size=int(design.get("outro_font_size_es", 48)) if design else 48,
            min_size=20,
            max_width=int(width * float(design.get("outro_text_width_ratio", 0.72))) if design else int(width * 0.72),
            max_lines=int(design.get("outro_max_lines", 5)) if design else 5,
            max_height=max_h,
            spacing=10,
        )
        _draw_centered_lines(draw, lines, font, outro_y, width, ink, 10)
        _draw_centered_lines(draw, [str(design.get("outro_ko", "다음 영상에서 또 연습해요"))], ko_font, int(design.get("outro_ko_y", 590)) if design else 590, width, muted, 12)
        _draw_clothing_cards(
            image,
            draw,
            segment.get("clothing_items"),
            design,
            origin=(width - 420, 485),
            card_size=88,
            accent=accent,
            label_font=_font(font_path, 15, font_index),
        )
        return image

    if segment_type == "block_header":
        block_font = _font(font_path, 34, font_index)
        title_font = _font(font_path, 78, font_index)
        ko_font = _font(font_path_ko, 40, font_index_ko)
        draw.rectangle((0, 120, width, 505), fill=accent)
        draw.text((84, 150), f"Bloque {int(segment['block_id']):02d}", font=block_font, fill=(255, 255, 255))
        _draw_centered_lines(draw, [str(segment["title_es"])], title_font, 260, width, (255, 255, 255), 14)
        _draw_centered_lines(draw, [str(segment["title_ko"])], ko_font, 380, width, (255, 255, 255), 12)
        _draw_clothing_cards(
            image,
            draw,
            segment.get("clothing_items"),
            design,
            origin=(width - 360, 515),
            card_size=96,
            accent=accent,
            label_font=_font(font_path, 16, font_index),
        )
        return image

    if segment_type == "dialogue":
        card_has_portrait = bool(design and design.get("show_character_portraits") and segment.get("speaker"))
        text_box = (70, int(width * 0.70)) if card_has_portrait else (90, width - 90)
        max_text_width = text_box[1] - text_box[0]
        label_font = _font(font_path, 28, font_index)
        speaker_font = _font(font_path, 46, font_index)
        ko_font = _font(font_path_ko, int(design.get("font_size_ko", 34)) if design else 34, font_index_ko)
        note_font = _font(font_path, 26, font_index)
        speaker = str(segment.get("speaker", ""))
        draw.text((70, 54), f"Línea {int(segment['line_num']):02d}", font=label_font, fill=accent)
        conversation_label = str(design.get("conversation_label", "Conversación A1")) if design else "Conversación A1"
        label_bbox = draw.textbbox((0, 0), conversation_label, font=label_font)
        draw.text((width - 70 - (label_bbox[2] - label_bbox[0]), 54), conversation_label, font=label_font, fill=muted)
        draw.text((text_box[0], 132), speaker, font=speaker_font, fill=accent)
        es_lines, es_font, es_size = _fit_lines(
            str(segment["text_es"]),
            draw=draw,
            font_path=font_path,
            font_index=font_index,
            start_size=int(design.get("font_size_es", 72)) if design else 72,
            min_size=int(design.get("min_font_size_es", 42)) if design else 42,
            max_width=max_text_width,
            max_lines=3,
        )
        next_y = _draw_centered_lines_in_box(draw, es_lines, es_font, 220, text_box, ink, max(10, es_size // 5))
        ko_lines, ko_font, _ = _fit_lines(
            str(segment["text_ko"]),
            draw=draw,
            font_path=font_path_ko,
            font_index=font_index_ko,
            start_size=int(design.get("font_size_ko", 34)) if design else 34,
            min_size=26,
            max_width=max_text_width,
            max_lines=2,
        )
        _draw_centered_lines_in_box(draw, ko_lines, ko_font, max(385, next_y + 24), text_box, muted, 10)
        focus = str(segment.get("focus", "")).strip()
        if focus:
            _draw_pill(draw, (text_box[0], 560, text_box[1], 620), focus, note_font, (255, 255, 255), accent)
        if card_has_portrait:
            _draw_character_portrait(
                image,
                draw,
                speaker,
                design,
                center=(1045, 305),
                size=190,
                accent=accent,
                label_font=_font(font_path, 24, font_index),
            )
        _draw_clothing_cards(
            image,
            draw,
            segment.get("clothing_items"),
            design,
            origin=(925, 500),
            card_size=105,
            accent=accent,
            label_font=_font(font_path, 15, font_index),
        )
        return image

    card_has_portrait = bool(design and design.get("show_character_portraits") and segment.get("character"))
    text_box = (70, int(width * 0.70)) if card_has_portrait else (0, width)
    max_text_width = text_box[1] - text_box[0]

    # phrase card
    label_font = _font(font_path, 28, font_index)
    es_lines, es_font, es_size = _fit_lines(
        str(segment["text_es"]),
        draw=draw,
        font_path=font_path,
        font_index=font_index,
        start_size=int(design.get("font_size_es", 88)) if design else 88,
        min_size=int(design.get("min_font_size_es", 54)) if design else 54,
        max_width=max_text_width,
        max_lines=2,
    )
    ko_lines, ko_font, _ = _fit_lines(
        str(segment["text_ko"]),
        draw=draw,
        font_path=font_path_ko,
        font_index=font_index_ko,
        start_size=int(design.get("font_size_ko", 36)) if design else 36,
        min_size=28,
        max_width=max_text_width,
        max_lines=2,
    )
    ex_lines, ex_font, _ = _fit_lines(
        f"Ejemplo: {segment['example_es']}",
        draw=draw,
        font_path=font_path,
        font_index=font_index,
        start_size=int(design.get("font_size_example", 34)) if design else 34,
        min_size=25,
        max_width=max_text_width,
        max_lines=2,
    )

    draw.text((70, 54), f"Frase {int(segment['frase_num']):02d}", font=label_font, fill=accent)
    draw.text((width - 220, 54), "Español A1", font=label_font, fill=muted)
    if card_has_portrait:
        _draw_character_portrait(
            image,
            draw,
            str(segment.get("character")),
            design,
            center=(1045, 305),
            size=190,
            accent=accent,
            label_font=_font(font_path, 24, font_index),
        )
    next_y = _draw_centered_lines_in_box(draw, es_lines, es_font, 135, text_box, ink, max(10, es_size // 5))
    _draw_centered_lines_in_box(draw, ko_lines, ko_font, max(315, next_y + 20), text_box, muted, 10)
    _draw_centered_lines_in_box(draw, ex_lines, ex_font, 445, text_box, (75, 82, 93), 10)

    pill_font = _font(font_path, 28, font_index)
    pause = float(segment.get("repeat_pause_s", 0.0))
    pill_center = (text_box[0] + text_box[1]) // 2
    _draw_pill(
        draw,
        (pill_center - 185, 598, pill_center + 185, 654),
        f"Repite ahora {pause:.0f}s",
        pill_font,
        (255, 255, 255),
        accent,
    )
    return image


def synthesize_card_thumbnail(segments: list[dict], design: dict | None, path: Path) -> None:
    """Create a simple fallback thumbnail for card projects."""
    width, height = (1280, 720)
    image = Image.new("RGB", (width, height), (248, 247, 242))
    draw = ImageDraw.Draw(image)
    accent = _color("coral", design)
    font_path = design.get("font_path") if design else None
    font_path_ko = design.get("font_path_ko") if design else None
    title_font = _font(font_path, 92, int(design.get("font_index", 0)) if design else 0)
    sub_font = _font(font_path, 54, int(design.get("font_index", 0)) if design else 0)
    ko_font = _font(font_path_ko, 42, int(design.get("font_index_ko", 0)) if design else 0)
    draw.rectangle((0, 0, width, 76), fill=accent)
    draw.rectangle((0, height - 76, width, height), fill=accent)
    characters = ["Peter", "Lucía", "Diego"] if design and design.get("character_images") else []
    if characters:
        _draw_character_lineup(image, draw, characters, design, y=180, size=118, accent=accent, width=width, label_font=_font(font_path, 20, int(design.get("font_index", 0))))
        title_y = 305
        sub_y = 420
        ko_y = 510
    else:
        title_y = 185
        sub_y = 330
        ko_y = 445
    _draw_centered_lines(draw, [str(design.get("thumbnail_title", "50 frases útiles"))], title_font, title_y, width, (31, 35, 40), 16)
    _draw_centered_lines(draw, [str(design.get("thumbnail_subtitle", "Español A1"))], sub_font, sub_y, width, accent, 12)
    _draw_centered_lines(draw, [str(design.get("thumbnail_ko", "오늘 바로 쓰는 스페인어 표현"))], ko_font, ko_y, width, (62, 68, 76), 12)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="JPEG", quality=92, optimize=True)


def build_card_video_clip(segments: list[dict], design: dict | None, timings: list[CardTiming]):
    from moviepy import CompositeVideoClip, ImageClip

    output_size = output_size_for_design(design)
    clips = []
    for segment, timing in zip(segments, timings):
        image = render_card_image(segment, timing, design)
        clip = ImageClip(np.asarray(image)).with_start(timing.start_s).with_duration(timing.duration_s)
        clips.append(clip)
    total_duration = timings[-1].end_s if timings else 0.0
    return CompositeVideoClip(clips, size=output_size).with_duration(total_duration)


def main() -> int:
    from segments import AUDIO, DESIGN, OUTPUT_NAME, RENDER_TYPE, SEGMENTS

    if RENDER_TYPE != RENDER_TYPE_CARDS:
        raise SystemExit(f"render_cards requires RENDER_TYPE='cards', got {RENDER_TYPE!r}")

    args = parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    audio_dir = OUTPUT_DIR / "audio"
    seg_audios = None
    tts_durations = None

    if AUDIO:
        seg_audios = synthesize_segments(SEGMENTS, AUDIO, audio_dir / "tts", render_type=RENDER_TYPE)
        tts_durations = {int(seg_audio["index"]): float(seg_audio["duration_s"]) for seg_audio in seg_audios}

    timings = build_card_timings(SEGMENTS, design=DESIGN, tts_durations=tts_durations, audio_cfg=AUDIO)
    if AUDIO and seg_audios is not None:
        assert_tts_fits_timeline(seg_audios, timings, AUDIO)
    total_duration_s = timings[-1].end_s if timings else 0.0
    clip = build_card_video_clip(SEGMENTS, DESIGN, timings)

    if args.preview:
        silent_path = OUTPUT_DIR / "preview-silent.mp4"
        output_path = OUTPUT_DIR / "preview.mp4"
        fps = 12
        preset = "ultrafast"
        crf = "26"
    else:
        silent_path = OUTPUT_DIR / f"{OUTPUT_NAME}-silent.mp4"
        output_path = OUTPUT_DIR / f"{OUTPUT_NAME}.mp4"
        fps = 30
        preset = "medium"
        crf = "18"

    clip.write_videofile(
        str(silent_path),
        codec="libx264",
        audio=False,
        fps=fps,
        preset=preset,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart", "-crf", crf],
    )
    clip.close()

    if AUDIO and seg_audios is not None:
        narration_wav = build_narration_wav(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "narration.wav")
        mix_wav = mix_with_bgm(narration_wav, AUDIO.get("bgm_path"), AUDIO, total_duration_s, audio_dir / "mix.wav")
        write_manifest(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "tts" / "manifest.json")
        mux_into_video(silent_path, mix_wav, AUDIO, output_path)
        silent_path.unlink(missing_ok=True)
    else:
        silent_path.rename(output_path)

    print(
        json.dumps(
            {
                "ok": True,
                "output": str(output_path),
                "fps": fps,
                "duration_s": round(total_duration_s, 3),
                "audio": bool(AUDIO),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
