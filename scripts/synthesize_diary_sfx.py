#!/usr/bin/env python3
"""Procedural synthesizer for historia-a1 Ep.1 v2 SFX assets.

Generates 8 stereo loop beds and 7 mono spot effects using numpy and wave.
Maintains CC0 compliance by generating all waveforms procedurally (no samples used).
"""

from __future__ import annotations

import os
import wave
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SFX_DIR = ROOT / "assets" / "audio" / "sfx"
SAMPLE_RATE = 44100


def save_wav(path: Path, data: np.ndarray, channels: int = 1) -> None:
    """Save a 1D or 2D float numpy array (-1.0 to 1.0) as 16-bit PCM WAV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # Clamp and convert to 16-bit integers
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
    
    # Normalize to RMS of ~0.25 to prevent clipping before mixing
    rms = np.sqrt(np.mean(filtered**2))
    if rms > 0:
        filtered = filtered * (0.25 / rms)
    return filtered


def make_stereo_loop(duration_s: float, filter_fn_l, filter_fn_r, fade_s: float = 0.5) -> np.ndarray:
    """Generate a seamless stereo loop by crossfading ends of two independent mono clips."""
    n_loop = int(duration_s * SAMPLE_RATE)
    n_fade = int(fade_s * SAMPLE_RATE)
    n_total = n_loop + n_fade
    
    # Left and Right are independent (decorrelated) for wide stereo field
    left_raw = make_filtered_noise(n_total / SAMPLE_RATE, filter_fn_l)
    right_raw = make_filtered_noise(n_total / SAMPLE_RATE, filter_fn_r)
    
    # Crossfade mask
    fade_out = np.linspace(1.0, 0.0, n_fade)
    fade_in = np.linspace(0.0, 1.0, n_fade)
    
    left = np.zeros(n_loop)
    right = np.zeros(n_loop)
    
    # Overlap loop ends
    left[:n_fade] = left_raw[:n_fade] * fade_in + left_raw[n_loop:] * fade_out
    left[n_fade:] = left_raw[n_fade:n_loop]
    
    right[:n_fade] = right_raw[:n_fade] * fade_in + right_raw[n_loop:] * fade_out
    right[n_fade:] = right_raw[n_fade:n_loop]
    
    return np.stack([left, right], axis=-1)


# --- Ambient Beds (Stereo, ~16s, Seamless Loop) ---

def synth_madrid_morning():
    # Warm low rumble + faint high street hiss
    f_l = lambda f: 1.0 / (1.0 + (f/100.0)**4) + 0.08 / (1.0 + ((f-3000.0)/800.0)**2)
    f_r = lambda f: 1.0 / (1.0 + (f/90.0)**4) + 0.08 / (1.0 + ((f-3200.0)/800.0)**2)
    data = make_stereo_loop(16.0, f_l, f_r)
    # Slow amplitude modulation to mimic wind/distant city flow
    t = np.linspace(0, 16.0, len(data), endpoint=False)
    mod = 0.85 + 0.15 * np.sin(2 * np.pi * 0.08 * t)[:, np.newaxis]
    save_wav(SFX_DIR / "madrid_morning.wav", data * mod, channels=2)


def synth_home_morning():
    # Quiet indoor room tone: low floor, no high hiss
    f_l = lambda f: 1.0 / (1.0 + (f/80.0)**4)
    f_r = lambda f: 1.0 / (1.0 + (f/75.0)**4)
    data = make_stereo_loop(16.0, f_l, f_r)
    save_wav(SFX_DIR / "home_morning.wav", data * 0.6, channels=2)


def synth_metro_inside():
    # Deep train rumble + metal squeals + track hum
    rumble_l = lambda f: 1.0 / (1.0 + (f/120.0)**4) + 0.03 / (1.0 + ((f-500.0)/150.0)**2)
    rumble_r = lambda f: 1.0 / (1.0 + (f/110.0)**4) + 0.03 / (1.0 + ((f-520.0)/150.0)**2)
    data = make_stereo_loop(16.0, rumble_l, rumble_r)
    
    t = np.linspace(0, 16.0, len(data), endpoint=False)
    # Track joints click pattern (periodic thuds)
    joint_clicks = np.zeros(len(data))
    for click_time in np.arange(0.2, 16.0, 1.25):
        idx = int(click_time * SAMPLE_RATE)
        # Double thud click
        for offset in [0, int(0.08 * SAMPLE_RATE)]:
            if idx + offset + 2000 < len(joint_clicks):
                click_pulse = np.exp(-np.linspace(0, 5, 2000)) * np.sin(2 * np.pi * 60.0 * np.linspace(0, 0.05, 2000))
                joint_clicks[idx+offset : idx+offset+2000] += click_pulse
                
    # Add track squeal (high-pitched sine waves fading in and out)
    squeal = 0.015 * np.sin(2 * np.pi * 2200.0 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.12 * t))
    squeal_stereo = np.stack([squeal, squeal * 0.7], axis=-1)
    
    # Track rumble amplitude modulation
    mod = 0.8 + 0.2 * np.sin(2 * np.pi * 0.4 * t)[:, np.newaxis]
    final_data = data * mod + joint_clicks[:, np.newaxis] * 0.3 + squeal_stereo
    save_wav(SFX_DIR / "metro_inside.wav", final_data * 0.9, channels=2)


def synth_soft_phone_typing():
    # Warm room tone + random typing clicks
    f_l = lambda f: 1.0 / (1.0 + (f/90.0)**4)
    f_r = lambda f: 1.0 / (1.0 + (f/90.0)**4)
    data = make_stereo_loop(16.0, f_l, f_r)
    
    # Rare random keyboard clicks
    clicks = np.zeros(len(data))
    np.random.seed(42)
    click_times = np.sort(np.random.uniform(0.5, 15.5, 25))
    for ct in click_times:
        idx = int(ct * SAMPLE_RATE)
        duration = int(0.01 * SAMPLE_RATE)
        t_click = np.linspace(0, 0.01, duration)
        # Typ click waveform (short envelope noise)
        click_val = np.random.normal(0, 0.08, duration) * np.exp(-t_click * 800.0)
        clicks[idx : idx + duration] += click_val
        
    final_data = data * 0.7 + clicks[:, np.newaxis]
    save_wav(SFX_DIR / "soft_phone_typing.wav", final_data, channels=2)


def synth_classroom_soft():
    # Mid-range mumbling/murmur filter + room floor
    murmur_l = lambda f: 1.0 / (1.0 + (f/80.0)**4) + 0.15 / (1.0 + ((f-400.0)/200.0)**2)
    murmur_r = lambda f: 1.0 / (1.0 + (f/80.0)**4) + 0.15 / (1.0 + ((f-450.0)/250.0)**2)
    data = make_stereo_loop(16.0, murmur_l, murmur_r)
    
    # Human speech modulations (slow envelopes on vocal bands)
    t = np.linspace(0, 16.0, len(data), endpoint=False)
    mod_l = 0.7 + 0.3 * np.sin(2 * np.pi * 0.15 * t) * np.cos(2 * np.pi * 0.35 * t)
    mod_r = 0.7 + 0.3 * np.cos(2 * np.pi * 0.18 * t) * np.sin(2 * np.pi * 0.41 * t)
    
    data[:, 0] *= mod_l
    data[:, 1] *= mod_r
    save_wav(SFX_DIR / "classroom_soft.wav", data * 0.8, channels=2)


def synth_madrid_street():
    # Traffic hum + car swell
    street_l = lambda f: 1.0 / (1.0 + (f/130.0)**4) + 0.05 / (1.0 + ((f-1500.0)/500.0)**2)
    street_r = lambda f: 1.0 / (1.0 + (f/120.0)**4) + 0.05 / (1.0 + ((f-1600.0)/500.0)**2)
    data = make_stereo_loop(16.0, street_l, street_r)
    
    # Swell effect (car drive-by passing left to right)
    t = np.linspace(0, 16.0, len(data), endpoint=False)
    car_center = 8.0 # at 8.0 seconds
    car_envelope = np.exp(-((t - car_center)/1.8)**2)
    
    # Car sound: low-pass noise
    car_noise = make_filtered_noise(16.0, lambda f: 1.0 / (1.0 + (f/160.0)**4))
    
    # Left-to-right panning
    pan_l = 1.0 - (t / 16.0)
    pan_r = t / 16.0
    
    data[:, 0] += car_noise * car_envelope * pan_l * 0.4
    data[:, 1] += car_noise * car_envelope * pan_r * 0.4
    save_wav(SFX_DIR / "madrid_street.wav", data * 0.8, channels=2)


def synth_rain_cafe():
    # Heavy high-frequency rain hiss + indoor cafe muffled voices
    rain_l = lambda f: 0.8 / (1.0 + ((f-4000.0)/2000.0)**2) + 0.4 / (1.0 + (f/100.0)**4)
    rain_r = lambda f: 0.8 / (1.0 + ((f-4200.0)/2000.0)**2) + 0.4 / (1.0 + (f/95.0)**4)
    data = make_stereo_loop(16.0, rain_l, rain_r)
    
    # Cafe background chatter modulation
    t = np.linspace(0, 16.0, len(data), endpoint=False)
    chatter_l = make_filtered_noise(16.0, lambda f: np.exp(-((f-600)/250)**2)) * (0.6 + 0.4 * np.sin(2*np.pi*0.22*t))
    chatter_r = make_filtered_noise(16.0, lambda f: np.exp(-((f-650)/250)**2)) * (0.6 + 0.4 * np.cos(2*np.pi*0.29*t))
    
    data[:, 0] += chatter_l * 0.25
    data[:, 1] += chatter_r * 0.25
    save_wav(SFX_DIR / "rain_cafe.wav", data * 0.8, channels=2)


def synth_quiet_night_room():
    # AC hum (50Hz + harmonics) + very quiet room tone
    f_l = lambda f: 1.0 / (1.0 + (f/60.0)**4)
    f_r = lambda f: 1.0 / (1.0 + (f/60.0)**4)
    data = make_stereo_loop(16.0, f_l, f_r)
    
    t = np.linspace(0, 16.0, len(data), endpoint=False)
    # AC Hum: 50 Hz, 100 Hz, 150 Hz sines
    ac_hum = 0.008 * np.sin(2 * np.pi * 50.0 * t) + 0.003 * np.sin(2 * np.pi * 100.0 * t) + 0.001 * np.sin(2 * np.pi * 150.0 * t)
    
    final_data = data * 0.45 + ac_hum[:, np.newaxis]
    save_wav(SFX_DIR / "quiet_night_room.wav", final_data, channels=2)


# --- Spot Effects (Mono, 0.5s - 3s One-shot) ---

def synth_door_close_footsteps():
    # Thud (door close) + 3 steps
    duration_s = 2.5
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    # 1. Door close thud at t=0.2
    idx_door = int(0.2 * SAMPLE_RATE)
    t_door = np.linspace(0, 0.4, int(0.4 * SAMPLE_RATE))
    # Low thud: low frequency sine + noise envelope
    door_wave = np.sin(2 * np.pi * 65.0 * t_door) * np.exp(-t_door * 15.0)
    door_wave += np.random.normal(0, 0.1, len(t_door)) * np.exp(-t_door * 25.0)
    data[idx_door : idx_door + len(t_door)] += door_wave * 0.8
    
    # 2. Footsteps at t=0.9, 1.5, 2.1
    for step_t in [0.9, 1.5, 2.1]:
        idx_step = int(step_t * SAMPLE_RATE)
        t_step = np.linspace(0, 0.25, int(0.25 * SAMPLE_RATE))
        step_wave = np.sin(2 * np.pi * 120.0 * t_step) * np.exp(-t_step * 30.0)
        # Scuff noise component
        step_wave += np.random.normal(0, 0.05, len(t_step)) * np.exp(-t_step * 45.0)
        data[idx_step : idx_step + len(t_step)] += step_wave * 0.25
        
    save_wav(SFX_DIR / "door_close_footsteps.wav", data, channels=1)


def synth_metro_chime():
    # Three rising chime notes: G4 (392Hz), B4 (494Hz), D5 (587Hz)
    duration_s = 1.5
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    notes = [392.00, 493.88, 587.33]
    delays = [0.0, 0.25, 0.5]
    
    for freq, delay in zip(notes, delays):
        idx = int(delay * SAMPLE_RATE)
        note_dur = duration_s - delay
        t = np.linspace(0, note_dur, int(note_dur * SAMPLE_RATE))
        # Sine + 2nd harmonic
        wave_form = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * 2.0 * freq * t)
        wave_form *= np.exp(-t * 4.0) # Decay
        data[idx : idx + len(t)] += wave_form * 0.35
        
    save_wav(SFX_DIR / "metro_chime.wav", data, channels=1)


def synth_phone_typing_send():
    # 3 quick ticks + 1 swoosh (sending sound)
    duration_s = 1.2
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    # 3 ticks at t=0.1, 0.25, 0.4
    for tick_t in [0.1, 0.25, 0.4]:
        idx = int(tick_t * SAMPLE_RATE)
        t = np.linspace(0, 0.015, int(0.015 * SAMPLE_RATE))
        tick_wave = np.random.normal(0, 0.3, len(t)) * np.exp(-t * 600.0)
        data[idx : idx + len(t)] += tick_wave * 0.12
        
    # Swoosh starts at t=0.55 to 1.1
    idx_sw = int(0.55 * SAMPLE_RATE)
    sw_dur_s = 0.45
    n_sw = int(sw_dur_s * SAMPLE_RATE)
    t_sw = np.linspace(0, sw_dur_s, n_sw)
    
    # Sweep filter frequency from 400Hz to 1800Hz
    noise = np.random.normal(0.0, 1.0, n_sw)
    spec = np.fft.rfft(noise)
    freqs = np.fft.rfftfreq(n_sw, d=1.0/SAMPLE_RATE)
    
    # Dynamic frequency sweep simulated via overlapping bandpasses
    swoosh_spec = np.zeros_like(spec)
    for step in range(10):
        frac = step / 9.0
        f_ctr = 400.0 + (1400.0 * frac)
        env = np.exp(-((t_sw - frac * sw_dur_s) / 0.1)**2)
        # Bandpass filter
        bp = np.exp(-((freqs - f_ctr)/100.0)**2)
        swoosh_spec += np.fft.rfft(noise * env) * bp
        
    swoosh = np.fft.irfft(swoosh_spec, n_sw)
    # Norm & envelope fade-in/out
    swoosh = swoosh / np.max(np.abs(swoosh)) * np.sin(np.pi * t_sw / sw_dur_s)
    
    data[idx_sw : idx_sw + n_sw] += swoosh * 0.35
    save_wav(SFX_DIR / "phone_typing_send.wav", data, channels=1)


def synth_chair_murmur():
    # Heavy friction wood scraping + brief vocal murmur
    duration_s = 1.6
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    # Scrape at t=0.2 to 0.8
    idx_sc = int(0.2 * SAMPLE_RATE)
    sc_dur = 0.6
    n_sc = int(sc_dur * SAMPLE_RATE)
    t_sc = np.linspace(0, sc_dur, n_sc)
    
    # Friction scrape: bandpass noise modulated by low freq oscillation
    scrape_noise = make_filtered_noise(sc_dur, lambda f: np.exp(-((f-250.0)/80.0)**2))
    scrape_mod = 0.5 + 0.5 * np.sin(2 * np.pi * 35.0 * t_sc)
    scrape = scrape_noise * scrape_mod * np.sin(np.pi * t_sc / sc_dur)
    
    data[idx_sc : idx_sc + n_sc] += scrape * 0.5
    
    # Soft vocal murmur at t=0.7 to 1.4
    idx_m = int(0.7 * SAMPLE_RATE)
    m_dur = 0.7
    murmur = make_filtered_noise(m_dur, lambda f: np.exp(-((f-350.0)/120.0)**2))
    # slow vocal envelope
    t_m = np.linspace(0, m_dur, int(m_dur * SAMPLE_RATE))
    murmur = murmur * np.sin(np.pi * t_m / m_dur)
    
    data[idx_m : idx_m + len(t_m)] += murmur * 0.15
    save_wav(SFX_DIR / "chair_murmur.wav", data, channels=1)


def synth_thunder_rain():
    # Sudden explosion crack + deep rumbling + rain swell
    duration_s = 3.0
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    # Thunder crack at t=0.1
    idx_cr = int(0.1 * SAMPLE_RATE)
    t_cr = np.linspace(0, 0.4, int(0.4 * SAMPLE_RATE))
    crack = np.random.normal(0, 0.4, len(t_cr)) * np.exp(-t_cr * 20.0)
    data[idx_cr : idx_cr + len(t_cr)] += crack
    
    # Deep rumble at t=0.15 to 2.8
    idx_rb = int(0.15 * SAMPLE_RATE)
    rb_dur = 2.65
    n_rb = int(rb_dur * SAMPLE_RATE)
    t_rb = np.linspace(0, rb_dur, n_rb)
    
    rumble_noise = make_filtered_noise(rb_dur, lambda f: 1.0 / (1.0 + (f/55.0)**4))
    # low frequency modulation (rumble variation)
    rumble_mod = 0.7 + 0.3 * np.sin(2 * np.pi * 8.0 * t_rb) * np.sin(2 * np.pi * 0.7 * t_rb)
    rumble = rumble_noise * rumble_mod * np.exp(-t_rb * 0.9)
    
    data[idx_rb : idx_rb + n_rb] += rumble * 0.75
    
    # Rain onset swell
    t = np.linspace(0, duration_s, n)
    rain_noise = make_filtered_noise(duration_s, lambda f: np.exp(-((f-3000)/1500)**2))
    rain_env = 0.08 * (1.0 - np.exp(-t * 2.0)) # fades in
    data += rain_noise * rain_env
    
    save_wav(SFX_DIR / "thunder_rain.wav", data, channels=1)


def synth_doorbell_cups():
    # Two-tone chime "ding-dong" (E5 659Hz, C5 523Hz) + cups clinking
    duration_s = 2.2
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    # Chime 1 (Ding) at t=0.1
    idx_d1 = int(0.1 * SAMPLE_RATE)
    t_d1 = np.linspace(0, 0.8, int(0.8 * SAMPLE_RATE))
    ding = np.sin(2 * np.pi * 659.25 * t_d1) * np.exp(-t_d1 * 4.0)
    data[idx_d1 : idx_d1 + len(t_d1)] += ding * 0.3
    
    # Chime 2 (Dong) at t=0.5
    idx_d2 = int(0.5 * SAMPLE_RATE)
    t_d2 = np.linspace(0, 1.0, int(1.0 * SAMPLE_RATE))
    dong = np.sin(2 * np.pi * 523.25 * t_d2) * np.exp(-t_d2 * 3.5)
    data[idx_d2 : idx_d2 + len(t_d2)] += dong * 0.3
    
    # Cups clink at t=1.2
    idx_cl = int(1.2 * SAMPLE_RATE)
    t_cl = np.linspace(0, 0.5, int(0.5 * SAMPLE_RATE))
    # Short high freq resonant chimes for glass/ceramic clink
    clink = np.sin(2 * np.pi * 2800.0 * t_cl) * np.exp(-t_cl * 60.0)
    clink += 0.5 * np.sin(2 * np.pi * 3900.0 * t_cl) * np.exp(-t_cl * 90.0)
    clink += 0.2 * np.random.normal(0, 1.0, len(t_cl)) * np.exp(-t_cl * 120.0)
    data[idx_cl : idx_cl + len(t_cl)] += clink * 0.25
    
    save_wav(SFX_DIR / "doorbell_cups.wav", data, channels=1)


def synth_night_tone_pen():
    # Sine chime 440Hz + scratchy pencil/pen on paper
    duration_s = 2.0
    n = int(duration_s * SAMPLE_RATE)
    data = np.zeros(n)
    
    # Chime note at t=0.1
    idx_ch = int(0.1 * SAMPLE_RATE)
    t_ch = np.linspace(0, 1.0, int(1.0 * SAMPLE_RATE))
    chime = np.sin(2 * np.pi * 440.0 * t_ch) * np.exp(-t_ch * 3.0)
    data[idx_ch : idx_ch + len(t_ch)] += chime * 0.2
    
    # Pen scratching at t=0.4, 0.9, 1.3
    for pen_t in [0.4, 0.9, 1.3]:
        idx_pen = int(pen_t * SAMPLE_RATE)
        scratch_dur = 0.25
        t_pen = np.linspace(0, scratch_dur, int(scratch_dur * SAMPLE_RATE))
        # High-pass noise + amplitude mod
        scratch = make_filtered_noise(scratch_dur, lambda f: np.exp(-((f-1200.0)/400.0)**2))
        scratch_env = np.sin(np.pi * t_pen / scratch_dur) * (0.8 + 0.2 * np.sin(2 * np.pi * 12.0 * t_pen))
        data[idx_pen : idx_pen + len(t_pen)] += scratch * scratch_env * 0.1
        
    save_wav(SFX_DIR / "night_tone_pen.wav", data, channels=1)


# --- Out-of-scene segment beds (intro / montage / outro) ---
# These fill the structural segments that carry no scene_id (and so no ambient
# bed): the cheerful morning opener, the recap montage, and the calm close.

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
    peak = np.max(np.abs(data))
    return data / peak * target if peak > 0 else data


def synth_intro_morning_madrid():
    # Cheerful morning opener: warm sunrise sparkle + birdsong + soft city waking.
    duration_s = 16.0
    n = int(duration_s * SAMPLE_RATE)
    rng = np.random.default_rng(7)

    # Soft warm base bed: low warmth + a little high "air"
    base = make_stereo_loop(
        16.0,
        lambda f: 0.6 / (1.0 + (f/120.0)**4) + 0.05 / (1.0 + ((f-5000.0)/2500.0)**2),
        lambda f: 0.6 / (1.0 + (f/110.0)**4) + 0.05 / (1.0 + ((f-5200.0)/2500.0)**2),
    ) * 0.18
    left, right = base[:, 0].copy(), base[:, 1].copy()

    # Sunrise sparkle: ascending bright major arpeggio (C5 E5 G5 C6 E6)
    for freq, st in zip([523.25, 659.25, 783.99, 1046.50, 1318.51],
                        [0.15, 0.45, 0.78, 1.15, 1.6]):
        bell = _bell(freq, duration_s - st, decay=2.6, harmonic=0.25) * 0.16
        idx = int(st * SAMPLE_RATE)
        m = min(len(bell), n - idx)
        left[idx:idx+m] += bell[:m] * 0.9
        right[idx:idx+m] += bell[:m] * 1.0
    # Warm reprise chord (C major) around t=8.5s
    for freq in (523.25, 659.25, 783.99):
        bell = _bell(freq, duration_s - 8.5, decay=1.8, harmonic=0.2) * 0.07
        idx = int(8.5 * SAMPLE_RATE)
        m = min(len(bell), n - idx)
        left[idx:idx+m] += bell[:m]
        right[idx:idx+m] += bell[:m]

    # Birdsong: cheerful chirps, denser early, panned across the field
    for ct in np.sort(rng.uniform(0.6, 15.0, 9)):
        chirp = _bird_chirp(rng.uniform(2200, 4200), rng) * rng.uniform(0.10, 0.18)
        idx = int(ct * SAMPLE_RATE)
        m = min(len(chirp), n - idx)
        pan = rng.random()
        left[idx:idx+m] += chirp[:m] * (0.4 + 0.6 * (1 - pan))
        right[idx:idx+m] += chirp[:m] * (0.4 + 0.6 * pan)

    data = _normalize_peak(_apply_fades(np.stack([left, right], axis=-1), 0.4, 1.8), 0.7)
    save_wav(SFX_DIR / "intro_morning_madrid.wav", data, channels=2)


def synth_montage_warm_shimmer():
    # Warm, positive recap bed for the 6s montage.
    duration_s = 6.0
    n = int(duration_s * SAMPLE_RATE)
    t = np.linspace(0, duration_s, n, endpoint=False)
    swell = np.sin(np.pi * np.clip(t / duration_s, 0, 1)) ** 0.6

    # Warm major pad: detuned sines (C4 E4 G4 C5)
    pad = np.zeros(n)
    for freq in (261.63, 329.63, 392.00, 523.25):
        for det in (-0.3, 0.0, 0.3):
            pad += np.sin(2 * np.pi * (freq + det) * t)
    pad = pad / 12.0 * swell * 0.5

    shimmer_l = make_filtered_noise(duration_s, lambda f: np.exp(-((f-6000)/3000)**2)) * (0.3 + 0.3*np.sin(2*np.pi*0.40*t)) * swell * 0.12
    shimmer_r = make_filtered_noise(duration_s, lambda f: np.exp(-((f-6300)/3000)**2)) * (0.3 + 0.3*np.cos(2*np.pi*0.45*t)) * swell * 0.12
    bell = _bell(659.25, duration_s, decay=2.0, harmonic=0.3) * 0.18

    data = np.stack([pad + shimmer_l + bell, pad + shimmer_r + bell], axis=-1)
    data = _normalize_peak(_apply_fades(data, 0.4, 1.0), 0.7)
    save_wav(SFX_DIR / "montage_warm_shimmer.wav", data, channels=2)


def synth_outro_evening_calm():
    # Calm evening close: soft room warmth + a gentle resolving chime motif.
    duration_s = 15.0
    n = int(duration_s * SAMPLE_RATE)
    base = make_stereo_loop(
        15.0,
        lambda f: 0.7 / (1.0 + (f/90.0)**4),
        lambda f: 0.7 / (1.0 + (f/85.0)**4),
    ) * 0.22
    left, right = base[:, 0].copy(), base[:, 1].copy()

    # Descending resolving chime (G5 E5 C5) at start, soft reprise mid-way
    for start_t, vol in ((0.3, 0.16), (7.5, 0.10)):
        for i, freq in enumerate((783.99, 659.25, 523.25)):
            st = start_t + i * 0.5
            bell = _bell(freq, duration_s - st, decay=2.2, harmonic=0.25) * vol
            idx = int(st * SAMPLE_RATE)
            m = min(len(bell), n - idx)
            left[idx:idx+m] += bell[:m]
            right[idx:idx+m] += bell[:m]

    data = _normalize_peak(_apply_fades(np.stack([left, right], axis=-1), 0.5, 2.5), 0.6)
    save_wav(SFX_DIR / "outro_evening_calm.wav", data, channels=2)


def main():
    print("Synthesizing audio effects for AV Diary Pilot...")
    synth_madrid_morning()
    synth_home_morning()
    synth_metro_inside()
    synth_soft_phone_typing()
    synth_classroom_soft()
    synth_madrid_street()
    synth_rain_cafe()
    synth_quiet_night_room()
    
    synth_door_close_footsteps()
    synth_metro_chime()
    synth_phone_typing_send()
    synth_chair_murmur()
    synth_thunder_rain()
    synth_doorbell_cups()
    synth_night_tone_pen()

    synth_intro_morning_madrid()
    synth_montage_warm_shimmer()
    synth_outro_evening_calm()
    print("Synthesis complete.")


if __name__ == "__main__":
    main()
