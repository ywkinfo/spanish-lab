"""Dispatch debug artifact generation by render type."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import segments as project_segments
from build.segment_adapter import RENDER_TYPE_CARDS, get_render_type


def run(script: str) -> None:
    subprocess.run([sys.executable, script], check=True)


def main() -> int:
    render_type = get_render_type(project_segments)
    if render_type == RENDER_TYPE_CARDS:
        scripts = ["checks/make_card_grid.py", "checks/make_card_subtitle_previews.py"]
    else:
        scripts = ["checks/make_overlay.py", "checks/make_contact_sheet.py", "checks/make_subtitle_previews.py"]
    for script in scripts:
        run(script)
    print(json.dumps({"ok": True, "render_type": render_type, "scripts": scripts}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
