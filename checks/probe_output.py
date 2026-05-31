"""Probe the rendered MP4 for expected technical properties."""

from __future__ import annotations

import argparse
from fractions import Fraction
import io
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.camera import output_size_for_design  # noqa: E402
from build.timeline import expected_total_duration  # noqa: E402
from segments import AUDIO, DESIGN, SEGMENTS, RENDER_TYPE, OUTPUT_NAME  # noqa: E402

MANIFEST_PATH = ROOT / "output" / "audio" / "tts" / "manifest.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate final MP4 output with ffprobe.")
    default_video = f"output/{OUTPUT_NAME}.mp4" if OUTPUT_NAME else "output/reunion-madrid.mp4"
    parser.add_argument("video", nargs="?", default=default_video)
    return parser.parse_args()


def ffprobe(path: Path) -> dict:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def extract_brightness(path: Path, timestamp: float) -> dict:
    result = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{timestamp:.3f}",
            "-i",
            str(path),
            "-frames:v",
            "1",
            "-vf",
            "scale=64:36",
            "-f",
            "image2pipe",
            "-vcodec",
            "png",
            "pipe:1",
        ],
        check=True,
        capture_output=True,
    )
    image = Image.open(io.BytesIO(result.stdout)).convert("RGB")
    arr = np.asarray(image)
    return {"timestamp": round(timestamp, 3), "mean": float(arr.mean()), "std": float(arr.std())}


def parse_rate(rate: str | None) -> float:
    if not rate:
        return 0.0
    try:
        return float(Fraction(rate))
    except (ValueError, ZeroDivisionError):
        return 0.0


def has_faststart(path: Path) -> bool:
    data = path.read_bytes()[:1024 * 1024]
    moov = data.find(b"moov")
    mdat = data.find(b"mdat")
    return moov != -1 and (mdat == -1 or moov < mdat)


def load_audio_manifest(errors: list[str]) -> dict | None:
    if not MANIFEST_PATH.exists():
        errors.append(f"audio manifest not found: {MANIFEST_PATH}")
        return None
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"audio manifest is not valid JSON: {exc}")
        return None


def run_volumedetect(path: Path) -> dict[str, float]:
    result = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(path),
            "-map",
            "0:a:0",
            "-af",
            "volumedetect",
            "-f",
            "null",
            "-",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    stats = {}
    for key in ["mean_volume", "max_volume"]:
        match = re.search(rf"{key}:\s*(-?\d+(?:\.\d+)?) dB", result.stderr)
        if match:
            stats[key] = float(match.group(1))
    return stats


def main() -> int:
    args = parse_args()
    path = ROOT / args.video
    errors: list[str] = []
    details: dict = {"video": str(path)}

    if not path.exists():
        print(json.dumps({"ok": False, "errors": [f"video not found: {path}"]}, ensure_ascii=False, indent=2))
        return 1

    try:
        probe = ffprobe(path)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [f"ffprobe failed: {exc}"]}, ensure_ascii=False, indent=2))
        return 1

    video_stream = next((stream for stream in probe["streams"] if stream.get("codec_type") == "video"), None)
    if not video_stream:
        errors.append("no video stream found")
    else:
        expected_size = output_size_for_design(DESIGN)
        width = int(video_stream.get("width", 0))
        height = int(video_stream.get("height", 0))
        codec = video_stream.get("codec_name")
        pix_fmt = video_stream.get("pix_fmt")
        fps = parse_rate(video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate"))
        details.update({"width": width, "height": height, "codec": codec, "pix_fmt": pix_fmt, "fps": fps})
        if (width, height) != expected_size:
            errors.append(f"expected {expected_size[0]}x{expected_size[1]}, got {width}x{height}")
        if codec != "h264":
            errors.append(f"expected h264 codec, got {codec}")
        if pix_fmt != "yuv420p":
            errors.append(f"expected yuv420p pix_fmt, got {pix_fmt}")
        if abs(fps - 30.0) > 0.01:
            errors.append(f"expected 30 fps, got {fps:.3f}")

    faststart = has_faststart(path)
    details["faststart"] = faststart
    if not faststart:
        errors.append("expected faststart MP4 with moov atom before mdat")

    manifest = load_audio_manifest(errors) if AUDIO else None
    duration = float(probe.get("format", {}).get("duration", 0))
    if RENDER_TYPE == "diary":
        from build.diary_timeline import expected_diary_total_duration
        expected = (
            float(manifest["total_duration_s"])
            if manifest and "total_duration_s" in manifest
            else expected_diary_total_duration(SEGMENTS, audio_cfg=AUDIO)
        )
    else:
        expected = (
            float(manifest["total_duration_s"])
            if manifest and "total_duration_s" in manifest
            else expected_total_duration(SEGMENTS, design=DESIGN)
        )
    details.update({"duration_s": round(duration, 3), "expected_duration_s": round(expected, 3)})
    if abs(duration - expected) > 0.5:
        errors.append(f"duration {duration:.3f}s differs from expected {expected:.3f}s by more than 0.5s")

    if AUDIO:
        audio_stream = next((stream for stream in probe["streams"] if stream.get("codec_type") == "audio"), None)
        if not audio_stream:
            errors.append("no audio stream found")
        else:
            audio_codec = audio_stream.get("codec_name")
            channels = int(audio_stream.get("channels", 0))
            sample_rate = int(audio_stream.get("sample_rate", 0))
            audio_duration = float(audio_stream.get("duration") or probe.get("format", {}).get("duration", 0))
            expected_sample_rate = int(AUDIO.get("sample_rate_hz", 44100))
            details.update(
                {
                    "audio_codec": audio_codec,
                    "audio_channels": channels,
                    "audio_sample_rate": sample_rate,
                    "audio_duration_s": round(audio_duration, 3),
                }
            )
            if audio_codec != "aac":
                errors.append(f"expected aac audio codec, got {audio_codec}")
            if channels < 1:
                errors.append(f"expected at least 1 audio channel, got {channels}")
            if sample_rate != expected_sample_rate:
                errors.append(f"expected audio sample rate {expected_sample_rate}, got {sample_rate}")
            if abs(audio_duration - duration) > 0.3:
                errors.append(
                    f"audio duration {audio_duration:.3f}s differs from video duration {duration:.3f}s by more than 0.3s"
                )
            try:
                volume = run_volumedetect(path)
                details["audio_volume"] = volume
                mean_volume = volume.get("mean_volume")
                max_volume = volume.get("max_volume")
                if mean_volume is None:
                    errors.append("could not read mean audio volume")
                elif mean_volume <= -50:
                    errors.append(f"audio appears silent: mean_volume={mean_volume:.1f} dB")
                if max_volume is None:
                    errors.append("could not read max audio volume")
                elif max_volume > -0.1:
                    errors.append(f"audio may be clipping: max_volume={max_volume:.1f} dB")
            except subprocess.CalledProcessError as exc:
                errors.append(f"audio volume analysis failed: {exc}")
        details["manual_checks"] = [
            "confirm narration starts shortly after each subtitle appears",
            "confirm BGM is audible when assets/audio/bgm.mp3 is present and does not mask narration",
        ]

    brightness = []
    if duration > 1:
        for ratio in [0.1, 0.3, 0.5, 0.7, 0.9]:
            try:
                stats = extract_brightness(path, duration * ratio)
                brightness.append(stats)
                if stats["mean"] < 5 or stats["mean"] > 250 or stats["std"] < 5:
                    errors.append(f"suspicious frame at {stats['timestamp']:.2f}s: {stats}")
            except subprocess.CalledProcessError as exc:
                errors.append(f"frame extraction failed at ratio {ratio}: {exc}")
    details["frame_stats"] = brightness

    print(json.dumps({"ok": not errors, "errors": errors, **details}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
