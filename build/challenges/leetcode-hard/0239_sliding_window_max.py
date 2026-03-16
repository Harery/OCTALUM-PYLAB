#!/usr/bin/env python3
"""
LeetCode Hard #239: Sliding Window Maximum

You are given an array of integers nums and an integer k.
Return the max sliding window for each window of size k.

Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]

Time Complexity: O(n)
Space Complexity: O(k)
"""

from __future__ import annotations

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Find max in each sliding window using monotonic deque.

    The deque stores indices of elements in decreasing order.
    The front always has the index of the current maximum.

    Args:
        nums: List of integers
        k: Window size

    Returns:
        List of maximum values for each window
    """
    if not nums or k == 0:
        return []

    result: list[int] = []
    dq: deque[int] = deque()  # Store indices

    for i, num in enumerate(nums):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of smaller elements (they won't be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Start recording results once we have a full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def max_sliding_window_simple(nums: list[int], k: int) -> list[int]:
    """
    Simple O(n*k) solution for comparison.

    Less efficient but easier to understand.
    """
    if not nums or k == 0:
        return []

    return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]


def test() -> None:
    """Test cases for sliding window maximum."""
    # Test case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    expected1 = [3, 3, 5, 5, 6, 7]
    result1 = max_sliding_window(nums1, k1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"

    # Test case 2: single element
    nums2 = [1]
    k2 = 1
    expected2 = [1]
    result2 = max_sliding_window(nums2, k2)
    assert result2 == expected2

    # Test case 3: decreasing
    nums3 = [9, 8, 7, 6, 5]
    k3 = 2
    expected3 = [9, 8, 7, 6]
    result3 = max_sliding_window(nums3, k3)
    assert result3 == expected3

    print("All tests passed!")


if __name__ == "__main__":
    test()
