# 0004: Show every question as a dot, with the threshold as a gate

**Status:** Accepted · 23 November 2026

## Context

Version 0.1.0 opened with four number tiles and a chart. The tiles looked like every other dashboard, and a visitor had to read the chart to understand what the threshold does. The page also shared one visual template with the other portfolio apps.

## Decision

Open with all 3,080 test questions drawn as dots, sorted by the model's confidence from left to right. The threshold is a yellow gate line that the visitor drags through the dots. Dots left of the gate wait for a person (grey). Dots right of it go out automatically, green when right and red when wrong. The result is written as one sentence under the gate instead of four tiles.

The page gets its own look: a cool grey-green background, Archivo and Public Sans, square corners and dark rules, chosen for a bank support operations tool.

## Consequences

- A visitor sees the trade-off before reading any number: moving the gate right adds red dots.
- The canvas is redrawn on each move. On 3,080 dots this is fast enough on a phone.
- The dots are drawn on a canvas, so screen readers get the sentence and the numbers above it, not the dots.
