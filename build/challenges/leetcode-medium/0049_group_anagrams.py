"""
LeetCode 49: Group Anagrams

Given array of strings strs, group the anagrams together.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Pattern: Hash Table with Sorted Key
Time: O(n * k log k) - n strings, k = avg length
Space: O(n * k)
"""

from __future__ import annotations

from collections import defaultdict


class Solution:
    def solve(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for strs, expected in test_cases:
        result = solution.solve(strs)
        result_sorted = sorted([sorted(g) for g in result])
        expected_sorted = sorted([sorted(g) for g in expected])
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} Input: {strs[:3]}... | {len(result)} groups")
