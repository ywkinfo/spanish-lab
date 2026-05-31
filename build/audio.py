"""Audio generation and muxing helpers for narrated videos."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from build.segment_adapter import RENDER_TYPE_CARDS, RENDER_TYPE_DIARY, get_render_type, narration_text
from build.timeline import SegmentTiming, prepare_timeline

OUTPUT_DIR = Path("output")
ROOT = Path(__file__).resolve().parents[1]

SegmentAudio = dict[str, Any]


def assert_tts_fits_timeline(
    seg_audios: list[SegmentAudio],
    timings: list[Any],
    audio_cfg: dict,
    *,
    tolerance_s: float | None = None,
) -> None:
    """Fail if any synthesized TTS clip would run into the next segment.

    Card timelines use explicit segment durations.  If a generated TTS clip is
    longer than its card duration, MoviePy overlays it with the following card's
    audio.  That is hard to notice from duration-only verification, so catch it
    before composing narration.
    """
    lead = float(audio_cfg.get("lead_padding_s", 0.3))
    tolerance = float(audio_cfg.get("tts_overlap_tolerance_s", 0.05) if tolerance_s is None else tolerance_s)
    timings_by_index = {int(timing.index): timing for timing in timings}
    errors: list[str] = []
    for seg_audio in seg_audios:
        index = int(seg_audio["index"])
        timing = timings_by_index[index]
        tts_duration = float(seg_audio["duration_s"])
        audio_end = float(timing.start_s) + lead + tts_duration
        allowed_end = float(timing.end_s) + tolerance
        if audio_end > allowed_end:
            errors.append(
                f"seg #{index}: TTS audio would end at {audio_end:.2f}s "
                f"after segment end {float(timing.end_s):.2f}s "
                f"(tts={tts_duration:.2f}s, lead={lead:.2f}s, tolerance={tolerance:.2f}s)"
            )
    if errors:
        raise ValueError("TTS overlaps following segment(s): " + "; ".join(errors))


def text_hash(text: str, voice: str, rate_wpm: int | str) -> str:
    payload = "\0".join([text, voice, str(rate_wpm)])
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:12]


def voice_for_segment(segment: dict, audio_cfg: dict) -> str:
    """Resolve the TTS voice for one segment, honoring character voice maps."""
    speaker = str(segment.get("speaker") or segment.get("character") or "")
    voice_map = audio_cfg.get("character_voices", {}) or {}
    if speaker and speaker in voice_map:
        return str(voice_map[speaker])
    engine = str(audio_cfg.get("tts_engine", "auto")).lower()
    if engine == "edge":
        return str(audio_cfg.get("edge_voice", audio_cfg.get("voice", "es-ES-ElviraNeural")))
    if engine == "flite":
        return str(audio_cfg.get("flite_voice", audio_cfg.get("voice", "slt")))
    return str(audio_cfg.get("voice", audio_cfg.get("flite_voice", "Mónica")))


def audio_cfg_for_segment(segment: dict, audio_cfg: dict) -> dict:
    """Return an audio config copy with the resolved segment voice applied."""
    resolved = dict(audio_cfg)
    voice = voice_for_segment(segment, audio_cfg)
    resolved["voice"] = voice
    engine = str(resolved.get("tts_engine", "auto")).lower()
    if engine == "edge":
        resolved["edge_voice"] = voice
    elif engine == "flite":
        resolved["flite_voice"] = voice
    return resolved


def probe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def build_tts_command(text: str, out_path: Path, text_path: Path, audio_cfg: dict) -> list[str]:
    """Build the platform-appropriate command for one TTS segment."""
    engine = str(audio_cfg.get("tts_engine", "auto")).lower()
    sample_rate = str(int(audio_cfg.get("sample_rate_hz", 44100)))
    if engine == "auto":
        engine = "say" if shutil.which("say") else "flite"

    if engine == "say":
        voice = str(audio_cfg.get("voice", "Mónica"))
        rate_wpm = str(int(audio_cfg.get("rate_wpm", 175)))
        return ["say", "-v", voice, "-r", rate_wpm, "-o", str(out_path), text]

    if engine == "flite":
        voice = str(audio_cfg.get("flite_voice", "slt"))
        return [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "lavfi",
            "-i",
            f"flite=textfile={text_path}:voice={voice}",
            "-ar",
            sample_rate,
            str(out_path),
        ]

    if engine == "edge":
        voice = str(audio_cfg.get("edge_voice", audio_cfg.get("voice", "es-ES-ElviraNeural")))
        rate = str(audio_cfg.get("edge_rate", "+0%"))
        pitch = str(audio_cfg.get("edge_pitch", "+0Hz"))
        volume = str(audio_cfg.get("edge_volume", "+0%"))
        return [
            sys.executable,
            "-m",
            "edge_tts",
            "--file",
            str(text_path),
            "--voice",
            voice,
            f"--rate={rate}",
            f"--pitch={pitch}",
            f"--volume={volume}",
            "--write-media",
            str(out_path),
        ]

    raise ValueError(f"Unsupported tts_engine: {engine}")


def synthesize_segments(
    segments: list[dict],
    audio_cfg: dict,
    cache_dir: Path,
    render_type: str = "kenburns",
) -> list[SegmentAudio]:
    """Generate or reuse cached TTS files for each segment."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    engine_cfg = str(audio_cfg.get("tts_engine", "auto")).lower()
    if engine_cfg == "edge":
        voice = str(audio_cfg.get("edge_voice", audio_cfg.get("voice", "es-ES-ElviraNeural")))
    elif engine_cfg == "flite":
        voice = str(audio_cfg.get("flite_voice", audio_cfg.get("voice", "slt")))
    else:
        voice = str(audio_cfg.get("voice", audio_cfg.get("flite_voice", "Mónica")))
    rate_wpm = int(audio_cfg.get("rate_wpm", 175))

    seg_audios: list[SegmentAudio] = []
    for index, segment in enumerate(segments, start=1):
        text = narration_text(segment, render_type)
        if not text:
            voice = voice_for_segment(segment, audio_cfg)
            digest = text_hash(text, voice, rate_wpm)
            seg_audios.append(
                {
                    "index": index,
                    "text": "",
                    "path": "",
                    "duration_s": 0.0,
                    "hash": digest,
                    "voice": voice,
                }
            )
            continue
        segment_audio_cfg = audio_cfg_for_segment(segment, audio_cfg)
        voice = voice_for_segment(segment, audio_cfg)
        digest = text_hash(text, voice, rate_wpm)
        engine = str(segment_audio_cfg.get("tts_engine", "auto")).lower()
        if engine == "auto" and not shutil.which("say"):
            engine = "flite"
        if engine == "edge":
            suffix = ".mp3"
        elif engine in {"auto", "say"} and shutil.which("say"):
            suffix = ".aiff"
        else:
            suffix = ".wav"
        path = cache_dir / f"seg_{index:02d}_{digest}{suffix}"
        text_path = cache_dir / f"seg_{index:02d}_{digest}.txt"
        if not path.exists() or path.stat().st_size == 0:
            text_path.write_text(text, encoding="utf-8")
            subprocess.run(
                build_tts_command(text, path, text_path, segment_audio_cfg),
                check=True,
            )
        duration_s = probe_duration(path)
        seg_audios.append(
            {
                "index": index,
                "text": text,
                "path": str(path),
                "duration_s": duration_s,
                "hash": digest,
                "voice": voice,
            }
        )
    return seg_audios


def write_manifest(
    seg_audios: list[SegmentAudio],
    timings: list[SegmentTiming],
    audio_cfg: dict,
    total_duration_s: float,
    manifest_path: Path,
) -> None:
    """Write audio timing metadata used by render and verification."""
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    timings_by_index = {timing.index: timing for timing in timings}
    segments = []
    for seg_audio in seg_audios:
        index = int(seg_audio["index"])
        timing = timings_by_index[index]
        segments.append(
            {
                "index": index,
                "text_hash": seg_audio["hash"],
                "voice": seg_audio.get("voice"),
                "audio_path": seg_audio["path"],
                "tts_duration_s": round(float(seg_audio["duration_s"]), 6),
                "computed_duration_s": round(timing.duration_s, 6),
                "start_s": round(timing.start_s, 6),
                "end_s": round(timing.end_s, 6),
            }
        )

    payload = {
        "voice": audio_cfg.get("voice"),
        "rate_wpm": audio_cfg.get("rate_wpm"),
        "sample_rate_hz": int(audio_cfg.get("sample_rate_hz", 44100)),
        "narration_path": str(OUTPUT_DIR / "audio" / "narration.wav"),
        "mix_path": str(OUTPUT_DIR / "audio" / "mix.wav"),
        "total_duration_s": round(total_duration_s, 6),
        "segments": segments,
    }
    manifest_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_narration_wav(
    seg_audios: list[SegmentAudio],
    timings: list[SegmentTiming],
    audio_cfg: dict,
    total_duration_s: float,
    out_path: Path,
) -> Path:
    """Compose segment AIFF clips into a single narration WAV."""
    from moviepy import AudioFileClip, CompositeAudioClip

    assert_tts_fits_timeline(seg_audios, timings, audio_cfg)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lead = float(audio_cfg.get("lead_padding_s", 0.3))
    sample_rate = int(audio_cfg.get("sample_rate_hz", 44100))
    timings_by_index = {timing.index: timing for timing in timings}
    audio_clips = []
    source_clips = []
    try:
        for seg_audio in seg_audios:
            if not seg_audio.get("path"):
                continue
            timing = timings_by_index[int(seg_audio["index"])]
            source = AudioFileClip(seg_audio["path"])
            source_clips.append(source)
            audio_clips.append(source.with_start(timing.start_s + lead))

        composite = CompositeAudioClip(audio_clips).with_duration(total_duration_s)
        try:
            composite.write_audiofile(
                str(out_path),
                fps=sample_rate,
                codec="pcm_s16le",
                logger=None,
            )
        finally:
            composite.close()
    finally:
        for clip in source_clips:
            clip.close()
    return out_path


def mix_sfx_layer(
    narration_wav: Path,
    sfx_manifest: list[dict] | None,
    timings: list[Any],
    total_duration_s: float,
    out_path: Path,
    story_scenes: list[dict] | None = None,
    audio_cfg: dict | None = None,
    segment_sfx: list[dict] | None = None,
) -> Path:
    """Layer SFX events (ambient loop bed and spot effects) on top of the narration WAV.

    Three layers are composited over the narration:
      1. Ambient beds   -- per-scene `ambient_sfx`, looped across each scene span.
      2. Spot effects   -- `sfx_manifest`, one-shots anchored to a scene line.
      3. Segment SFX    -- `segment_sfx`, sound for the non-scene segments
                           (intro / montage / outro) which carry no `scene_id`
                           and are therefore anchored by segment `type`.
    """
    from moviepy import AudioFileClip, CompositeAudioClip
    from moviepy.audio.fx import AudioLoop

    has_sfx = False
    if sfx_manifest:
        has_sfx = True
    if story_scenes and any(scene.get("ambient_sfx") for scene in story_scenes):
        has_sfx = True
    if segment_sfx:
        has_sfx = True

    if not has_sfx:
        if narration_wav.resolve() != out_path.resolve():
            shutil.copyfile(narration_wav, out_path)
        return out_path

    out_path.parent.mkdir(parents=True, exist_ok=True)
    audio_clips = []
    source_clips = []
    try:
        base_clip = AudioFileClip(str(narration_wav))
        source_clips.append(base_clip)
        audio_clips.append(base_clip.with_start(0.0))

        # 1. Layer 1: Ambient Bed (ambient_sfx loop)
        if story_scenes:
            for scene in story_scenes:
                ambient_path = scene.get("ambient_sfx")
                if not ambient_path:
                    continue
                
                sid = scene.get("scene_id")
                scene_timings = [t for t in timings if getattr(t, "scene_id", None) == sid]
                if not scene_timings:
                    continue
                
                scene_start = min(t.start_s for t in scene_timings)
                scene_end = max(t.end_s for t in scene_timings)
                span = scene_end - scene_start
                if span <= 0:
                    continue
                
                bed_file_path = ROOT / ambient_path
                if not bed_file_path.exists():
                    print(f"warning: Ambient SFX path not found, skipping: {bed_file_path}")
                    continue
                
                bed_clip = AudioFileClip(str(bed_file_path))
                source_clips.append(bed_clip)
                
                # Volume (applied first to AudioFileClip)
                default_bed_db = -20.0
                if audio_cfg and "ambient_bed_db" in audio_cfg:
                    default_bed_db = float(audio_cfg["ambient_bed_db"])
                bed_vol_db = float(scene.get("ambient_sfx_volume_db") or default_bed_db)
                bed_vol_factor = 10.0 ** (bed_vol_db / 20.0)
                bed_clip = bed_clip.with_volume_scaled(bed_vol_factor)
                
                # Loop (applied second)
                bed_clip = bed_clip.with_effects([AudioLoop(duration=span)])
                
                bed_clip = bed_clip.with_start(scene_start)
                audio_clips.append(bed_clip)

        # 2. Layer 2: Spot effects
        if sfx_manifest:
            for sfx in sfx_manifest:
                sfx_path = ROOT / sfx["path"]
                if not sfx_path.exists():
                    print(f"warning: SFX path not found, skipping: {sfx_path}")
                    continue

                scene_id = sfx["scene_id"]
                # Find anchor start time
                anchor_start = None
                line_idx = sfx.get("line_index")
                if line_idx is not None:
                    timing = next(
                        (t for t in timings 
                         if getattr(t, "scene_id", None) == scene_id 
                         and getattr(t, "line_index", None) == line_idx 
                         and getattr(t, "type", None) == "diary_line"),
                        None
                    )
                    if timing:
                        anchor_start = timing.start_s
                    else:
                        print(f"warning: Spot SFX references out of bounds line_index {line_idx} in scene {scene_id}, falling back to scene start")
                
                if anchor_start is None:
                    # Fallback to scene_header start
                    header_timing = next(
                        (t for t in timings 
                         if getattr(t, "scene_id", None) == scene_id 
                         and getattr(t, "type", None) == "scene_header"),
                        None
                    )
                    if header_timing:
                        anchor_start = header_timing.start_s
                    else:
                        # Fallback to first timing of the scene
                        scene_timings = [t for t in timings if getattr(t, "scene_id", None) == scene_id]
                        if scene_timings:
                            anchor_start = min(t.start_s for t in scene_timings)
                        else:
                            print(f"warning: Spot SFX references scene_id {scene_id} which has no timing, skipping")
                            continue

                offset_val = float(sfx.get("offset_s", sfx.get("start_s", 0.0)))
                abs_start = anchor_start + offset_val

                sfx_clip = AudioFileClip(str(sfx_path))
                source_clips.append(sfx_clip)

                vol_db = float(sfx.get("volume_db", -12.0))
                vol_factor = 10.0 ** (vol_db / 20.0)
                sfx_clip = sfx_clip.with_volume_scaled(vol_factor)

                sfx_clip = sfx_clip.with_start(abs_start)
                audio_clips.append(sfx_clip)

        # 3. Layer 3: Out-of-scene segment SFX (intro / montage / outro).
        # These structural segments carry no scene_id, so they are anchored by
        # segment `type`.  mode="bed" loops the clip across the segment span
        # (e.g. a cheerful morning bed under the whole intro); mode="spot" places
        # a single one-shot at `offset_s` from the segment start.
        if segment_sfx:
            for entry in segment_sfx:
                seg_path = ROOT / entry["path"]
                if not seg_path.exists():
                    print(f"warning: Segment SFX path not found, skipping: {seg_path}")
                    continue

                seg_type = entry.get("segment_type")
                seg_timings = [t for t in timings if getattr(t, "type", None) == seg_type]
                if not seg_timings:
                    print(f"warning: Segment SFX references segment_type {seg_type!r} with no timing, skipping")
                    continue

                span_start = min(t.start_s for t in seg_timings)
                span_end = max(t.end_s for t in seg_timings)
                span = span_end - span_start
                if span <= 0:
                    continue

                seg_clip = AudioFileClip(str(seg_path))
                source_clips.append(seg_clip)

                vol_db = float(entry.get("volume_db", -18.0))
                seg_clip = seg_clip.with_volume_scaled(10.0 ** (vol_db / 20.0))

                mode = str(entry.get("mode", "bed"))
                if mode == "bed":
                    seg_clip = seg_clip.with_effects([AudioLoop(duration=span)])
                    seg_clip = seg_clip.with_start(span_start)
                else:  # spot
                    offset_val = float(entry.get("offset_s", 0.0))
                    seg_clip = seg_clip.with_start(span_start + offset_val)
                audio_clips.append(seg_clip)

        composite = CompositeAudioClip(audio_clips).with_duration(total_duration_s)
        try:
            composite.write_audiofile(
                str(out_path),
                fps=44100,
                codec="pcm_s16le",
                logger=None,
            )
        finally:
            composite.close()
    finally:
        for clip in source_clips:
            clip.close()

    return out_path


def _ffmpeg_volume_db(value: Any, default: float) -> str:
    return f"{float(value if value is not None else default):.3f}"


def mix_with_bgm(
    narration_wav: Path,
    bgm_path: str | Path | None,
    audio_cfg: dict,
    total_duration_s: float,
    out_path: Path,
) -> Path:
    """Mix narration with optional BGM using ffmpeg filters."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    bgm = Path(bgm_path) if bgm_path else None
    if not bgm or not bgm.exists():
        if narration_wav.resolve() != out_path.resolve():
            shutil.copyfile(narration_wav, out_path)
        return out_path

    bgm_db = _ffmpeg_volume_db(audio_cfg.get("bgm_volume_db"), -22.0)
    narration_db = _ffmpeg_volume_db(audio_cfg.get("narration_volume_db"), 0.0)
    fade_in = max(0.0, float(audio_cfg.get("fade_in_s", 1.5)))
    fade_out = max(0.0, float(audio_cfg.get("fade_out_s", 2.0)))
    fade_out_start = max(0.0, total_duration_s - fade_out)
    sample_rate = int(audio_cfg.get("sample_rate_hz", 44100))
    bgm_chain = (
        f"[1:a]atrim=0:{total_duration_s:.6f},asetpts=PTS-STARTPTS,"
        f"volume={bgm_db}dB,"
        f"afade=t=in:st=0:d={fade_in:.6f},"
        f"afade=t=out:st={fade_out_start:.6f}:d={fade_out:.6f}[bgm]"
    )

    if bool(audio_cfg.get("ducking", True)):
        threshold = float(audio_cfg.get("ducking_threshold", 0.05))
        ratio = float(audio_cfg.get("ducking_ratio", 8))
        attack = int(audio_cfg.get("ducking_attack_ms", 120))
        release = int(audio_cfg.get("ducking_release_ms", 600))
        filter_complex = (
            f"{bgm_chain};"
            f"[0:a]volume={narration_db}dB,asplit=2[nar1][nar2];"
            f"[bgm][nar1]sidechaincompress=threshold={threshold}:ratio={ratio}:"
            f"attack={attack}:release={release}[ducked];"
            f"[ducked][nar2]amix=inputs=2:normalize=0:duration=first:dropout_transition=0[mixed];"
            f"[mixed]alimiter=level_in=1:level_out=1:limit=0.9,loudnorm=I=-14:TP=-1.5:LRA=11,"
            f"apad,atrim=0:{total_duration_s:.6f},aresample={sample_rate}[mix]"
        )
    else:
        filter_complex = (
            f"{bgm_chain};"
            f"[0:a]volume={narration_db}dB[nar];"
            f"[bgm][nar]amix=inputs=2:normalize=0:duration=first:dropout_transition=0[mixed];"
            f"[mixed]alimiter=level_in=1:level_out=1:limit=0.9,loudnorm=I=-14:TP=-1.5:LRA=11,"
            f"apad,atrim=0:{total_duration_s:.6f},aresample={sample_rate}[mix]"
        )

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(narration_wav),
            "-stream_loop",
            "-1",
            "-i",
            str(bgm),
            "-filter_complex",
            filter_complex,
            "-map",
            "[mix]",
            "-t",
            f"{total_duration_s:.6f}",
            str(out_path),
        ],
        check=True,
    )
    return out_path


def mux_into_video(silent_mp4: Path, mix_wav: Path, audio_cfg: dict, out_path: Path) -> Path:
    """Mux a prepared audio file into a silent MP4 without re-encoding video."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    codec = str(audio_cfg.get("audio_codec", "aac"))
    bitrate = f"{int(audio_cfg.get('audio_bitrate_kbps', 192))}k"
    sample_rate = str(int(audio_cfg.get("sample_rate_hz", 44100)))
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(silent_mp4),
            "-i",
            str(mix_wav),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            codec,
            "-b:a",
            bitrate,
            "-ar",
            sample_rate,
            "-shortest",
            "-movflags",
            "+faststart",
            str(out_path),
        ],
        check=True,
    )
    return out_path


def main() -> int:
    import segments as project_segments
    from segments import AUDIO, DESIGN, SEGMENTS

    if not AUDIO:
        print(json.dumps({"ok": True, "audio": False, "message": "project has no AUDIO config"}))
        return 0

    render_type = get_render_type(project_segments)
    audio_dir = OUTPUT_DIR / "audio"
    seg_audios = synthesize_segments(SEGMENTS, AUDIO, audio_dir / "tts", render_type=render_type)
    tts_durations = {int(seg_audio["index"]): float(seg_audio["duration_s"]) for seg_audio in seg_audios}
    if render_type == RENDER_TYPE_CARDS:
        from build.card_timeline import build_card_timings

        timings = build_card_timings(SEGMENTS, design=DESIGN, tts_durations=tts_durations, audio_cfg=AUDIO)
    elif render_type == RENDER_TYPE_DIARY:
        from build.diary_timeline import build_diary_timings

        timings = build_diary_timings(SEGMENTS, design=DESIGN, tts_durations=tts_durations, audio_cfg=AUDIO)
    else:
        timings = prepare_timeline(SEGMENTS, design=DESIGN, tts_durations=tts_durations, audio_cfg=AUDIO)
    total_duration_s = timings[-1].end_s if timings else 0.0
    assert_tts_fits_timeline(seg_audios, timings, AUDIO)
    write_manifest(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "tts" / "manifest.json")
    print(
        json.dumps(
            {
                "ok": True,
                "audio": True,
                "segments": len(seg_audios),
                "manifest": str(audio_dir / "tts" / "manifest.json"),
                "total_duration_s": round(total_duration_s, 3),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
