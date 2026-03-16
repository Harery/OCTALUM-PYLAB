"""
LeetCode #704: Binary Search

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 < nums[i], target < 10^4
    - All the integers in nums are unique.
    - nums is sorted in ascending order.
"""

from typing import List


class Solution:
    """
    Classic binary search with left/right pointers.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    def solve(self, nums: List[int], target: int) -> int:
        """Search for target in sorted array."""
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve([-1, 0, 3, 5, 9, 12], 9)
    print(f"Test 1: target=9 -> {result1}")
    assert result1 == 4

    result2 = solution.solve([-1, 0, 3, 5, 9, 12], 2)
    print(f"Test 2: target=2 -> {result2}")
    assert result2 == -1

    result3 = solution.solve([5], 5)
    print(f"Test 3: nums=[5], target=5 -> {result3}")
    assert result3 == 0

    result4 = solution.solve([5], -5)
    print(f"Test 4: nums=[5], target=-5 -> {result4}")
    assert result4 == -1

    result5 = solution.solve([1, 2, 3, 4, 5], 1)
    print(f"Test 5: target=1 (first) -> {result5}")
    assert result5 == 0

    result6 = solution.solve([1, 2, 3, 4, 5], 5)
    print(f"Test 6: target=5 (last) -> {result6}")
    assert result6 == 4

    result7 = solution.solve([1, 2, 3, 4, 5], 3)
    print(f"Test 7: target=3 (middle) -> {result7}")
    assert result7 == 2

    result8 = solution.solve([-10, -5, 0, 5, 10], -5)
    print(f"Test 8: target=-5 (negative) -> {result8}")
    assert result8 == 1

    result9 = solution.solve([1, 3, 5, 7, 9, 11], 6)
    print(f"Test 9: target=6 (not found) -> {result9}")
    assert result9 == -1

    print("\nAll tests passed!")
