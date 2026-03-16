# 🏗️ Build Module

Core learning content for OCTALUM-PYLAB, organized into 5 submodules.

## Structure

```
build/
├── foundations/       # Phase 1: Python Fundamentals
├── data-structures/   # Phase 2-4: Data Structures
├── algorithms/        # Phase 3,6: Algorithms
├── patterns/          # Phase 5: Coding Patterns
└── challenges/        # Phase 7: LeetCode Challenges
```

## Quick Navigation

| Module | Description | Files |
|--------|-------------|-------|
| [Foundations](foundations/) | Python basics, control flow, functions | 12 |
| [Data Structures](data-structures/) | Arrays to graphs | 30+ |
| [Algorithms](algorithms/) | Search, sort, DP, graphs | 25+ |
| [Patterns](patterns/) | 12 coding patterns | 24 |
| [Challenges](challenges/) | LeetCode problems | TBD |

## How to Use

### Run Examples

```bash
# Run any Python file directly
python build/foundations/01-python-basics/variables.py

# Or with uv
uv run python build/algorithms/01-searching/binary_search.py
```

### Import as Module

```python
from build.algorithms.searching import binary_search

result = binary_search([1, 2, 3, 4, 5], 3)
print(result)  # 2
```

### Run Tests

```bash
# Test specific module
pytest verify/tests/test_algorithms/ -v

# Test with coverage
pytest verify/tests/ --cov=build --cov-report=html
```

## Contributing

When adding new content:

1. Place files in appropriate subdirectory
2. Add type hints to all functions
3. Include `if __name__ == "__main__":` block
4. Create corresponding README.md
5. Add tests in `verify/tests/`
