#!/usr/bin/env python3
"""
OCTALUM-PYLAB Project Setup Script

Initialize and configure the learning environment.

Usage:
    python ship/scripts/setup.py           # Full setup
    python ship/scripts/setup.py --check   # Check prerequisites
    python ship/scripts/setup.py --hooks   # Install git hooks only
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def check_python_version() -> bool:
    """Check Python version is 3.10+."""
    version = sys.version_info
    if version >= (3, 10):
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    print(f"❌ Python {version.major}.{version.minor} (need 3.10+)")
    return False


def check_uv() -> bool:
    """Check if uv is installed."""
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
        print(f"✅ uv: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("❌ uv not installed (https://docs.astral.sh/uv/)")
        return False


def check_git() -> bool:
    """Check if git is installed."""
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        print(f"✅ {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("❌ git not installed")
        return False


def install_dependencies() -> bool:
    """Install project dependencies."""
    print("\n📦 Installing dependencies...")
    result = subprocess.run(["uv", "sync", "--all-extras"], cwd=PROJECT_ROOT)
    if result.returncode == 0:
        print("✅ Dependencies installed")
        return True
    print("❌ Failed to install dependencies")
    return False


def install_hooks() -> bool:
    """Install pre-commit hooks."""
    print("\n🪝 Installing git hooks...")
    result = subprocess.run(
        ["uv", "run", "pre-commit", "install", "--install-hooks"],
        cwd=PROJECT_ROOT,
    )
    if result.returncode == 0:
        print("✅ Git hooks installed")
        return True
    print("❌ Failed to install hooks")
    return False


def create_venv() -> bool:
    """Create virtual environment."""
    print("\n🐍 Creating virtual environment...")
    result = subprocess.run(["uv", "venv"], cwd=PROJECT_ROOT)
    if result.returncode == 0:
        print("✅ Virtual environment created")
        return True
    print("❌ Failed to create venv")
    return False


def run_checks() -> bool:
    """Run all prerequisite checks."""
    print("\n🔍 Checking prerequisites...\n")
    results = [
        check_python_version(),
        check_git(),
        check_uv(),
    ]
    all_passed = all(results)

    print("\n" + "=" * 40)
    if all_passed:
        print("✅ All checks passed!")
    else:
        print("❌ Some checks failed. Please fix before continuing.")

    return all_passed


def full_setup() -> bool:
    """Run full setup."""
    print("\n🚀 OCTALUM-PYLAB Setup\n")
    print("=" * 40)

    if not run_checks():
        return False

    if not create_venv():
        return False

    if not install_dependencies():
        return False

    if not install_hooks():
        return False

    print("\n" + "=" * 40)
    print("✅ Setup complete!")
    print("\nNext steps:")
    print("  1. Activate venv: source .venv/bin/activate")
    print("  2. Run tests: uv run pytest verify/tests -v")
    print("  3. Start learning: python build/foundations/01-python-basics/hello.py")
    print("=" * 40)

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="OCTALUM-PYLAB Setup")
    parser.add_argument("--check", action="store_true", help="Check prerequisites only")
    parser.add_argument("--hooks", action="store_true", help="Install git hooks only")
    parser.add_argument("--deps", action="store_true", help="Install dependencies only")

    args = parser.parse_args()

    if args.check:
        return 0 if run_checks() else 1
    if args.hooks:
        return 0 if install_hooks() else 1
    if args.deps:
        return 0 if install_dependencies() else 1

    return 0 if full_setup() else 1


if __name__ == "__main__":
    sys.exit(main())
