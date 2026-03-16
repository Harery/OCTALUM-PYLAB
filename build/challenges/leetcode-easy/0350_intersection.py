"""
LeetCode #350: Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Constraints:
    - 1 <= nums1.length, nums2.length <= 1000
    - 0 <= nums1[i], nums2[i] <= 1000
"""

from typing import List, Dict


class Solution:
    """
    Uses hash map to count occurrences in first array, then match with second.

    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    """

    def solve(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Find intersection with duplicates."""
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counter: Dict[int, int] = {}
        for num in nums1:
            counter[num] = counter.get(num, 0) + 1

        result: List[int] = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.solve([1, 2, 2, 1], [2, 2])
    print(f"Test 1: {result1}")
    assert sorted(result1) == [2, 2]

    result2 = solution.solve([4, 9, 5], [9, 4, 9, 8, 4])
    print(f"Test 2: {result2}")
    assert sorted(result2) == [4, 9]

    result3 = solution.solve([1, 2, 3], [4, 5, 6])
    print(f"Test 3: {result3}")
    assert result3 == []

    result4 = solution.solve([1, 1, 1], [1, 1, 1])
    print(f"Test 4: {result4}")
    assert sorted(result4) == [1, 1, 1]

    result5 = solution.solve([], [1, 2, 3])
    print(f"Test 5: {result5}")
    assert result5 == []

    result6 = solution.solve([1, 2, 3], [])
    print(f"Test 6: {result6}")
    assert result6 == []

    result7 = solution.solve([1, 2, 2, 3, 3, 3], [2, 2, 2, 3, 3])
    print(f"Test 7: {result7}")
    assert sorted(result7) == [2, 2, 3, 3]

    result8 = solution.solve([0, 0, 0], [0])
    print(f"Test 8: {result8}")
    assert result8 == [0]

    print("\nAll tests passed!")
