# 0001. Build a clean-room engine that loads assets from the player's own disc

- **Decision:** D1
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D1, §4

## Context

The project wants to publish a faithful reimplementation as widely as the law allows. Under UK law, functionality, data file formats and game ideas are not protected (*SAS v WPL*, *Nova v Mazooma*).

## Decision

Build a clean-room engine that reads the game's assets from the player's own disc at runtime.

## Consequences

- It is the only route that can plausibly be published.
- The engine ships with no game assets; players must supply their own disc.
- Every format and behaviour must be rebuilt from allowed inputs only (see [clean-room.md](../clean-room.md)).
