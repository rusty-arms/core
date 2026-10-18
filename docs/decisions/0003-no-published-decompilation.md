# 0003. No published decompilation or static recompilation

- **Decision:** D3
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D3, §3, §4

## Context

Decompilation and static recompilation are common routes for game ports.

## Decision

Do not publish a decompilation or a static recompilation of the retail program. Decompiler output of the retail executable is also a forbidden input to implementers.

## Consequences

- Publishing either one distributes a translation of the original program, which falls outside UK CDPA s50B(3)(d) and outside the US *Connectix* reasoning.
- Behaviour must be learned by observation instead (see [0004](0004-oracle-first.md)).
