"""Timeline helpers for static card-based lessons."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CardTiming:
    index: int
    type: str
    text_es: str
    text_ko: str | None
    example_es: str | None
    color_block: str | None
    block_id: int | None
    frase_num: int | None
    start_s: float
    duration_s: float
    end_s: float
    repeat_pause_s: float


def _int_or_none(value: object) -> int | None:
    return int(value) if value is not None else None


def build_card_timings(
    segments: Iterable[dict],
    design: dict | None = None,
    tts_durations: dict[int, float] | None = None,
    audio_cfg: dict | None = None,
) -> list[CardTiming]:
    """Build card timings using explicit ``duration_s`` values."""
    del design, tts_durations, audio_cfg
    timings: list[CardTiming] = []
    cursor = 0.0
    for index, segment in enumerate(segments, start=1):
        duration = float(segment["duration_s"])
        segment_type = str(segment.get("type", "phrase"))
        timing = CardTiming(
            index=index,
            type=segment_type,
            text_es=str(segment.get("text_es", segment.get("title_es", ""))),
            text_ko=str(segment["text_ko"]) if "text_ko" in segment else segment.get("title_ko"),
            example_es=str(segment["example_es"]) if "example_es" in segment else None,
            color_block=segment.get("color_block"),
            block_id=_int_or_none(segment.get("block_id")),
            frase_num=_int_or_none(segment.get("frase_num")),
            start_s=cursor,
            duration_s=duration,
            end_s=cursor + duration,
            repeat_pause_s=float(segment.get("repeat_pause_s", 0.0)),
        )
        timings.append(timing)
        cursor = timing.end_s
    return timings


def expected_card_total_duration(segments: list[dict]) -> float:
    timings = build_card_timings(segments)
    return timings[-1].end_s if timings else 0.0
