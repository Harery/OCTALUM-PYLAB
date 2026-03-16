"""
LeetCode #202: Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of
  the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay),
  or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Example 1:
    Input: n = 19
    Output: true
    Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

Example 2:
    Input: n = 2
    Output: false

Constraints:
    - 1 <= n <= 2^31 - 1
"""


class Solution:
    """
    Time Complexity: O(log n) - number of digits in n
    Space Complexity: O(log n) - storing seen numbers in set
    """

    def solve(self, n: int) -> bool:
        """Check if n is a happy number."""
        seen: set[int] = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self._sum_of_squares(n)

        return n == 1

    def _sum_of_squares(self, num: int) -> int:
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve(19)
    print(f"Test 1: n=19 -> {result1}")
    assert result1 is True

    result2 = solution.solve(2)
    print(f"Test 2: n=2 -> {result2}")
    assert result2 is False

    result3 = solution.solve(1)
    print(f"Test 3: n=1 -> {result3}")
    assert result3 is True

    result4 = solution.solve(7)
    print(f"Test 4: n=7 -> {result4}")
    assert result4 is True

    result5 = solution.solve(4)
    print(f"Test 5: n=4 -> {result5}")
    assert result5 is False

    result6 = solution.solve(100)
    print(f"Test 6: n=100 -> {result6}")
    assert result6 is True

    result7 = solution.solve(1111111)
    print(f"Test 7: n=1111111 -> {result7}")
    assert result7 is True

    print("\nAll tests passed!")
