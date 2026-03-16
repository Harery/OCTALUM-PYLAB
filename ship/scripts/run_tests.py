#!/usr/bin/env python3
"""
OCTALUM-PYLAB Test Runner

Run tests for the learning repository.

Usage:
    python ship/scripts/run_tests.py              # Run all tests
    python ship/scripts/run_tests.py --coverage   # Run with coverage
    python ship/scripts/run_tests.py --watch      # Watch mode
    python ship/scripts/run_tests.py foundations  # Run specific module
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
TEST_DIR = PROJECT_ROOT / "verify" / "tests"


def run_pytest(args: list[str]) -> int:
    """Run pytest with given arguments."""
    cmd = ["uv", "run", "pytest", "-v", *args]
    result = subprocess.run(cmd, cwd=PROJECT_ROOT)
    return result.returncode


def run_with_coverage() -> int:
    """Run tests with coverage report."""
    cmd = [
        "uv",
        "run",
        "pytest",
        "-v",
        "--cov=build",
        "--cov-report=term-missing",
        "--cov-report=html:verify/coverage/html",
        str(TEST_DIR),
    ]
    result = subprocess.run(cmd, cwd=PROJECT_ROOT)
    return result.returncode


def run_module(module: str) -> int:
    """Run tests for a specific module."""
    test_path = TEST_DIR / f"test_{module}"
    if not test_path.exists():
        print(f"Error: No tests found for module '{module}'")
        return 1
    return run_pytest([str(test_path), "-v"])


def run_watch() -> int:
    """Run tests in watch mode (requires pytest-watch)."""
    try:
        cmd = ["uv", "run", "ptw", str(TEST_DIR), "-v"]
        subprocess.run(cmd, cwd=PROJECT_ROOT)
    except FileNotFoundError:
        print("pytest-watch not installed. Install with: uv pip install pytest-watch")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="OCTALUM-PYLAB Test Runner")
    parser.add_argument(
        "module",
        nargs="?",
        help="Run tests for specific module (foundations, data_structures, algorithms)",
    )
    parser.add_argument(
        "--coverage",
        "-c",
        action="store_true",
        help="Run with coverage report",
    )
    parser.add_argument(
        "--watch",
        "-w",
        action="store_true",
        help="Run in watch mode",
    )
    parser.add_argument(
        "--fast",
        "-f",
        action="store_true",
        help="Skip slow tests",
    )
    parser.add_argument(
        "--parallel",
        "-p",
        action="store_true",
        help="Run tests in parallel",
    )

    args = parser.parse_args()
    pytest_args = [str(TEST_DIR)]

    if args.watch:
        return run_watch()

    if args.coverage:
        return run_with_coverage()

    if args.module:
        return run_module(args.module)

    if args.fast:
        pytest_args.extend(["-m", "not slow"])

    if args.parallel:
        pytest_args.extend(["-n", "auto"])

    return run_pytest(pytest_args)


if __name__ == "__main__":
    sys.exit(main())
