"""Render entry point for preview and final MP4 outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from build.audio import build_narration_wav, mix_with_bgm, mux_into_video, synthesize_segments, write_manifest
from build.timeline import build_video_clip
from build.timeline import prepare_timeline
from segments import AUDIO, DESIGN, IMAGE_PATH, OUTPUT_NAME, SEGMENTS

OUTPUT_DIR = Path("output")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render the Spanish-learning video.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preview", action="store_true", help="Render a fast 12 fps preview.")
    mode.add_argument("--final", action="store_true", help="Render the final 30 fps MP4.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    audio_dir = OUTPUT_DIR / "audio"
    seg_audios = None
    tts_durations = None

    if AUDIO:
        seg_audios = synthesize_segments(SEGMENTS, AUDIO, audio_dir / "tts")
        tts_durations = {int(seg_audio["index"]): float(seg_audio["duration_s"]) for seg_audio in seg_audios}

    timings = prepare_timeline(SEGMENTS, design=DESIGN, tts_durations=tts_durations, audio_cfg=AUDIO)
    total_duration_s = timings[-1].end_s if timings else 0.0
    clip = build_video_clip(IMAGE_PATH, SEGMENTS, design=DESIGN, timings=timings)

    if args.preview:
        silent_path = OUTPUT_DIR / "preview-silent.mp4"
        output_path = OUTPUT_DIR / "preview.mp4"
        fps = 12
        preset = "ultrafast"
        crf = "26"
    else:
        silent_path = OUTPUT_DIR / f"{OUTPUT_NAME}-silent.mp4"
        output_path = OUTPUT_DIR / f"{OUTPUT_NAME}.mp4"
        fps = 30
        preset = "medium"
        crf = "18"

    clip.write_videofile(
        str(silent_path),
        codec="libx264",
        audio=False,
        fps=fps,
        preset=preset,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart", "-crf", crf],
    )
    clip.close()

    if AUDIO and seg_audios is not None:
        narration_wav = build_narration_wav(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "narration.wav")
        mix_wav = mix_with_bgm(narration_wav, AUDIO.get("bgm_path"), AUDIO, total_duration_s, audio_dir / "mix.wav")
        write_manifest(seg_audios, timings, AUDIO, total_duration_s, audio_dir / "tts" / "manifest.json")
        mux_into_video(silent_path, mix_wav, AUDIO, output_path)
        silent_path.unlink(missing_ok=True)
    else:
        silent_path.rename(output_path)

    print(
        json.dumps(
            {
                "ok": True,
                "output": str(output_path),
                "fps": fps,
                "duration_s": round(total_duration_s, 3),
                "audio": bool(AUDIO),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
