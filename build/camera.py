"""Camera crop and resize logic."""

from __future__ import annotations

from typing import Tuple

import numpy as np
from PIL import Image

from .easing import clamp

DEFAULT_OUTPUT_SIZE = (1024, 576)


def output_size_for_design(design: dict | None = None) -> tuple[int, int]:
    if design and "output_size" in design:
        width, height = design["output_size"]
        return int(width), int(height)
    return DEFAULT_OUTPUT_SIZE


try:
    from segments import DESIGN as PROJECT_DESIGN
except Exception:
    PROJECT_DESIGN = None


OUTPUT_SIZE = output_size_for_design(PROJECT_DESIGN)
TARGET_ASPECT = 16 / 9


def crop_and_resize(
    image: Image.Image,
    frame: dict[str, float],
    zoom: float,
    output_size: Tuple[int, int] = OUTPUT_SIZE,
) -> np.ndarray:
    """Render a camera frame from the source image.

    ``frame`` is the final 16:9 camera view in source-image coordinates.
    ``zoom`` values above 1.0 push in around the frame center.
    """
    if zoom <= 0:
        raise ValueError(f"zoom must be positive, got {zoom}")

    source_w, source_h = image.size
    frame_w = float(frame["w"])
    frame_h = float(frame["h"])
    crop_w = frame_w / zoom
    crop_h = frame_h / zoom

    if crop_w > source_w or crop_h > source_h:
        raise ValueError(f"crop exceeds source bounds: {crop_w}x{crop_h} for {source_w}x{source_h}")

    center_x = float(frame["x"]) + frame_w / 2.0
    center_y = float(frame["y"]) + frame_h / 2.0
    left = clamp(center_x - crop_w / 2.0, 0.0, source_w - crop_w)
    top = clamp(center_y - crop_h / 2.0, 0.0, source_h - crop_h)
    right = left + crop_w
    bottom = top + crop_h

    crop_box = (
        int(round(left)),
        int(round(top)),
        int(round(right)),
        int(round(bottom)),
    )
    rendered = image.crop(crop_box).resize(output_size, Image.Resampling.LANCZOS)
    return np.asarray(rendered.convert("RGB"))


def composite_rgba(base_rgb: Image.Image, overlay_rgba: Image.Image, opacity: float = 1.0) -> Image.Image:
    """Alpha-composite a full-frame RGBA overlay onto an RGB frame."""
    opacity = clamp(opacity, 0.0, 1.0)
    base = base_rgb.convert("RGBA")
    overlay = overlay_rgba.copy()
    if opacity < 1.0:
        alpha = overlay.getchannel("A").point(lambda value: int(value * opacity))
        overlay.putalpha(alpha)
    return Image.alpha_composite(base, overlay).convert("RGB")
