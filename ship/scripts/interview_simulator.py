#!/usr/bin/env python3
"""Interview Simulator CLI - Practice coding interviews under timed conditions.

Usage:
    uv run interview-sim                    # Start interactive session
    uv run interview-sim --company google   # Company-specific focus
    uv run interview-sim --level senior     # Difficulty level
    uv run interview-sim --time 30          # Custom time limit
"""

from __future__ import annotations

import argparse
import json
import random
import signal
import sys
import time
from datetime import datetime
from pathlib import Path

# Project structure
PROJECT_ROOT = Path(__file__).parent.parent.parent
CHALLENGES_DIR = PROJECT_ROOT / "build" / "challenges"
PROGRESS_DIR = PROJECT_ROOT / "record" / "progress"
SESSIONS_FILE = PROGRESS_DIR / "interview_sessions.json"

# Company profiles with problem preferences
COMPANY_PROFILES: dict[str, dict] = {
    "google": {
        "focus": ["graphs", "dynamic-programming", "arrays"],
        "difficulty_dist": {"easy": 0.1, "medium": 0.5, "hard": 0.4},
        "tips": "Focus on scalability and edge cases. Explain your thought process.",
    },
    "amazon": {
        "focus": ["trees", "arrays", "system-design"],
        "difficulty_dist": {"easy": 0.2, "medium": 0.5, "hard": 0.3},
        "tips": "Use STAR method for behavioral. Think about leadership principles.",
    },
    "meta": {
        "focus": ["arrays", "strings", "two-pointers"],
        "difficulty_dist": {"easy": 0.15, "medium": 0.6, "hard": 0.25},
        "tips": "Move fast, optimize later. Focus on clean, readable code.",
    },
    "startup": {
        "focus": ["arrays", "strings", "dynamic-programming"],
        "difficulty_dist": {"easy": 0.3, "medium": 0.5, "hard": 0.2},
        "tips": "Show versatility. Be ready to wear multiple hats.",
    },
}

# Level difficulty multipliers
LEVEL_CONFIG: dict[str, dict] = {
    "junior": {"easy": 0.5, "medium": 0.35, "hard": 0.15},
    "mid": {"easy": 0.2, "medium": 0.5, "hard": 0.3},
    "senior": {"easy": 0.1, "medium": 0.4, "hard": 0.5},
}


def get_available_problems() -> list[dict[str, str]]:
    """Scan all challenge directories for problems."""
    problems = []

    for difficulty in ["easy", "medium", "hard"]:
        challenge_dir = CHALLENGES_DIR / f"leetcode-{difficulty}"
        if not challenge_dir.exists():
            continue

        for py_file in challenge_dir.glob("*.py"):
            if py_file.name.startswith("_"):
                continue

            parts = py_file.stem.split("_", 1)
            problem_id = parts[0] if parts else "???"
            problem_name = parts[1].replace("_", " ").title() if len(parts) > 1 else py_file.stem

            problems.append({
                "id": problem_id,
                "name": problem_name,
                "file": str(py_file.relative_to(PROJECT_ROOT)),
                "difficulty": difficulty,
                "category": _guess_category(py_file.stem),
            })

    return problems


def _guess_category(filename: str) -> str:
    """Guess category from filename."""
    filename_lower = filename.lower()

    if any(kw in filename_lower for kw in ["tree", "bst", "binary"]):
        return "trees"
    if any(kw in filename_lower for kw in ["linked", "list"]):
        return "linked-lists"
    if any(kw in filename_lower for kw in ["stack", "queue", "paren"]):
        return "stacks-queues"
    if any(kw in filename_lower for kw in ["graph", "island", "path"]):
        return "graphs"
    if any(kw in filename_lower for kw in ["sub", "window", "string"]):
        return "strings"
    if any(kw in filename_lower for kw in ["pointer", "sum", "two"]):
        return "two-pointers"
    if any(kw in filename_lower for kw in ["dp", "climb", "coin"]):
        return "dynamic-programming"

    return "arrays"


def select_problem(
    problems: list[dict],
    company: str | None,
    level: str,
) -> dict | None:
    """Select a problem based on company and level preferences."""
    if not problems:
        return None

    # Get difficulty distribution
    if company and company in COMPANY_PROFILES:
        dist = COMPANY_PROFILES[company]["difficulty_dist"]
    else:
        dist = LEVEL_CONFIG.get(level, LEVEL_CONFIG["mid"])

    # Choose difficulty based on distribution
    rand_val = random.random()
    cumulative = 0.0
    chosen_diff = "medium"

    for diff, prob in dist.items():
        cumulative += prob
        if rand_val <= cumulative:
            chosen_diff = diff
            break

    # Filter by difficulty
    filtered = [p for p in problems if p["difficulty"] == chosen_diff]

    if not filtered:
        filtered = problems  # Fallback to all

    # Prefer company focus categories
    if company and company in COMPANY_PROFILES:
        focus = COMPANY_PROFILES[company]["focus"]
        focus_problems = [p for p in filtered if p["category"] in focus]
        if focus_problems:
            return random.choice(focus_problems)

    return random.choice(filtered)


def load_sessions() -> dict:
    """Load session history."""
    if not SESSIONS_FILE.exists():
        return {"sessions": []}

    with SESSIONS_FILE.open() as f:
        return json.load(f)


def save_sessions(data: dict) -> None:
    """Save session history."""
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)

    with SESSIONS_FILE.open("w") as f:
        json.dump(data, f, indent=2)


def run_timer(minutes: int, problem: dict, company: str | None) -> dict:
    """Run countdown timer with warnings."""
    total_seconds = minutes * 60
    warnings_at = {15 * 60, 10 * 60, 5 * 60, 1 * 60}
    warned = set()

    start_time = time.time()
    completed = False

    # Colors
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Company tips
    tips = ""
    if company and company in COMPANY_PROFILES:
        tips = f"\n  {BLUE}Tips: {COMPANY_PROFILES[company]['tips']}{RESET}"

    def handle_interrupt(_signum, _frame):
        """Handle Ctrl+C gracefully."""
        nonlocal completed
        print(f"\n\n{YELLOW}[!] Session interrupted. Saving progress...{RESET}")
        completed = True

    signal.signal(signal.SIGINT, handle_interrupt)

    print(f"\n{BOLD}{GREEN}{'=' * 60}{RESET}")
    print(f"{BOLD}  INTERVIEW SESSION STARTED{RESET}")
    print(f"{GREEN}{'=' * 60}{RESET}")
    print(f"\n  {BOLD}Problem:{RESET} #{problem['id']} - {problem['name']}")
    print(f"  {BOLD}Difficulty:{RESET} {problem['difficulty']}")
    print(f"  {BOLD}Category:{RESET} {problem['category']}")
    print(f"  {BOLD}Time Limit:{RESET} {minutes} minutes")
    print(f"\n  {BOLD}File:{RESET} {problem['file']}")
    if company:
        print(f"  {BOLD}Company:{RESET} {company.upper()}{tips}")
    print(f"\n{GREEN}{'=' * 60}{RESET}")
    print(f"\n  Open the file and start coding!")
    print(f"  Press Ctrl+C when done or to end early.\n")

    while not completed:
        elapsed = time.time() - start_time
        remaining = total_seconds - elapsed

        if remaining <= 0:
            print(f"\n{RED}[TIME'S UP!] Session ended.{RESET}\n")
            break

        # Check for warnings
        for warn_time in warnings_at:
            if remaining <= warn_time and warn_time not in warned:
                warned.add(warn_time)
                mins = warn_time // 60
                if mins > 0:
                    print(f"{YELLOW}[!] {mins} minutes remaining!{RESET}")
                else:
                    print(f"{RED}[!] Less than 1 minute!{RESET}")

        # Display time
        mins = int(remaining // 60)
        secs = int(remaining % 60)
        time_str = f"\r  Time remaining: {mins:02d}:{secs:02d}  "
        sys.stdout.write(time_str)
        sys.stdout.flush()
        time.sleep(1)

    elapsed = time.time() - start_time

    return {
        "problem_id": problem["id"],
        "problem_name": problem["name"],
        "difficulty": problem["difficulty"],
        "category": problem["category"],
        "company": company,
        "time_limit": minutes,
        "actual_time": round(elapsed / 60, 1),
        "completed_at": datetime.now().isoformat(),
    }


def generate_feedback(session: dict) -> str:
    """Generate feedback based on session."""
    lines = []
    lines.append("\n" + "=" * 50)
    lines.append("  SESSION SUMMARY")
    lines.append("=" * 50)

    time_ratio = session["actual_time"] / session["time_limit"]

    if time_ratio <= 0.5:
        lines.append(f"\n  Speed: FAST (completed in {session['actual_time']:.1f}/{session['time_limit']} min)")
        lines.append("  Great pace! Make sure you're not rushing.")
    elif time_ratio <= 0.8:
        lines.append(f"\n  Speed: GOOD (completed in {session['actual_time']:.1f}/{session['time_limit']} min)")
        lines.append("  Solid timing. Keep practicing for consistency.")
    else:
        lines.append(f"\n  Speed: SLOW (completed in {session['actual_time']:.1f}/{session['time_limit']} min)")
        lines.append("  Consider practicing similar problems to improve speed.")

    lines.append(f"\n  Category: {session['category']}")
    lines.append(f"  Difficulty: {session['difficulty']}")

    if session.get("company"):
        lines.append(f"  Company: {session['company'].upper()}")

    lines.append("\n  Next steps:")
    lines.append("  - Review your solution")
    lines.append("  - Compare with optimal approach")
    lines.append("  - Practice similar problems")
    lines.append("=" * 50 + "\n")

    return "\n".join(lines)


def show_stats() -> None:
    """Display interview statistics."""
    data = load_sessions()
    sessions = data.get("sessions", [])

    print("\n\033[1m  INTERVIEW SIMULATOR STATS\033[0m")
    print("  " + "=" * 40)

    if not sessions:
        print("  No sessions completed yet.")
        print("  Run 'uv run interview-sim' to start practicing!\n")
        return

    total_time = sum(s.get("actual_time", 0) for s in sessions)
    by_company: dict[str, int] = {}
    by_difficulty: dict[str, int] = {}

    for s in sessions:
        company = s.get("company", "general")
        by_company[company] = by_company.get(company, 0) + 1
        diff = s.get("difficulty", "unknown")
        by_difficulty[diff] = by_difficulty.get(diff, 0) + 1

    print(f"  Total sessions: {len(sessions)}")
    print(f"  Total practice time: {total_time:.1f} minutes")
    print("\n  By difficulty:")
    for diff in ["easy", "medium", "hard"]:
        count = by_difficulty.get(diff, 0)
        bar = "#" * count
        print(f"    {diff:8} {bar} ({count})")

    print("\n  By company:")
    for company, count in sorted(by_company.items()):
        print(f"    {company:12} {count} sessions")

    print()


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Coding interview simulator with timed sessions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    uv run interview-sim                    Start interactive session
    uv run interview-sim --company google   Google-style interview
    uv run interview-sim --level senior     Senior-level problems
    uv run interview-sim --time 30          30-minute session
    uv run interview-sim --stats            Show progress stats
        """,
    )

    parser.add_argument(
        "--company", "-c",
        choices=list(COMPANY_PROFILES.keys()),
        help="Company-specific interview focus",
    )
    parser.add_argument(
        "--level", "-l",
        choices=list(LEVEL_CONFIG.keys()),
        default="mid",
        help="Experience level (default: mid)",
    )
    parser.add_argument(
        "--time", "-t",
        type=int,
        default=45,
        help="Time limit in minutes (default: 45)",
    )
    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Show session statistics",
    )

    args = parser.parse_args()

    if args.stats:
        show_stats()
        return 0

    # Get problems and select one
    problems = get_available_problems()

    if not problems:
        print("\n\033[91m[!] No problems found. Add problems to build/challenges/\033[0m\n")
        return 1

    problem = select_problem(problems, args.company, args.level)

    if not problem:
        print("\n\033[91m[!] Could not select a problem.\033[0m\n")
        return 1

    # Run the timed session
    session = run_timer(args.time, problem, args.company)

    # Save session
    data = load_sessions()
    data.setdefault("sessions", []).append(session)
    save_sessions(data)

    # Generate feedback
    print(generate_feedback(session))

    return 0


if __name__ == "__main__":
    sys.exit(main())
