"""
LeetCode #414: Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this
array. If the third maximum does not exist, return the maximum number.

Example 1:
    Input: nums = [3,2,1]
    Output: 1
    Explanation: The first distinct maximum is 3, the second is 2, and the
                 third is 1.

Example 2:
    Input: nums = [1,2]
    Output: 2
    Explanation: The first distinct maximum is 2, the second is 1, and the
                 third does not exist, so the maximum (2) is returned.

Example 3:
    Input: nums = [2,2,3,1]
    Output: 1
    Explanation: The first distinct maximum is 3, the second is 2, and the
                 third is 1.

Constraints:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List, Optional


class Solution:
    """
    Track top 3 distinct maximums in single pass.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, nums: List[int]) -> int:
        """Return third distinct max or max if less than 3 distinct."""
        first: Optional[int] = None
        second: Optional[int] = None
        third: Optional[int] = None

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        return third if third is not None else first


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve([3, 2, 1])
    print(f"Test 1: nums=[3,2,1] -> {result1}")
    assert result1 == 1

    result2 = solution.solve([1, 2])
    print(f"Test 2: nums=[1,2] -> {result2}")
    assert result2 == 2

    result3 = solution.solve([2, 2, 3, 1])
    print(f"Test 3: nums=[2,2,3,1] -> {result3}")
    assert result3 == 1

    result4 = solution.solve([1, 1, 2])
    print(f"Test 4: nums=[1,1,2] -> {result4}")
    assert result4 == 2

    result5 = solution.solve([5, 5, 5, 5])
    print(f"Test 5: nums=[5,5,5,5] -> {result5}")
    assert result5 == 5

    result6 = solution.solve([1, 2, 3, 4, 5])
    print(f"Test 6: nums=[1,2,3,4,5] -> {result6}")
    assert result6 == 3

    result7 = solution.solve([-1, -2, -3])
    print(f"Test 7: nums=[-1,-2,-3] -> {result7}")
    assert result7 == -3

    result8 = solution.solve([1])
    print(f"Test 8: nums=[1] -> {result8}")
    assert result8 == 1

    result9 = solution.solve([1, 2, -2147483648])
    print(f"Test 9: nums=[1,2,-2147483648] -> {result9}")
    assert result9 == -2147483648

    print("\nAll tests passed!")
