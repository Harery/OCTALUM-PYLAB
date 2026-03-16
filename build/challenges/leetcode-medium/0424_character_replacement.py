"""
LeetCode 424: Longest Repeating Character Replacement

Given string s and integer k, you can change any character at most k times.
Return the length of the longest substring containing the same letter.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4

Pattern: Sliding Window
Time: O(n)
Space: O(26) - 26 letters
"""

from __future__ import annotations


class Solution:
    def solve(self, s: str, k: int) -> int:
        char_count: dict[str, int] = {}
        left = 0
        max_len = 0
        max_count = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])

            if (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
    ]

    for s, k, expected in test_cases:
        result = solution.solve(s, k)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}', k={k} | Output: {result}")
