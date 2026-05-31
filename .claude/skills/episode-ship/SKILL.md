---
description: Run the Spanish Lab publish gauntlet for an existing project and produce an upload-ready checklist.
argument-hint: "<project_module>"
---

# Episode Ship

Use this skill to take an existing Spanish Lab project module to an upload-ready bundle.

Arguments:

`$ARGUMENTS`

## Current Projects

!`find projects -maxdepth 1 -name '*.py' -not -name '__init__.py' -print | sort`

## Workflow

1. Resolve `PROJECT` from `$ARGUMENTS`. If omitted, infer from the current episode context; otherwise ask for the module name.
2. Confirm the project module exists under `projects/`.
3. Run:

```sh
PROJECT=<module> make check
PROJECT=<module> make debug
PROJECT=<module> make test
PROJECT=<module> make lint-spanish
PROJECT=<module> make tts
PROJECT=<module> make preview
PROJECT=<module> make preview-qa-pack
PROJECT=<module> make preview-qa
```

If global `python3` cannot import project dependencies such as Pillow, add `PYTHON=.venv/bin/python` to each Make command.

4. Pause for human review of `output/preview.mp4`. Use `output/debug/preview_qa_advisory.json` as advisory context only; it never replaces human preview review in v1.
5. After approval, run:

```sh
PROJECT=<module> make publish
PROJECT=<module> make verify
```

6. Dispatch `designer` for thumbnail review or variants if needed.
7. Dispatch `seo-promo` for final YouTube copy review.
8. Dispatch `publisher-qa` for the final readiness checklist.

## Upload-Ready Checklist

The final answer must include absolute paths for:

- MP4
- thumbnail JPG
- metadata MD
- metadata JSON

Also report:

- title
- duration
- chapter count
- verification result
- any known gap

## Rules

- Do not upload to YouTube.
- Do not silently overwrite existing publish artifacts.
- If publish refuses because artifacts already exist, report the collision and recommend a `RENDER_VERSION` bump only if a new package is needed.
- Preview QA is advisory only. It must not block or approve publish by itself.
- Append `preview_review`, `thumbnail_chosen`, and `seo_finalized` events to the memory decision JSONL when those gates complete.
