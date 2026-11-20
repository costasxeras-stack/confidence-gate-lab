# 0002: Host on GitHub Pages instead of Vercel

**Status:** Accepted · 20 November 2026

## Context

The portfolio default is Vercel's free plan for apps with an Express server. This app has no server (see 0001).

## Decision

Host it on GitHub Pages from the `main` branch. Because my portfolio site uses the custom domain kostasxeras.com, the app is served at https://kostasxeras.com/confidence-gate-lab/ with no extra setup.

## Consequences

- One setting to turn on, no second account, and the demo sits under my own domain.
- If the app ever needs a server (for example to call a language model live), it moves to Vercel and this decision gets a new record.
