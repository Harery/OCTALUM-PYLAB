"""
LeetCode #27: Remove Element

Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then
the first k elements of nums should hold the final result.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]

Example 2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]

Constraints:
    - 0 <= nums.length <= 100
    - 0 <= nums[i] <= 50
    - 0 <= val <= 100
"""

from typing import List


class Solution:
    """
    Solution class for Remove Element problem.

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using constant extra space
    """

    def solve(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val from nums in-place.

        Args:
            nums: List of integers (modified in-place)
            val: Value to remove from the list

        Returns:
            Number of elements remaining after removal (k),
            with first k elements containing the remaining elements
        """
        # Pointer for position to place next valid element
        write_index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic removal
    nums1 = [3, 2, 2, 3]
    k1 = solution.solve(nums1, 3)
    print(f"Test 1: k={k1}, nums[:k]={nums1[:k1]}")
    assert k1 == 2 and sorted(nums1[:k1]) == [2, 2]

    # Test case 2: Multiple removals
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = solution.solve(nums2, 2)
    print(f"Test 2: k={k2}, nums[:k]={nums2[:k2]}")
    assert k2 == 5 and sorted(nums2[:k2]) == [0, 0, 1, 3, 4]

    # Test case 3: Remove all elements
    nums3 = [1, 1, 1, 1]
    k3 = solution.solve(nums3, 1)
    print(f"Test 3: k={k3}, nums[:k]={nums3[:k3]}")
    assert k3 == 0

    # Test case 4: Remove none
    nums4 = [1, 2, 3, 4]
    k4 = solution.solve(nums4, 5)
    print(f"Test 4: k={k4}, nums[:k]={nums4[:k4]}")
    assert k4 == 4 and nums4[:k4] == [1, 2, 3, 4]

    # Test case 5: Empty array
    nums5: List[int] = []
    k5 = solution.solve(nums5, 1)
    print(f"Test 5: k={k5}, nums[:k]={nums5[:k5]}")
    assert k5 == 0

    # Test case 6: Single element to remove
    nums6 = [5]
    k6 = solution.solve(nums6, 5)
    print(f"Test 6: k={k6}, nums[:k]={nums6[:k6]}")
    assert k6 == 0

    # Test case 7: Single element to keep
    nums7 = [5]
    k7 = solution.solve(nums7, 3)
    print(f"Test 7: k={k7}, nums[:k]={nums7[:k7]}")
    assert k7 == 1 and nums7[:k7] == [5]

    print("\nAll tests passed!")
