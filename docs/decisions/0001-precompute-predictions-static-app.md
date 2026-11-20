# 0001: Precompute predictions and ship a static app

**Status:** Accepted · 20 November 2026

## Context

The app needs predictions and confidence scores for 3,080 questions from two models. They could be computed live on a server or once, offline.

## Decision

Train both models once, offline, and store each test question's top prediction, confidence and runner-up in `data/results.json` (263 KB). The app is one HTML file that reads that file.

## Consequences

- No server, no API key and no running cost.
- Every number on screen can be checked against the data file.
- Visitors cannot type their own question. That is fine for this lab, which is about choosing a threshold on labelled data, not about trying the classifier.
