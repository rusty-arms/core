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

### 2026-10-27: MST magic and byte order
- **Type:** format
- **What:** The archive's magic is the 32-bit value 0x474E4146 in the archive's own byte order: `GNAF` in big-endian, `FANG` in little-endian. The GameCube archive is `GNAF` and big-endian throughout. That `FANG` means little-endian for Xbox and PS2 is still a lead. The DJs_MA_TOOLs README's help text has GameCube byte order the wrong way round, and its code is right.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_lib/mst.py`. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure. Every header and table field decodes consistently as big-endian.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes for GameCube; no (lead only) for `FANG`

### 2026-10-27: MST version word
- **Type:** format
- **What:** The version word is four bytes: platform flags (top byte), major, minor, sub-version. The GameCube archive is 1.8.0 with flags 0x18. Flag 0x10 is consistent with GameCube; the meaning of 0x08 is unknown. Flags 0x01 Xbox, 0x20 PS2 and 0x04 PC are leads.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_lib/mst.py`. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** partly (GameCube value only)

### 2026-10-27: MST archive size field
- **Type:** format
- **What:** The header word at offset 8 equals the archive file's length in bytes.
- **How:** structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure: compared with the file size.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes

### 2026-10-27: MST entry table position and capacity
- **Type:** format
- **What:** The header is 108 bytes. Offsets 12 and 16 hold the used and free row counts. The entry table starts at 108 with used + free rows of 36 bytes; the free rows follow the used ones and are all zero. Rows are not sorted by name, location or timestamp. The DJs_MA_TOOLs writer lists only 26 header words, but both its tools start the table at 108, as the disc does.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_lib/mst.py` and `mst_insert.py`. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes

### 2026-10-27: MST support table
- **Type:** format
- **What:** Offsets 20 and 24 hold used and free support-row counts. The support table follows the entry table directly, with 20-byte rows: a 16-byte NUL-terminated name and a Unix timestamp. Free rows are zero. Support rows have no data in the archive; their names share one extension that no main entry uses. On the GameCube disc both tables have the same total capacity. What the table is for is unknown.
- **How:** Lead: the field names in DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_insert.py`. Row layout found by structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes (layout); purpose unknown

### 2026-10-27: MST data offset
- **Type:** format
- **What:** The header word at offset 28 is the start of entry data: the end of the support table rounded up to a multiple of 2048. The gap is zero bytes, and the first entry in file order starts exactly there.
- **How:** Lead: field name in DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_insert.py`. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes

### 2026-10-27: MST per-type version words
- **Type:** format
- **What:** Header offsets 32 to 71 hold ten small non-zero words. DJs_MA_TOOLs names them as compiler versions for tga, ape, mtx, csv, fnt, sma, gt, wvb, fpr and cam. That mapping is not confirmed: no value appears as a constant field near the start of every entry of the matching type, and there are no wvb entries. Offset 72 holds one more small non-zero word of unknown meaning, and offsets 76 to 107 are zero.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_insert.py`. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure, including a search of each type's entry headers for its claimed value.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** partly (word positions yes; meanings no, lead only)

### 2026-10-27: MST entry row layout
- **Type:** format
- **What:** For version 1.8.0 each 36-byte row is a 20-byte NUL-terminated name, then the absolute data location, the exact data length (not rounded up, not always a multiple of 4), a timestamp and a content word. Every row's data lies inside the file; no two entries overlap or share a location.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_lib/mst.py`. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes

### 2026-10-27: MST entry names and types
- **Type:** format
- **What:** Names are read up to the first NUL. About one row in twenty has non-zero leftover bytes after it, which must be ignored. Observed names: at most 15 characters, lower case, unique even ignoring case, no directory separators, only letters, digits, space, `$`, `-`, `_` and exactly one dot. The extension (two or three letters) gives the type: tga, ape, mtx, csv, fnt, sma, gt, fpr, cam, wld, rdg and sfb occur.
- **How:** structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes

### 2026-10-27: MST entry data placement
- **Type:** format
- **What:** Every entry starts at a multiple of 32. In file order each entry starts at the previous entry's end rounded up to 32, or else up to 2048. The 2048 rounding comes almost only before textures, and it lines up with a field in the texture's own header. Padding is zero. File order differs from table order, with types interleaved. The file ends at the last entry's end rounded up to 32.
- **How:** Lead: 32-byte rounding in DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_insert.py`. Checked and extended by structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes (rule for 2048 unknown)

### 2026-10-27: MST timestamps
- **Type:** format
- **What:** Entry and support timestamps are Unix seconds. On the GameCube disc all of them lie between late 2000 and August 2003, none is zero, and they are not in table or file order.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_lib/mst.py` reads them as Unix times. Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes (what event they record is unknown)

### 2026-10-27: MST entry content word
- **Type:** format
- **What:** The last word of each entry row depends only on content. It is zero for every rdg, gt, cam and fnt entry and non-zero for all others. Byte-identical entries always share it, and shared non-zero values only occur on identical data. It is not standard CRC-32, CRC-32/BZIP2, CRC-32/MPEG-2, CRC-32C, Adler-32, a byte or word sum, XOR, FNV-1 or FNV-1a over the data. The algorithm, and whether the game checks it, are unknown.
- **How:** Lead: DJs_MA_TOOLs (MIT) at commit `b74fc4b` calls it unknown (`mst_lib/mst.py`) or a CRC (`mst_insert.py`). Checked: structural analysis of the owner's GameCube archive in the lab, with throwaway scripts that print only structure, grouping entries by identical data and testing those checksums.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** yes (properties); algorithm unknown

### 2026-10-27: MST older 16-byte names (lead)
- **Type:** format
- **What:** DJs_MA_TOOLs reads 16-byte names in archives of version 1.7 or earlier, and 24-byte names in PS2 archives. Not observable on the GameCube disc, which is 1.8.0 with 20-byte names.
- **How:** DJs_MA_TOOLs (MIT) at commit `b74fc4b`, `mst_lib/mst.py`.
- **Session:** Observer session (Claude Code) in the lab, 2026-10-27
- **Verified:** no (lead only)

### 2026-10-27: Reference disk verified
- **Type:** import
- **What:** Added the default iso under `disc` subdirectory and validated it using dolphin.
- **How:** See step 4 of [owner-checklist.md](../docs/setup/owner-checklist.md)
- **Session:** Ed
- **Verified:** yes

### 2026-10-18: Research brief imported
- **Type:** import
- **What:** The clean-room research brief was imported unchanged as [research/brief.md](research/brief.md). It is the source of truth for decisions D1–D9 and the policies in this repo. Facts it takes from Exavolt's docs are leads only, to be verified by observation.
- **How:** Brief imported from research pass, 2026-10-18. Compiled from public sources outside the source leak and the ports built on it.
- **Session:** Claude Code cloud session setting up `core`, 2026-10-18.
- **Verified:** no (research summary)

## Incidents

None recorded.
