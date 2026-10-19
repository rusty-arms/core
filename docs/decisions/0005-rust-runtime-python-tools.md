# 0005. Rust for the runtime, Python for the tools

- **Decision:** D5
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D5, §7 Runtime

## Context

Agents need tight feedback; GameCube data is big-endian; format tooling and Blender integration are needed.

## Decision

Write the runtime in Rust and the tools in Python.

## Consequences

- Rust's compiler feedback keeps agents on track, and its explicit endianness suits big-endian GameCube data.
- Python suits format tooling and Blender.
- Rendering via wgpu or the SDL3 GPU API, with SDL3 for windows and input. Avoid Bevy, whose networking crates pin different Bevy versions.
