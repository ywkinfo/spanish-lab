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
    assert len(tmpl.STORY_SCENES) > 0, "STORY_SCENES must not be empty"
    scene = tmpl.STORY_SCENES[0]
    for key in ["scene_id", "title_es", "title_ko", "pause_s", "lines"]:
        assert key in scene, f"Scene missing key: {key}"
    assert isinstance(scene["lines"], list) and len(scene["lines"]) > 0, "Scene lines must be a non-empty list"

    # Assert SFX structures
    assert hasattr(tmpl, "SFX_MANIFEST") and isinstance(tmpl.SFX_MANIFEST, list), "SFX_MANIFEST must be a list"
    if tmpl.SFX_MANIFEST:
        sfx = tmpl.SFX_MANIFEST[0]
        for key in ["id", "kind", "scene_id", "path", "volume_db"]:
            assert key in sfx, f"SFX_MANIFEST missing key: {key}"

    assert hasattr(tmpl, "SEGMENT_SFX") and isinstance(tmpl.SEGMENT_SFX, list), "SEGMENT_SFX must be a list"
    if tmpl.SEGMENT_SFX:
        seg_sfx = tmpl.SEGMENT_SFX[0]
        for key in ["id", "kind", "segment_type", "mode", "path", "volume_db"]:
            assert key in seg_sfx, f"SEGMENT_SFX missing key: {key}"

    # Assert SEGMENTS & DESIGN & AUDIO
    assert hasattr(tmpl, "SEGMENTS") and isinstance(tmpl.SEGMENTS, list), "SEGMENTS must be a list"
    assert hasattr(tmpl, "DESIGN") and isinstance(tmpl.DESIGN, dict), "DESIGN must be a dict"
    assert hasattr(tmpl, "AUDIO") and isinstance(tmpl.AUDIO, dict), "AUDIO must be a dict"
    
    print("Diary template validation successful. (Syntax + Schema OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
