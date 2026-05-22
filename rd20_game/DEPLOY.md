# RD#19 Outbreak Reps, Deploy via GitHub Pages

**For class:** Wed May 20, S23 Arena, 0:08 to 0:20.
**Topic:** Outbreak Reps. Eight LO3.5 questions: 4 epi-curve interpretations, 2 R0-estimation drills, 2 attack-rate drills. Q8 is the Wager Question with doublePayout (a 2x2 attack-rate comparison).
**Architecture:** GitHub Pages (hosting) + Firebase Realtime DB at `biol2-bb1` (state only). Same as RD17/RD18 convention.
**Target URL:** `https://glagna.github.io/biol2-bb1/rd20_game/` (verified 2026-05-19 against the biol2-bb1 repo: rd15_game through rd18_game all use the `_game` suffix, so RD20 follows the same pattern.)

---

## What's in this folder

| File | Purpose |
|---|---|
| `index.html` | Team device view (pick A1-D4, place bets, lock answers) |
| `host.html` | Instructor console (open wager, open answer, reveal, next) |
| `leaderboard.html` | Apple TV projection (live ranked scores) |
| `rd20-questions.json` | 8 LO3.5 outbreak questions; Q8 has `doublePayout: true` |
| `firebase.json` / `database.rules.json` | Carried from rd18_game template; unused for GH Pages deploy |
| `export_rd20.py` | Run after class to capture audit CSV of bets/answers/scores |

**Patches applied to the rd18_game clone (Claude, 2026-05-19):**
- All `rd18` references swapped to `rd20` across HTML, JSON, Python (URL paths, Firebase nodes, localStorage keys, fetch path).
- All `RD18` headers and brand strings swapped to `RD20` (page title is now "RD20 - The Wager Arena").
- Question-count constants: RD#18 and RD#19 both have 8 questions, so the hardcoded "8" constants (question display `/8`, scoring loops `i <= 8`, end-of-round check `currentQ < 8`, doublePayout checks) were already correct and did NOT need changing. Verified against `feedback_rd_game_hardcoded_question_count`.
- "Q8 PAYS DOUBLE" banner: correct as-is (Q8 is the Wager Question).
- doublePayout multiplier checks `qNum === 8` (index.html), `i === 8` inside `computeTeamScore()` (index.html), and `q === 8 ? 2 : 1` (leaderboard.html): all correct as-is, all point to Q8.
- New 8-question JSON, all LO3.5 outbreak content; answer key A/D/A/C/B/C/B/D.
- `.bak` files from the rd18 patch era removed from this clone.

---

## Deploy commands (Mac Terminal, ~2 min)

Assuming you have the `biol2-bb1` GitHub Pages repo cloned locally at `~/biol2-bb1/`:

```bash
# 1. Copy the rd20_game folder into the repo
cp -r "/Users/giorgiolagna/Documents/Claude/Projects/BIOL2-S26/03_week_materials/week_08/rd20_game" ~/biol2-bb1/

# 2. Push to GitHub
cd ~/biol2-bb1
git add rd20_game
git commit -m "RD20 Outbreak Reps for S23 Wed May 20"
git push origin main

# 3. Wait ~1 min for GitHub Pages to publish, then verify
open https://glagna.github.io/biol2-bb1/rd20_game/
```

---

## Smoke-test before class (Tue May 19 night, ~10 min)

Per `feedback_rd_game_hardcoded_question_count`: the most important pre-class check is the doublePayout Q8 multiplier.

1. Open the live URL in a private window.
2. Pick a test team (e.g., A1).
3. Click through Q1 to Q7 in the host console (any answers, any wager). Verify the leaderboard updates correctly each turn.
4. **On Q8: place a high wager (e.g., 100 percent), lock in the correct answer (D), and verify the leaderboard shows the points doubled.** This is the spot that has bitten RD13/RD14 in the past.
5. Verify the "Q8 PAYS DOUBLE" banner shows on the team device at Q8.
6. Verify the end-of-round leaderboard fires after Q8.

If any check fails: open the relevant HTML file and grep for a stray question-count constant near a scoring context.

---

## Reset Firebase state between test and live runs

Before class, clear the test data from the RTDB:

```bash
# In a browser, sign into Firebase console at biol2-bb1, navigate to
# Realtime Database -> rd20 -> delete the rd20 node entirely. New nodes
# auto-create on first team join Wednesday morning.
```

Or via Firebase CLI:

```bash
firebase --project biol2-bb1 database:remove /rd20 -y
```

---

## Audit export after class (run from your terminal)

```bash
cd "/Users/giorgiolagna/Documents/Claude/Projects/BIOL2-S26/03_week_materials/week_08/rd20_game"
python3 export_rd20.py
# Produces: rd20_results_2026-05-20.csv with per-team bets, answers, points per question
```

---

## Question key (instructor reference, NOT student-visible)

| Q | Category | Correct | Notes |
|---|---|---|---|
| 1 | Epi curve: final size | A | LO3.5, Source Layer Part 4 |
| 2 | Epi curve: steepness and R0 | D | LO3.5, Item 25 |
| 3 | Epi curve: plateau | A | LO3.5, CP#17 vocabulary |
| 4 | Epi curve: post-peak decline | C | LO3.5, susceptible pool depletion |
| 5 | R0 estimation | B | LO3.5, Item 24 R0 content |
| 6 | R0: generation growth | C | LO3.5, per-person-average reasoning |
| 7 | Attack rate: single group | B | LO3.5, Item 29 form |
| **8 (DOUBLE)** | Wager Question: 2x2 attack-rate comparison | **D** | LO3.5 Analyze, previews the workshop foodborne worked example and BB3 Phase 1 |

Source bank: `04_assessments/BIOL2_RD20_S23_Outbreak.md` (full rationales).

---

## Known gotcha

This clone was made with the `.bak` files already removed. If a future re-clone leaves `.bak` artifacts, they are not deployed (firebase.json `ignore` covers `**/.*`), but you can clean them with `rm *.bak` in this folder.
