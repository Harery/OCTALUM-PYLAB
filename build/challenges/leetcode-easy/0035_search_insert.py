"""
LeetCode #35: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums contains distinct values sorted in ascending order.
    - -10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    """
    Solution class for Search Insert Position using binary search.

    Time Complexity: O(log n) - binary search
    Space Complexity: O(1) - only using constant extra space
    """

    def solve(self, nums: List[int], target: int) -> int:
        """
        Find the index where target is or should be inserted.

        Args:
            nums: Sorted list of distinct integers
            target: Value to find or insert

        Returns:
            Index of target if found, otherwise insertion position
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If not found, left is the insertion position
        return left


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Target found
    nums1 = [1, 3, 5, 6]
    result1 = solution.solve(nums1, 5)
    print(f"Test 1: nums={nums1}, target=5 -> {result1}")
    assert result1 == 2

    # Test case 2: Target not found, insert in middle
    nums2 = [1, 3, 5, 6]
    result2 = solution.solve(nums2, 2)
    print(f"Test 2: nums={nums2}, target=2 -> {result2}")
    assert result2 == 1

    # Test case 3: Target not found, insert at end
    nums3 = [1, 3, 5, 6]
    result3 = solution.solve(nums3, 7)
    print(f"Test 3: nums={nums3}, target=7 -> {result3}")
    assert result3 == 4

    # Test case 4: Target not found, insert at beginning
    nums4 = [1, 3, 5, 6]
    result4 = solution.solve(nums4, 0)
    print(f"Test 4: nums={nums4}, target=0 -> {result4}")
    assert result4 == 0

    # Test case 5: Single element found
    nums5 = [1]
    result5 = solution.solve(nums5, 1)
    print(f"Test 5: nums={nums5}, target=1 -> {result5}")
    assert result5 == 0

    # Test case 6: Single element insert before
    nums6 = [1]
    result6 = solution.solve(nums6, 0)
    print(f"Test 6: nums={nums6}, target=0 -> {result6}")
    assert result6 == 0

    # Test case 7: Single element insert after
    nums7 = [1]
    result7 = solution.solve(nums7, 2)
    print(f"Test 7: nums={nums7}, target=2 -> {result7}")
    assert result7 == 1

    # Test case 8: Target at first position
    nums8 = [1, 3, 5]
    result8 = solution.solve(nums8, 1)
    print(f"Test 8: nums={nums8}, target=1 -> {result8}")
    assert result8 == 0

    # Test case 9: Target at last position
    nums9 = [1, 3, 5]
    result9 = solution.solve(nums9, 5)
    print(f"Test 9: nums={nums9}, target=5 -> {result9}")
    assert result9 == 2

    print("\nAll tests passed!")
