"""
LeetCode #344: Reverse String

Write a function that reverses a string. The input string is given as an
array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints:
    - 1 <= s.length <= 10^5
    - s[i] is a printable ascii character.
"""

from typing import List


class Solution:
    """
    Two-pointer swap from both ends toward center.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, s: List[str]) -> None:
        """Reverse string in-place."""
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = Solution()

    s1 = ["h", "e", "l", "l", "o"]
    solution.solve(s1)
    print(f"Test 1: {s1}")
    assert s1 == ["o", "l", "l", "e", "h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    solution.solve(s2)
    print(f"Test 2: {s2}")
    assert s2 == ["h", "a", "n", "n", "a", "H"]

    s3 = ["a"]
    solution.solve(s3)
    print(f"Test 3: {s3}")
    assert s3 == ["a"]

    s4 = ["a", "b"]
    solution.solve(s4)
    print(f"Test 4: {s4}")
    assert s4 == ["b", "a"]

    s5 = ["1", "2", "3", "4", "5"]
    solution.solve(s5)
    print(f"Test 5: {s5}")
    assert s5 == ["5", "4", "3", "2", "1"]

    s6 = ["!", "@", "#", "$", "%"]
    solution.solve(s6)
    print(f"Test 6: {s6}")
    assert s6 == ["%", "$", "#", "@", "!"]

    s7 = ["x", "x", "x"]
    solution.solve(s7)
    print(f"Test 7: {s7}")
    assert s7 == ["x", "x", "x"]

    print("\nAll tests passed!")
