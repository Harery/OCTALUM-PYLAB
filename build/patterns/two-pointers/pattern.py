"""
Two Pointers Pattern

Use when: Array/string problems where you compare or process pairs of elements
Time: Usually O(n) with single pass
Space: O(1) in-place processing
"""

from typing import List, Optional

# ============================================================
# TEMPLATE 1: Opposite Direction (start from both ends)
# ============================================================

def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target in SORTED array.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome, ignoring non-alphanumeric.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def reverse_array(nums: List[int]) -> None:
    """Reverse array in-place. Time: O(n), Space: O(1)"""
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ============================================================
# TEMPLATE 2: Same Direction (fast/slow pointers)
# ============================================================

def remove_duplicates_sorted(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place.
    Returns new length. Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    write = 1  # Position to write next unique element

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write


def move_zeros(nums: List[int]) -> None:
    """
    Move all zeros to end while maintaining order.
    Time: O(n), Space: O(1)
    """
    write = 0  # Position for next non-zero

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


def remove_element(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in-place.
    Time: O(n), Space: O(1)
    """
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write


# ============================================================
# TEMPLATE 3: Two Arrays / Lists
# ============================================================

def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place (nums1 has buffer).
    Start from end to avoid overwriting. Time: O(m+n), Space: O(1)
    """
    p1, p2, write = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1

    # Copy remaining elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]


def intersection_sorted(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find intersection of two sorted arrays. Time: O(n+m), Space: O(1)"""
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result


# ============================================================
# TEMPLATE 4: Triple Pointers (Three Sum variations)
# ============================================================

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets summing to zero.
    Time: O(n²), Space: O(1) excluding output
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ============================================================
# TEMPLATE 5: Container With Most Water type
# ============================================================

def max_area(height: List[int]) -> int:
    """
    Find max area between two lines.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        max_water = max(max_water, width * min_height)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


def trap_rain_water(height: List[int]) -> int:
    """
    Calculate trapped rainwater.
    Time: O(n), Space: O(1)
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    # Two Sum Sorted
    print("Two Sum:", two_sum_sorted([2, 7, 11, 15], 9))

    # Palindrome
    print("Palindrome:", is_palindrome("A man, a plan, a canal: Panama"))

    # Remove Duplicates
    arr = [1, 1, 2, 2, 3, 4, 4]
    print("Remove dups length:", remove_duplicates_sorted(arr), arr)

    # Three Sum
    print("Three Sum:", three_sum([-1, 0, 1, 2, -1, -4]))

    # Max Area
    print("Max Area:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    # Trap Water
    print("Trap Water:", trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
