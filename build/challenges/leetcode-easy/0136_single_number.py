"""
LeetCode #136: Single Number

Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -3 * 10^4 <= nums[i] <= 3 * 10^4
    - Each element in the array appears twice except for one element
      which appears only once.
"""

from typing import List


class Solution:
    """
    Solution class for Single Number using XOR.

    XOR Properties:
    - a ^ a = 0 (any number XOR itself is 0)
    - a ^ 0 = a (any number XOR 0 is itself)
    - XOR is commutative and associative

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using one variable
    """

    def solve(self, nums: List[int]) -> int:
        """
        Find the single number that appears only once.

        Args:
            nums: List where every element appears twice except one

        Returns:
            The element that appears only once
        """
        result = 0

        for num in nums:
            result ^= num

        return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [2, 2, 1]
    result1 = solution.solve(nums1)
    print(f"Test 1: nums={nums1} -> {result1}")
    assert result1 == 1

    # Test case 2: Single number in middle
    nums2 = [4, 1, 2, 1, 2]
    result2 = solution.solve(nums2)
    print(f"Test 2: nums={nums2} -> {result2}")
    assert result2 == 4

    # Test case 3: Single element
    nums3 = [1]
    result3 = solution.solve(nums3)
    print(f"Test 3: nums={nums3} -> {result3}")
    assert result3 == 1

    # Test case 4: Negative numbers
    nums4 = [-1, -1, -2]
    result4 = solution.solve(nums4)
    print(f"Test 4: nums={nums4} -> {result4}")
    assert result4 == -2

    # Test case 5: Mixed positive and negative
    nums5 = [1, -1, 1]
    result5 = solution.solve(nums5)
    print(f"Test 5: nums={nums5} -> {result5}")
    assert result5 == -1

    # Test case 6: Larger array
    nums6 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    result6 = solution.solve(nums6)
    print(f"Test 6: nums={nums6} -> {result6}")
    assert result6 == 5

    # Test case 7: Zero in array
    nums7 = [0, 1, 1]
    result7 = solution.solve(nums7)
    print(f"Test 7: nums={nums7} -> {result7}")
    assert result7 == 0

    # Test case 8: Single zero
    nums8 = [0, 0, 0, 0, 5]
    result8 = solution.solve(nums8)
    print(f"Test 8: nums={nums8} -> {result8}")
    assert result8 == 5

    print("\nAll tests passed!")
