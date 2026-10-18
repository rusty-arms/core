# 0004. Oracle-first: Dolphin running the retail disc is the referee

- **Decision:** D4
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D4, §4, §7 Oracle, §9 Identities

## Context

Agents write most of the code. Every AI port that scaled was checked against something the agent could not edit; the ones without such a check failed.

## Decision

Use Dolphin, running the retail disc, as the oracle. Layer it: round-trip tests, screenshot diffs, RAM-state traces under scripted inputs, deterministic replays, and developer playtests.

## Consequences

- UK CDPA s50BA lets a lawful user observe, study and test a program's functioning while running it.
- The oracle and its golden data must be out of agents' reach; agents must not be able to post the `oracle` status themselves.
- Phase 0 must deliver a Dolphin oracle rig.
