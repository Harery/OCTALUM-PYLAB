"""
LeetCode 33: Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order with distinct values.
The array is rotated at an unknown pivot. Given target, return its index or -1.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Pattern: Modified Binary Search
Time: O(log n)
Space: O(1)
"""

from __future__ import annotations


class Solution:
    def solve(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
    ]

    for nums, target, expected in test_cases:
        result = solution.solve(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} | Output: {result}")
