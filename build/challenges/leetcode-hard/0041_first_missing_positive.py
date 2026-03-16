#!/usr/bin/env python3
"""
LeetCode Hard #41: First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
    Input: nums = [1,2,0]
    Output: 3

Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def first_missing_positive(nums: list[int]) -> int:
    """
    Find the smallest missing positive integer using cyclic sort.

    Place each positive integer x at index x-1 (if possible),
    then scan to find the first position where index+1 != value.

    Args:
        nums: List of integers (modified in place)

    Returns:
        The smallest missing positive integer
    """
    n = len(nums)

    # Place each number in its correct position
    # nums[i] should be at index nums[i] - 1 if 1 <= nums[i] <= n
    i = 0
    while i < n:
        correct_idx = nums[i] - 1

        # Check if nums[i] is in valid range and not already in correct position
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    # Find the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


def first_missing_positive_hash(nums: list[int]) -> int:
    """
    Alternative solution using hash set.

    Time: O(n), Space: O(n)

    Easier to understand but uses extra space.
    """
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i


def test() -> None:
    """Test cases for first missing positive."""
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
        ([], 1),
        ([2, 1], 3),
        ([1, 1], 2),
    ]

    for nums, expected in test_cases:
        # Make a copy since function modifies in place
        result = first_missing_positive(nums.copy())
        assert result == expected, (
            f"Failed for {nums}: expected {expected}, got {result}"
        )

    print("All tests passed!")


if __name__ == "__main__":
    test()
