"""
LeetCode #258: Add Digits

Given an integer num, repeatedly add all its digits until the result has
only one digit, and return it.

Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is: 38 --> 3 + 8 --> 11 --> 1 + 1 --> 2.

Example 2:
    Input: num = 0
    Output: 0

Constraints:
    - 0 <= num <= 2^31 - 1
"""


class Solution:
    """
    Uses digital root formula: dr(n) = 1 + (n - 1) % 9 for n > 0

    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def solve(self, num: int) -> int:
        """Return digital root using mathematical formula."""
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

    def solve_iterative(self, num: int) -> int:
        """Return digital root using iterative approach."""
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve(38)
    print(f"Test 1: num=38 -> {result1}")
    assert result1 == 2

    result2 = solution.solve(0)
    print(f"Test 2: num=0 -> {result2}")
    assert result2 == 0

    result3 = solution.solve(9)
    print(f"Test 3: num=9 -> {result3}")
    assert result3 == 9

    result4 = solution.solve(10)
    print(f"Test 4: num=10 -> {result4}")
    assert result4 == 1

    result5 = solution.solve(12345)
    print(f"Test 5: num=12345 -> {result5}")
    assert result5 == 6

    result6 = solution.solve(999999999)
    print(f"Test 6: num=999999999 -> {result6}")
    assert result6 == 9

    result7 = solution.solve(1000000000)
    print(f"Test 7: num=1000000000 -> {result7}")
    assert result7 == 1

    for i in range(20):
        formula_result = solution.solve(i)
        iterative_result = solution.solve_iterative(i)
        assert formula_result == iterative_result, f"Mismatch at {i}"
    print("Test 8: Formula matches iterative for 0-19")

    print("\nAll tests passed!")
