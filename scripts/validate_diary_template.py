#!/usr/bin/env python3
"""Structural validator for the _template_historia_diary.py file.

Performs static import checks and asserts required diary schema definitions,
bypassing path-existence or silence-detection checks.
"""

from __future__ import annotations

import sys
import py_compile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "projects" / "_template_historia_diary.py"


def main() -> int:
    print("Validating diary template syntax...")
    
    # 1. Compile Check
    try:
        py_compile.compile(str(TEMPLATE_PATH), doraise=True)
    except py_compile.PyCompileError as e:
        print(f"Error: Template failed to compile syntactically: {e}")
        return 1
        
    # 2. Schema Import & Structural Check
    sys.path.insert(0, str(ROOT))
    try:
        import projects._template_historia_diary as tmpl
    except Exception as e:
        print(f"Error: Failed to import template module: {e}")
        return 1

    # Assert required global parameters
    required_strings = [
        "DESCRIP_PATH", "OUTPUT_NAME", "PUBLIC_SLUG", 
        "SERIES", "SERIES_TITLE", "LEVEL", "LANGUAGE"
    ]
    for field in required_strings:
        assert hasattr(tmpl, field), f"Missing global field: {field}"
        assert isinstance(getattr(tmpl, field), str), f"Field {field} must be a string"

    assert hasattr(tmpl, "EPISODE") and isinstance(tmpl.EPISODE, int), "EPISODE must be an int"
    assert hasattr(tmpl, "RENDER_TYPE") and tmpl.RENDER_TYPE == "diary", "RENDER_TYPE must be 'diary'"

    # Assert STORY_SCENES schema
    assert hasattr(tmpl, "STORY_SCENES") and isinstance(tmpl.STORY_SCENES, list), "STORY_SCENES must be a list"
    assert len(tmpl.STORY_SCENES) == 8, f"STORY_SCENES must contain exactly 8 scenes, got {len(tmpl.STORY_SCENES)}"
    for idx, scene in enumerate(tmpl.STORY_SCENES, start=1):
        assert scene["scene_id"] == idx, f"Scene at index {idx-1} must have scene_id {idx}, got {scene['scene_id']}"
        for key in ["scene_id", "title_es", "title_ko", "pause_s", "lines"]:
            assert key in scene, f"Scene {idx} missing key: {key}"
        assert isinstance(scene["lines"], list) and len(scene["lines"]) > 0, f"Scene {idx} lines must be a non-empty list"

    # Assert SFX structures
    assert hasattr(tmpl, "SFX_MANIFEST") and isinstance(tmpl.SFX_MANIFEST, list), "SFX_MANIFEST must be a list"
    for idx, sfx in enumerate(tmpl.SFX_MANIFEST):
        for key in ["id", "kind", "scene_id", "line_index", "offset_s", "path", "volume_db", "license"]:
            assert key in sfx, f"SFX_MANIFEST item at index {idx} missing key: {key}"
        assert sfx["kind"] == "spot", f"SFX_MANIFEST item at index {idx} 'kind' must be 'spot', got {sfx['kind']}"
        assert isinstance(sfx["scene_id"], int), f"SFX_MANIFEST item {idx} scene_id must be int, got {type(sfx['scene_id'])}"
        assert isinstance(sfx["line_index"], int), f"SFX_MANIFEST item {idx} line_index must be int, got {type(sfx['line_index'])}"
        assert isinstance(sfx["offset_s"], (int, float)) and sfx["offset_s"] >= 0.0, f"SFX_MANIFEST item {idx} offset_s must be a non-negative number, got {sfx['offset_s']}"
        assert isinstance(sfx["volume_db"], (int, float)), f"SFX_MANIFEST item {idx} volume_db must be numeric, got {type(sfx['volume_db'])}"

    assert hasattr(tmpl, "SEGMENT_SFX") and isinstance(tmpl.SEGMENT_SFX, list), "SEGMENT_SFX must be a list"
    assert len(tmpl.SEGMENT_SFX) == 3, f"SEGMENT_SFX must contain exactly 3 items, got {len(tmpl.SEGMENT_SFX)}"
    seg_types = {item.get("segment_type") for item in tmpl.SEGMENT_SFX}
    expected_types = {"intro", "montage", "outro"}
    assert seg_types == expected_types, f"SEGMENT_SFX must cover exactly {expected_types}, got {seg_types}"
    for idx, item in enumerate(tmpl.SEGMENT_SFX):
        for key in ["id", "kind", "segment_type", "mode", "offset_s", "path", "volume_db", "license"]:
            assert key in item, f"SEGMENT_SFX item at index {idx} missing key: {key}"
        assert item["kind"] == "segment", f"SEGMENT_SFX item at index {idx} 'kind' must be 'segment', got {item['kind']}"
        assert item["segment_type"] in {"intro", "montage", "outro"}, f"SEGMENT_SFX item {idx} segment_type must be in {{intro, montage, outro}}, got {item['segment_type']}"
        assert item["mode"] in {"bed", "spot"}, f"SEGMENT_SFX item {idx} mode must be 'bed' or 'spot', got {item['mode']}"
        assert isinstance(item["offset_s"], (int, float)) and item["offset_s"] >= 0.0, f"SEGMENT_SFX item {idx} offset_s must be a non-negative number, got {item['offset_s']}"
        assert isinstance(item["volume_db"], (int, float)), f"SEGMENT_SFX item {idx} volume_db must be numeric, got {type(item['volume_db'])}"

    # Assert SEGMENTS & DESIGN & AUDIO
    assert hasattr(tmpl, "SEGMENTS") and isinstance(tmpl.SEGMENTS, list), "SEGMENTS must be a list"
    segments = tmpl.SEGMENTS
    
    # Check segment shapes
    assert len(segments) >= 27, f"SEGMENTS list is too short, got {len(segments)}"
    assert segments[0]["type"] == "intro", f"First segment must be 'intro', got {segments[0]['type']}"
    
    current_idx = 1
    for s_id in range(1, 9):
        # Expect scene_header
        assert current_idx < len(segments), f"Expected 'scene_header' for scene_id {s_id}, but reached end of SEGMENTS"
        assert segments[current_idx]["type"] == "scene_header", f"Expected segment {current_idx} to be 'scene_header', got {segments[current_idx]['type']}"
        assert segments[current_idx]["scene_id"] == s_id, f"Expected segment {current_idx} to reference scene_id {s_id}, got {segments[current_idx]['scene_id']}"
        current_idx += 1
        
        # Expect at least one diary_line
        has_line = False
        while current_idx < len(segments) and segments[current_idx]["type"] == "diary_line":
            assert segments[current_idx]["scene_id"] == s_id, f"Expected segment {current_idx} 'diary_line' to reference scene_id {s_id}, got {segments[current_idx]['scene_id']}"
            has_line = True
            current_idx += 1
        assert has_line, f"Scene {s_id} must have at least one 'diary_line' segment"
        
        # Expect pause
        assert current_idx < len(segments), f"Expected 'pause' for scene_id {s_id}, but reached end of SEGMENTS"
        assert segments[current_idx]["type"] == "pause", f"Expected segment {current_idx} to be 'pause', got {segments[current_idx]['type']}"
        assert segments[current_idx]["scene_id"] == s_id, f"Expected segment {current_idx} to reference scene_id {s_id}, got {segments[current_idx]['scene_id']}"
        current_idx += 1
        
    # Expect montage
    assert current_idx < len(segments), "Expected 'montage' segment, but reached end of SEGMENTS"
    assert segments[current_idx]["type"] == "montage", f"Expected segment {current_idx} to be 'montage', got {segments[current_idx]['type']}"
    current_idx += 1
    
    # Expect outro
    assert current_idx < len(segments), "Expected 'outro' segment, but reached end of SEGMENTS"
    assert segments[current_idx]["type"] == "outro", f"Expected segment {current_idx} to be 'outro', got {segments[current_idx]['type']}"
    current_idx += 1
    
    # Check no trailing segments
    assert current_idx == len(segments), f"Unexpected extra segments at the end: {segments[current_idx:]}"

    # Assert CHAPTERS references valid segment indexes and conforms to exact shape
    assert hasattr(tmpl, "CHAPTERS") and isinstance(tmpl.CHAPTERS, list), "CHAPTERS must be a list"
    assert len(tmpl.CHAPTERS) == 10, f"CHAPTERS must have exactly 10 chapters (intro + 8 scenes + outro), got {len(tmpl.CHAPTERS)}"
    
    scene_headers = [i + 1 for i, seg in enumerate(segments) if seg.get("type") == "scene_header"]
    assert len(scene_headers) == 8, f"Expected 8 scene headers in SEGMENTS, found {len(scene_headers)}"
    
    for idx, chap in enumerate(tmpl.CHAPTERS):
        for key in ["segment", "title"]:
            assert key in chap, f"Chapter index {idx} missing key: {key}"
        seg_num = chap["segment"]
        assert isinstance(seg_num, int), f"Chapter segment index must be an integer, got {type(seg_num)}"
        
    assert tmpl.CHAPTERS[0]["segment"] == 1, f"First chapter must point to segment 1, got {tmpl.CHAPTERS[0]['segment']}"
    for s_id in range(1, 9):
        expected_seg = scene_headers[s_id - 1]
        assert tmpl.CHAPTERS[s_id]["segment"] == expected_seg, f"Chapter {s_id} for scene {s_id} must point to segment {expected_seg}, got {tmpl.CHAPTERS[s_id]['segment']}"
    assert tmpl.CHAPTERS[9]["segment"] == len(segments), f"Last chapter must point to final segment {len(segments)}, got {tmpl.CHAPTERS[9]['segment']}"

    assert hasattr(tmpl, "DESIGN") and isinstance(tmpl.DESIGN, dict), "DESIGN must be a dict"
    assert hasattr(tmpl, "AUDIO") and isinstance(tmpl.AUDIO, dict), "AUDIO must be a dict"
    
    print("Diary template validation successful. (Syntax + Schema OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
