"""Tests for data structures module - Lists and Arrays."""

from __future__ import annotations

import pytest


class TestListOperations:
    """Tests for list operations."""

    def test_append(self, sample_array: list[int]) -> None:
        """Test list append operation."""
        sample_array.append(100)
        assert sample_array[-1] == 100
        assert len(sample_array) == 8

    def test_extend(self, sample_array: list[int]) -> None:
        """Test list extend operation."""
        sample_array.extend([1, 2])
        assert len(sample_array) == 9
        assert sample_array[-2:] == [1, 2]

    def test_insert(self, sample_array: list[int]) -> None:
        """Test list insert operation."""
        sample_array.insert(0, 999)
        assert sample_array[0] == 999

    def test_remove(self, sample_array: list[int]) -> None:
        """Test list remove operation."""
        sample_array.remove(64)
        assert 64 not in sample_array

    def test_pop(self, sample_array: list[int]) -> None:
        """Test list pop operation."""
        popped = sample_array.pop()
        assert popped == 90
        assert len(sample_array) == 6

    def test_pop_index(self, sample_array: list[int]) -> None:
        """Test list pop with index."""
        popped = sample_array.pop(0)
        assert popped == 64
        assert sample_array[0] == 34

    def test_index(self, sample_array: list[int]) -> None:
        """Test list index operation."""
        idx = sample_array.index(25)
        assert idx == 2

    def test_count(self, duplicate_array: list[int]) -> None:
        """Test list count operation."""
        assert duplicate_array.count(5) == 3
        assert duplicate_array.count(1) == 2

    def test_sort(self, sample_array: list[int]) -> None:
        """Test list sort operation."""
        sample_array.sort()
        assert sample_array == [11, 12, 22, 25, 34, 64, 90]

    def test_reverse(self, sorted_array: list[int]) -> None:
        """Test list reverse operation."""
        sorted_array.reverse()
        assert sorted_array == [90, 64, 34, 25, 22, 12, 11]

    def test_copy(self, sample_array: list[int]) -> None:
        """Test list copy operation."""
        copy = sample_array.copy()
        assert copy == sample_array
        assert copy is not sample_array

    def test_clear(self, sample_array: list[int]) -> None:
        """Test list clear operation."""
        sample_array.clear()
        assert sample_array == []


class TestListSlicing:
    """Tests for list slicing operations."""

    def test_slice_start_end(self, sample_array: list[int]) -> None:
        """Test slicing with start and end."""
        result = sample_array[1:4]
        assert result == [34, 25, 12]

    def test_slice_start_only(self, sample_array: list[int]) -> None:
        """Test slicing with start only."""
        result = sample_array[3:]
        assert result == [12, 22, 11, 90]

    def test_slice_end_only(self, sample_array: list[int]) -> None:
        """Test slicing with end only."""
        result = sample_array[:3]
        assert result == [64, 34, 25]

    def test_slice_negative(self, sample_array: list[int]) -> None:
        """Test slicing with negative indices."""
        result = sample_array[-3:]
        assert result == [22, 11, 90]

    def test_slice_step(self, sample_array: list[int]) -> None:
        """Test slicing with step."""
        result = sample_array[::2]
        assert result == [64, 25, 22, 90]

    def test_slice_reverse(self, sample_array: list[int]) -> None:
        """Test slicing to reverse."""
        result = sample_array[::-1]
        assert result == [90, 11, 22, 12, 25, 34, 64]


class TestListComprehensions:
    """Tests for list comprehensions."""

    def test_basic_comprehension(self) -> None:
        """Test basic list comprehension."""
        result = [x * 2 for x in range(5)]
        assert result == [0, 2, 4, 6, 8]

    def test_filtered_comprehension(self) -> None:
        """Test filtered list comprehension."""
        result = [x for x in range(10) if x % 2 == 0]
        assert result == [0, 2, 4, 6, 8]

    def test_nested_comprehension(self) -> None:
        """Test nested list comprehension."""
        result = [[i * j for j in range(3)] for i in range(3)]
        assert result == [[0, 0, 0], [0, 1, 2], [0, 2, 4]]


class TestEdgeCases:
    """Tests for edge cases."""

    def test_empty_array_operations(self, empty_array: list[int]) -> None:
        """Test operations on empty array."""
        assert len(empty_array) == 0
        empty_array.append(1)
        assert empty_array == [1]
        empty_array.pop()
        assert empty_array == []

    def test_single_element(self, single_element_array: list[int]) -> None:
        """Test operations on single element array."""
        assert len(single_element_array) == 1
        assert single_element_array[0] == 42
        single_element_array.append(43)
        assert len(single_element_array) == 2
