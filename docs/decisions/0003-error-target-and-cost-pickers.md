# 0003: Offer two ways to pick the threshold, by error target and by cost

**Status:** Accepted · 20 November 2026

## Context

A slider alone shows the trade-off but does not say which point to choose. Teams usually reason in one of two ways: "we accept at most X% wrong", or "a wrong answer costs this much and a human check costs that much".

## Decision

Offer both. The error-target picker returns the threshold with the most automation at or under the chosen error rate. The cost picker returns the threshold with the lowest total cost per 1,000 questions. Both round the threshold up, so the result never goes over the target because of rounding.

The two costs are inputs with neutral starting values (10 and 1), labelled as the visitor's own assumptions. They are not presented as findings.

## Consequences

- A visitor gets a concrete recommendation in one tap, and can see how it moves when the costs change.
- The starting costs shape the first recommendation a visitor sees. The label makes clear they are assumptions to replace.
