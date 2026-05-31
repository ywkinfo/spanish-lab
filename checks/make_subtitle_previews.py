"""Render each subtitle overlay as a standalone PNG."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from build.camera import output_size_for_design  # noqa: E402
from build.subtitles import layout_subtitle, render_subtitle_image  # noqa: E402
from segments import DESIGN, SEGMENTS  # noqa: E402

OUTPUT_DIR = ROOT / "output" / "debug" / "subtitle_previews"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_size = output_size_for_design(DESIGN)
    details = []
    for index, segment in enumerate(SEGMENTS, start=1):
        output = OUTPUT_DIR / f"seg_{index:02d}.png"
        image = render_subtitle_image(segment["text"], video_size=output_size, design=DESIGN)
        image.save(output)
        layout = layout_subtitle(segment["text"], video_size=output_size, design=DESIGN)
        details.append(
            {
                "segment": index,
                "output": str(output),
                "font_size": layout.font_size,
                "lines": len(layout.lines),
            }
        )
    print(json.dumps({"ok": True, "outputs": details}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
