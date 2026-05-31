# Ep.11 time/departure thumbnail draft pattern

Session context: user asked for A1 Ep.11 plan, then specifically asked to show the thumbnail first before full episode production.

## Topic and copy
- Episode concept: train/metro station after buying a ticket; ask departure time and platform.
- Main title: `¿A qué hora sale?`
- Korean subtitle: `몇 시에 출발해요?`
- Supporting pill: `hora · tren · andén`
- Badge: `Español A1 · Ep.11`

## Source-art prompt shape
Generate a 16:9 warm modern semi-flat station scene:
- Madrid train/metro station interior.
- Characters on the right: Jin holding a ticket, Lucía pointing to the board, Diego gesturing toward the platform.
- Departure board with abstract rows/clock icons only; explicitly request no readable text, logos, numbers, or watermarks.
- Leave the left ~45% as dark/clean negative space for title overlay.
- Ensure full heads/hair visible and clear faces.

## Overlay pattern
Use the established Ep.7-style layout:
- darkened/blurred station background as full bleed;
- large cream rounded panel on the left;
- coral episode badge at top;
- large white Spanish title with dark stroke, stacked as `¿A qué hora` / `sale?`;
- Korean subtitle in white pill;
- teal supporting vocabulary pill;
- small Spanish Lab label in bottom-right.

## QA checks
Before handoff, inspect the draft for:
- Spanish and Korean legibility at thumbnail size;
- no title clipping or panel overlap;
- no accidental readable text/logo on station board or train;
- three characters visible, especially no cropped hair/heads;
- station board reinforces the time/departure topic without competing with title.

## Implementation note
When composing overlays in Hermes/Linux, if the generic execution environment lacks Pillow, run the script with the Spanish Lab repo virtualenv (`/opt/data/repos/spanish-lab/.venv/bin/python`) where project dependencies are already installed. This is a reusable fallback for thumbnail still composition, not a claim that the tool is unavailable.