# Roadmap

Source: [research brief](research/brief.md) §11.

The durations come from the research and assume heavier agent use than the Claude Pro plan allows. **On Pro, expect the slow end of each range, or longer.** They are indicative, not commitments. The project moves one task per session.

| Phase | Indicative duration | Goal | Exit gate | Shareable output |
|---|---|---|---|---|
| 0. Foundations | ~1 month | Org and `core` repo; agent-kit hooks; local lab; Dolphin oracle rig; disc hash verification | An agent replays a scripted input file in Dolphin and produces a RAM trace and screenshots. The hooks block deliberately bad actions. | `core`, `agent-kit` |
| 1. Read the whole disc | 2–4 months | Parsers for MST, CSV, WLD, GX textures, meshes, animations, audio, fonts, AI graphs and AMX; a level viewer | Every entry type round-trips. Viewer screenshots match Dolphin. | `tools`, `specs` |
| 2. Walk, shoot, possess | 6–9 months | Fixed-tick simulation designed for N players; weapons, bots, AMX VM, possession, vehicles, physics, per-level logic | Each level completes in replay. RAM-trace diffs are within tolerance. The developer signs off after playing. | Private builds |
| 3. Online co-op | 3–6 months, overlapping Phase 2 | Localhost, then LAN, then direct internet, then ICE/TURN; mission-by-mission co-op audit; late join; difficulty scaling | A two-player campaign over a simulated lossy link; four-player soak tests | Small tester group |
| 4. Remaster polish | Ongoing; 2–3 months of focused work | Interpolation, widescreen HUD, rebinding, gyro, HD override archive and recipe | Replay checksums are identical across frame rates. | **1.0: public engine, no assets** |
| 5. New content | After 1.0 | Open level format, Blender add-on, mission scripting, original models | A new mission plays in co-op using only disc assets plus original art. | Public, with AI use labelled |

## Phase 0 breakdown

1. `core` repo (this repo).
2. `agent-kit`: a Claude Code plugin holding the guard hook, the reviewer and chores subagents, and the session-discipline rules.
3. `specs` skeleton.
4. Lab setup (local only).
5. Dolphin oracle rig: scripted input replay producing a RAM trace and screenshots.

## Known unknowns

- The original simulation tick rate, and how much logic is tied to frame rate. Measure it in Dolphin.
- The compiled GameCube mesh, texture, animation, audio-bank, font and AI-graph formats. None has a public spec; this is the Phase 1 gap.
- Each level has bespoke load, unload, work and draw logic in the executable: 42 pieces to reimplement by observation.
