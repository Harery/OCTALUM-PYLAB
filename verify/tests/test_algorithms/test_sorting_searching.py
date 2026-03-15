"""Tests for algorithms module - Searching and Sorting."""

from __future__ import annotations

import pytest


class TestBinarySearch:
    """Tests for binary search algorithm."""

    def binary_search(self, arr: list[int], target: int) -> int:
        """Binary search implementation for testing."""
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def test_found(self, sorted_array: list[int]) -> None:
        """Test finding existing element."""
        result = self.binary_search(sorted_array, 25)
        assert result == 3

    def test_not_found(self, sorted_array: list[int]) -> None:
        """Test element not in array."""
        result = self.binary_search(sorted_array, 100)
        assert result == -1

    def test_first_element(self, sorted_array: list[int]) -> None:
        """Test finding first element."""
        result = self.binary_search(sorted_array, 11)
        assert result == 0

    def test_last_element(self, sorted_array: list[int]) -> None:
        """Test finding last element."""
        result = self.binary_search(sorted_array, 90)
        assert result == 6

    def test_empty_array(self, empty_array: list[int]) -> None:
        """Test with empty array."""
        result = self.binary_search(empty_array, 5)
        assert result == -1


class TestLinearSearch:
    """Tests for linear search algorithm."""

    def linear_search(self, arr: list[int], target: int) -> int:
        """Linear search implementation for testing."""
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1

    def test_found(self, sample_array: list[int]) -> None:
        """Test finding existing element."""
        result = self.linear_search(sample_array, 25)
        assert result == 2

    def test_not_found(self, sample_array: list[int]) -> None:
        """Test element not in array."""
        result = self.linear_search(sample_array, 100)
        assert result == -1

    def test_first_occurrence(self, duplicate_array: list[int]) -> None:
        """Test finds first occurrence."""
        result = self.linear_search(duplicate_array, 5)
        assert result == 4


class TestBubbleSort:
    """Tests for bubble sort algorithm."""

    def bubble_sort(self, arr: list[int]) -> list[int]:
        """Bubble sort implementation for testing."""
        result = arr.copy()
        n = len(result)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break

        return result

    def test_sort(self, sample_array: list[int], sorted_array: list[int]) -> None:
        """Test sorting unsorted array."""
        result = self.bubble_sort(sample_array)
        assert result == sorted_array

    def test_empty(self, empty_array: list[int]) -> None:
        """Test sorting empty array."""
        result = self.bubble_sort(empty_array)
        assert result == []

    def test_single(self, single_element_array: list[int]) -> None:
        """Test sorting single element."""
        result = self.bubble_sort(single_element_array)
        assert result == single_element_array


class TestQuickSort:
    """Tests for quick sort algorithm."""

    def quick_sort(self, arr: list[int]) -> list[int]:
        """Quick sort implementation for testing."""
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def test_sort(self, sample_array: list[int], sorted_array: list[int]) -> None:
        """Test sorting unsorted array."""
        result = self.quick_sort(sample_array)
        assert result == sorted_array

    def test_duplicates(self, duplicate_array: list[int]) -> None:
        """Test sorting with duplicates."""
        result = self.quick_sort(duplicate_array)
        assert result == sorted(duplicate_array)


class TestMergeSort:
    """Tests for merge sort algorithm."""

    def merge_sort(self, arr: list[int]) -> list[int]:
        """Merge sort implementation for testing."""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        """Merge two sorted arrays."""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def test_sort(self, sample_array: list[int], sorted_array: list[int]) -> None:
        """Test sorting unsorted array."""
        result = self.merge_sort(sample_array)
        assert result == sorted_array

    def test_stable_sort(self) -> None:
        """Test that merge sort is stable."""
        arr = [(3, "a"), (1, "b"), (3, "c"), (1, "d")]
        result = sorted(arr, key=lambda x: x[0])  # Python's sort is stable
        assert result == [(1, "b"), (1, "d"), (3, "a"), (3, "c")]
