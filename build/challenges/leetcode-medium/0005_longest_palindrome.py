"""
LeetCode 5: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab" (or "aba")

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Pattern: Expand Around Center
Time: O(n²)
Space: O(1)
"""

from __future__ import annotations


class Solution:
    def solve(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest = s[0]

        for i in range(len(s)):
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
    ]

    for s, expected in test_cases:
        result = solution.solve(s)
        status = "✓" if result in expected else "✗"
        print(f"{status} s='{s}' | Output: '{result}'")
