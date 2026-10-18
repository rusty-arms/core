# Legal guardrails

> **This is general information, not legal advice.** Get a UK solicitor's view before any public release.

Source: [research brief](research/brief.md) §4. UK law first, then US.

## Never do

- Never use the leaked source, or anything built on or learned from it ([0002](decisions/0002-no-leaked-source.md)).
- Never publish a decompilation or a static recompilation of the retail program ([0003](decisions/0003-no-published-decompilation.md)).
- Never ship, link to or document a way to dump discs or bypass protection (CDPA s296 and s296ZA; *Nintendo v Playables* treats these as strict liability).
- Never commit or ship game assets: models, textures, animations, audio, fonts, scripts, data or movies ([media policy](media-policy.md)).
- Never publish 3D recreations of Glitch or other named characters (*Shazam v Only Fools*).
- Never use the original game's name in the project's title or logo. One factual compatibility line is fine.
- Never take money for the project ([0007](decisions/0007-no-assets-distinct-name-no-money.md)).
- Keep copies of your own disc for personal use only (private copying exception quashed in 2015).
- Never file a DMCA counter-notice without UK legal advice.

## UK: Copyright, Designs and Patents Act 1988

- **s50BA:** a lawful user may observe, study and test a program's functioning while running it. This is the legal basis for using Dolphin as the oracle.
- **s50B:** decompiling is allowed only to make an independent program interoperate, and never to create a program that is "substantially similar in its expression" (s50B(3)(d)).
- **s296A:** contract terms, such as an EULA, that try to override s50A–50BA are void.
- **s28B:** the private-copying exception was quashed in 2015, so copying your own disc is technically infringing for its art, audio and video. The practical risk is low; keep it for personal use only.
- **s296 and s296ZA:** circumvention. See "Never do".
- **Unprotected:** functionality, data formats and game ideas (*SAS v World Programming*, CA 2013 and CJEU C-406/10; *Nova v Mazooma*; *Navitaire v easyJet*).
- **Characters** can be protected works (*Shazam v Only Fools*).
- **Trade Secrets Regulations 2018, reg 3:** using leaked trade secrets is unlawful where it amounts to a breach of confidence.
- **Trademark:** the US mark for the original name (reg. no. 2898071) is held by Blizzard Entertainment and was renewed in March 2024. The UK register has **not been checked**.

## US

- ***Sega v Accolade* and *Sony v Connectix*:** intermediate copies made while reverse engineering are fair use, provided the final product contains no copied code.
- ***Davidson v Jung*:** enforced EULA bans on reverse engineering. Owners in this game's rights chain have litigated before.
- **DMCA §1201 exemptions** run until 28 October 2027. None covers an individual dumping a working disc to play a port.

## Enforcement climate

- Activision revoked a fan licence for *The Silver Lining* (2010), sent a cease-and-desist to the H2M mod (2024), filed a DMCA notice over leaked networking source (June 2026), and had footage of an AI-built decompilation taken down (October 2026).
- Microsoft's Game Content Usage Rules probably don't cover this title, and they forbid reverse engineering to access assets anyway.
- Ports that need the player's own copy have mostly survived, but that is the rights holder's choice, not a safe harbour.
- An official re-release would change the picture.

## DMCA / takedown response plan

If GitHub receives a takedown notice for any project repo:

1. **Do not file a counter-notice.** Filing one submits you to US jurisdiction, and in the re3 case Take-Two answered counter-notices with a lawsuit.
2. Keep a local copy of the affected repos and of the notice. *(Project practice; not from the brief.)*
3. Check the notice against the clean-room record: the [provenance log](provenance-log.md), the specs, and the guard CI history. *(Project practice; not from the brief.)*
4. Get UK legal advice before taking any further step.
5. Know the timeline: GitHub restores content 10–14 days after a counter-notice unless the claimant sues.
6. Record what happened, without quoting any forbidden material, in the provenance log.

Because the lab is never on GitHub ([0009](decisions/0009-lab-off-github.md)), a takedown cannot reach it.

## Open legal questions

- Whether the original name is registered in the UK or EU.
- Whether a closed Discord counts as "the public" for copyright purposes.
- Whether Microsoft plans an official re-release.
