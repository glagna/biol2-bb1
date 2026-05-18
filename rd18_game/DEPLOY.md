# RD#18 Cumulative L3 Challenge, Deploy via GitHub Pages

**For class:** Mon May 18, S22 Arena, 0:08 to 0:20.
**Topic:** Cumulative Level 3 challenge (LO3.1, 3.2, 3.3, 3.5) plus 2 Level 2 callbacks (CRISPR mechanism + risk literacy). Q8 is the Deep Think Challenge with doublePayout (cross-LO synthesis stem).
**Architecture:** GitHub Pages (hosting) + Firebase Realtime DB at `biol2-bb1` (state only). Same as RD15/RD16/RD17 convention.
**Target URL:** `https://glagna.github.io/biol2-bb1/rd18_game/`

---

## What's in this folder

| File | Purpose |
|---|---|
| `index.html` | Team device view (pick A1-D4, place bets, lock answers) |
| `host.html` | Instructor console (open wager, open answer, reveal, next) |
| `leaderboard.html` | Apple TV projection (live ranked scores) |
| `rd18-questions.json` | 8 cumulative L3 questions + 2 L2 callbacks; Q8 has `doublePayout: true` |
| `firebase.json` / `database.rules.json` | Carried from rd17_game template; unused for GH Pages deploy |
| `export_rd18.py` | Run after class to capture audit CSV of bets/answers/scores |

**Patches applied to the rd17_game clone (Claude, 2026-05-17):**
- All `rd17` references swapped to `rd18` across HTML, JSON, Python (URL paths, Firebase nodes, localStorage keys)
- All `RD17` headers and brand strings swapped to `RD18`
- Question count loops and hardcoded "5" constants swapped to "8" (10 spots across host.html, index.html, leaderboard.html per `feedback_rd_game_hardcoded_question_count`)
- "Q5 PAYS DOUBLE" banner swapped to "Q8 PAYS DOUBLE"
- doublePayout multiplier check `qNum === 5` swapped to `qNum === 8` (index.html line 793) and `q === 5 ? 2 : 1` swapped to `q === 8 ? 2 : 1` (leaderboard.html line 244)
- End-of-round check `currentQ < 5` swapped to `currentQ < 8` (host.html line 423)
- New 8-question JSON for cumulative L3 plus L2 callbacks; answer key B/B/B/C/C/B/C/A
- database.rules.json: added `rd18` entry (with rd17 retained for backwards-compat)

---

## Deploy commands (Mac Terminal, ~2 min)

Assuming you have the `biol2-bb1` GitHub Pages repo cloned locally at `~/biol2-bb1/`:

```bash
# 1. Copy the rd18_game folder into the repo
cp -r "/Users/giorgiolagna/Documents/Claude/Projects/BIOL2-S26/03_week_materials/week_08/rd18_game" ~/biol2-bb1/

# 2. Push to GitHub
cd ~/biol2-bb1
git add rd18_game
git commit -m "RD18 cumulative L3 challenge for S22 Mon May 18"
git push origin main

# 3. Wait ~1 min for GitHub Pages to publish, then verify
open https://glagna.github.io/biol2-bb1/rd18_game/
```

---

## Smoke-test before class (Sun May 17 night, ~10 min)

Per `feedback_rd_game_hardcoded_question_count`: the most important pre-class check is the doublePayout Q8 multiplier.

1. Open the live URL in a private window.
2. Pick a test team (e.g., A1).
3. Click through Q1 to Q7 in the host console (any answers, any wager). Verify the leaderboard updates correctly each turn.
4. **On Q8: place a high wager (e.g., 100 percent), lock in the correct answer (A), and verify the leaderboard shows the points doubled.** This is the spot that has bitten RD13/RD14/RD17 in the past.
5. Verify the "Q8 PAYS DOUBLE" banner shows on the team device at Q8.
6. Verify the end-of-round leaderboard fires after Q8 (not Q5, not Q7).

If any check fails: open the relevant HTML file and grep for any remaining "5" near a question-count context. The 10 spots are listed in the Patches section above.

---

## Reset Firebase state between test and live runs

Before class, clear the test data from the RTDB:

```bash
# In a browser, sign into Firebase console at biol2-bb1, navigate to
# Realtime Database -> rd18 -> delete the rd18 node entirely. New nodes
# auto-create on first team join Monday morning.
```

Or via Firebase CLI:

```bash
firebase --project biol2-bb1 database:remove /rd18 -y
```

---

## Audit export after class (run from your terminal)

```bash
cd "/Users/giorgiolagna/Documents/Claude/Projects/BIOL2-S26/03_week_materials/week_08/rd18_game"
python3 export_rd18.py
# Produces: rd18_results_2026-05-18.csv with per-team bets, answers, points per question
```

---

## Question key (instructor reference, NOT student-visible)

| Q | Category | Correct | Notes |
|---|---|---|---|
| 1 | Innate vs adaptive | B | LO3.1, Item 21 anchor |
| 2 | Vaccine training | B | LO3.2, Item 22 anchor |
| 3 | HIT math at R₀=2 | B | LO3.3 (HIT=50%), Item 24 reinforcement |
| 4 | Epi curve plateau | C | LO3.5, CP#17 calibrated error catch |
| 5 | L2 callback, CRISPR mechanism | C | LO2.3a reactivation |
| 6 | L2 callback, risk literacy | B | LO2.5 reactivation |
| 7 | R₀ from data (S23 forward-anchor) | C | LO3.5, generic scenario, no Santa Clara leak |
| **8 (DOUBLE)** | Cross-LO synthesis, 1955 polio vaccine | **A** | BB3 cognitive demand preview |

Source bank: `04_assessments/BIOL2_RD18_S22_Cumulative_Challenge.md` (full rationales + lab-stimulus security audit).

---

## Known gotcha

The `.bak` files in this folder are sed artifacts that the sandbox couldn't delete. They are not deployed (firebase.json `ignore` already covers `**/.*` and they will be removed by `git add` filters), but you can clean them locally:

```bash
cd "/Users/giorgiolagna/Documents/Claude/Projects/BIOL2-S26/03_week_materials/week_08/rd18_game"
rm *.bak
```
