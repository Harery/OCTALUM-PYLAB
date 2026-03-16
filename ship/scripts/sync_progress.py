#!/usr/bin/env python3
"""
PROGRESS.md Sync Script

Scans the codebase and updates PROGRESS.md with actual completion status.
This connects the gamified progress tracker to real file completion.

Usage:
    python ship/scripts/sync_progress.py

Time Complexity: O(n) where n = total files
Space Complexity: O(1)
"""

from __future__ import annotations

import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.parent.parent

# XP values for different content types
XP_VALUES = {
    "foundation": 15,
    "data_structure": 25,
    "algorithm": 30,
    "pattern": 35,
    "challenge_easy": 20,
    "challenge_medium": 40,
    "challenge_hard": 60,
    "notebook": 30,
}


def count_files(directory: str, pattern: str = "*.py") -> int:
    """Count files matching pattern in directory."""
    dir_path = PROJECT_ROOT / directory
    if not dir_path.exists():
        return 0
    return len(list(dir_path.rglob(pattern)))


def count_notebooks() -> int:
    """Count Jupyter notebooks."""
    notebooks_dir = PROJECT_ROOT / "learn" / "notebooks"
    if not notebooks_dir.exists():
        return 0
    return len(list(notebooks_dir.glob("*.ipynb")))


def count_challenges() -> dict[str, int]:
    """Count challenge problems by difficulty."""
    challenges_dir = PROJECT_ROOT / "build" / "challenges"
    counts: dict[str, int] = {"easy": 0, "medium": 0, "hard": 0}

    for difficulty in counts:
        diff_dir = challenges_dir / f"leetcode-{difficulty}"
        if diff_dir.exists():
            counts[difficulty] = len(
                [f for f in diff_dir.glob("*.py") if not f.name.startswith("_")]
            )

    return counts


def count_foundations() -> dict[str, int]:
    """Count foundation files."""
    foundations_dir = PROJECT_ROOT / "build" / "foundations"
    if not foundations_dir.exists():
        return {}

    counts: dict[str, int] = {}
    for subdir in foundations_dir.iterdir():
        if subdir.is_dir():
            py_files = len([f for f in subdir.glob("*.py") if not f.name.startswith("_")])
            if py_files > 0:
                counts[subdir.name] = py_files
    return counts


def count_data_structures() -> dict[str, int]:
    """Count data structure files."""
    ds_dir = PROJECT_ROOT / "build" / "data-structures"
    if not ds_dir.exists():
        return {}

    counts: dict[str, int] = {}
    for subdir in ds_dir.iterdir():
        if subdir.is_dir():
            py_files = len([f for f in subdir.glob("*.py") if not f.name.startswith("_")])
            if py_files > 0:
                counts[subdir.name] = py_files
    return counts


def count_algorithms() -> dict[str, int]:
    """Count algorithm files."""
    algo_dir = PROJECT_ROOT / "build" / "algorithms"
    if not algo_dir.exists():
        return {}

    counts: dict[str, int] = {}
    for subdir in algo_dir.iterdir():
        if subdir.is_dir():
            py_files = len([f for f in subdir.glob("*.py") if not f.name.startswith("_")])
            if py_files > 0:
                counts[subdir.name] = py_files
    return counts


def count_patterns() -> dict[str, int]:
    """Count pattern files."""
    patterns_dir = PROJECT_ROOT / "build" / "patterns"
    if not patterns_dir.exists():
        return {}

    counts: dict[str, int] = {}
    for subdir in patterns_dir.iterdir():
        if subdir.is_dir():
            py_files = len([f for f in subdir.glob("*.py") if not f.name.startswith("_")])
            if py_files > 0:
                counts[subdir.name] = py_files
    return counts


def calculate_total_xp() -> tuple[int, int]:
    """Calculate total XP earned and max possible."""
    xp_earned = 0

    # Challenges
    challenges = count_challenges()
    xp_earned += challenges["easy"] * XP_VALUES["challenge_easy"]
    xp_earned += challenges["medium"] * XP_VALUES["challenge_medium"]
    xp_earned += challenges["hard"] * XP_VALUES["challenge_hard"]

    # Notebooks
    xp_earned += count_notebooks() * XP_VALUES["notebook"]

    # Foundations
    for _name, count in count_foundations().items():
        xp_earned += count * XP_VALUES["foundation"]

    # Data Structures
    for _name, count in count_data_structures().items():
        xp_earned += count * XP_VALUES["data_structure"]

    # Algorithms
    for _name, count in count_algorithms().items():
        xp_earned += count * XP_VALUES["algorithm"]

    # Patterns
    for _name, count in count_patterns().items():
        xp_earned += count * XP_VALUES["pattern"]

    # Max XP for 100% (approximate target)
    max_xp = 1000

    return min(xp_earned, max_xp), max_xp


def get_level(xp: int) -> tuple[str, str]:
    """Get level name and emoji based on XP."""
    if xp < 100:
        return "🎓 Learner", "learners"
    elif xp < 250:
        return "⚡ Coder", "coders"
    elif xp < 500:
        return "🔥 Developer", "developers"
    elif xp < 750:
        return "💎 Engineer", "engineers"
    else:
        return "🏆 Master", "masters"


def generate_progress_bar(percentage: int) -> str:
    """Generate ASCII progress bar."""
    filled = percentage // 5
    empty = 20 - filled
    return "█" * filled + "░" * empty


def update_progress_md() -> None:
    """Update PROGRESS.md with current statistics."""
    progress_file = PROJECT_ROOT / "PROGRESS.md"

    xp, max_xp = calculate_total_xp()
    percentage = min((xp / max_xp) * 100, 100) if max_xp > 0 else 0
    level, _ = get_level(xp)

    challenges = count_challenges()
    notebooks = count_notebooks()

    content = f"""# 🎮 Learning Progress Tracker

Track your journey from Python novice to algorithm master!

---

## 📊 Overall Progress

```
{generate_progress_bar(int(percentage))}  {percentage:.0f}% Complete
```

| Stat | Value |
|------|-------|
| **Level** | {level} |
| **Total XP** | {xp} / {max_xp} |
| **Current Streak** | 0 days |
| **Last Practice** | Not started |

---

## 🏅 Badges

| Badge | Status | Requirement |
|-------|--------|-------------|
| 🐍 Python Novice | {'✅ Earned' if xp >= 100 else '🔒 Locked'} | Complete foundations (100 XP) |
| 📊 Data Master | {'✅ Earned' if xp >= 250 else '🔒 Locked'} | Complete data structures (250 XP) |
| ⚡ Algo Ninja | {'✅ Earned' if xp >= 400 else '🔒 Locked'} | Complete algorithms (400 XP) |
| 🧩 Pattern Pro | {'✅ Earned' if xp >= 600 else '🔒 Locked'} | Master patterns (600 XP) |
| 🏆 Interview Ready | {'✅ Earned' if xp >= 800 else '🔒 Locked'} | Complete challenges (800 XP) |
| 💎 OCTALUM Scholar | {'✅ Earned' if xp >= 1000 else '🔒 Locked'} | 100% completion (1000 XP) |

---

## 📝 Challenge Problems

| Difficulty | Completed | XP Each |
|------------|-----------|---------|
| 🟢 Easy | {challenges['easy']} | +20 |
| 🟡 Medium | {challenges['medium']} | +40 |
| 🔴 Hard | {challenges['hard']} | +60 |

**Total Challenge XP:** {challenges['easy'] * 20 + challenges['medium'] * 40 + challenges['hard'] * 60}

---

## 📓 Notebooks

| Notebook | Status |
|----------|--------|
| Sorting Visualization | {'✅' if notebooks >= 1 else '🔒'} |
| BST Visualization | {'✅' if notebooks >= 2 else '🔒'} |
| DP Visualization | {'✅' if notebooks >= 3 else '🔒'} |
| Graph Traversal | {'✅' if notebooks >= 4 else '🔒'} |
| Pattern Recognition | {'✅' if notebooks >= 5 else '🔒'} |

---

## 🎯 Next Goals

"""

    # Add recommendations based on current progress
    if challenges["hard"] < 5:
        content += "- [ ] Complete 5 LeetCode Hard problems (+300 XP)\n"
    if challenges["medium"] < 10:
        content += "- [ ] Complete 10 LeetCode Medium problems (+400 XP)\n"
    if notebooks < 5:
        content += "- [ ] Complete all 5 Jupyter notebooks (+150 XP)\n"

    content += """
---

*Last updated automatically by `sync_progress.py`*
"""

    with progress_file.open("w") as f:
        f.write(content)

    print(f"✅ PROGRESS.md updated!")
    print(f"   XP: {xp}/{max_xp} ({percentage:.0f}%)")
    print(f"   Level: {level}")
    print(f"   Challenges: {challenges['easy']} easy, {challenges['medium']} medium, {challenges['hard']} hard")


def main() -> int:
    """Main entry point."""
    print("🔄 Syncing PROGRESS.md with actual file completion...\n")
    update_progress_md()
    return 0


if __name__ == "__main__":
    exit(main())
