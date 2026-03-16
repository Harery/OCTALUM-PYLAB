"""
LeetCode #88: Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead
be stored inside the array nums1. To accommodate this, nums1 has a length
of m + n, where the first m elements denote the elements that should be
merged, and the last n elements are set to 0 and should be ignored.

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]

Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9
"""

from typing import List


class Solution:
    """
    Solution class for Merge Sorted Array.

    Time Complexity: O(m + n) - single pass through both arrays
    Space Complexity: O(1) - merging in place
    """

    def solve(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place to create sorted array.

        Args:
            nums1: List with m valid elements and n space for merging
            m: Number of valid elements in nums1
            nums2: List to merge into nums1
            n: Number of elements in nums2

        Returns:
            None (modifies nums1 in-place)
        """
        # Start from the end to avoid overwriting elements
        p1 = m - 1  # Pointer for nums1 valid elements
        p2 = n - 1  # Pointer for nums2
        write = m + n - 1  # Write position from end

        # Merge from right to left
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1

        # Copy remaining elements from nums2 (if any)
        # Remaining elements from nums1 are already in place
        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic merge
    nums1_1 = [1, 2, 3, 0, 0, 0]
    solution.solve(nums1_1, 3, [2, 5, 6], 3)
    print(f"Test 1: {nums1_1}")
    assert nums1_1 == [1, 2, 2, 3, 5, 6]

    # Test case 2: nums2 empty
    nums1_2 = [1]
    solution.solve(nums1_2, 1, [], 0)
    print(f"Test 2: {nums1_2}")
    assert nums1_2 == [1]

    # Test case 3: nums1 empty
    nums1_3 = [0]
    solution.solve(nums1_3, 0, [1], 1)
    print(f"Test 3: {nums1_3}")
    assert nums1_3 == [1]

    # Test case 4: nums2 all smaller
    nums1_4 = [4, 5, 6, 0, 0, 0]
    solution.solve(nums1_4, 3, [1, 2, 3], 3)
    print(f"Test 4: {nums1_4}")
    assert nums1_4 == [1, 2, 3, 4, 5, 6]

    # Test case 5: nums2 all larger
    nums1_5 = [1, 2, 3, 0, 0, 0]
    solution.solve(nums1_5, 3, [4, 5, 6], 3)
    print(f"Test 5: {nums1_5}")
    assert nums1_5 == [1, 2, 3, 4, 5, 6]

    # Test case 6: Single elements
    nums1_6 = [2, 0]
    solution.solve(nums1_6, 1, [1], 1)
    print(f"Test 6: {nums1_6}")
    assert nums1_6 == [1, 2]

    # Test case 7: With negatives
    nums1_7 = [-3, -1, 0, 0, 0]
    solution.solve(nums1_7, 2, [-2, 2, 4], 3)
    print(f"Test 7: {nums1_7}")
    assert nums1_7 == [-3, -2, -1, 2, 4]

    # Test case 8: All same elements
    nums1_8 = [1, 1, 1, 0, 0, 0]
    solution.solve(nums1_8, 3, [1, 1, 1], 3)
    print(f"Test 8: {nums1_8}")
    assert nums1_8 == [1, 1, 1, 1, 1, 1]

    print("\nAll tests passed!")
