PYTHON ?= $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)
PROJECT ?= reunion_madrid
export PROJECT
OUTPUT_NAME := $(shell PROJECT=$(PROJECT) $(PYTHON) -c "from segments import OUTPUT_NAME; print(OUTPUT_NAME)")

.PHONY: all check debug test lint-spanish tts preview preview-cards preview-diary preview-qa-pack preview-qa render render-cards render-diary publish publish-cards publish-diary publish-existing verify propose-frames-pack propose-frames clean

all: check debug test render verify

check:
	$(PYTHON) checks/validate_segments.py

debug: check
	$(PYTHON) checks/make_debug.py

test:
	$(PYTHON) checks/test_units.py

lint-spanish:
	$(PYTHON) checks/lint_spanish.py

tts:
	$(PYTHON) -m build.audio

preview: check
	$(PYTHON) -m build.render --preview

preview-cards: check
	$(PYTHON) -m build.render_cards --preview

preview-qa-pack:
	$(PYTHON) checks/preview_qa_pack.py

preview-qa:
	$(PYTHON) checks/preview_qa.py

render: check
	$(PYTHON) -m build.render --final

render-cards: check
	$(PYTHON) -m build.render_cards --final

publish:
	@if [ ! -f output/$(OUTPUT_NAME).mp4 ] && [ ! -f output/preview.mp4 ]; then \
		$(MAKE) render; \
	fi
	$(PYTHON) -m build.publish

publish-cards:
	@if [ ! -f output/$(OUTPUT_NAME).mp4 ] && [ ! -f output/preview.mp4 ]; then \
		$(MAKE) render-cards; \
	fi
	$(PYTHON) -m build.publish

preview-diary: check
	$(PYTHON) -m build.render_diary --preview

render-diary: check
	$(PYTHON) -m build.render_diary --final

publish-diary:
	@if [ ! -f output/$(OUTPUT_NAME).mp4 ] && [ ! -f output/preview.mp4 ]; then \
		$(MAKE) render-diary; \
	fi
	$(PYTHON) -m build.publish

publish-existing:
	$(PYTHON) -m build.publish --skip-render-check

verify:
	$(PYTHON) checks/probe_output.py output/$(OUTPUT_NAME).mp4

propose-frames-pack:
	$(PYTHON) -m build.propose_frames_pack

propose-frames:
	$(PYTHON) -m build.propose_frames

clean:
	rm -rf output
