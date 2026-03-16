"""
LeetCode #1: Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
"""

from typing import List


class Solution:
    """
    Solution class for Two Sum problem using hash map approach.

    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(n) - storing at most n elements in hash map
    """

    def solve(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices whose values sum to target.

        Args:
            nums: List of integers
            target: Target sum to find

        Returns:
            List of two indices whose values sum to target
        """
        seen: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []  # Should never reach here given problem constraints


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.solve(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1} -> {result1}")
    assert result1 == [0, 1] or result1 == [1, 0]

    # Test case 2: Target in middle
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.solve(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2} -> {result2}")
    assert result2 == [1, 2] or result2 == [2, 1]

    # Test case 3: Duplicate values
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.solve(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3} -> {result3}")
    assert result3 == [0, 1] or result3 == [1, 0]

    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = solution.solve(nums4, target4)
    print(f"Test 4: nums={nums4}, target={target4} -> {result4}")
    assert result4 == [2, 4] or result4 == [4, 2]

    # Test case 5: Mixed positive and negative
    nums5 = [1, 5, -3, 7, -8]
    target5 = -11
    result5 = solution.solve(nums5, target5)
    print(f"Test 5: nums={nums5}, target={target5} -> {result5}")
    assert result5 == [2, 4] or result5 == [4, 2]

    print("\nAll tests passed!")
