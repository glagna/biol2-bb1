# Firebase RTDB rules status for RD20 — Fri May 15 readiness

**Verified 2026-05-14 22:00 PT** by Claude via direct HTTP PUT probes to the Firebase RTDB REST endpoint.

## TL;DR

**No rules deployment is needed for tomorrow.** Deployed rules are still in test mode and will accept the game's writes. The local `database.rules.json` in this folder has been updated with hardened (auth-required) rules for future use, but **do not deploy them tonight** because the RD client does not authenticate and the hardened rules would block all writes.

## What the probe showed

| Probe | Result |
|---|---|
| `PUT /rd20/state/phase = "probe"` (unauthenticated) | Succeeded |
| `PUT /rd16/state/phase = "probe"` (unauthenticated) | Succeeded |
| `GET /rd20/state` (unauthenticated) | Succeeded (read returned the value just written) |
| `GET /rd16/state` (unauthenticated) | Succeeded |

Both probe values were deleted immediately after the test. /rd20/state is back to null; /rd16/state retains the answerKey + currentQ from past RD16 games and is fine.

## Why this matters

The local `rd16_game/database.rules.json` file is **stale relative to what is actually deployed**. The local file declares hardened rules requiring `auth.uid`. The deployed rules in the Firebase console are still the wide-open test-mode rules from when the database was provisioned. Test-mode rules expire roughly one month after creation; memory `reference_bb1_firebase_project` notes the current window expires around **2026-05-16**.

The RD client (`index.html`, `host.html`, `leaderboard.html`) does **not** call `signInAnonymously()`. It never authenticates. If we deploy the hardened rules tonight, every write from the game will fail because `auth.uid` will be null. RD20 would 100% break Friday morning.

## What to do — three paths after Friday

These are post-class options; none are required for tomorrow.

1. **Easiest: extend test mode in the Firebase console.** Console > Realtime Database > Rules. Find the line that says something like `"$exp": "auth != null || now < 1747401600000"` (the epoch timestamp is the expiry). Bump the timestamp forward by a month or three. Publish. Done. This buys time until you're ready for option 2 or 3.

2. **Middle: deploy permissive-but-validated rules.** Write rules that don't require auth but do validate field shapes (string lengths, A/B/C/D constraints, numeric bet ranges 1-3). Slightly safer than pure test mode against accidental garbage writes. Roughly what the deployed rules already look like minus the `auth.uid` checks.

3. **Best: deploy the hardened rules in `database.rules.json` AND add `signInAnonymously()` to the client.** Three lines of client code in `index.html` / `host.html` / `leaderboard.html` (import Auth, get an anon user, then use the Firestore SDK as today). This is the right long-term answer; about 30 min of work and a smoke test.

The hardened rules now sitting in `database.rules.json` cover rd13 through rd20 with the same per-round structure (state writeable only by hosts, teams writeable by team or host, hosts node read-only). When you're ready for option 3, the rules file is paste-ready.

## Files in this folder relevant to rules

- `database.rules.json` — hardened rules covering rd13-rd20 + bb1 (do not deploy tonight)
- `firebase.json` — Firebase project config; carried from rd15_game template; unused for GH Pages deploy
