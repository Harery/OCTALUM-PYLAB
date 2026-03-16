#!/usr/bin/env python3
"""
LeetCode Hard #42: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def trap(height: list[int]) -> int:
    """
    Calculate trapped rainwater using two-pointer approach.

    Water at any position is determined by the minimum of the
    maximum heights on both sides, minus the current height.

    Args:
        height: List of bar heights

    Returns:
        Total units of water that can be trapped
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            # Process left side
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            # Process right side
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


def trap_with_stack(height: list[int]) -> int:
    """
    Alternative solution using monotonic stack.

    Time: O(n), Space: O(n)

    Stack stores indices of bars in decreasing order of height.
    """
    if not height:
        return 0

    stack: list[int] = []
    water = 0

    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            # Pop the bottom of the "bowl"
            bottom_idx = stack.pop()

            if not stack:
                break

            # Calculate width and height of water trapped
            width = i - stack[-1] - 1
            water_height = min(h, height[stack[-1]]) - height[bottom_idx]
            water += width * water_height

        stack.append(i)

    return water


def test() -> None:
    """Test cases for trapping rain water."""
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([1], 0),
        ([2, 0, 2], 2),
        ([3, 0, 0, 2, 0, 4], 10),
    ]

    for height, expected in test_cases:
        result = trap(height)
        assert result == expected, (
            f"Failed for {height}: expected {expected}, got {result}"
        )

        # Also test stack solution
        result_stack = trap_with_stack(height)
        assert result_stack == expected

    print("All tests passed!")


if __name__ == "__main__":
    test()
