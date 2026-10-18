# Clean-room policy

Source: [research brief](research/brief.md) §3. See also decisions [0001](decisions/0001-clean-room-engine.md), [0002](decisions/0002-no-leaked-source.md) and [0003](decisions/0003-no-published-decompilation.md).

The project reimplements the game from observation and public documentation only. The `specs` repo is the clean-room wall between the people (and agents) who look at the game and the ones who write the engine.

## Roles

### Observers
- May use the disc, Dolphin and the lab.
- Write **specs** in their own words, describing formats and behaviour.
- Specs contain no copied code.
- Specs contain no retail bytes beyond what identifies a structure, such as magic numbers.

### Implementers
- See only the specs, public documentation and synthetic test fixtures.
- Never see the lab, decompiler output or forbidden material.
- Test against the disc only by running the engine locally.

## Allowed inputs

- The bytes of the developer's own disc.
- Behaviour observed while running the game in Dolphin. UK CDPA s50BA lets a lawful user observe, study and test a program's functioning.
- Code and documentation from **DJs_MA_TOOLs**, which is MIT-licensed, with attribution.
- Public documentation of GameCube hardware and media formats: GX, DSP ADPCM audio, and Bink via FFmpeg's open decoder.
- Public gameplay descriptions: speedrun knowledge bases, StrategyWiki, reviews.
- General game-design ideas, which are unprotected (*Nova*). For example, "a downed player watches until the next checkpoint".
- Facts stated in Exavolt's public docs, as **leads only**. Verify each one by observation before relying on it.

## Forbidden inputs

- The 2019 source leak in any form, including file listings and summaries of it.
- Any port, fork, document, commit message or write-up built on the leak. This includes the 2026 AI-assisted PC ports.
- Internet Archive copies of the source or of prototype discs. *(Project rule, stricter than the brief.)*
- The community's PASM compiler. Its origin is unclear, so avoid every pipeline that depends on it.
- Decompiler output of the retail executable.
- The Dolphin HD texture pack for the game, which contains textures of unknown origin.
- **Exavolt's code.** It has no licence, so it is all rights reserved until its author grants permission.
- Ripped assets from any website, Steam Workshop pack or model archive.

Committed files describe forbidden material generically, as above. They never name or link the leak-based repos. Specific names live only in the maintainer's local blocklist.

## If you meet forbidden material

This applies to people and agents alike, including material that turns up in search results, a link or a pasted snippet.

1. Stop.
2. Do not summarise or quote it.
3. Tell the developer.
4. Record the incident in the [provenance log](provenance-log.md): date, session, and a generic description of what appeared and where. Do not quote the material.

## Provenance

Every format fact and every behaviour fact gets a dated entry in the [provenance log](provenance-log.md) recording what was learned, how it was learned, and which session learned it.
