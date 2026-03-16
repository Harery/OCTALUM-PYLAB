"""
LeetCode 15: 3Sum

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Pattern: Two Pointers + Sorting
Time: O(n²) - nested loop with sorted array
Space: O(1) - excluding output
"""

from __future__ import annotations


class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result: list[list[int]] = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 2, -2, -1], []),
    ]

    for nums, expected in test_cases:
        result = solution.solve(nums)
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        status = "✓" if result_set == expected_set else "✗"
        print(f"{status} Input: {nums} | Output: {result}")
