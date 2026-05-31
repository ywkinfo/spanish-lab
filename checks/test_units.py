"""Unit tests for the video generation helpers."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
import warnings
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from PIL import Image, ImageDraw  # noqa: E402

from build.design import apply_grade, ease_in_out_cubic, letter_spaced_width  # noqa: E402
from build.easing import ease_in_out_quad  # noqa: E402
from build.publish import (  # noqa: E402
    decision_log_name,
    format_timestamp,
    make_description,
    thumbnail_prefix,
    validate_chapters,
    versioned_prefix,
    write_decision_snapshot,
)
from build.audio import assert_tts_fits_timeline, build_tts_command, mix_sfx_layer  # noqa: E402
from build.segment_adapter import (  # noqa: E402
    RENDER_TYPE_CARDS,
    RENDER_TYPE_KENBURNS,
    description_text,
    display_text,
    narration_text,
)
from build.subtitles import layout_subtitle, load_font  # noqa: E402
from build.timeline import duration_for_text, segment_duration  # noqa: E402
from segments import EPISODE, OUTPUT_NAME, RENDER_VERSION, SERIES  # noqa: E402


class EasingTests(unittest.TestCase):
    def test_boundaries(self) -> None:
        self.assertEqual(ease_in_out_quad(0), 0)
        self.assertEqual(ease_in_out_quad(1), 1)

    def test_monotonic(self) -> None:
        values = [ease_in_out_quad(i / 20) for i in range(21)]
        self.assertEqual(values, sorted(values))


class EaseInOutCubicTests(unittest.TestCase):
    def test_boundaries(self) -> None:
        self.assertEqual(ease_in_out_cubic(0), 0)
        self.assertEqual(ease_in_out_cubic(1), 1)

    def test_midpoint_and_monotonic(self) -> None:
        self.assertAlmostEqual(ease_in_out_cubic(0.5), 0.5)
        values = [ease_in_out_cubic(i / 20) for i in range(21)]
        self.assertEqual(values, sorted(values))


class DurationTests(unittest.TestCase):
    def test_clamps_short_text(self) -> None:
        self.assertEqual(duration_for_text("hola"), 4.5)

    def test_mid_length_text(self) -> None:
        text = "x" * 78
        self.assertAlmostEqual(duration_for_text(text), 6.0)

    def test_clamps_long_text(self) -> None:
        text = "x" * 300
        self.assertEqual(duration_for_text(text), 10.5)

    def test_explicit_segment_duration_wins(self) -> None:
        segment = {"text": "hola", "duration_s": 12}
        self.assertEqual(segment_duration(segment, 1, {1: 1.0}, {"min_duration_s": 4}), 12.0)

    def test_tts_duration_preserves_readability_floor(self) -> None:
        segment = {"text": "x" * 78}
        audio_cfg = {"lead_padding_s": 0.2, "tail_padding_s": 0.3, "readability_floor_ratio": 0.9}
        self.assertAlmostEqual(segment_duration(segment, 1, {1: 2.0}, audio_cfg), 5.4)

    def test_tts_duration_extends_long_speech(self) -> None:
        segment = {"text": "hola"}
        audio_cfg = {"lead_padding_s": 0.2, "tail_padding_s": 0.3, "min_duration_s": 4.0}
        self.assertAlmostEqual(segment_duration(segment, 1, {1: 8.0}, audio_cfg), 8.5)


class SubtitleTests(unittest.TestCase):
    def test_long_spanish_sentence_fits_two_lines(self) -> None:
        text = (
            "A través de los grandes ventanales se ven los tejados y las cúpulas "
            "de los edificios clásicos de la ciudad."
        )
        layout = layout_subtitle(text)
        self.assertLessEqual(len(layout.lines), 2)
        self.assertGreaterEqual(layout.font_size, 21)


class ApplyGradeTests(unittest.TestCase):
    def test_preserves_size_and_mode(self) -> None:
        image = Image.new("RGB", (4, 3), (100, 120, 140))
        graded = apply_grade(image, {"saturation": 1.1, "contrast": 1.05, "warmth": 6})
        self.assertEqual(graded.size, image.size)
        self.assertEqual(graded.mode, "RGB")


class LetterSpacingTests(unittest.TestCase):
    def test_spacing_increases_measured_width(self) -> None:
        scratch = Image.new("RGBA", (300, 80), (0, 0, 0, 0))
        draw = ImageDraw.Draw(scratch)
        font = load_font(24)
        compact = letter_spaced_width(draw, "mercado", font, 0.0)
        spaced = letter_spaced_width(draw, "mercado", font, 2.0)
        self.assertGreater(spaced, compact)


class PublishNamingTests(unittest.TestCase):
    def test_versioned_prefix_uses_publish_metadata(self) -> None:
        expected = f"{SERIES}-ep{int(EPISODE):02d}-{OUTPUT_NAME}-16x9-v{int(RENDER_VERSION)}"
        self.assertEqual(versioned_prefix(), expected)

    def test_thumbnail_prefix_omits_aspect_and_version(self) -> None:
        expected = f"{SERIES}-ep{int(EPISODE):02d}-{OUTPUT_NAME}"
        self.assertEqual(thumbnail_prefix(), expected)

    def test_format_timestamp(self) -> None:
        self.assertEqual(format_timestamp(0), "0:00")
        self.assertEqual(format_timestamp(65.9), "1:05")
        self.assertEqual(format_timestamp(3661), "1:01:01")

    def test_chapter_validation_rejects_short_chapter(self) -> None:
        chapters = [
            {"start_s": 0.0, "title": "A"},
            {"start_s": 9.9, "title": "B"},
            {"start_s": 20.0, "title": "C"},
        ]
        with self.assertRaisesRegex(RuntimeError, "at least 10 seconds"):
            validate_chapters(chapters, 40.0)


class PublishDecisionLogTests(unittest.TestCase):
    def test_decision_log_name_uses_episode_and_slug(self) -> None:
        self.assertEqual(decision_log_name(5, "plaza-mayor"), "ep05-plaza-mayor.jsonl")

    def test_decision_snapshot_copies_events_without_mutating_log(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            log = root / "ep05-plaza-mayor.jsonl"
            before = (
                json.dumps({"event": "greenlight", "candidate": "plaza-mayor"}, ensure_ascii=False) + "\n"
                + json.dumps({"event": "preview_review", "verdict": "approved"}, ensure_ascii=False) + "\n"
            )
            log.write_text(before, encoding="utf-8")
            snapshot = root / "descripcion-ep05-plaza-mayor-16x9-v1-decisions.json"

            self.assertTrue(write_decision_snapshot(snapshot, log, episode=5, slug="plaza-mayor"))

            payload = json.loads(snapshot.read_text(encoding="utf-8"))
            self.assertEqual(payload["episode"], 5)
            self.assertEqual(payload["slug"], "plaza-mayor")
            self.assertEqual([event["event"] for event in payload["events"]], ["greenlight", "preview_review"])
            self.assertEqual(log.read_text(encoding="utf-8"), before)

    def test_missing_decision_log_warns_without_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            snapshot = root / "snapshot.json"
            missing_log = root / "missing.jsonl"
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                self.assertFalse(write_decision_snapshot(snapshot, missing_log, episode=5, slug="missing"))

            self.assertFalse(snapshot.exists())
            self.assertTrue(any("decision log not found" in str(warning.message) for warning in caught))


class PublishDescriptionTests(unittest.TestCase):
    def test_make_description_includes_optional_korean_teaser(self) -> None:
        description = make_description([], teaser="한국어 티저")

        self.assertIn("한국어 티저", description)
        self.assertLess(description.index("한국어 티저"), description.index("Guion del video:"))


class SegmentAdapterTests(unittest.TestCase):
    def test_kenburns_narration_preserves_text_for_hashes(self) -> None:
        segment = {"text": "La escena se desarrolla en Madrid."}
        self.assertEqual(narration_text(segment, RENDER_TYPE_KENBURNS), segment["text"])

    def test_card_phrase_narration(self) -> None:
        segment = {"type": "phrase", "frase_num": 1, "text_es": "Hola.", "text_ko": "안녕하세요."}
        self.assertEqual(narration_text(segment, RENDER_TYPE_CARDS), "Frase número 1. Hola. Repite conmigo. Hola.")

    def test_card_description_text(self) -> None:
        segment = {"type": "phrase", "frase_num": 1, "text_es": "Hola.", "text_ko": "안녕하세요."}
        self.assertEqual(description_text(segment, RENDER_TYPE_CARDS), "01. Hola. — 안녕하세요.")

    def test_card_display_text(self) -> None:
        segment = {"type": "phrase", "frase_num": 1, "text_es": "Hola.", "text_ko": "안녕하세요."}
        self.assertEqual(display_text(segment, RENDER_TYPE_CARDS), "#01 Hola. / 안녕하세요.")


class AudioSynthesisTests(unittest.TestCase):
    def test_tts_overlap_guard_rejects_audio_longer_than_card(self) -> None:
        seg_audios = [{"index": 1, "duration_s": 17.88}]
        timings = [SimpleNamespace(index=1, start_s=0.0, end_s=12.0)]

        with self.assertRaisesRegex(ValueError, "overlaps following segment"):
            assert_tts_fits_timeline(seg_audios, timings, {"lead_padding_s": 0.2})

    def test_tts_overlap_guard_accepts_audio_inside_card(self) -> None:
        seg_audios = [{"index": 1, "duration_s": 9.528}]
        timings = [SimpleNamespace(index=1, start_s=0.0, end_s=12.0)]

        assert_tts_fits_timeline(seg_audios, timings, {"lead_padding_s": 0.2})

    def test_flite_tts_command_uses_text_file_and_ffmpeg_filter(self) -> None:
        out_path = Path("output/audio/tts/seg_01_test.wav")
        text_path = Path("output/audio/tts/seg_01_test.txt")

        command = build_tts_command(
            text="Hola, ¿cómo estás?",
            out_path=out_path,
            text_path=text_path,
            audio_cfg={"tts_engine": "flite", "flite_voice": "slt"},
        )

        self.assertEqual(command[0], "ffmpeg")
        self.assertTrue(any(f"textfile={text_path}" in part for part in command))
        self.assertTrue(any("voice=slt" in part for part in command))
        self.assertEqual(command[-1], str(out_path))

    def test_edge_tts_command_uses_spanish_voice_and_media_output(self) -> None:
        out_path = Path("output/audio/tts/seg_01_test.mp3")
        text_path = Path("output/audio/tts/seg_01_test.txt")

        command = build_tts_command(
            text="Hola, ¿cómo estás?",
            out_path=out_path,
            text_path=text_path,
            audio_cfg={"tts_engine": "edge", "edge_voice": "es-ES-ElviraNeural", "edge_rate": "-10%"},
        )

        self.assertIn("edge_tts", command)
        self.assertIn("--voice", command)
        self.assertIn("es-ES-ElviraNeural", command)
        self.assertIn("--write-media", command)
        self.assertIn(str(out_path), command)
        self.assertIn("--rate=-10%", command)

    def test_mix_sfx_layer_empty_manifest_copies_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            narration = root / "narration.wav"
            narration.write_text("dummy wave content")
            out = root / "mixed.wav"

            mix_sfx_layer(narration, None, [], 10.0, out)
            self.assertTrue(out.exists())
            self.assertEqual(out.read_text(), "dummy wave content")


class CardRendererTests(unittest.TestCase):
    def test_outro_korean_line_uses_korean_font(self) -> None:
        from build import render_cards

        calls = []

        def fake_font(path, size, index=0):
            return {"path": path, "size": size, "index": index}

        def fake_fit_lines(text, *, font_path, font_index, start_size, **_kwargs):
            return [text], {"path": font_path, "size": start_size, "index": font_index}, start_size

        def fake_draw_centered_lines(_draw, lines, font, y, width, fill, spacing):
            calls.append({"lines": list(lines), "font": font})
            return y + 40

        design = {
            "output_size": (1280, 720),
            "background_color": (248, 247, 242),
            "text_color": (31, 35, 40),
            "muted_text_color": (96, 101, 109),
            "font_path": "latin-font",
            "font_path_ko": "korean-font",
            "font_index": 0,
            "font_index_ko": 0,
            "font_size_ko": 36,
        }
        segment = {
            "type": "outro",
            "text_es": "Muy bien. Ya tienes 50 frases útiles para empezar a hablar español.",
            "color_block": "neutral",
        }

        with (
            patch.object(render_cards, "_font", side_effect=fake_font),
            patch.object(render_cards, "_fit_lines", side_effect=fake_fit_lines),
            patch.object(render_cards, "_draw_centered_lines", side_effect=fake_draw_centered_lines),
        ):
            render_cards.render_card_image(segment, None, design)

        korean_calls = [call for call in calls if call["lines"] == ["다음 영상에서 또 연습해요"]]
        self.assertEqual(len(korean_calls), 1)
        self.assertEqual(korean_calls[0]["font"]["path"], "korean-font")

    def test_cards_smoke_render(self) -> None:
        from projects import como_estas_a1
        from build.render_cards import render_card_image

        rendered_types = set()
        for segment in como_estas_a1.SEGMENTS:
            segment_type = segment.get("type")
            if segment_type in rendered_types:
                continue
            image = render_card_image(segment, None, como_estas_a1.DESIGN)
            self.assertEqual(image.size, (1280, 720))
            rendered_types.add(segment_type)

        self.assertIn("intro", rendered_types)
        self.assertIn("block_header", rendered_types)
        self.assertIn("phrase", rendered_types)
        self.assertIn("outro", rendered_types)



class MetadataValidatorTests(unittest.TestCase):
    def test_valid_historia_a1_metadata_passes(self) -> None:
        from checks.validate_segments import validate_metadata

        with (
            patch("checks.validate_segments.SERIES", "historia-a1"),
            patch("checks.validate_segments.RENDER_TYPE", "cards"),
            patch("checks.validate_segments.LANGUAGE", "es"),
            patch("checks.validate_segments.PUBLIC_SLUG", "historia-a1-un-dia-de-lucia"),
            patch("checks.validate_segments.OUTPUT_NAME", "historia-un-dia-de-lucia"),
            patch("checks.validate_segments.SERIES_TITLE", "Español A1 -- Mini-historias"),
            patch("checks.validate_segments.YOUTUBE_TITLE", "Un día de Lucía"),
            patch("checks.validate_segments.DESCRIPTION_INTRO", "Sigue un día..."),
            patch("checks.validate_segments.DESCRIPTION_OUTRO", "Vuelve a ver..."),
            patch("checks.validate_segments.KOREAN_TEASER", "한국어 티저"),
            patch("checks.validate_segments.EPISODE", 1),
            patch("checks.validate_segments.RENDER_VERSION", 4),
            patch("checks.validate_segments.PHRASES", [(1, "a", "b", "c")]),
            patch("checks.validate_segments.BLOCKS", [{"start": 1}]),
            patch("checks.validate_segments.CHAPTERS", [{"segment": 1}]),
            patch("checks.validate_segments.MINI_QUIZ", [("q1", "a1"), ("q2", "a2"), ("q3", "a3"), ("q4", "a4"), ("q5", "a5")]),
            patch("checks.validate_segments.BASE_TAGS", ["tag"]),
            patch("checks.validate_segments.EXTRA_TAGS", ["tag"]),
            patch("checks.validate_segments.BASE_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.EXTRA_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.DESCRIP_PATH", "historia-a1-un-dia-de-lucia/descrip.md"),
        ):
            errors = validate_metadata()
            self.assertEqual(errors, [])

    def test_missing_korean_teaser_fails(self) -> None:
        from checks.validate_segments import validate_metadata

        with (
            patch("checks.validate_segments.SERIES", "historia-a1"),
            patch("checks.validate_segments.RENDER_TYPE", "cards"),
            patch("checks.validate_segments.LANGUAGE", "es"),
            patch("checks.validate_segments.PUBLIC_SLUG", "historia-a1-un-dia-de-lucia"),
            patch("checks.validate_segments.OUTPUT_NAME", "historia-un-dia-de-lucia"),
            patch("checks.validate_segments.SERIES_TITLE", "Español A1 -- Mini-historias"),
            patch("checks.validate_segments.YOUTUBE_TITLE", "Un día de Lucía"),
            patch("checks.validate_segments.DESCRIPTION_INTRO", "Sigue un día..."),
            patch("checks.validate_segments.DESCRIPTION_OUTRO", "Vuelve a ver..."),
            patch("checks.validate_segments.KOREAN_TEASER", ""),  # missing
            patch("checks.validate_segments.EPISODE", 1),
            patch("checks.validate_segments.RENDER_VERSION", 4),
            patch("checks.validate_segments.PHRASES", [(1, "a", "b", "c")]),
            patch("checks.validate_segments.BLOCKS", [{"start": 1}]),
            patch("checks.validate_segments.CHAPTERS", [{"segment": 1}]),
            patch("checks.validate_segments.MINI_QUIZ", [("q1", "a1"), ("q2", "a2"), ("q3", "a3"), ("q4", "a4"), ("q5", "a5")]),
            patch("checks.validate_segments.BASE_TAGS", ["tag"]),
            patch("checks.validate_segments.EXTRA_TAGS", ["tag"]),
            patch("checks.validate_segments.BASE_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.EXTRA_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.DESCRIP_PATH", "historia-a1-un-dia-de-lucia/descrip.md"),
        ):
            errors = validate_metadata()
            self.assertTrue(any("KOREAN_TEASER" in err for err in errors))

    def test_mismatched_public_slug_fails(self) -> None:
        from checks.validate_segments import validate_metadata

        with (
            patch("checks.validate_segments.SERIES", "historia-a1"),
            patch("checks.validate_segments.RENDER_TYPE", "cards"),
            patch("checks.validate_segments.LANGUAGE", "es"),
            patch("checks.validate_segments.PUBLIC_SLUG", "mismatched-slug"),  # mismatch
            patch("checks.validate_segments.OUTPUT_NAME", "historia-un-dia-de-lucia"),
            patch("checks.validate_segments.SERIES_TITLE", "Español A1 -- Mini-historias"),
            patch("checks.validate_segments.YOUTUBE_TITLE", "Un día de Lucía"),
            patch("checks.validate_segments.DESCRIPTION_INTRO", "Sigue un día..."),
            patch("checks.validate_segments.DESCRIPTION_OUTRO", "Vuelve a ver..."),
            patch("checks.validate_segments.KOREAN_TEASER", "한국어 티저"),
            patch("checks.validate_segments.EPISODE", 1),
            patch("checks.validate_segments.RENDER_VERSION", 4),
            patch("checks.validate_segments.PHRASES", [(1, "a", "b", "c")]),
            patch("checks.validate_segments.BLOCKS", [{"start": 1}]),
            patch("checks.validate_segments.CHAPTERS", [{"segment": 1}]),
            patch("checks.validate_segments.MINI_QUIZ", [("q1", "a1"), ("q2", "a2"), ("q3", "a3"), ("q4", "a4"), ("q5", "a5")]),
            patch("checks.validate_segments.BASE_TAGS", ["tag"]),
            patch("checks.validate_segments.EXTRA_TAGS", ["tag"]),
            patch("checks.validate_segments.BASE_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.EXTRA_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.DESCRIP_PATH", "historia-a1-un-dia-de-lucia/descrip.md"),
        ):
            errors = validate_metadata()
            self.assertTrue(any("PUBLIC_SLUG" in err and "match" in err for err in errors))

    def test_invalid_mini_quiz_count_fails(self) -> None:
        from checks.validate_segments import validate_metadata

        with (
            patch("checks.validate_segments.SERIES", "historia-a1"),
            patch("checks.validate_segments.RENDER_TYPE", "cards"),
            patch("checks.validate_segments.LANGUAGE", "es"),
            patch("checks.validate_segments.PUBLIC_SLUG", "historia-a1-un-dia-de-lucia"),
            patch("checks.validate_segments.OUTPUT_NAME", "historia-un-dia-de-lucia"),
            patch("checks.validate_segments.SERIES_TITLE", "Español A1 -- Mini-historias"),
            patch("checks.validate_segments.YOUTUBE_TITLE", "Un día de Lucía"),
            patch("checks.validate_segments.DESCRIPTION_INTRO", "Sigue un día..."),
            patch("checks.validate_segments.DESCRIPTION_OUTRO", "Vuelve a ver..."),
            patch("checks.validate_segments.KOREAN_TEASER", "한국어 티저"),
            patch("checks.validate_segments.EPISODE", 1),
            patch("checks.validate_segments.RENDER_VERSION", 4),
            patch("checks.validate_segments.PHRASES", [(1, "a", "b", "c")]),
            patch("checks.validate_segments.BLOCKS", [{"start": 1}]),
            patch("checks.validate_segments.CHAPTERS", [{"segment": 1}]),
            patch("checks.validate_segments.MINI_QUIZ", [("q1", "a1"), ("q2", "a2")]),  # only 2 questions, should be 5
            patch("checks.validate_segments.BASE_TAGS", ["tag"]),
            patch("checks.validate_segments.EXTRA_TAGS", ["tag"]),
            patch("checks.validate_segments.BASE_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.EXTRA_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.DESCRIP_PATH", "historia-a1-un-dia-de-lucia/descrip.md"),
        ):
            errors = validate_metadata()
            self.assertTrue(any("MINI_QUIZ" in err and "5 questions" in err for err in errors))

    def test_valid_historia_a1_diary_metadata_passes(self) -> None:
        from checks.validate_segments import validate_metadata

        with (
            patch("checks.validate_segments.SERIES", "historia-a1"),
            patch("checks.validate_segments.RENDER_TYPE", "diary"),
            patch("checks.validate_segments.LANGUAGE", "es"),
            patch("checks.validate_segments.PUBLIC_SLUG", "historia-a1-un-dia-de-lucia"),
            patch("checks.validate_segments.OUTPUT_NAME", "historia-un-dia-de-lucia"),
            patch("checks.validate_segments.SERIES_TITLE", "Español A1 -- Mini-historias"),
            patch("checks.validate_segments.YOUTUBE_TITLE", "Un día de Lucía"),
            patch("checks.validate_segments.DESCRIPTION_INTRO", "Sigue un día..."),
            patch("checks.validate_segments.DESCRIPTION_OUTRO", "Vuelve a ver..."),
            patch("checks.validate_segments.KOREAN_TEASER", "한국어 티저"),
            patch("checks.validate_segments.EPISODE", 1),
            patch("checks.validate_segments.RENDER_VERSION", 5),
            patch("checks.validate_segments.STORY_SCENES", [{"scene_id": 1, "title_es": "a", "title_ko": "b", "lines": []}]),
            patch("checks.validate_segments.CHAPTERS", [{"segment": 1}]),
            patch("checks.validate_segments.MINI_QUIZ", [("q1", "a1"), ("q2", "a2"), ("q3", "a3"), ("q4", "a4"), ("q5", "a5")]),
            patch("checks.validate_segments.BASE_TAGS", ["tag"]),
            patch("checks.validate_segments.EXTRA_TAGS", ["tag"]),
            patch("checks.validate_segments.BASE_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.EXTRA_HASHTAGS", ["#tag"]),
            patch("checks.validate_segments.DESCRIP_PATH", "historia-a1-un-dia-de-lucia/descrip.md"),
        ):
            errors = validate_metadata()
            self.assertEqual(errors, [])

    def test_non_historia_series_skips_validation(self) -> None:
        from checks.validate_segments import validate_metadata

        with (
            patch("checks.validate_segments.SERIES", "frases-a1"),
            patch("checks.validate_segments.PUBLIC_SLUG", ""),
        ):
            errors = validate_metadata()
            self.assertEqual(errors, [])


class DiaryValidatorTests(unittest.TestCase):
    def test_valid_diary_data_passes(self) -> None:
        from checks.validate_diary import validate as validate_diary
        story_scenes = [
            {
                "scene_id": 1,
                "title_es": "Escena 1",
                "title_ko": "장면 1",
                "image_path": "",
                "ambient_sfx": "",
                "pause_s": 5.0,
                "lines": [
                    {"kind": "narration", "speaker": "", "text_es": "Hola", "text_ko": "안녕", "duration_s": 40.0}
                ]
            }
        ]
        errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, ["scene #1: image_path is empty"])
        self.assertEqual(summary["scenes"], 1)

    def test_duplicate_scene_id_fails(self) -> None:
        from checks.validate_diary import validate as validate_diary
        story_scenes = [
            {
                "scene_id": 1,
                "title_es": "Escena 1",
                "title_ko": "장면 1",
                "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B", "duration_s": 50.0}]
            },
            {
                "scene_id": 1,
                "title_es": "Escena 2",
                "title_ko": "장면 2",
                "lines": [{"kind": "narration", "speaker": "", "text_es": "C", "text_ko": "D", "duration_s": 50.0}]
            }
        ]
        errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
        self.assertIn("duplicate scene_id 1", errors)

    def test_invalid_line_duration_fails(self) -> None:
        from checks.validate_diary import validate as validate_diary
        story_scenes = [
            {
                "scene_id": 1,
                "title_es": "Escena 1",
                "title_ko": "장면 1",
                "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B", "duration_s": -1.0}]
            }
        ]
        errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
        self.assertTrue(any("duration_s must be a positive number" in err for err in errors))

    def test_ambient_sfx_requires_license(self) -> None:
        from checks.validate_diary import validate as validate_diary
        story_scenes = [
            {
                "scene_id": 1,
                "title_es": "Escena 1",
                "title_ko": "장면 1",
                "ambient_sfx": "assets/audio/sfx/madrid_morning.wav",
                "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B"}]
            }
        ]
        errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
        self.assertTrue(any("ambient_sfx_license must be a non-empty string" in err for err in errors))

    def test_spot_sfx_checks_bounds(self) -> None:
        from checks.validate_diary import validate as validate_diary
        story_scenes = [
            {
                "scene_id": 1,
                "title_es": "Escena 1",
                "title_ko": "장면 1",
                "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B"}]
            }
        ]
        sfx_manifest = [
            {
                "id": "spot1",
                "kind": "spot",
                "scene_id": 1,
                "line_index": 5, # out of bounds
                "offset_s": 0.0,
                "path": "assets/audio/sfx/door_close_footsteps.wav",
                "volume_db": -12.0,
                "license": "CC0"
            }
        ]
        errors, warnings, summary = validate_diary(story_scenes, sfx_manifest, {}, "descrip.md")
        self.assertTrue(any("line_index 5 is out of bounds" in err for err in errors))

    def test_low_resolution_image_warns(self) -> None:
        # Proves the Pillow-based size guard actually fires (the previous
        # hand-rolled parser returned None on some files, silently passing).
        from checks.validate_diary import validate as validate_diary
        with tempfile.TemporaryDirectory() as tmp:
            img_path = Path(tmp) / "tiny.png"
            Image.new("RGB", (100, 100), (120, 120, 120)).save(img_path, format="PNG")
            story_scenes = [
                {
                    "scene_id": 1, "title_es": "Escena 1", "title_ko": "장면 1",
                    "image_path": str(img_path), "ambient_sfx": "", "pause_s": 5.0,
                    "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B", "duration_s": 40.0}],
                }
            ]
            errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
            self.assertEqual(errors, [])
            self.assertTrue(any("below the recommended minimum of 1600x900" in w for w in warnings))

    def test_image_format_extension_mismatch_warns(self) -> None:
        # A JPEG saved with a .png extension must be flagged (the real defect:
        # the FLUX scene images are JPEG content behind .png names).
        from checks.validate_diary import validate as validate_diary
        with tempfile.TemporaryDirectory() as tmp:
            img_path = Path(tmp) / "scene.png"
            Image.new("RGB", (1600, 900), (120, 120, 120)).save(img_path, format="JPEG")
            story_scenes = [
                {
                    "scene_id": 1, "title_es": "Escena 1", "title_ko": "장면 1",
                    "image_path": str(img_path), "ambient_sfx": "", "pause_s": 5.0,
                    "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B", "duration_s": 40.0}],
                }
            ]
            errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
            self.assertEqual(errors, [])
            self.assertTrue(any("but has a .png extension" in w for w in warnings))

    def test_silent_audio_warns(self) -> None:
        import wave
        from array import array as _array
        from checks.validate_diary import validate as validate_diary
        with tempfile.TemporaryDirectory() as tmp:
            wav_path = Path(tmp) / "ambient.wav"
            with wave.open(str(wav_path), "wb") as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(44100)
                wav.writeframes(_array("h", [0] * 4410).tobytes())
            story_scenes = [
                {
                    "scene_id": 1, "title_es": "Escena 1", "title_ko": "장면 1",
                    "image_path": "", "ambient_sfx": str(wav_path),
                    "ambient_sfx_license": "CC0", "pause_s": 5.0,
                    "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B", "duration_s": 40.0}],
                }
            ]
            errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
            other_errors = [e for e in errors if "effectively silent" not in e]
            self.assertEqual(other_errors, [])
            self.assertTrue(any("effectively silent" in e for e in errors))

    def test_duplicate_audio_content_warns(self) -> None:
        import wave
        from array import array as _array
        from checks.validate_diary import validate as validate_diary
        with tempfile.TemporaryDirectory() as tmp:
            payload = _array("h", [10000] * 4410).tobytes()  # non-silent
            paths = [Path(tmp) / "a.wav", Path(tmp) / "b.wav"]
            for path in paths:
                with wave.open(str(path), "wb") as wav:
                    wav.setnchannels(1)
                    wav.setsampwidth(2)
                    wav.setframerate(44100)
                    wav.writeframes(payload)
            story_scenes = [
                {
                    "scene_id": 1, "title_es": "Escena 1", "title_ko": "장면 1",
                    "image_path": "", "ambient_sfx": str(paths[0]),
                    "ambient_sfx_license": "CC0", "pause_s": 5.0,
                    "lines": [{"kind": "narration", "speaker": "", "text_es": "A", "text_ko": "B", "duration_s": 40.0}],
                },
                {
                    "scene_id": 2, "title_es": "Escena 2", "title_ko": "장면 2",
                    "image_path": "", "ambient_sfx": str(paths[1]),
                    "ambient_sfx_license": "CC0", "pause_s": 5.0,
                    "lines": [{"kind": "narration", "speaker": "", "text_es": "C", "text_ko": "D", "duration_s": 40.0}],
                },
            ]
            errors, warnings, summary = validate_diary(story_scenes, None, {}, "descrip.md")
            other_errors = [e for e in errors if "identical audio content shared" not in e]
            self.assertEqual(other_errors, [])
            self.assertTrue(any("identical audio content shared by 2 entries" in e for e in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
