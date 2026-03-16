"""
LeetCode #268: Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in
                 range [0,3]. 2 is the missing number.

Example 2:
    Input: nums = [0,1]
    Output: 2

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8

Constraints:
    - n == nums.length
    - 1 <= n <= 10^4
    - 0 <= nums[i] <= n
    - All the numbers of nums are unique.
"""

from typing import List


class Solution:
    """
    Uses XOR property: a ^ a = 0 and a ^ 0 = a

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, nums: List[int]) -> int:
        """Find missing number using XOR."""
        n = len(nums)
        missing = n

        for i, num in enumerate(nums):
            missing ^= i ^ num

        return missing

    def solve_sum(self, nums: List[int]) -> int:
        """Find missing number using sum formula."""
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve([3, 0, 1])
    print(f"Test 1: nums=[3,0,1] -> {result1}")
    assert result1 == 2

    result2 = solution.solve([0, 1])
    print(f"Test 2: nums=[0,1] -> {result2}")
    assert result2 == 2

    result3 = solution.solve([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(f"Test 3: nums=[9,6,4,2,3,5,7,0,1] -> {result3}")
    assert result3 == 8

    result4 = solution.solve([0])
    print(f"Test 4: nums=[0] -> {result4}")
    assert result4 == 1

    result5 = solution.solve([1])
    print(f"Test 5: nums=[1] -> {result5}")
    assert result5 == 0

    result6 = solution.solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"Test 6: nums=[0,1,2,3,4,5,6,7,8,9] -> {result6}")
    assert result6 == 10

    for i in range(1, 20):
        nums = list(range(i + 1))
        missing = nums.pop(i // 2)
        xor_result = solution.solve(nums)
        sum_result = solution.solve_sum(nums)
        assert xor_result == missing == sum_result
    print("Test 7: XOR and Sum methods match for various inputs")

    print("\nAll tests passed!")
