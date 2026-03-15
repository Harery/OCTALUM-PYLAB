"""Pytest configuration and shared fixtures for OCTALUM-PYLAB tests."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Generator

import pytest

# Add build directory to path for imports
build_path = Path(__file__).parent.parent.parent / "build"
if str(build_path) not in sys.path:
    sys.path.insert(0, str(build_path))


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def sample_array() -> list[int]:
    """Returns a sample unsorted array for testing."""
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def sorted_array() -> list[int]:
    """Returns a sorted array for testing."""
    return [11, 12, 22, 25, 34, 64, 90]


@pytest.fixture
def empty_array() -> list[int]:
    """Returns an empty array for edge case testing."""
    return []


@pytest.fixture
def single_element_array() -> list[int]:
    """Returns single element array for edge case testing."""
    return [42]


@pytest.fixture
def duplicate_array() -> list[int]:
    """Returns array with duplicates for testing."""
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


@pytest.fixture
def sample_string() -> str:
    """Returns a sample string for testing."""
    return "hello world"


@pytest.fixture
def sample_linked_list_values() -> list[int]:
    """Returns values for creating a linked list."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_graph_dict() -> dict[int, list[int]]:
    """Returns an adjacency list representation of a graph."""
    return {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3],
    }


@pytest.fixture
def sample_tree_values() -> list[int | None]:
    """Returns values for creating a binary tree (level order)."""
    return [1, 2, 3, 4, 5, 6, 7]


@pytest.fixture
def intervals() -> list[list[int]]:
    """Returns sample intervals for merge interval testing."""
    return [[1, 3], [2, 6], [8, 10], [15, 18]]


@pytest.fixture
def merged_intervals() -> list[list[int]]:
    """Returns expected merged intervals."""
    return [[1, 6], [8, 10], [15, 18]]


# =============================================================================
# Pytest Configuration
# =============================================================================


def pytest_configure(config: pytest.Config) -> None:
    """Configure custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks integration tests")
    config.addinivalue_line("markers", "visualization: marks visualization tests")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip slow tests by default."""
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")

    for item in items:
        if "slow" in item.keywords and not config.getoption("--runslow"):
            item.add_marker(skip_slow)


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options."""
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help="Run slow tests",
    )
