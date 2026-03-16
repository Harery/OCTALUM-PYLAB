"""
LeetCode 39: Combination Sum

Given array of distinct integers candidates and target, find all unique combinations
where candidate numbers sum to target. Same number may be chosen unlimited times.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Pattern: Backtracking
Time: O(N^(T/M+1)) - N=candidates, T=target, M=min candidate
Space: O(T/M) - recursion depth
"""

from __future__ import annotations


class Solution:
    def solve(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(start: int, current: list[int], remaining: int) -> None:
            if remaining == 0:
                result.append(current.copy())
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ]

    for candidates, target, expected in test_cases:
        result = solution.solve(candidates, target)
        result_sorted = sorted([sorted(x) for x in result])
        expected_sorted = sorted([sorted(x) for x in expected])
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} candidates={candidates}, target={target}")
