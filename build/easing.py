"""Small easing and interpolation helpers."""

from __future__ import annotations


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def clamp01(value: float) -> float:
    return clamp(value, 0.0, 1.0)


def ease_in_out_quad(value: float) -> float:
    """Return the quadratic ease-in/ease-out value for a 0..1 progress value."""
    p = clamp01(value)
    if p < 0.5:
        return 2.0 * p * p
    return 1.0 - ((-2.0 * p + 2.0) ** 2) / 2.0


def lerp(start: float, end: float, progress: float) -> float:
    p = clamp01(progress)
    return start + (end - start) * p


def lerp_frame(start: dict[str, int], end: dict[str, int], progress: float) -> dict[str, float]:
    p = clamp01(progress)
    return {
        "x": lerp(start["x"], end["x"], p),
        "y": lerp(start["y"], end["y"], p),
        "w": lerp(start["w"], end["w"], p),
        "h": lerp(start["h"], end["h"], p),
    }
