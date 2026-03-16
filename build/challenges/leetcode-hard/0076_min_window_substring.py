#!/usr/bin/env python3
"""
LeetCode Hard #76: Minimum Window Substring

Given two strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included.
If there is no such substring, return the empty string "".

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Time Complexity: O(|s| + |t|)
Space Complexity: O(|s| + |t|) for hash maps
"""

from __future__ import annotations

from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Find minimum window substring using sliding window with character counts.

    Expands the window until all characters are found, then contracts
    from the left to find the minimum valid window.

    Args:
        s: Source string
        t: Target string with required characters

    Returns:
        Minimum window substring, or "" if not found
    """
    if not s or not t:
        return ""

    # Count characters in t
    target_counts = Counter(t)
    required = len(target_counts)  # Number of unique chars needed

    # Window counters
    window_counts: dict[str, int] = {}
    formed = 0  # Number of unique chars in window with desired frequency

    # Result: (window length, left, right)
    result = (float("inf"), 0, 0)

    left = 0

    for right, char in enumerate(s):
        # Add character to window
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if this character's count matches target
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        # Try to contract the window
        while left <= right and formed == required:
            char = s[left]

            # Update result if smaller window found
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)

            # Remove leftmost character from window
            window_counts[char] -= 1
            if char in target_counts and window_counts[char] < target_counts[char]:
                formed -= 1

            left += 1

    length, start, end = result
    return "" if length == float("inf") else s[start : end + 1]


def test() -> None:
    """Test cases for minimum window substring."""
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("", "a", ""),
        ("a", "", ""),
        ("ab", "b", "b"),
    ]

    for s, t, expected in test_cases:
        result = min_window(s, t)
        assert result == expected, (
            f"Failed for s='{s}', t='{t}': expected '{expected}', got '{result}'"
        )

    print("All tests passed!")


if __name__ == "__main__":
    test()
