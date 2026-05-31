#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parent
errors = []

def fail(msg):
    errors.append(msg)

def table_rows_after_heading(text, heading):
    idx = text.find(heading)
    if idx == -1:
        return []
    tail = text[idx:].splitlines()
    rows = []
    in_table = False
    for line in tail:
        if line.startswith('|'):
            in_table = True
            if not re.match(r'^\|\s*-+', line):
                rows.append(line)
        elif in_table:
            break
    # remove header
    return rows[1:] if rows else []

# Section P: Ep.26-35 planning docs
q = root / 'docs/benchmark/questions.md'
a = root / 'docs/benchmark/v0-audit.md'
p = root / 'docs/benchmark/positioning.md'
b = root / 'docs/content-backlog.md'
ext_md = root / 'docs/benchmark/external-benchmark.md'
ext_json = root / 'docs/benchmark/external-benchmark-data.json'
internal_md = root / 'docs/benchmark/internal-baseline.md'
for path in [q, a, p, b, ext_md, ext_json, internal_md]:
    if not path.exists():
        fail(f'missing {path.relative_to(root)}')

if a.exists():
    audit = a.read_text(encoding='utf-8')
    mapping_rows = table_rows_after_heading(audit, '## 3. Ep.26–35 renumbered mapping')
    if len(mapping_rows) != 10:
        fail(f'v0-audit mapping rows expected 10, got {len(mapping_rows)}')
    for i, row in enumerate(mapping_rows, start=26):
        if f'| {i} |' not in row:
            fail(f'v0-audit row for Ep.{i} missing or out of order')
        for token in ['keep', '`', 'partial', 'none']:
            pass
        cells = [c.strip() for c in row.strip('|').split('|')]
        # Ep, decision, slug_candidate, CEFR, one learning point, existing_public_match, title
        if len(cells) < 7:
            fail(f'v0-audit Ep.{i} has too few columns')
            continue
        if not cells[1]:
            fail(f'v0-audit Ep.{i} missing decision')
        if not cells[2].startswith('`'):
            fail(f'v0-audit Ep.{i} missing slug_candidate')
        if not cells[5]:
            fail(f'v0-audit Ep.{i} missing existing_public_match')

if p.exists():
    pos = p.read_text(encoding='utf-8')
    if '## v0-renumbered' not in pos:
        fail('positioning.md missing v0-renumbered section')
    if '## v1 slate' not in pos:
        fail('positioning.md missing v1 slate section')
    v0_rows = table_rows_after_heading(pos, '## v0-renumbered')
    v1_rows = table_rows_after_heading(pos, '## v1 slate')
    if len(v0_rows) != 10:
        fail(f'positioning v0 rows expected 10, got {len(v0_rows)}')
    if len(v1_rows) != 10:
        fail(f'positioning v1 rows expected 10, got {len(v1_rows)}')
    if 'Ep.19–25' not in pos or 'Ep.26–35' not in pos or 'renumbered' not in pos:
        fail('positioning.md missing renumbering note')

if b.exists():
    lines = [ln for ln in b.read_text(encoding='utf-8').splitlines() if ln.startswith('|')]
    if len(lines) < 3:
        fail('content-backlog.md missing table rows')
    else:
        header = [c.strip() for c in lines[0].strip('|').split('|')]
        if len(header) != 5:
            fail(f'content-backlog schema expected 5 columns, got {len(header)}')
        data_rows = [ln for ln in lines[2:] if ln.strip()]
        if len(data_rows) != 1:
            fail(f'content-backlog expected exactly 1 data row, got {len(data_rows)}')
        if data_rows and 'a1-me-gusta-porque-reason' not in data_rows[0]:
            fail('content-backlog missing requested slug a1-me-gusta-porque-reason')

if ext_json.exists():
    import json
    data = json.loads(ext_json.read_text(encoding='utf-8'))
    if len(data) != 75:
        fail(f'external benchmark JSON expected 75 videos, got {len(data)}')
    channel_counts = {}
    for row in data:
        channel_counts[row.get('channel')] = channel_counts.get(row.get('channel'), 0) + 1
    if sorted(channel_counts.values()) != [15, 15, 15, 15, 15]:
        fail(f'external benchmark expected five 15-video channels, got {channel_counts}')

if ext_md.exists():
    text = ext_md.read_text(encoding='utf-8')
    if '| **Total** | **75** |' not in text:
        fail('external-benchmark.md missing Phase 3 total 75 row')

if internal_md.exists():
    text = internal_md.read_text(encoding='utf-8')
    for ep in range(1, 26):
        if f'| {ep} |' not in text:
            fail(f'internal-baseline.md missing Ep.{ep}')

if errors:
    print('Section P: FAIL')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)
print('Section P: PASS')
print('All local verification checks passed.')
PY
