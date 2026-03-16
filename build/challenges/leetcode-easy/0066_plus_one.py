"""
LeetCode #66: Plus One

You are given a large integer represented as an integer array digits, where
each digits[i] is the ith digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
                 Incrementing by one gives 123 + 1 = 124.

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]

Example 3:
    Input: digits = [9]
    Output: [1,0]

Constraints:
    - 1 <= digits.length <= 100
    - 0 <= digits[i] <= 9
    - digits does not contain any leading 0's.
"""

from typing import List


class Solution:
    """
    Solution class for Plus One problem.

    Time Complexity: O(n) - worst case traversing entire array
    Space Complexity: O(1) - modifying in place, O(n) only for result expansion
    """

    def solve(self, digits: List[int]) -> List[int]:
        """
        Increment the large integer by one.

        Args:
            digits: List of digits representing a large integer

        Returns:
            List of digits representing the incremented integer
        """
        # Start from the least significant digit
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, it becomes 0 and we carry over
            digits[i] = 0

        # If we reach here, all digits were 9 (e.g., 999 -> 1000)
        return [1] + digits


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic increment
    digits1 = [1, 2, 3]
    result1 = solution.solve(digits1)
    print(f"Test 1: digits=[1,2,3] -> {result1}")
    assert result1 == [1, 2, 4]

    # Test case 2: No carry
    digits2 = [4, 3, 2, 1]
    result2 = solution.solve(digits2)
    print(f"Test 2: digits=[4,3,2,1] -> {result2}")
    assert result2 == [4, 3, 2, 2]

    # Test case 3: Single 9 requires carry and expansion
    digits3 = [9]
    result3 = solution.solve(digits3)
    print(f"Test 3: digits=[9] -> {result3}")
    assert result3 == [1, 0]

    # Test case 4: Multiple 9s at end
    digits4 = [1, 9, 9]
    result4 = solution.solve(digits4)
    print(f"Test 4: digits=[1,9,9] -> {result4}")
    assert result4 == [2, 0, 0]

    # Test case 5: All 9s
    digits5 = [9, 9, 9]
    result5 = solution.solve(digits5)
    print(f"Test 5: digits=[9,9,9] -> {result5}")
    assert result5 == [1, 0, 0, 0]

    # Test case 6: Single non-9 digit
    digits6 = [5]
    result6 = solution.solve(digits6)
    print(f"Test 6: digits=[5] -> {result6}")
    assert result6 == [6]

    # Test case 7: Carry in middle
    digits7 = [1, 2, 9]
    result7 = solution.solve(digits7)
    print(f"Test 7: digits=[1,2,9] -> {result7}")
    assert result7 == [1, 3, 0]

    # Test case 8: Large number with no carry
    digits8 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    result8 = solution.solve(digits8)
    print(f"Test 8: digits=[9,8,7,6,5,4,3,2,1,0] -> {result8}")
    assert result8 == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

    print("\nAll tests passed!")
