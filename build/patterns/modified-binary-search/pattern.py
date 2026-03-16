"""
Modified Binary Search Pattern

Use when: Rotated arrays, unknown size, ceil/floor, rotated sorted
Time: O(log n), Space: O(1)
"""

from typing import List, Optional

# ============================================================
# TEMPLATE 1: Standard Binary Search
# ============================================================

def binary_search(nums: List[int], target: int) -> int:
    """Standard binary search. Time: O(log n)"""
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


def binary_search_recursive(nums: List[int], target: int, left: int = 0, right: int = None) -> int:
    """Recursive version. Time: O(log n)"""
    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# ============================================================
# TEMPLATE 2: Lower/Upper Bound
# ============================================================

def lower_bound(nums: List[int], target: int) -> int:
    """First index where nums[i] >= target. Time: O(log n)"""
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(nums: List[int], target: int) -> int:
    """First index where nums[i] > target. Time: O(log n)"""
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def search_range(nums: List[int], target: int) -> List[int]:
    """Find first and last position of target."""
    first = lower_bound(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = upper_bound(nums, target) - 1
    return [first, last]


# ============================================================
# TEMPLATE 3: Rotated Sorted Array
# ============================================================

def search_rotated(nums: List[int], target: int) -> int:
    """
    Search in rotated sorted array.
    Time: O(log n)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def find_min_rotated(nums: List[int]) -> int:
    """Find minimum in rotated array. Time: O(log n)"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


def find_rotation_index(nums: List[int]) -> int:
    """Find rotation pivot index. Time: O(log n)"""
    left, right = 0, len(nums) - 1

    if nums[left] <= nums[right]:
        return 0

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            return mid + 1

        if nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid + 1

    return 0


# ============================================================
# TEMPLATE 4: Search with Duplicates
# ============================================================

def search_rotated_duplicates(nums: List[int], target: int) -> bool:
    """
    Search in rotated array with duplicates.
    Worst case: O(n) when all elements same
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        # Can't determine which side is sorted
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


def find_min_rotated_duplicates(nums: List[int]) -> int:
    """Find min with duplicates. Worst case: O(n)"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1

    return nums[left]


# ============================================================
# TEMPLATE 5: Infinite/Unknown Size Array
# ============================================================

class ArrayReader:
    def __init__(self, arr: List[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        return float('inf')


def search_unknown_size(reader: ArrayReader, target: int) -> int:
    """Search in array of unknown size. Time: O(log n)"""
    left, right = 0, 1

    # Exponential search to find bounds
    while reader.get(right) < target:
        left = right
        right *= 2

    # Binary search in bounds
    while left <= right:
        mid = left + (right - left) // 2
        val = reader.get(mid)

        if val == target:
            return mid
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ============================================================
# TEMPLATE 6: Ceiling/Floor
# ============================================================

def ceiling_of_number(nums: List[int], target: int) -> int:
    """Smallest number >= target. Time: O(log n)"""
    if target > nums[-1]:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return nums[left]


def floor_of_number(nums: List[int], target: int) -> int:
    """Largest number <= target. Time: O(log n)"""
    if target < nums[0]:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return nums[right]


# ============================================================
# TEMPLATE 7: Peak Finding
# ============================================================

def find_peak_element(nums: List[int]) -> int:
    """Find any peak element. Time: O(log n)"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


def find_peak_2d(matrix: List[List[int]]) -> List[int]:
    """Find peak in 2D matrix. Time: O(n log m)"""
    rows, cols = len(matrix), len(matrix[0])

    def max_in_col(col: int) -> int:
        max_row = 0
        for r in range(1, rows):
            if matrix[r][col] > matrix[max_row][col]:
                max_row = r
        return max_row

    left, right = 0, cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        max_row = max_in_col(mid)

        left_val = matrix[max_row][mid - 1] if mid > 0 else -1
        right_val = matrix[max_row][mid + 1] if mid < cols - 1 else -1

        if left_val < matrix[max_row][mid] > right_val:
            return [max_row, mid]
        elif left_val > matrix[max_row][mid]:
            right = mid - 1
        else:
            left = mid + 1

    return [-1, -1]


# ============================================================
# TEMPLATE 8: Search in 2D Matrix
# ============================================================

def search_matrix(nums: List[List[int]], target: int) -> bool:
    """Search in row/col sorted matrix. Time: O(log(m×n))"""
    if not nums or not nums[0]:
        return False

    rows, cols = len(nums), len(nums[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        val = nums[mid // cols][mid % cols]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_matrix_2(nums: List[List[int]], target: int) -> bool:
    """Matrix sorted row and col wise. Time: O(m + n)"""
    if not nums or not nums[0]:
        return False

    row, col = 0, len(nums[0]) - 1

    while row < len(nums) and col >= 0:
        if nums[row][col] == target:
            return True
        elif nums[row][col] < target:
            row += 1
        else:
            col -= 1

    return False


# ============================================================
# TEMPLATE 9: Binary Search on Answer
# ============================================================

def sqrt_int(x: int) -> int:
    """Integer square root. Time: O(log x)"""
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right


def min_speed_on_time(dist: List[int], hour: float) -> int:
    """Min speed to reach on time. Binary search on answer."""
    if len(dist) > hour + 1:
        return -1

    def can_arrive(speed: int) -> bool:
        total = 0
        for i, d in enumerate(dist):
            t = d / speed
            total += math.ceil(t) if i < len(dist) - 1 else t
        return total <= hour

    import math
    left, right = 1, 10**7

    while left < right:
        mid = left + (right - left) // 2
        if can_arrive(mid):
            right = mid
        else:
            left = mid + 1

    return left


def split_array_largest_sum(nums: List[int], k: int) -> int:
    """Minimize largest sum among k splits. Binary search on answer."""
    left, right = max(nums), sum(nums)

    def can_split(max_sum: int) -> bool:
        count = 1
        current = 0
        for num in nums:
            if current + num > max_sum:
                count += 1
                current = num
            else:
                current += num
        return count <= k

    while left < right:
        mid = left + (right - left) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1

    return left


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    print("Binary search 9:", binary_search(nums, 9))

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    print("Search rotated 0:", search_rotated(nums2, 0))
    print("Min rotated:", find_min_rotated(nums2))

    nums3 = [1, 2, 3, 3, 3, 4, 5]
    print("Search range 3:", search_range(nums3, 3))

    nums4 = [1, 2, 1, 3, 5, 6, 4]
    print("Peak element:", find_peak_element(nums4))

    print("Sqrt 8:", sqrt_int(8))
