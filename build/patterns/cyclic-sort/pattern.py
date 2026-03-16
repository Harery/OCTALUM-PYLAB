"""
Cyclic Sort Pattern

Use when: Array contains numbers in a range (1 to n or 0 to n-1)
Time: O(n), Space: O(1)
"""

from typing import List, Optional

# ============================================================
# TEMPLATE 1: Basic Cyclic Sort
# ============================================================

def cyclic_sort(nums: List[int]) -> None:
    """
    Sort array in-place where nums contains 1 to n.
    Time: O(n), Space: O(1)

    Key insight: Value v should be at index v-1 (for 1-indexed)
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1  # Where nums[i] should go

        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1


def cyclic_sort_zero_indexed(nums: List[int]) -> None:
    """
    Sort array where nums contains 0 to n-1.
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i]  # 0-indexed: value = index

        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1


# ============================================================
# TEMPLATE 2: Find Missing Number
# ============================================================

def find_missing_number(nums: List[int]) -> int:
    """
    Find missing number in array of 0 to n.
    Time: O(n), Space: O(1)
    """
    i = 0
    n = len(nums)

    while i < n:
        correct_idx = nums[i]
        if nums[i] < n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n  # Missing n itself


def find_missing_number_xor(nums: List[int]) -> int:
    """
    Alternative using XOR. No modification.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    missing = n

    for i, num in enumerate(nums):
        missing ^= i ^ num

    return missing


def find_all_missing_numbers(nums: List[int]) -> List[int]:
    """
    Find all missing numbers in 1 to n.
    Time: O(n), Space: O(1) excluding output
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)

    return missing


# ============================================================
# TEMPLATE 3: Find Duplicate Number
# ============================================================

def find_duplicate(nums: List[int]) -> int:
    """
    Find duplicate in array of 1 to n with one duplicate.
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1

        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]

    return -1


def find_duplicate_fast_slow(nums: List[int]) -> int:
    """
    Find duplicate without modifying array (Floyd's cycle).
    Time: O(n), Space: O(1)
    """
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


def find_all_duplicates(nums: List[int]) -> List[int]:
    """
    Find all duplicates in array of 1 to n.
    Time: O(n), Space: O(1) excluding output
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicates.append(nums[i])

    return duplicates


# ============================================================
# TEMPLATE 4: Find Missing and Duplicate
# ============================================================

def find_error_nums(nums: List[int]) -> List[int]:
    """
    Find duplicate and missing number.
    Returns [duplicate, missing].
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    return [-1, -1]


# ============================================================
# TEMPLATE 5: First Missing Positive
# ============================================================

def first_missing_positive(nums: List[int]) -> int:
    """
    Find first missing positive integer.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    i = 0

    while i < n:
        correct_idx = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


# ============================================================
# TEMPLATE 6: Corrupt Pair
# ============================================================

def find_corrupt_pair(nums: List[int]) -> List[int]:
    """
    Find one duplicate and one missing number.
    Returns [duplicate, missing].
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    return []


# ============================================================
# TEMPLATE 7: Smallest Missing Positive in Sorted Array
# ============================================================

def smallest_missing_positive_sorted(nums: List[int]) -> int:
    """
    Find smallest missing positive in sorted array.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > mid + 1:
            right = mid
        else:
            left = mid + 1

    return left + 1


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    arr = [3, 1, 5, 4, 2]
    cyclic_sort(arr)
    print("Cyclic sort:", arr)

    print("Missing in [4, 0, 3, 1]:", find_missing_number([4, 0, 3, 1]))

    print("All missing in [2, 3, 1, 8, 2, 3, 5, 1]:",
          find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))

    print("Duplicate in [1, 4, 4, 3, 2]:", find_duplicate([1, 4, 4, 3, 2]))

    print("Error nums [1, 2, 2, 4]:", find_error_nums([1, 2, 2, 4]))

    print("First missing positive [3, 4, -1, 1]:",
          first_missing_positive([3, 4, -1, 1]))
