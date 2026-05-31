"""Design helpers for project-specific video styling."""

from __future__ import annotations

from collections.abc import Callable, Sequence

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

from .easing import clamp, clamp01, ease_in_out_quad


def ease_in_out_cubic(value: float) -> float:
    """Return the cubic ease-in/ease-out value for a 0..1 progress value."""
    p = clamp01(value)
    if p < 0.5:
        return 4.0 * p * p * p
    return 1.0 - ((-2.0 * p + 2.0) ** 3) / 2.0


def easing_fn(name: str | None) -> Callable[[float], float]:
    """Return an easing function by token name."""
    if name in (None, "ease_in_out_quad"):
        return ease_in_out_quad
    if name == "ease_in_out_cubic":
        return ease_in_out_cubic
    if name == "linear":
        return clamp01
    raise ValueError(f"unknown easing function: {name}")


def _channel_delta(channel: Image.Image, delta: int) -> Image.Image:
    return channel.point(lambda value: int(clamp(value + delta, 0, 255)))


def apply_grade(image: Image.Image, grade: dict | None) -> Image.Image:
    """Apply a small one-pass color grade while preserving image size."""
    if not grade:
        return image

    graded = image.convert("RGB")
    saturation = float(grade.get("saturation", 1.0))
    contrast = float(grade.get("contrast", 1.0))
    warmth = int(grade.get("warmth", 0))

    if saturation != 1.0:
        graded = ImageEnhance.Color(graded).enhance(saturation)
    if contrast != 1.0:
        graded = ImageEnhance.Contrast(graded).enhance(contrast)
    if warmth:
        red, green, blue = graded.split()
        graded = Image.merge(
            "RGB",
            (
                _channel_delta(red, warmth),
                green,
                _channel_delta(blue, -round(warmth / 2)),
            ),
        )
    return graded


def _advance(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> float:
    try:
        return float(draw.textlength(text, font=font))
    except AttributeError:
        bbox = draw.textbbox((0, 0), text, font=font)
        return float(bbox[2] - bbox[0])


def letter_spaced_width(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.ImageFont,
    spacing: float,
) -> int:
    """Measure text drawn one character at a time with extra tracking."""
    if not text:
        return 0
    width = sum(_advance(draw, char, font) for char in text)
    width += max(0, len(text) - 1) * spacing
    return int(round(width))


def draw_letter_spaced(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.ImageFont,
    spacing: float,
    fill: Sequence[int],
) -> None:
    """Draw text with simple per-character letter spacing."""
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=font, fill=tuple(fill))
        x += _advance(draw, char, font) + spacing


def draw_gradient_bar(
    image: Image.Image,
    bar_top: int,
    bar_bottom: int,
    color_top: Sequence[int],
    color_bottom: Sequence[int],
    corner_radius: int = 0,
) -> None:
    """Draw a vertical RGBA gradient bar across the full frame width."""
    width, _ = image.size
    bar_height = max(1, bar_bottom - bar_top)
    gradient = Image.new("RGBA", (width, bar_height), (0, 0, 0, 0))
    pixels = gradient.load()
    top = tuple(color_top)
    bottom = tuple(color_bottom)

    for y in range(bar_height):
        progress = y / max(1, bar_height - 1)
        color = tuple(round(top[i] + (bottom[i] - top[i]) * progress) for i in range(4))
        for x in range(width):
            pixels[x, y] = color

    if corner_radius > 0:
        mask = Image.new("L", (width, bar_height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle((0, 0, width, bar_height), radius=corner_radius, fill=255)
        layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        layer.paste(gradient, (0, bar_top), mask)
        image.alpha_composite(layer)
        return

    image.alpha_composite(gradient, (0, bar_top))


def draw_drop_shadow_text(
    image: Image.Image,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.ImageFont,
    fill: Sequence[int],
    shadow_color: Sequence[int],
    shadow_offset: tuple[int, int],
    shadow_blur: float,
    letter_spacing: float,
) -> None:
    """Draw text with a blurred shadow and optional letter spacing."""
    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_xy = (xy[0] + shadow_offset[0], xy[1] + shadow_offset[1])
    draw_letter_spaced(shadow_draw, shadow_xy, text, font, letter_spacing, shadow_color)
    if shadow_blur > 0:
        shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
    image.alpha_composite(shadow)

    draw = ImageDraw.Draw(image)
    draw_letter_spaced(draw, xy, text, font, letter_spacing, fill)
