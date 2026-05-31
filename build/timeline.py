"""Timeline construction for camera movement and subtitle layers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from PIL import Image

from .camera import OUTPUT_SIZE, crop_and_resize, output_size_for_design
from .design import apply_grade, easing_fn
from .easing import lerp, lerp_frame
from .subtitles import render_subtitle_image

TRANSITION_S = 0.8
FADE_S = 0.3


@dataclass(frozen=True)
class SegmentTiming:
    index: int
    text: str
    frame: dict[str, int]
    zoom_start: float
    zoom_end: float
    start_s: float
    duration_s: float
    end_s: float


def duration_for_text(text: str) -> float:
    return max(4.5, min(10.5, len(text) / 13.0))


def segment_duration(
    segment: dict,
    index: int,
    tts_durations: dict[int, float] | None = None,
    audio_cfg: dict | None = None,
) -> float:
    if "duration_s" in segment:
        return float(segment["duration_s"])

    text_floor = duration_for_text(segment["text"])
    if tts_durations and index in tts_durations:
        cfg = audio_cfg or {}
        lead = float(cfg.get("lead_padding_s", 0.3))
        tail = float(cfg.get("tail_padding_s", 0.5))
        min_duration = float(cfg.get("min_duration_s", 4.0))
        readability_ratio = float(cfg.get("readability_floor_ratio", 0.9))
        return max(tts_durations[index] + lead + tail, text_floor * readability_ratio, min_duration)

    return text_floor


def transition_s(design: dict | None = None) -> float:
    return float(design.get("transition_s", TRANSITION_S)) if design else TRANSITION_S


def fade_s(design: dict | None = None) -> float:
    return float(design.get("fade_s", FADE_S)) if design else FADE_S


def prepare_timeline(
    segments: Iterable[dict],
    design: dict | None = None,
    tts_durations: dict[int, float] | None = None,
    audio_cfg: dict | None = None,
) -> list[SegmentTiming]:
    segment_list = list(segments)
    timings: list[SegmentTiming] = []
    cursor = 0.0
    drift = float(design.get("idle_zoom_drift", 0.0)) if design else 0.0
    for index, segment in enumerate(segment_list, start=1):
        duration = segment_duration(segment, index, tts_durations=tts_durations, audio_cfg=audio_cfg)
        zoom = segment.get("zoom", {})
        start = float(zoom.get("start", 1.0))
        end = float(zoom.get("end", 1.04))
        if drift and start == 1.0 and end == 1.0:
            end = 1.0 + drift
        timings.append(
            SegmentTiming(
                index=index,
                text=segment["text"],
                frame=segment["frame"],
                zoom_start=start,
                zoom_end=end,
                start_s=cursor,
                duration_s=duration,
                end_s=cursor + duration,
            )
        )
        cursor += duration
        if index < len(segment_list):
            cursor += transition_s(design)
    return timings


def expected_total_duration(
    segments: list[dict],
    design: dict | None = None,
    tts_durations: dict[int, float] | None = None,
    audio_cfg: dict | None = None,
) -> float:
    segment_total = sum(
        segment_duration(segment, index, tts_durations=tts_durations, audio_cfg=audio_cfg)
        for index, segment in enumerate(segments, start=1)
    )
    return segment_total + max(0, len(segments) - 1) * transition_s(design)


def state_at_time(
    t: float,
    timings: list[SegmentTiming],
    design: dict | None = None,
) -> tuple[dict[str, float], float]:
    """Return interpolated frame and zoom for absolute timeline time ``t``."""
    if not timings:
        raise ValueError("timeline has no segments")

    ease = easing_fn(design.get("easing") if design else "ease_in_out_quad")
    total = timings[-1].end_s
    if t >= total:
        last = timings[-1]
        return last.frame, last.zoom_end

    for current, next_segment in zip(timings, timings[1:]):
        if current.start_s <= t <= current.end_s:
            progress = ease((t - current.start_s) / current.duration_s)
            return current.frame, lerp(current.zoom_start, current.zoom_end, progress)

        transition_start = current.end_s
        transition_end = next_segment.start_s
        if transition_start < t < transition_end:
            transition_duration = transition_end - transition_start
            progress = ease((t - transition_start) / transition_duration)
            frame = lerp_frame(current.frame, next_segment.frame, progress)
            zoom = lerp(current.zoom_end, next_segment.zoom_start, progress)
            return frame, zoom

    last = timings[-1]
    progress = ease((t - last.start_s) / last.duration_s)
    return last.frame, lerp(last.zoom_start, last.zoom_end, progress)


def make_subtitle_clip(
    text: str,
    start_s: float,
    duration_s: float,
    output_size: tuple[int, int] = OUTPUT_SIZE,
    design: dict | None = None,
):
    from moviepy import ImageClip, VideoClip

    overlay = render_subtitle_image(text, video_size=output_size, design=design)
    overlay_array = np.asarray(overlay)
    rgb = overlay_array[:, :, :3]
    alpha = overlay_array[:, :, 3].astype("float32") / 255.0

    clip = ImageClip(rgb).with_start(start_s).with_duration(duration_s)

    def mask_frame(local_t: float) -> np.ndarray:
        fade_duration = fade_s(design)
        fade = min(1.0, local_t / fade_duration, max(0.0, (duration_s - local_t) / fade_duration))
        return alpha * fade

    mask = VideoClip(frame_function=mask_frame, is_mask=True, duration=duration_s).with_start(start_s)
    return clip.with_mask(mask)


def build_video_clip(
    image_path: str,
    segments: list[dict],
    design: dict | None = None,
    timings: list[SegmentTiming] | None = None,
):
    from moviepy import CompositeVideoClip, VideoClip

    image = Image.open(image_path).convert("RGB")
    if design:
        image = apply_grade(image, design.get("grade"))
    output_size = output_size_for_design(design)
    timings = timings or prepare_timeline(segments, design=design)
    total_duration = timings[-1].end_s if timings else 0.0

    def make_frame(t: float) -> np.ndarray:
        frame, zoom = state_at_time(t, timings, design=design)
        return crop_and_resize(image, frame, zoom, output_size=output_size)

    camera_clip = VideoClip(frame_function=make_frame, duration=total_duration)
    subtitle_clips = [
        make_subtitle_clip(timing.text, timing.start_s, timing.duration_s, output_size=output_size, design=design)
        for timing in timings
    ]
    return CompositeVideoClip([camera_clip, *subtitle_clips], size=output_size)
