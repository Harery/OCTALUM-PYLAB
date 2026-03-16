"""
LeetCode 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3 (substring "abc")

Example 2:
    Input: s = "bbbbb"
    Output: 1 (substring "b")

Pattern: Sliding Window
Time: O(n)
Space: O(min(m, n)) - m = charset size
"""

from __future__ import annotations


class Solution:
    def solve(self, s: str) -> int:
        char_index: dict[str, int] = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("au", 2),
    ]

    for s, expected in test_cases:
        result = solution.solve(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}' | Output: {result}")
