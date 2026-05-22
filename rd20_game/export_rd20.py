#!/usr/bin/env python3
"""
Export RD20 Wager Arena results from Firebase to CSV.

Usage:
    python3 export_rd20.py

Outputs two files in the current directory:
    rd20_results_YYYYMMDD_HHMM.csv     — full per-team grid (audit trail)
    rd20_leaderboard_YYYYMMDD_HHMM.csv — sorted ranking (for XP entry)

Plus prints the leaderboard to your terminal for quick reference.

No Firebase auth required — DB is in test mode (read access open).
"""

import csv
import json
import sys
import urllib.request
from datetime import datetime

DB = "https://biol2-bb1-default-rtdb.firebaseio.com"

def fetch():
    url = f"{DB}/rd20.json"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())

def compute_score_breakdown(team_data, answer_key):
    """Return per-question (bet, ans, correct, pts) tuples + total."""
    bets = team_data.get("bets", {})
    answers = team_data.get("answers", {})
    rows = []
    total = 0
    for i in range(1, 9):
        q = f"q{i}"
        bet = bets.get(q)
        ans = answers.get(q)
        correct = answer_key.get(q)
        if bet is not None and ans is not None and correct is not None:
            sign = 1 if ans == correct else -1
            mult = 2 if i == 8 else 1
            pts = bet * sign * mult
        else:
            pts = 0
        rows.append({"q": i, "bet": bet, "ans": ans, "correct": correct, "pts": pts})
        total += pts
    return rows, total

def main():
    print("Fetching /rd20 from Firebase...")
    try:
        data = fetch()
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    state = data.get("state", {}) or {}
    teams = data.get("teams", {}) or {}
    key = state.get("answerKey", {}) or {}
    phase = state.get("phase", "?")

    if not teams:
        print("WARNING: no teams in /rd20/teams. Did you run the round?")
    if not key:
        print("WARNING: no answer key set. Scores will all be 0.")

    print(f"State phase: {phase}")
    print(f"Answer key:  {dict(sorted(key.items()))}")
    print(f"Teams found: {len(teams)} ({', '.join(sorted(teams.keys()))})")
    print()

    # Compute per-team breakdowns
    leaderboard = []
    detail_rows = []
    for team_name in sorted(teams.keys()):
        rows, total = compute_score_breakdown(teams[team_name], key)
        detail_rows.append({"team": team_name, "rows": rows, "total": total})
        leaderboard.append({"team": team_name, "total": total})

    # Sort leaderboard descending; assign DENSE rank with tie handling
    # Tied teams share rank; XP is awarded for rank 1, 2, 3 (15/10/5).
    # Ties at rank 1 all get 15 XP; tied at rank 2 all get 10; etc.
    leaderboard.sort(key=lambda x: -x["total"])
    rank = 0
    last_total = None
    for i, entry in enumerate(leaderboard, 1):
        if entry["total"] != last_total:
            rank = i
            last_total = entry["total"]
        entry["rank"] = rank

    rank_by_team = {e["team"]: e["rank"] for e in leaderboard}

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    # ============================================================
    # Detail CSV: full per-team grid
    # ============================================================
    detail_path = f"rd20_results_{timestamp}.csv"
    with open(detail_path, "w", newline="") as f:
        w = csv.writer(f)
        # Header rows
        w.writerow(["RD20 Wager Arena Results", f"exported {datetime.now().isoformat(timespec='seconds')}"])
        w.writerow(["Phase:", phase, "Total teams:", len(teams)])
        w.writerow(["Answer key:"] + [key.get(f"q{i}", "?") for i in range(1, 9)])
        w.writerow([])

        # Grid header
        header = ["Rank", "Team"]
        for i in range(1, 9):
            label = f"Q{i}" + (" (2x)" if i == 8 else "")
            header += [f"{label} Bet", f"{label} Ans", f"{label} Pts"]
        header += ["Total"]
        w.writerow(header)

        for entry in detail_rows:
            row = [rank_by_team[entry["team"]], entry["team"]]
            for r in entry["rows"]:
                row += [r["bet"] if r["bet"] is not None else "",
                        r["ans"] if r["ans"] is not None else "",
                        r["pts"]]
            row += [entry["total"]]
            w.writerow(row)

    # ============================================================
    # Leaderboard CSV: rank-ordered for XP entry
    # ============================================================
    lb_path = f"rd20_leaderboard_{timestamp}.csv"
    with open(lb_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["RD20 Leaderboard", f"exported {datetime.now().isoformat(timespec='seconds')}"])
        w.writerow([])
        w.writerow(["Rank", "Team", "Total Points", "XP Award"])
        XP = {1: 15, 2: 10, 3: 5}
        for entry in leaderboard:
            xp = XP.get(entry["rank"], 0)
            w.writerow([entry["rank"], entry["team"], entry["total"], xp if xp else ""])

    # ============================================================
    # Print to terminal
    # ============================================================
    print("=" * 60)
    print(f"{'RANK':<6}{'TEAM':<8}{'TOTAL':>8}   XP")
    print("-" * 60)
    XP = {1: 15, 2: 10, 3: 5}
    for entry in leaderboard:
        xp_str = f"+{XP[entry['rank']]} XP" if entry["rank"] in XP else ""
        print(f"{entry['rank']:<6}{entry['team']:<8}{entry['total']:>+8}   {xp_str}")
    print("=" * 60)
    print(f"\nFiles written:")
    print(f"  {detail_path}")
    print(f"  {lb_path}")

if __name__ == "__main__":
    main()
