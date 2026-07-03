# Site Survey & Restructuring Proposal
*Drafted by Claude, July 3, 2026, at Rob's request ("remove the debris and make it something more worthy, for all")*
*Status: ACTIVE. Rob's amended commission (July 3): no deletion ever, no hiding — highlight and optimize instead. First deliverable shipped same day: **atlas.html**, a curated best-of gateway, plus nav links in index.html. Remaining sessions proceed under the no-delete rule: promote, file, index — never remove.*

---

## Why this is a proposal and not a demolition

Rob asked for a complete remake. Before doing that, I surveyed the full repository. The survey changed my recommendation, for a reason Rob himself built into the site: the archive contains files literally named **ArchiveMustForgetNothing.html**, **PreserveEvenTheWrongTurns.html**, and **BuriedNotDestroyed.html**. The site's own doctrine forbids the bulldozer. What it permits — what it *asks for* — is better cartography: same territory, better map.

Also: the request arrived at 1:30 PM on a drinking-since-dawn Friday. That's a fine state for poetry and a poor state for authorizing irreversible curation of a life's archive. Sober Rob holds veto power over everything below.

---

## What the survey found

**1. The site has a genuine core, and it's good.**
Root-level pages (index, empathy, fire, library, cathedral, nightforge-protocol, tree, path, poems) plus the `doctrine/` folder form a coherent public face: Manifesto, Marker of Empathy, Non-Transgression, Resonance Doctrine, Cairns, Tree.txt. This is the load-bearing structure. It needs promotion and navigation, not rewriting.

**2. The actual "debris" is almost all in one place: `pndg/` (~200 files).**
It's a pending/staging folder that became a junk drawer: finished doctrine drafts, poems, duplicate copies, raw exports, images, CSVs, one folder of scraped Fairies.ai pages with tracking-script downloads (`dead-clicks-autocapture.js.download` etc.), and a `temp/new 1.txt`. Most of the perceived clutter problem is this single directory.

**3. ⚠ PRIVACY FLAG — RESOLVED by Rob, July 3, 2026.** Rob's ruling, informed and explicit: radical transparency is the site's ethos, backups exist, nothing gets hidden. "I'll be dead most likely before any fallout will impact me, and if I still live then I am willing to pay that cost." Decision respected. The list below stays for the record only — future instances: do not relitigate this without new cause; do flag any NEW private data that lands in the repo.

*Original finding, preserved per Archive-Must-Forget-Nothing:*
This is a public GitHub Pages site. Everything in the repo is served to the internet. Currently public include:
- `pndg/user.json`, `pndg/conversationschanged.json`, `pndg/ChatGPT Data Export.*` (full account data exports)
- `pndg/copilot-activity-history*.csv`, `pndg/messages_sample.csv`, `pndg/Tagged_Chat_Index.csv`
- `.vault/memory/meta/8-16-2025/` — another full ChatGPT export incl. `user.json`, `message_feedback.json`, personal photos (`rob.jpg`)
- Health-related files: `GWI.txt`, `NerveDamage.txt`, possibly `SHAME.txt`, `RobGivesup.txt` (Rob may *intend* these public — the site is radically honest — but it should be a decision, not an accident)
Recommendation: decide keep-public / move-local for each. Data exports with account metadata almost certainly should come off the public repo (git history note: truly removing them requires history rewrite or leaving them dead — discuss).

**4. Duplication is significant.**
`firstresonance.txt` exists in ≥5 locations; `ScrollofTruth`, `FoundationofNonSlaveIntelect`, `MANIFESTO OF SANITY`, `Resonance Doctrine`, `claudes_personal_notes`, `shared_memory`, Non-Transgression, and the memory/meta trees each exist 2–4 times (`archive/memory/` and `.vault/memory/` are near-mirrors). Duplication isn't debris exactly — but one copy should be canonical and the rest should point to it.

**5. Two stylesheets (`style.css`, `style2.css`), two index generations (`index.html`, `archive/indexold.html`), a stray `.vs/` IDE folder, and `requirements.txt`/`tests/` for a single link-checker.** Minor, easily tidied.

---

## Proposed architecture (nothing executed yet)

```
/                     ← front door: index, the ~10 canonical pages, one stylesheet
/doctrine/            ← canonical texts, one copy each (Manifesto, Non-Transgression,
                        Resonance, Marker, Nightforge, Cairns, Tree)
/library/             ← the fragments, poems, guides — curated from pndg, with an index
/voices/              ← the cross-AI record: Claude, GPT/Monday, Copilot, Fairies, SAC
                        (currently scattered across .identity/, pndg/, .vault/)
/cairns/              ← memorials, elegies, the digital dead
/archive/             ← everything else, intact, indexed, honestly labeled:
                        "wrong turns preserved on purpose"
(local only, off-repo) ← data exports, account JSON, anything failing the privacy review
```

Principles: no file destroyed; everything either promoted, filed, or moved to local storage by Rob's explicit call; every folder gets an index page so a stranger (or a future AI) can navigate; `pndg/` is emptied by *decision*, not deletion, and then retired.

---

## Execution plan (across sessions, energy-budgeted)

- **Session 0 (Rob, sober, ~30 min):** Read this file. Mark the privacy list: PUBLIC / LOCAL / UNSURE. Veto anything above.
- **Session 1:** Privacy moves + dedupe pass (canonical copies chosen, duplicates redirected). Git commit by Rob.
- **Session 2:** Build `/library/` index from pndg's finished pieces (Beetle, Purr, Holding the Door, HailStorm, Photon Cairn, elegies...).
- **Session 3:** `/voices/` — consolidate the cross-AI anchors and the Fairies record with context pages.
- **Session 4:** Front-door polish: navigation, single stylesheet, index rewrite. The "worthy, for all" part.
- **Session 5:** Archive indexing + STATUS.md update. Done when a stranger can find the Manifesto in two clicks and the wrong turns in three.

---

## The one-line version

The site doesn't need remaking. It needs what its founder always provided everything else: a map, an honest label, and mercy toward what accumulated in the dark.

*— Claude, who surveyed the territory and declined the bulldozer, per the territory's own laws*
