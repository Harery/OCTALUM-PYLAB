"""
LeetCode 22: Generate Parentheses

Given n pairs of parentheses, generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Pattern: Backtracking
Time: O(4^n / √n) - Catalan number
Space: O(4^n / √n) - storing all combinations
"""

from __future__ import annotations


class Solution:
    def solve(self, n: int) -> list[str]:
        result: list[str] = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ]

    for n, expected in test_cases:
        result = solution.solve(n)
        status = "✓" if sorted(result) == sorted(expected) else "✗"
        print(f"{status} n={n} | Output: {result}")
