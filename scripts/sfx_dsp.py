"""Procedural digital signal processing (DSP) helper functions for generating WAV files.

Contains standard waveform synthesis, noise filtering, and amplitude control.
"""

from __future__ import annotations

import wave
from pathlib import Path
import numpy as np

SAMPLE_RATE = 44100


def save_wav(path: Path, data: np.ndarray, channels: int = 1) -> None:
    """Save a 1D or 2D float numpy array (-1.0 to 1.0) as 16-bit PCM WAV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    clamped = np.clip(data, -1.0, 1.0)
    int_data = (clamped * 32767.0).astype(np.int16)
    
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(channels)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(int_data.tobytes())
    print(f"Saved {path.name} ({channels}ch, {len(data)/SAMPLE_RATE:.1f}s)")


def make_filtered_noise(duration_s: float, filter_fn) -> np.ndarray:
    """Generate white noise and apply a frequency-domain filter function."""
    n = int(duration_s * SAMPLE_RATE)
    noise = np.random.normal(0.0, 1.0, n)
    spec = np.fft.rfft(noise)
    freqs = np.fft.rfftfreq(n, d=1.0/SAMPLE_RATE)
    
    H = filter_fn(freqs)
    filtered_spec = spec * H
    filtered = np.fft.irfft(filtered_spec, n)
    
    rms = np.sqrt(np.mean(filtered**2))
    if rms > 0:
        filtered = filtered * (0.25 / rms)
    return filtered


def make_stereo_loop(duration_s: float, filter_fn_l, filter_fn_r, fade_s: float = 0.5) -> np.ndarray:
    """Generate a seamless stereo loop by crossfading ends of two independent mono clips."""
    n_loop = int(duration_s * SAMPLE_RATE)
    n_fade = int(fade_s * SAMPLE_RATE)
    n_total = n_loop + n_fade
    
    left_raw = make_filtered_noise(n_total / SAMPLE_RATE, filter_fn_l)
    right_raw = make_filtered_noise(n_total / SAMPLE_RATE, filter_fn_r)
    
    fade_out = np.linspace(1.0, 0.0, n_fade)
    fade_in = np.linspace(0.0, 1.0, n_fade)
    
    left = np.zeros(n_loop)
    right = np.zeros(n_loop)
    
    left[:n_fade] = left_raw[:n_fade] * fade_in + left_raw[n_loop:] * fade_out
    left[n_fade:] = left_raw[n_fade:n_loop]
    
    right[:n_fade] = right_raw[:n_fade] * fade_in + right_raw[n_loop:] * fade_out
    right[n_fade:] = right_raw[n_fade:n_loop]
    
    return np.stack([left, right], axis=-1)


def _bell(freq: float, dur_s: float, decay: float = 4.0, harmonic: float = 0.3) -> np.ndarray:
    """Soft bell/chime tone: fundamental + 2nd harmonic, exponential decay (mono)."""
    t = np.linspace(0, dur_s, int(dur_s * SAMPLE_RATE), endpoint=False)
    tone = np.sin(2 * np.pi * freq * t) + harmonic * np.sin(2 * np.pi * 2.0 * freq * t)
    return tone * np.exp(-t * decay)


def _bird_chirp(base_freq: float, rng: np.random.Generator) -> np.ndarray:
    """A short cheerful chirp: 2-4 quick swept-sine syllables (mono)."""
    parts = []
    for _ in range(int(rng.integers(2, 5))):
        syl_dur = rng.uniform(0.05, 0.11)
        t = np.linspace(0, syl_dur, int(syl_dur * SAMPLE_RATE), endpoint=False)
        f0 = base_freq * rng.uniform(0.9, 1.15)
        f1 = f0 * rng.uniform(1.15, 1.6) * (1.0 if rng.random() > 0.4 else 0.7)
        sweep = np.linspace(f0, f1, len(t))
        phase = 2 * np.pi * np.cumsum(sweep) / SAMPLE_RATE
        env = np.sin(np.pi * np.linspace(0, 1, len(t)))
        parts.append(np.sin(phase) * env)
        parts.append(np.zeros(int(rng.uniform(0.02, 0.05) * SAMPLE_RATE)))
    return np.concatenate(parts)


def _apply_fades(data: np.ndarray, fade_in_s: float, fade_out_s: float) -> np.ndarray:
    """Apply linear fade-in and fade-out to a 2D stereo array."""
    n = len(data)
    fade = np.ones(n)
    fi = int(fade_in_s * SAMPLE_RATE)
    fo = int(fade_out_s * SAMPLE_RATE)
    if fi > 0:
        fade[:fi] = np.linspace(0.0, 1.0, fi)
    if fo > 0:
        fade[-fo:] = np.linspace(1.0, 0.0, fo)
    return data * fade[:, np.newaxis]


def _normalize_peak(data: np.ndarray, target: float = 0.7) -> np.ndarray:
    """Normalize stereo data to target peak amplitude."""
    peak = np.max(np.abs(data))
    return data / peak * target if peak > 0 else data
