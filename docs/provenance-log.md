# Provenance log

Every format fact and every behaviour fact gets a dated entry: what was learned, how it was learned, and which session learned it. Incidents (forbidden material encountered) are logged here too, described generically and never quoted. See [clean-room.md](clean-room.md).

## Template

```
### YYYY-MM-DD: <short title>
- **Type:** format | behaviour | import | incident
- **What:** <the fact, in your own words>
- **How:** <e.g. "observed in Dolphin: RAM watch at level start", "round-trip analysis of MST entries", "DJs_MA_TOOLs mst_lib/mst.py (MIT)">
- **Session:** <who or which agent session, date>
- **Verified:** yes / no (lead only)
```

## Entries

### 2026-10-18: Research brief imported
- **Type:** import
- **What:** The clean-room research brief was imported unchanged as [research/brief.md](research/brief.md). It is the source of truth for decisions D1–D9 and the policies in this repo. Facts it takes from Exavolt's docs are leads only, to be verified by observation.
- **How:** Brief imported from research pass, 2026-10-18. Compiled from public sources outside the source leak and the ports built on it.
- **Session:** Claude Code cloud session setting up `core`, 2026-10-18.
- **Verified:** no (research summary)

## Incidents

None recorded.
