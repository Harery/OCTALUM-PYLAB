"""
LeetCode #169: Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    - n == nums.length
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and O(1) space?
"""

from typing import List


class Solution:
    """
    Solution class for Majority Element using Boyer-Moore Voting Algorithm.

    Boyer-Moore Voting Algorithm:
    - Maintain a candidate and count
    - If count is 0, set current element as candidate
    - If current element equals candidate, increment count
    - Otherwise, decrement count
    - The majority element will survive as the final candidate

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using two variables
    """

    def solve(self, nums: List[int]) -> int:
        """
        Find the majority element (appears more than n/2 times).

        Args:
            nums: List with a guaranteed majority element

        Returns:
            The majority element
        """
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Simple majority
    nums1 = [3, 2, 3]
    result1 = solution.solve(nums1)
    print(f"Test 1: nums={nums1} -> {result1}")
    assert result1 == 3

    # Test case 2: Longer array with majority
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = solution.solve(nums2)
    print(f"Test 2: nums={nums2} -> {result2}")
    assert result2 == 2

    # Test case 3: Single element
    nums3 = [1]
    result3 = solution.solve(nums3)
    print(f"Test 3: nums={nums3} -> {result3}")
    assert result3 == 1

    # Test case 4: All same elements
    nums4 = [5, 5, 5, 5]
    result4 = solution.solve(nums4)
    print(f"Test 4: nums={nums4} -> {result4}")
    assert result4 == 5

    # Test case 5: Negative numbers
    nums5 = [-1, -1, 2, -1, 3, -1]
    result5 = solution.solve(nums5)
    print(f"Test 5: nums={nums5} -> {result5}")
    assert result5 == -1

    # Test case 6: Majority at beginning
    nums6 = [6, 6, 6, 1, 2, 3]
    result6 = solution.solve(nums6)
    print(f"Test 6: nums={nums6} -> {result6}")
    assert result6 == 6

    # Test case 7: Majority at end
    nums7 = [1, 2, 3, 7, 7, 7]
    result7 = solution.solve(nums7)
    print(f"Test 7: nums={nums7} -> {result7}")
    assert result7 == 7

    # Test case 8: Exactly n/2 + 1 occurrences
    nums8 = [1, 2, 1, 3, 1]
    result8 = solution.solve(nums8)
    print(f"Test 8: nums={nums8} -> {result8}")
    assert result8 == 1

    print("\nAll tests passed!")
