# Dolphin oracle rig

Source: [research brief](research/brief.md) §7 Oracle; decision [D4](decisions/0004-oracle-first.md). This page records how the rig works and why. Its code and usage notes live in the [`oracle`](https://github.com/rusty-arms/oracle) repo.

## What it does

The rig replays a scripted input file in Dolphin, running the owner's verified disc, and records:

- a **RAM trace**: chosen values from emulated main memory, one CSV row per frame;
- **screenshots** at chosen frames, as PNG files;
- a **run record** (`run.json`) with hashes of every input and output, the Dolphin command and settings, and whether repeated runs matched.

That is the Phase 0 exit gate in the [roadmap](roadmap.md): "An agent replays a scripted input file in Dolphin and produces a RAM trace and screenshots."

## How it talks to Dolphin

Mainline Dolphin can play back input recordings, but it cannot read memory or save screenshots on chosen frames from a script. The rig uses a public fork of Dolphin that embeds Python and exposes memory reads, per-frame controller input, frame events, drawn frames and savestates to a script. The fork's preview releases ship Windows x64 builds only. The lab PC runs Linux, so the owner chose to build the fork from source there: its scripting module links against the system Python, and the rig provides a build script. A local Windows VM running the Windows build is the fallback; it was set aside because without GPU acceleration it renders in software and runs much slower.

A launcher on the lab PC (`python3 -m oracle.replay`) starts Dolphin with the rig's script and waits for the run to finish. The script, inside Dolphin, sets the controller each frame from the input file, reads the watched addresses, saves the screenshots, and writes its results.

The brief mentions a scriptable-Dolphin MCP server. One exists, built on the same fork, but in its first release it has no screenshots, and it drives the game one tool call at a time, which is too slow and too loose for repeatable recordings. It may still help an observer explore interactively later. It is not used for golden data.

## Repeatable runs

A golden trace is only useful if the same inputs always give the same trace. Each run:

- starts Dolphin with a fresh, empty user folder, so no everyday settings, memory cards or controller setup leak in;
- sets single-core emulation and a fixed real-time clock, turns cheats off and sets internal resolution to 1x;
- refuses to write into a folder that already has files.

`--repeat N` replays N times and fails unless every trace and screenshot is identical. The first real run must show that two runs from boot match; until it does, determinism is unconfirmed.

## Where things live

| What | Where | On GitHub? |
|---|---|---|
| The rig's code, generic examples, tests against a fake Dolphin | `oracle` repo | Yes, public |
| Real input scripts | Lab `inputs/` | No |
| Watch lists (addresses in the game are observations) | Lab `notes/` | No |
| Traces, `run.json` and Dolphin's log | Lab `traces/` | No |
| The scripting Dolphin build | Lab PC, outside the lab | No |
| Screenshots | Lab `captures/` | No |

The rig's repo holds no game data and no addresses in the game. Its examples use only made-up inputs and generic GameCube boot values from public hardware documentation.

## Who may run it

- **Observer sessions,** started inside the lab, run the rig and read its output. What they learn goes into specs, in their own words, with a provenance entry for each fact.
- **Implementer sessions** never see traces or screenshots. In Phase 2 they get only a pass or fail from the oracle runner.
- **Golden traces are verifier data.** Nobody edits one to make a comparison pass; the launcher never overwrites one.

## Later work

- **Oracle runner** (Phase 1–2): a separate local process with its own token that replays engine runs, compares their traces with the golden ones (`python3 -m oracle.compare`), and posts the required `oracle` commit status. See [org-and-permissions.md](org-and-permissions.md).
- **Guard for golden data:** an `agent-kit` guard rule that blocks agents, observers included, from editing files under the lab's `traces/`. A guard change needs the owner's approval.
- **Measure the tick rate:** the original simulation tick rate is a known unknown in the roadmap. The rig is the tool for measuring it.
