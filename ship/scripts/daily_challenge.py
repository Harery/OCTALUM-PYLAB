#!/usr/bin/env python3
"""Daily Challenge CLI - Get personalized coding challenges.

Usage:
    uv run daily-challenge                    # Get today's challenge
    uv run daily-challenge --category trees   # Specific category
    uv run daily-challenge --difficulty hard  # Specific difficulty
    uv run daily-challenge --log              # Log completion
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime
from pathlib import Path

# Project structure
PROJECT_ROOT = Path(__file__).parent.parent.parent
CHALLENGES_DIR = PROJECT_ROOT / "build" / "challenges"
PROGRESS_DIR = PROJECT_ROOT / "record" / "progress"
PROGRESS_FILE = PROGRESS_DIR / "daily_challenges.json"

# Categories and their directories
CATEGORIES: dict[str, str] = {
    "arrays": "leetcode-easy",
    "linked-lists": "leetcode-easy",
    "stacks-queues": "leetcode-easy",
    "trees": "leetcode-easy",
    "graphs": "leetcode-easy",
    "dynamic-programming": "leetcode-easy",
    "medium": "leetcode-medium",
    "hard": "leetcode-hard",
}

DIFFICULTIES = ["easy", "medium", "hard"]


def get_available_problems(
    category: str | None = None, difficulty: str | None = None
) -> list[dict[str, str]]:
    """Scan challenge directories for available problems."""
    problems = []

    # Determine which directories to scan
    dirs_to_scan = []
    if difficulty:
        dirs_to_scan.append(f"leetcode-{difficulty}")
    else:
        dirs_to_scan = ["leetcode-easy", "leetcode-medium", "leetcode-hard"]

    for dir_name in dirs_to_scan:
        challenge_dir = CHALLENGES_DIR / dir_name
        if not challenge_dir.exists():
            continue

        for py_file in challenge_dir.glob("*.py"):
            if py_file.name.startswith("_"):
                continue

            # Extract problem info from filename
            parts = py_file.stem.split("_", 1)
            problem_id = parts[0] if parts else "???"
            problem_name = parts[1].replace("_", " ").title() if len(parts) > 1 else py_file.stem

            problems.append({
                "id": problem_id,
                "name": problem_name,
                "file": str(py_file.relative_to(PROJECT_ROOT)),
                "difficulty": dir_name.replace("leetcode-", ""),
                "category": _guess_category(py_file.stem),
            })

    return problems


def _guess_category(filename: str) -> str:
    """Guess category from filename keywords."""
    filename_lower = filename.lower()

    if any(kw in filename_lower for kw in ["tree", "bst", "binary"]):
        return "trees"
    if any(kw in filename_lower for kw in ["linked", "list", "node"]):
        return "linked-lists"
    if any(kw in filename_lower for kw in ["stack", "queue", "paren"]):
        return "stacks-queues"
    if any(kw in filename_lower for kw in ["graph", "island", "path"]):
        return "graphs"
    if any(kw in filename_lower for kw in ["dp", "climb", "coin", "subsequence"]):
        return "dynamic-programming"

    return "arrays"


def load_progress() -> dict:
    """Load progress from JSON file."""
    if not PROGRESS_FILE.exists():
        return {"completed": [], "history": []}

    with PROGRESS_FILE.open() as f:
        return json.load(f)


def save_progress(data: dict) -> None:
    """Save progress to JSON file."""
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)

    with PROGRESS_FILE.open("w") as f:
        json.dump(data, f, indent=2)


def get_todays_challenge(category: str | None, difficulty: str | None) -> dict | None:
    """Select a challenge for today."""
    problems = get_available_problems(category, difficulty)

    if not problems:
        return None

    # Load progress to avoid repeats
    progress = load_progress()
    completed_ids = {p["id"] for p in progress.get("completed", [])}

    # Prefer uncompleted problems
    uncompleted = [p for p in problems if p["id"] not in completed_ids]

    if uncompleted:
        return random.choice(uncompleted)

    return random.choice(problems)


def display_challenge(problem: dict) -> None:
    """Display the challenge with colored output."""
    # Color codes
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Difficulty color
    diff_colors = {"easy": GREEN, "medium": YELLOW, "hard": RED}
    diff_color = diff_colors.get(problem["difficulty"], "")

    # Estimated time based on difficulty
    time_estimates = {"easy": "15-20 min", "medium": "30-45 min", "hard": "60+ min"}
    time_est = time_estimates.get(problem["difficulty"], "???")

    print(f"\n{BOLD}{BLUE}{'=' * 50}{RESET}")
    print(f"{BOLD}  DAILY CHALLENGE{RESET}")
    print(f"{BLUE}{'=' * 50}{RESET}\n")

    print(f"  {BOLD}Problem:{RESET}  #{problem['id']} - {problem['name']}")
    print(f"  {BOLD}Category:{RESET} {problem['category']}")
    print(f"  {BOLD}Difficulty:{RESET} {diff_color}{problem['difficulty'].upper()}{RESET}")
    print(f"  {BOLD}Est. Time:{RESET} {time_est}")
    print(f"\n  {BOLD}File:{RESET} {problem['file']}")

    print(f"\n{BLUE}{'=' * 50}{RESET}")
    print(f"  Run: {GREEN}code {problem['file']}{RESET}")
    print(f"  Log: {GREEN}uv run daily-challenge --log{RESET}")
    print(f"{BLUE}{'=' * 50}{RESET}\n")


def log_completion(problem: dict) -> None:
    """Log completion of today's challenge."""
    progress = load_progress()

    entry = {
        "id": problem["id"],
        "name": problem["name"],
        "difficulty": problem["difficulty"],
        "completed_at": datetime.now().isoformat(),
    }

    # Add to completed list (avoid duplicates)
    completed = progress.get("completed", [])
    if not any(c["id"] == problem["id"] for c in completed):
        completed.append(entry)

    # Add to history
    history = progress.get("history", [])
    history.append(entry)

    progress["completed"] = completed
    progress["history"] = history

    save_progress(progress)

    print(f"\n\033[92m[+] Challenge #{problem['id']} marked as complete!\033[0m")
    print(f"    Total completed: {len(completed)} problems\n")


def show_stats() -> None:
    """Display progress statistics."""
    progress = load_progress()
    completed = progress.get("completed", [])

    print("\n\033[1m  DAILY CHALLENGE STATS\033[0m")
    print("  " + "=" * 40)

    if not completed:
        print("  No challenges completed yet.")
        print("  Run 'uv run daily-challenge' to get started!\n")
        return

    # Count by difficulty
    by_difficulty: dict[str, int] = {}
    for p in completed:
        diff = p.get("difficulty", "unknown")
        by_difficulty[diff] = by_difficulty.get(diff, 0) + 1

    print(f"  Total completed: {len(completed)}")
    print("\n  By difficulty:")
    for diff in DIFFICULTIES:
        count = by_difficulty.get(diff, 0)
        bar = "#" * count
        print(f"    {diff:8} {bar} ({count})")

    print()


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Daily coding challenge selector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    uv run daily-challenge                    Get today's challenge
    uv run daily-challenge --category trees   Get a tree problem
    uv run daily-challenge --difficulty hard  Get a hard problem
    uv run daily-challenge --log              Log completion
    uv run daily-challenge --stats            Show progress
        """,
    )

    parser.add_argument(
        "--category", "-c",
        choices=list(CATEGORIES.keys()),
        help="Filter by category",
    )
    parser.add_argument(
        "--difficulty", "-d",
        choices=DIFFICULTIES,
        help="Filter by difficulty",
    )
    parser.add_argument(
        "--log", "-l",
        action="store_true",
        help="Log completion of last challenge",
    )
    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Show progress statistics",
    )

    args = parser.parse_args()

    if args.stats:
        show_stats()
        return 0

    if args.log:
        # Get last challenge from progress
        progress = load_progress()
        history = progress.get("history", [])
        if not history:
            print("\n\033[91m[!] No challenge to log. Get one first!\033[0m\n")
            return 1

        last = history[-1]
        log_completion(last)
        return 0

    # Get and display challenge
    problem = get_todays_challenge(args.category, args.difficulty)

    if not problem:
        print("\n\033[91m[!] No problems found matching criteria.\033[0m\n")
        return 1

    display_challenge(problem)
    return 0


if __name__ == "__main__":
    sys.exit(main())
