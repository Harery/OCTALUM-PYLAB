# Contributing to OCTALUM-PYLAB

Thank you for your interest in contributing to OCTALUM-PYLAB! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

### Reporting Issues

1. Check if the issue already exists
2. Use the issue template
3. Include:
   - Python version
   - Steps to reproduce
   - Expected vs actual behavior
   - Code samples

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit with conventional commits
6. Push and create a PR

## Development Setup

### Prerequisites

- Python 3.10+
- uv (recommended) or pip
- Git

### Quick Start

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/OCTALUM-PYLAB.git
cd OCTALUM-PYLAB

# Install uv
pip install uv

# Install dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=build --cov-report=html

# Run specific test file
uv run pytest verify/tests/test_foundations/test_basics.py
```

### Code Style

We use **Ruff** for linting and formatting:

```bash
# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .
```

### Type Checking

```bash
uv run pyright
```

## Contribution Types

### Adding New Algorithms/Data Structures

1. Place in appropriate directory under `build/`
2. Include:
   - Type hints on all functions
   - Time/space complexity in docstrings
   - Example usage in `if __name__ == "__main__"`
   - README.md with explanation

### Adding Exercises

1. Place in appropriate module's `exercises.py`
2. Include solution with explanation
3. Add corresponding test

### Improving Documentation

1. Update relevant `.md` files
2. Ensure Mermaid diagrams render correctly
3. Check all links work

## Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add binary search tree implementation
fix: correct edge case in quicksort
docs: update installation instructions
test: add tests for linked list
refactor: simplify merge sort code
```

## Pull Request Process

1. Ensure all CI checks pass
2. Update documentation if needed
3. Add tests for new functionality
4. Request review from maintainers
5. Address review feedback

## Questions?

- Open a [Discussion](https://github.com/Harery/OCTALUM-PYLAB/discussions)
- Email: octalume@harery.com

---

Thank you for helping make OCTALUM-PYLAB better!
