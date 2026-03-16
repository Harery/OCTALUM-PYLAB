"""
LeetCode #242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and
false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters.
"""

from typing import Dict


class Solution:
    """
    Time Complexity: O(n) - single pass through both strings
    Space Complexity: O(1) - at most 26 characters in counter
    """

    def solve(self, s: str, t: str) -> bool:
        """Check if t is an anagram of s."""
        if len(s) != len(t):
            return False

        counter: Dict[str, int] = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter:
                return False
            counter[char] -= 1
            if counter[char] < 0:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve("anagram", "nagaram")
    print(f"Test 1: s='anagram', t='nagaram' -> {result1}")
    assert result1 is True

    result2 = solution.solve("rat", "car")
    print(f"Test 2: s='rat', t='car' -> {result2}")
    assert result2 is False

    result3 = solution.solve("a", "a")
    print(f"Test 3: s='a', t='a' -> {result3}")
    assert result3 is True

    result4 = solution.solve("ab", "ba")
    print(f"Test 4: s='ab', t='ba' -> {result4}")
    assert result4 is True

    result5 = solution.solve("ab", "abc")
    print(f"Test 5: s='ab', t='abc' -> {result5}")
    assert result5 is False

    result6 = solution.solve("", "")
    print(f"Test 6: s='', t='' -> {result6}")
    assert result6 is True

    result7 = solution.solve("listen", "silent")
    print(f"Test 7: s='listen', t='silent' -> {result7}")
    assert result7 is True

    result8 = solution.solve("hello", "world")
    print(f"Test 8: s='hello', t='world' -> {result8}")
    assert result8 is False

    print("\nAll tests passed!")
