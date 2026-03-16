"""
LeetCode #217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    """
    Time Complexity: O(n) - single pass with set lookup O(1)
    Space Complexity: O(n) - worst case storing all elements in set
    """

    def solve(self, nums: List[int]) -> bool:
        """Check if array contains any duplicates."""
        seen: set[int] = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve([1, 2, 3, 1])
    print(f"Test 1: nums=[1,2,3,1] -> {result1}")
    assert result1 is True

    result2 = solution.solve([1, 2, 3, 4])
    print(f"Test 2: nums=[1,2,3,4] -> {result2}")
    assert result2 is False

    result3 = solution.solve([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print(f"Test 3: nums=[1,1,1,3,3,4,3,2,4,2] -> {result3}")
    assert result3 is True

    result4 = solution.solve([1])
    print(f"Test 4: nums=[1] -> {result4}")
    assert result4 is False

    result5 = solution.solve([1, 1])
    print(f"Test 5: nums=[1,1] -> {result5}")
    assert result5 is True

    result6 = solution.solve([-1, -2, -3, -1])
    print(f"Test 6: nums=[-1,-2,-3,-1] -> {result6}")
    assert result6 is True

    result7 = solution.solve([0, 0, 0])
    print(f"Test 7: nums=[0,0,0] -> {result7}")
    assert result7 is True

    print("\nAll tests passed!")
