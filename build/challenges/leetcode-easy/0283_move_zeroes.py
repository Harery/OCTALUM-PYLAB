"""
LeetCode #283: Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


class Solution:
    """
    Two-pointer approach: one for reading, one for writing non-zeros.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def solve(self, nums: List[int]) -> None:
        """Move all zeros to end in-place."""
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    solution = Solution()

    nums1 = [0, 1, 0, 3, 12]
    solution.solve(nums1)
    print(f"Test 1: {nums1}")
    assert nums1 == [1, 3, 12, 0, 0]

    nums2 = [0]
    solution.solve(nums2)
    print(f"Test 2: {nums2}")
    assert nums2 == [0]

    nums3 = [1, 2, 3]
    solution.solve(nums3)
    print(f"Test 3: {nums3}")
    assert nums3 == [1, 2, 3]

    nums4 = [0, 0, 0, 0]
    solution.solve(nums4)
    print(f"Test 4: {nums4}")
    assert nums4 == [0, 0, 0, 0]

    nums5 = [1, 0, 2, 0, 3, 0, 4]
    solution.solve(nums5)
    print(f"Test 5: {nums5}")
    assert nums5 == [1, 2, 3, 4, 0, 0, 0]

    nums6 = [0, 0, 1]
    solution.solve(nums6)
    print(f"Test 6: {nums6}")
    assert nums6 == [1, 0, 0]

    nums7 = [-1, 0, -2, 0, -3]
    solution.solve(nums7)
    print(f"Test 7: {nums7}")
    assert nums7 == [-1, -2, -3, 0, 0]

    print("\nAll tests passed!")
