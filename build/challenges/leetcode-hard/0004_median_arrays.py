#!/usr/bin/env python3
"""
LeetCode Hard #4: Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.0

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.5

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""

from __future__ import annotations


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays using binary search.

    Uses the partition approach to find the correct split point
    in both arrays such that all elements on the left are smaller
    than all elements on the right.

    Args:
        nums1: First sorted array
        nums2: Second sorted array

    Returns:
        The median value as a float
    """
    # Ensure nums1 is the smaller array for log(min(m,n)) complexity
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    total = m + n
    half = (total + 1) // 2

    while left <= right:
        # Partition positions
        partition1 = (left + right) // 2
        partition2 = half - partition1

        # Edge cases: use infinity for out-of-bounds
        max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float("inf") if partition1 == m else nums1[partition1]

        max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float("inf") if partition2 == n else nums2[partition2]

        # Check if we found the correct partition
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # Found the correct partition
            if total % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            return float(max(max_left1, max_left2))

        if max_left1 > min_right2:
            # Move partition1 to the left
            right = partition1 - 1
        else:
            # Move partition1 to the right
            left = partition1 + 1

    raise ValueError("Input arrays are not sorted or invalid")


def test() -> None:
    """Test cases for median of two sorted arrays."""
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([], [2, 3], 2.5),
        ([1, 3, 5], [2, 4, 6], 3.5),
        ([1, 2, 3], [4, 5, 6, 7, 8], 4.5),
    ]

    for nums1, nums2, expected in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        assert abs(result - expected) < 0.0001, (
            f"Failed for {nums1} + {nums2}: expected {expected}, got {result}"
        )
    print("All tests passed!")


if __name__ == "__main__":
    test()
