# 0006. Host-authoritative co-op with per-object ownership

- **Decision:** D6
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D6, §7 Online co-op

## Context

Online co-op is a new feature; no version of the original had co-op campaign or online play.

## Decision

Use a host-authoritative model with per-object ownership, not lockstep.

## Consequences

- Fan co-op projects converged on this design; lockstep is fragile with AI enemies and physics.
- A listen-server host owns AI, physics props, scripts, triggers, cutscenes and saves. Each object has one owner that simulates it; others interpolate.
- Player identity is kept separate from the screen slot so split-screen and online play combine.
