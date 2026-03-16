"""
LeetCode 46: Permutations

Given an array nums of distinct integers, return all possible permutations.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Pattern: Backtracking
Time: O(n! * n) - n! permutations, n for copying
Space: O(n) - recursion depth + used array
"""

from __future__ import annotations


class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        used = [False] * len(nums)

        def backtrack(current: list[int]) -> None:
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()
                    used[i] = False

        backtrack([])
        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ]

    for nums, expected in test_cases:
        result = solution.solve(nums)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} nums={nums} | {len(result)} permutations")
