#!/usr/bin/env python3
"""Generate a deterministic Spanish Lab brand-BGM draft loop.

This is a lightweight procedural fallback when local AI music generation is not
available or when a quick, copyright-clean draft is needed for taste review.
It writes a warm cafe-style stereo WAV and optionally an MP3 if ffmpeg is run
separately.

Usage from the spanish-lab repo root:
    .venv/bin/python /opt/data/skills/media/spanish-lab-a1-card-episode-production/scripts/generate_spanish_lab_bgm_draft.py \
      --out assets/audio/spanish-lab-brand-bgm-draft-20s.wav
    ffmpeg -y -i assets/audio/spanish-lab-brand-bgm-draft-20s.wav \
      -codec:a libmp3lame -b:a 192k assets/audio/spanish-lab-brand-bgm-draft-20s.mp3
"""

from __future__ import annotations

import argparse
import math
import random
import wave
from pathlib import Path

import numpy as np


def generate(out: Path, *, seconds_hint: float = 22.0, bpm: int = 88, seed: int = 7) -> None:
    sr = 44_100
    bars = max(4, round(seconds_hint / (4 * 60 / bpm)))
    beats = bars * 4
    dur = beats * 60 / bpm
    n = int(sr * dur)
    chords = [
        ("Am7", [220.00, 261.63, 329.63, 392.00]),
        ("Fmaj7", [174.61, 220.00, 261.63, 329.63]),
        ("Cmaj7", [130.81, 196.00, 246.94, 329.63]),
        ("G6", [196.00, 246.94, 293.66, 329.63]),
    ]
    beat_len = 60 / bpm
    bar_len = 4 * beat_len
    rng = random.Random(seed)
    left = np.zeros(n, dtype=np.float32)
    right = np.zeros(n, dtype=np.float32)

    # Soft electric-piano arpeggio.
    for b in range(bars):
        _, freqs = chords[b % 4]
        base = b * bar_len
        pattern = [0, 2, 3, 1, 2, 3, 2, 1]
        for i, idx in enumerate(pattern):
            start = base + i * (bar_len / 8)
            length = bar_len / 5
            s = int(start * sr)
            e = min(n, int((start + length) * sr))
            tt = np.arange(e - s) / sr
            f = freqs[idx]
            env = np.exp(-tt * 3.2) * (1 - np.exp(-tt * 35))
            tone = (np.sin(2 * math.pi * f * tt) + 0.35 * np.sin(2 * math.pi * 2 * f * tt)) * env * 0.045
            pan = -0.25 + 0.5 * (idx / 3)
            left[s:e] += tone * (0.75 - pan * 0.25)
            right[s:e] += tone * (0.75 + pan * 0.25)

    # Nylon-guitar-like offbeat plucks.
    for beat in range(beats):
        if beat % 2 == 1:
            _, freqs = chords[(beat // 4) % 4]
            f = freqs[0] * 2
            start = beat * beat_len + 0.06
            s = int(start * sr)
            e = min(n, int((start + 0.42) * sr))
            tt = np.arange(e - s) / sr
            env = np.exp(-tt * 7.5) * (1 - np.exp(-tt * 90))
            tone = (np.sin(2 * math.pi * f * tt) + 0.2 * np.sin(2 * math.pi * 3 * f * tt)) * env * 0.025
            left[s:e] += tone * 0.8
            right[s:e] += tone * 0.95

    # Very light shaker/cafe air.
    for beat in range(beats * 2):
        start = beat * (beat_len / 2)
        s = int(start * sr)
        e = min(n, int((start + 0.055) * sr))
        tt = np.arange(e - s) / sr
        env = np.exp(-tt * 45)
        white = np.array([rng.uniform(-1, 1) for _ in range(e - s)], dtype=np.float32)
        tick = white * env * 0.006
        left[s:e] += tick * 0.7
        right[s:e] += tick * 0.9

    # Warm root pad/bass.
    for b in range(bars):
        root = chords[b % 4][1][0] / 2
        start = b * bar_len
        s = int(start * sr)
        e = min(n, int((start + bar_len) * sr))
        tt = np.arange(e - s) / sr
        env = np.minimum(1, tt / 0.4) * np.minimum(1, (bar_len - tt) / 0.5)
        tone = np.sin(2 * math.pi * root * tt) * env * 0.022
        left[s:e] += tone
        right[s:e] += tone

    fade = int(0.08 * sr)
    window = np.ones(n)
    window[:fade] = np.linspace(0, 1, fade)
    window[-fade:] = np.linspace(1, 0, fade)
    stereo = np.stack([left * window, right * window], axis=1)
    peak = np.max(np.abs(stereo)) or 1
    stereo = stereo / peak * 0.22  # draft mean around low background level

    out.parent.mkdir(parents=True, exist_ok=True)
    pcm = (np.clip(stereo, -1, 1) * 32767).astype("<i2")
    with wave.open(str(out), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(sr)
        wav.writeframes(pcm.tobytes())
    print(f"wrote {out} ({dur:.2f}s)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("assets/audio/spanish-lab-brand-bgm-draft-20s.wav"))
    parser.add_argument("--seconds", type=float, default=22.0)
    parser.add_argument("--bpm", type=int, default=88)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    generate(args.out, seconds_hint=args.seconds, bpm=args.bpm, seed=args.seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
