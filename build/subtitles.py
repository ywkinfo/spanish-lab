"""PIL subtitle rendering with pixel-measured wrapping."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

from .design import (
    draw_drop_shadow_text,
    draw_gradient_bar,
    letter_spaced_width,
)

VIDEO_SIZE = (1024, 576)
DEFAULT_FONT_SIZE = 28
MIN_FONT_SIZE = 21
MAX_TEXT_WIDTH_RATIO = 0.90
MAX_LINES = 2
_WARNED_FONT_FALLBACKS: set[str] = set()


@dataclass(frozen=True)
class SubtitleLayout:
    lines: list[str]
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont
    font_size: int
    width: int
    height: int
    line_heights: list[int]


def find_font_path(preferred: str | None = None) -> str | None:
    if preferred:
        if Path(preferred).exists():
            return preferred
        if preferred not in _WARNED_FONT_FALLBACKS:
            print(f"warning: font not found, falling back: {preferred}", file=sys.stderr)
            _WARNED_FONT_FALLBACKS.add(preferred)

    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return None


def load_font(size: int, design: dict | None = None) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    font_path = find_font_path(design.get("font_path") if design else None)
    if font_path:
        return ImageFont.truetype(font_path, size=size, index=int(design.get("font_index", 0)) if design else 0)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def text_width(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.ImageFont,
    stroke_width: int = 0,
    letter_spacing: float = 0.0,
) -> int:
    if letter_spacing:
        return letter_spaced_width(draw, text, font, letter_spacing)
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    return bbox[2] - bbox[0]


def line_height(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, stroke_width: int = 0) -> int:
    bbox = draw.textbbox((0, 0), text or "Ag", font=font, stroke_width=stroke_width)
    return bbox[3] - bbox[1]


def wrap_text_pixels(
    text: str,
    font: ImageFont.ImageFont,
    max_width: int,
    draw: ImageDraw.ImageDraw,
    stroke_width: int = 2,
    letter_spacing: float = 0.0,
) -> list[str]:
    words = text.split()
    if not words:
        return [""]

    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if text_width(draw, candidate, font, stroke_width=stroke_width, letter_spacing=letter_spacing) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def measure_layout(
    lines: Iterable[str],
    font: ImageFont.ImageFont,
    draw: ImageDraw.ImageDraw,
    stroke_width: int = 2,
    letter_spacing: float = 0.0,
) -> tuple[int, int, list[int]]:
    measured_lines = list(lines)
    widths = [
        text_width(draw, line, font, stroke_width=stroke_width, letter_spacing=letter_spacing)
        for line in measured_lines
    ]
    heights = [line_height(draw, line, font, stroke_width=stroke_width) for line in measured_lines]
    spacing = max(6, int(getattr(font, "size", DEFAULT_FONT_SIZE) * 0.22))
    total_height = sum(heights) + spacing * max(0, len(measured_lines) - 1)
    return max(widths) if widths else 0, total_height, heights


def layout_subtitle(
    text: str,
    video_size: tuple[int, int] = VIDEO_SIZE,
    font_size: int = DEFAULT_FONT_SIZE,
    min_font_size: int = MIN_FONT_SIZE,
    max_lines: int = MAX_LINES,
    design: dict | None = None,
) -> SubtitleLayout:
    if design:
        font_size = int(design.get("font_size", font_size))
        min_font_size = int(design.get("min_font_size", min_font_size))
        stroke_width = 0
        letter_spacing = float(design.get("letter_spacing", 0.0))
    else:
        stroke_width = 2
        letter_spacing = 0.0

    max_width = int(video_size[0] * MAX_TEXT_WIDTH_RATIO)
    scratch = Image.new("RGBA", video_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(scratch)

    last_layout: SubtitleLayout | None = None
    for size in range(font_size, min_font_size - 1, -1):
        font = load_font(size, design=design)
        lines = wrap_text_pixels(text, font, max_width, draw, stroke_width=stroke_width, letter_spacing=letter_spacing)
        width, height, line_heights = measure_layout(
            lines,
            font,
            draw,
            stroke_width=stroke_width,
            letter_spacing=letter_spacing,
        )
        layout = SubtitleLayout(lines, font, size, width, height, line_heights)
        last_layout = layout
        if len(lines) <= max_lines and width <= max_width:
            return layout

    if last_layout is None:
        raise ValueError("could not lay out subtitle text")
    return last_layout


def render_subtitle_image(
    text: str,
    video_size: tuple[int, int] = VIDEO_SIZE,
    font_size: int = DEFAULT_FONT_SIZE,
    bar_alpha: int = 140,
    design: dict | None = None,
) -> Image.Image:
    """Render a transparent full-frame subtitle overlay."""
    width, height = video_size
    if design:
        layout = layout_subtitle(text, video_size=video_size, font_size=font_size, design=design)
        image = Image.new("RGBA", video_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        pad_x = int(design.get("bar_padding_x", 36))
        pad_y = int(design.get("bar_padding_y", 22))
        bottom_margin = int(height * float(design.get("bar_bottom_margin_ratio", 0.07)))
        bar_bottom = height - bottom_margin
        bar_top = max(0, bar_bottom - layout.height - pad_y * 2)

        if design.get("bar_style") == "gradient":
            draw_gradient_bar(
                image,
                bar_top,
                bar_bottom,
                design.get("bar_top_color", (0, 0, 0, bar_alpha)),
                design.get("bar_bottom_color", (0, 0, 0, bar_alpha)),
                int(design.get("bar_corner_radius", 0)),
            )
        else:
            draw.rectangle((0, bar_top, width, bar_bottom), fill=(0, 0, 0, bar_alpha))

        accent_h = int(design.get("bar_accent_height", 0))
        if accent_h > 0:
            draw.rectangle(
                (0, bar_top, width, min(bar_bottom, bar_top + accent_h)),
                fill=tuple(design.get("bar_accent_color", (255, 255, 255, 255))),
            )

        letter_spacing = float(design.get("letter_spacing", 0.0))
        spacing = max(8, int(layout.font_size * 0.24))
        current_y = bar_top + pad_y
        for line, line_h in zip(layout.lines, layout.line_heights):
            line_w = text_width(draw, line, layout.font, letter_spacing=letter_spacing)
            x = max(pad_x, (width - line_w) // 2)
            draw_drop_shadow_text(
                image,
                (x, current_y),
                line,
                layout.font,
                design.get("text_color", (255, 255, 255, 255)),
                design.get("text_shadow_color", (0, 0, 0, 200)),
                tuple(design.get("text_shadow_offset", (0, 2))),
                float(design.get("text_shadow_blur", 0)),
                letter_spacing,
            )
            current_y += line_h + spacing

        return image

    layout = layout_subtitle(text, video_size=video_size, font_size=font_size)
    image = Image.new("RGBA", video_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    pad_x = 28
    pad_y = 16
    bottom_margin = int(height * 0.08)
    bar_bottom = height - bottom_margin
    bar_top = max(0, bar_bottom - layout.height - pad_y * 2)
    draw.rectangle((0, bar_top, width, bar_bottom), fill=(0, 0, 0, bar_alpha))

    spacing = max(6, int(layout.font_size * 0.22))
    current_y = bar_top + pad_y
    for line, line_h in zip(layout.lines, layout.line_heights):
        line_w = text_width(draw, line, layout.font, stroke_width=2)
        x = max(pad_x, (width - line_w) // 2)
        draw.text(
            (x, current_y),
            line,
            font=layout.font,
            fill=(255, 255, 255, 255),
            stroke_width=2,
            stroke_fill=(0, 0, 0, 255),
        )
        current_y += line_h + spacing

    return image
