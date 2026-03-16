"""
LeetCode #26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k unique elements after removing the duplicates,
then the first k elements of nums should hold the final result.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.
"""

from typing import List


class Solution:
    """
    Solution class for Remove Duplicates from Sorted Array.

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using constant extra space
    """

    def solve(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.

        Args:
            nums: Sorted list of integers (modified in-place)

        Returns:
            Number of unique elements (k), with first k elements of nums
            containing the unique elements
        """
        if not nums:
            return 0

        # Pointer for position to place next unique element
        write_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic duplicates
    nums1 = [1, 1, 2]
    k1 = solution.solve(nums1)
    print(f"Test 1: k={k1}, nums[:k]={nums1[:k1]}")
    assert k1 == 2 and nums1[:k1] == [1, 2]

    # Test case 2: Multiple duplicates
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.solve(nums2)
    print(f"Test 2: k={k2}, nums[:k]={nums2[:k2]}")
    assert k2 == 5 and nums2[:k2] == [0, 1, 2, 3, 4]

    # Test case 3: No duplicates
    nums3 = [1, 2, 3, 4, 5]
    k3 = solution.solve(nums3)
    print(f"Test 3: k={k3}, nums[:k]={nums3[:k3]}")
    assert k3 == 5 and nums3[:k3] == [1, 2, 3, 4, 5]

    # Test case 4: All same elements
    nums4 = [7, 7, 7, 7, 7]
    k4 = solution.solve(nums4)
    print(f"Test 4: k={k4}, nums[:k]={nums4[:k4]}")
    assert k4 == 1 and nums4[:k4] == [7]

    # Test case 5: Single element
    nums5 = [42]
    k5 = solution.solve(nums5)
    print(f"Test 5: k={k5}, nums[:k]={nums5[:k5]}")
    assert k5 == 1 and nums5[:k5] == [42]

    # Test case 6: Two elements same
    nums6 = [1, 1]
    k6 = solution.solve(nums6)
    print(f"Test 6: k={k6}, nums[:k]={nums6[:k6]}")
    assert k6 == 1 and nums6[:k6] == [1]

    # Test case 7: Two elements different
    nums7 = [1, 2]
    k7 = solution.solve(nums7)
    print(f"Test 7: k={k7}, nums[:k]={nums7[:k7]}")
    assert k7 == 2 and nums7[:k7] == [1, 2]

    print("\nAll tests passed!")
