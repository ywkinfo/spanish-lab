"""Package segment text and image metadata for frame proposal tools."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from segments import IMAGE_PATH, OUTPUT_NAME, SEGMENTS  # noqa: E402

OUTPUT_PATH = ROOT / "output" / "debug" / "frame_proposal_input.json"
STOPWORDS = {
    "antes",
    "tambien",
    "también",
    "para",
    "como",
    "pero",
    "porque",
    "sobre",
    "dentro",
    "fuera",
    "este",
    "esta",
    "estos",
    "estas",
    "tiene",
    "estan",
    "están",
    "parece",
    "vemos",
    "imagen",
}


def keywords(text: str, limit: int = 8) -> list[str]:
    words = []
    for raw in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{4,}", text.lower()):
        if raw in STOPWORDS:
            continue
        if raw not in words:
            words.append(raw)
        if len(words) >= limit:
            break
    return words


def package() -> dict[str, Any]:
    image = ROOT / IMAGE_PATH
    width, height = Image.open(image).size
    payload = {
        "project": OUTPUT_NAME,
        "image": IMAGE_PATH,
        "image_size": {"width": width, "height": height},
        "policy": "proposal_only_producer_decides",
        "segments": [
            {
                "index": index,
                "text": str(segment.get("text", "")),
                "current_frame": segment.get("frame"),
                "keywords": keywords(str(segment.get("text", ""))),
            }
            for index, segment in enumerate(SEGMENTS, start=1)
        ],
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    payload = package()
    print(json.dumps({"ok": True, "path": OUTPUT_PATH.relative_to(ROOT).as_posix(), "segments": len(payload["segments"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
