"""Static validation for diary-type story projects."""

from __future__ import annotations

import hashlib
import math
import wave
from array import array
from pathlib import Path

try:
    from PIL import Image
except Exception:  # pragma: no cover - Pillow is a project dependency
    Image = None

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_IMAGE_EXT = {".png", ".jpg", ".jpeg"}
ALLOWED_AUDIO_EXT = {".wav", ".mp3", ".m4a"}

# Map a file extension to the format Pillow reports for it, so a JPEG saved as
# ``.png`` (or vice versa) is flagged instead of silently passing.
EXT_TO_IMAGE_FORMAT = {".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG"}

# Below this peak level a clip is treated as silence (a placeholder, not a real
# sound effect). 16-bit digital silence sits near -90 dBFS; real beds/spots are
# well above -50 dBFS.
SILENCE_PEAK_DBFS = -50.0


def get_image_size(file_path: Path) -> tuple[int, int] | None:
    """Return ``(width, height)`` using Pillow; ``None`` if unreadable.

    Pillow sniffs the real file contents, so this works even when the extension
    lies about the format. The previous hand-rolled header parser returned
    ``None`` for such files, silently skipping the resolution guard entirely.
    """
    if Image is None:
        return None
    try:
        with Image.open(file_path) as img:
            return int(img.width), int(img.height)
    except Exception:
        return None


def get_image_format(file_path: Path) -> str | None:
    """Return Pillow's format string (e.g. ``"PNG"``/``"JPEG"``) or ``None``."""
    if Image is None:
        return None
    try:
        with Image.open(file_path) as img:
            return img.format
    except Exception:
        return None


def file_md5(file_path: Path) -> str | None:
    """Return the hex MD5 of a file's bytes, or ``None`` if unreadable."""
    try:
        digest = hashlib.md5()
        with file_path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except Exception:
        return None


def audio_peak_dbfs(file_path: Path) -> float | None:
    """Peak level of a PCM WAV in dBFS, or ``None`` for non-PCM/unreadable.

    Used to catch silent placeholder clips. Non-WAV (mp3/m4a) and non-PCM WAV
    return ``None`` (the silence check is skipped) so no audio-decoder
    dependency is introduced.
    """
    try:
        with wave.open(str(file_path), "rb") as wav:
            if wav.getcomptype() != "NONE":
                return None
            sampwidth = wav.getsampwidth()
            nframes = wav.getnframes()
            if nframes == 0:
                return None
            raw = wav.readframes(nframes)
    except Exception:
        return None
    spec = {2: ("h", 32768.0), 4: ("i", 2147483648.0)}.get(sampwidth)
    if spec is None:
        return None
    typecode, full_scale = spec
    samples = array(typecode)
    try:
        samples.frombytes(raw)
    except ValueError:
        return None
    peak = max((abs(sample) for sample in samples), default=0)
    if peak <= 0:
        return -120.0
    return 20.0 * math.log10(peak / full_scale)


def _check_image_file(prefix: str, suffix: str, full_path: Path, warnings: list[str]) -> None:
    """Append resolution / format-mismatch warnings for an existing image."""
    sz = get_image_size(full_path)
    if sz:
        w, h = sz
        if w < 1600 or h < 900:
            warnings.append(
                f"{prefix}: image resolution {w}x{h} is below the recommended minimum of 1600x900 "
                f"(a full-bleed diary background needs ~1.25x the 16:9 viewport for the Ken Burns zoom)"
            )
    fmt = get_image_format(full_path)
    expected_fmt = EXT_TO_IMAGE_FORMAT.get(suffix.lower())
    if fmt and expected_fmt and fmt != expected_fmt:
        warnings.append(
            f"{prefix}: image is {fmt} data but has a {suffix} extension "
            f"(re-encode or rename so the extension matches the real format)"
        )


def validate(
    story_scenes: list[dict],
    sfx_manifest: list[dict] | None,
    design: dict,
    descrip_path: str,
    segment_sfx: list[dict] | None = None,
) -> tuple[list[str], list[str], dict]:
    """Validate a diary-type story project and return (errors, warnings, summary)."""
    errors: list[str] = []
    warnings: list[str] = []

    # -- Rule 1: story_scenes must not be None or empty -----------------------
    if not story_scenes:
        errors.append("story_scenes is empty or None")
        summary = {
            "scenes": 0,
            "total_lines": 0,
            "total_sfx": 0,
            "story_body_duration_s": 0.0,
            "estimated_duration_s": 0.0,
            "warnings": warnings,
            "errors": errors,
        }
        return errors, warnings, summary

    # -- Rule 2: scene_id uniqueness and ascending order -----------------------
    scene_ids: list[int] = []
    for index, scene in enumerate(story_scenes, start=1):
        sid = scene.get("scene_id")
        if sid is not None:
            scene_ids.append(sid)

    seen_ids: set[int] = set()
    for sid in scene_ids:
        if sid in seen_ids:
            errors.append(f"duplicate scene_id {sid}")
        seen_ids.add(sid)

    if scene_ids != sorted(scene_ids):
        errors.append(f"scene_id values are not in ascending order: {scene_ids}")

    # -- Build lookup of valid scene IDs for SFX validation --------------------
    valid_scene_ids: set[int] = set(scene_ids)

    # -- Per-scene validation --------------------------------------------------
    total_lines = 0
    total_duration = 0.0

    for index, scene in enumerate(story_scenes, start=1):
        prefix = f"scene #{index}"

        # Rule 3: required fields
        sid = scene.get("scene_id")
        if sid is None or not isinstance(sid, int):
            errors.append(f"{prefix}: scene_id must be an int")

        title_es = scene.get("title_es")
        if not isinstance(title_es, str) or not title_es.strip():
            errors.append(f"{prefix}: title_es must be a non-empty string")

        title_ko = scene.get("title_ko")
        if not isinstance(title_ko, str) or not title_ko.strip():
            errors.append(f"{prefix}: title_ko must be a non-empty string")

        lines = scene.get("lines")
        if not isinstance(lines, list) or len(lines) == 0:
            errors.append(f"{prefix}: lines must be a non-empty list")
            continue

        # Rule 4: scene image_path & resolution check
        image_path = scene.get("image_path", "")
        if isinstance(image_path, str):
            if image_path == "":
                warnings.append(f"{prefix}: image_path is empty")
            else:
                img_file = Path(image_path)
                if img_file.suffix.lower() not in ALLOWED_IMAGE_EXT:
                    errors.append(
                        f"{prefix}: image_path extension {img_file.suffix!r} not in {sorted(ALLOWED_IMAGE_EXT)}"
                    )
                full_path = ROOT / image_path
                if not full_path.exists():
                    errors.append(f"{prefix}: image_path not found: {image_path}")
                else:
                    _check_image_file(prefix, img_file.suffix, full_path, warnings)

        # Rule 5: ambient_sfx & license
        ambient_sfx = scene.get("ambient_sfx", "")
        if isinstance(ambient_sfx, str) and ambient_sfx:
            sfx_p = Path(ambient_sfx)
            if sfx_p.suffix.lower() not in ALLOWED_AUDIO_EXT:
                errors.append(
                    f"{prefix}: ambient_sfx extension {sfx_p.suffix!r} not in {sorted(ALLOWED_AUDIO_EXT)}"
                )
            if not (ROOT / ambient_sfx).exists():
                errors.append(f"{prefix}: ambient_sfx not found: {ambient_sfx}")
            
            # Check license
            ambient_lic = scene.get("ambient_sfx_license", "")
            if not isinstance(ambient_lic, str) or not ambient_lic.strip():
                errors.append(f"{prefix}: ambient_sfx_license must be a non-empty string when ambient_sfx is specified")

        # Rule 6: validate each line
        scene_duration = 0.0
        for li, line in enumerate(lines, start=1):
            line_prefix = f"{prefix}, line #{li}"

            kind = line.get("kind")
            if not isinstance(kind, str):
                errors.append(f"{line_prefix}: kind must be a string")

            text_es = line.get("text_es")
            if not isinstance(text_es, str) or not text_es.strip():
                errors.append(f"{line_prefix}: text_es must be a non-empty string")

            text_ko = line.get("text_ko")
            if not isinstance(text_ko, str) or not text_ko.strip():
                errors.append(f"{line_prefix}: text_ko must be a non-empty string")

            # Check duration_s is optional, if present must be positive
            dur = line.get("duration_s")
            if dur is not None:
                if not isinstance(dur, (int, float)) or dur <= 0:
                    errors.append(f"{line_prefix}: duration_s must be a positive number")
            
            # Check min_hold_s and processing_pause_s
            min_hold = line.get("min_hold_s")
            if min_hold is not None:
                if not isinstance(min_hold, (int, float)) or min_hold <= 0:
                    errors.append(f"{line_prefix}: min_hold_s must be a positive number")
            
            proc_pause = line.get("processing_pause_s")
            if proc_pause is not None:
                if not isinstance(proc_pause, (int, float)) or proc_pause < 0:
                    errors.append(f"{line_prefix}: processing_pause_s must be a non-negative number")

            # Check line-level image_path override
            line_img = line.get("image_path")
            if line_img is not None:
                if not isinstance(line_img, str):
                    errors.append(f"{line_prefix}: image_path must be a string")
                elif line_img:
                    lf = Path(line_img)
                    if lf.suffix.lower() not in ALLOWED_IMAGE_EXT:
                        errors.append(
                            f"{line_prefix}: image_path extension {lf.suffix!r} not in {sorted(ALLOWED_IMAGE_EXT)}"
                        )
                    full_lf = ROOT / line_img
                    if not full_lf.exists():
                        errors.append(f"{line_prefix}: image_path not found: {line_img}")
                    else:
                        _check_image_file(line_prefix, lf.suffix, full_lf, warnings)

            # Statically estimate line duration for Scene duration bounds check (Rule 7)
            # Default pacing configurations: lead=0.25, tail=0.4, processing_pause=2.5, min_hold=2.5
            d_dur = float(dur) if dur is not None else 0.0
            l_min_hold = max(2.5, d_dur)
            min_hold_val = float(min_hold) if min_hold is not None else l_min_hold
            proc_pause_val = float(proc_pause) if proc_pause is not None else 2.5
            
            t_es = text_es or ""
            proxy = max(4.5, min(10.5, len(t_es) / 13.0))
            line_duration = max(proxy + 0.25 + 0.4 + proc_pause_val, min_hold_val)
            scene_duration += line_duration

            total_lines += 1

        # Rule 7: per-scene duration check (using static estimations)
        pause_s = scene.get("pause_s", 0)
        if isinstance(pause_s, (int, float)):
            scene_duration += pause_s

        if not (45 <= scene_duration <= 105):
            warnings.append(
                f"{prefix}: total estimated duration {scene_duration:.1f}s is outside 45-105s range"
            )

        total_duration += scene_duration

    # -- Rule 8: SFX manifest validation --------------------------------------
    total_sfx = 0
    if sfx_manifest is not None and len(sfx_manifest) > 0:
        total_sfx = len(sfx_manifest)
        for si, entry in enumerate(sfx_manifest, start=1):
            sfx_prefix = f"sfx #{si}"

            sfx_id = entry.get("id")
            if not isinstance(sfx_id, str):
                errors.append(f"{sfx_prefix}: id must be a string")

            kind = entry.get("kind")
            if kind != "spot":
                errors.append(f"{sfx_prefix}: kind must be 'spot'")

            sfx_path = entry.get("path")
            if not isinstance(sfx_path, str):
                errors.append(f"{sfx_prefix}: path must be a string")
            else:
                sp = Path(sfx_path)
                if sp.suffix.lower() not in ALLOWED_AUDIO_EXT:
                    errors.append(
                        f"{sfx_prefix}: path extension {sp.suffix!r} not in {sorted(ALLOWED_AUDIO_EXT)}"
                    )
                if not (ROOT / sfx_path).exists():
                    errors.append(f"{sfx_prefix}: path not found: {sfx_path}")

            sfx_license = entry.get("license")
            if not isinstance(sfx_license, str) or not sfx_license.strip():
                errors.append(f"{sfx_prefix}: license must be a non-empty string")

            sfx_scene_id = entry.get("scene_id")
            if not isinstance(sfx_scene_id, int):
                errors.append(f"{sfx_scene_id}: scene_id must be an int")
            elif sfx_scene_id not in valid_scene_ids:
                errors.append(f"{sfx_prefix}: scene_id {sfx_scene_id} does not reference an existing scene")
            else:
                # Validate line_index against the specified scene's lines
                scene_dict = next(s for s in story_scenes if s["scene_id"] == sfx_scene_id)
                num_lines = len(scene_dict.get("lines", []))
                line_idx = entry.get("line_index")
                if line_idx is not None:
                    if not isinstance(line_idx, int) or not (1 <= line_idx <= num_lines):
                        errors.append(
                            f"{sfx_prefix}: line_index {line_idx} is out of bounds (1-{num_lines}) for scene {sfx_scene_id}"
                        )

            # check offset_s or start_s
            offset_s = entry.get("offset_s", entry.get("start_s"))
            if offset_s is None or not isinstance(offset_s, (int, float)) or offset_s < 0:
                errors.append(f"{sfx_prefix}: offset_s (or start_s) must be a number >= 0")

            volume_db = entry.get("volume_db")
            if not isinstance(volume_db, (int, float)):
                errors.append(f"{sfx_prefix}: volume_db must be a number")

    # -- Rule 8b: out-of-scene segment SFX validation -------------------------
    # `segment_sfx` places sound on the structural segments (intro / montage /
    # outro) that have no scene_id and so cannot be reached by ambient beds or
    # the scene-anchored spot manifest.
    valid_segment_sfx_types = {"intro", "montage", "outro"}
    valid_segment_sfx_modes = {"bed", "spot"}
    total_segment_sfx = 0
    if segment_sfx is not None and len(segment_sfx) > 0:
        total_segment_sfx = len(segment_sfx)
        for si, entry in enumerate(segment_sfx, start=1):
            seg_prefix = f"segment_sfx #{si}"

            if not isinstance(entry.get("id"), str):
                errors.append(f"{seg_prefix}: id must be a string")

            seg_type = entry.get("segment_type")
            if seg_type not in valid_segment_sfx_types:
                errors.append(
                    f"{seg_prefix}: segment_type {seg_type!r} must be one of {sorted(valid_segment_sfx_types)}"
                )

            mode = entry.get("mode", "bed")
            if mode not in valid_segment_sfx_modes:
                errors.append(f"{seg_prefix}: mode {mode!r} must be one of {sorted(valid_segment_sfx_modes)}")

            seg_path = entry.get("path")
            if not isinstance(seg_path, str):
                errors.append(f"{seg_prefix}: path must be a string")
            else:
                sp = Path(seg_path)
                if sp.suffix.lower() not in ALLOWED_AUDIO_EXT:
                    errors.append(
                        f"{seg_prefix}: path extension {sp.suffix!r} not in {sorted(ALLOWED_AUDIO_EXT)}"
                    )
                if not (ROOT / seg_path).exists():
                    errors.append(f"{seg_prefix}: path not found: {seg_path}")

            seg_license = entry.get("license")
            if not isinstance(seg_license, str) or not seg_license.strip():
                errors.append(f"{seg_prefix}: license must be a non-empty string")

            offset_s = entry.get("offset_s", 0.0)
            if not isinstance(offset_s, (int, float)) or offset_s < 0:
                errors.append(f"{seg_prefix}: offset_s must be a number >= 0")

            seg_volume_db = entry.get("volume_db")
            if not isinstance(seg_volume_db, (int, float)):
                errors.append(f"{seg_prefix}: volume_db must be a number")

    # -- Rule 9: audio asset integrity (silence + duplicate placeholder scan) --
    # Collect every referenced, existing audio asset (ambient beds + spot SFX)
    # and flag silent or byte-identical clips -- the classic signature of
    # batch-generated placeholders that pass path/extension checks but carry no
    # real sound. These are errors so builds are blocked, and they surface loudly at
    # `make check` time, before any render.
    audio_refs: list[tuple[str, Path]] = []
    for index, scene in enumerate(story_scenes, start=1):
        amb = scene.get("ambient_sfx", "")
        if isinstance(amb, str) and amb:
            amb_path = ROOT / amb
            if amb_path.exists():
                audio_refs.append((f"scene #{index} ambient_sfx", amb_path))
    if sfx_manifest:
        for si, entry in enumerate(sfx_manifest, start=1):
            sp = entry.get("path")
            if isinstance(sp, str) and sp:
                spot_path = ROOT / sp
                if spot_path.exists():
                    eid = entry.get("id")
                    label = f"sfx #{si} ({eid})" if isinstance(eid, str) and eid else f"sfx #{si}"
                    audio_refs.append((label, spot_path))
    if segment_sfx:
        for si, entry in enumerate(segment_sfx, start=1):
            sp = entry.get("path")
            if isinstance(sp, str) and sp:
                seg_path = ROOT / sp
                if seg_path.exists():
                    eid = entry.get("id")
                    label = f"segment_sfx #{si} ({eid})" if isinstance(eid, str) and eid else f"segment_sfx #{si}"
                    audio_refs.append((label, seg_path))

    hash_to_labels: dict[str, list[str]] = {}
    for label, path in audio_refs:
        peak = audio_peak_dbfs(path)
        if peak is not None and peak <= SILENCE_PEAK_DBFS:
            errors.append(
                f"{label}: audio is effectively silent (peak {peak:.1f} dBFS) "
                f"-- placeholder, not a real sound effect?"
            )
        digest = file_md5(path)
        if digest:
            hash_to_labels.setdefault(digest, []).append(label)
    for labels in hash_to_labels.values():
        if len(labels) > 1:
            errors.append(
                f"identical audio content shared by {len(labels)} entries "
                f"(likely placeholders): {', '.join(labels)}"
            )

    # -- Build summary ---------------------------------------------------------
    # Estimated duration includes: total_duration + intro (16s) + outro (15s) + header slides (3s * number of scenes)
    intro_outro_headers = 16.0 + 15.0 + (3.0 * len(story_scenes))
    summary = {
        "scenes": len(story_scenes),
        "total_lines": total_lines,
        "total_sfx": total_sfx,
        "total_segment_sfx": total_segment_sfx,
        "story_body_duration_s": round(total_duration, 3),
        "estimated_duration_s": round(total_duration + intro_outro_headers, 3),
        "warnings": warnings,
        "errors": errors,
    }
    return errors, warnings, summary
