"""Timeline helpers for diary-style lessons."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
from build.segment_adapter import RENDER_TYPE_DIARY, narration_text
from build.timeline import duration_for_text


@dataclass(frozen=True)
class DiaryTiming:
    index: int
    type: str
    scene_id: int | None
    kind: str | None
    speaker: str | None
    text_es: str
    text_ko: str | None
    title_es: str | None
    title_ko: str | None
    start_s: float
    duration_s: float
    end_s: float
    line_index: int | None = None


def _int_or_none(value: object) -> int | None:
    return int(value) if value is not None else None


def segment_duration(
    segment: dict,
    index: int,
    tts_durations: dict[int, float] | None,
    audio_cfg: dict | None,
) -> float:
    """Compute segment duration, extending it if TTS narration is longer than explicit duration."""
    if not audio_cfg:
        audio_cfg = {}
    
    seg_type = segment.get("type", "diary_line")
    lead = float(audio_cfg.get("lead_padding_s", 0.25))
    tail = float(audio_cfg.get("tail_padding_s", 0.4))
    
    if seg_type == "diary_line":
        processing_pause_s = float(segment.get("processing_pause_s") or audio_cfg.get("processing_pause_s", 2.5))
        min_hold_s = float(segment.get("min_hold_s") or audio_cfg.get("min_hold_s", 2.5))
        
        if "duration_s" in segment:
            explicit_dur = float(segment["duration_s"])
            min_hold_s = max(min_hold_s, explicit_dur)
            
        if tts_durations and index in tts_durations:
            tts_dur = tts_durations[index]
            return max(tts_dur + lead + tail + processing_pause_s, min_hold_s)
        else:
            text = narration_text(segment, RENDER_TYPE_DIARY)
            proxy = duration_for_text(text)
            return max(proxy + lead + tail + processing_pause_s, min_hold_s)
            
    elif seg_type in ("intro", "outro", "scene_header", "montage"):
        explicit_dur = float(segment.get("duration_s", 3.0))
        if tts_durations and index in tts_durations:
            tts_dur = tts_durations[index]
            return max(tts_dur + lead + tail, explicit_dur)
        return explicit_dur
        
    elif seg_type == "pause":
        return float(segment.get("duration_s", 0.0))
        
    return float(segment.get("duration_s", 0.0))


def build_diary_timings(
    segments: Iterable[dict],
    design: dict | None = None,
    tts_durations: dict[int, float] | None = None,
    audio_cfg: dict | None = None,
) -> list[DiaryTiming]:
    """Build diary timings, accumulating durations chronologically."""
    del design
    timings: list[DiaryTiming] = []
    cursor = 0.0
    
    # We keep track of the current scene and the 1-based index of diary_lines in it
    current_scene_id = None
    line_counter = 0
    
    for index, segment in enumerate(segments, start=1):
        duration = segment_duration(segment, index, tts_durations, audio_cfg)
        segment_type = str(segment.get("type", "diary_line"))
        scene_id = _int_or_none(segment.get("scene_id"))
        
        line_idx = None
        if segment_type == "diary_line":
            if scene_id != current_scene_id:
                current_scene_id = scene_id
                line_counter = 0
            line_counter += 1
            line_idx = line_counter
            
        timing = DiaryTiming(
            index=index,
            type=segment_type,
            scene_id=scene_id,
            kind=segment.get("kind"),
            speaker=segment.get("speaker"),
            text_es=str(segment.get("text_es", "")),
            text_ko=str(segment["text_ko"]) if "text_ko" in segment else None,
            title_es=str(segment.get("title_es")) if "title_es" in segment else None,
            title_ko=str(segment.get("title_ko")) if "title_ko" in segment else None,
            start_s=cursor,
            duration_s=duration,
            end_s=cursor + duration,
            line_index=line_idx,
        )
        timings.append(timing)
        cursor = timing.end_s
    return timings


def expected_diary_total_duration(segments: list[dict], audio_cfg: dict | None = None) -> float:
    timings = build_diary_timings(segments, audio_cfg=audio_cfg)
    return timings[-1].end_s if timings else 0.0
