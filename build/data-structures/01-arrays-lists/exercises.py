"""
Array and List Practice Exercises
=================================
Practice problems with solutions for mastering Python lists.

Each problem includes:
- Problem description
- Solution approach
- Time and space complexity analysis
"""

from __future__ import annotations


# ============================================================================
# EASY EXERCISES
# ============================================================================

def exercise_1_two_sum(nums: list[int], target: int) -> list[int]:
    """
    EASY: Two Sum

    Given an array of integers and a target, return indices of two numbers
    that add up to the target.

    Example:
        nums = [2, 7, 11, 15], target = 9
        return [0, 1] (because nums[0] + nums[1] = 9)

    Solution: Use hash map for O(1) lookups
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def exercise_2_max_consecutive_ones(nums: list[int]) -> int:
    """
    EASY: Max Consecutive Ones

    Given a binary array, find the maximum number of consecutive 1s.

    Example:
        nums = [1, 1, 0, 1, 1, 1]
        return 3

    Solution: Single pass with counter
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_count = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


def exercise_3_remove_duplicates(nums: list[int]) -> int:
    """
    EASY: Remove Duplicates from Sorted Array

    Remove duplicates in place and return new length.

    Example:
        nums = [1, 1, 2]
        After: nums = [1, 2, _], return 2

    Solution: Two pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index


def exercise_4_merge_sorted_arrays(
    nums1: list[int], m: int, nums2: list[int], n: int
) -> None:
    """
    EASY: Merge Sorted Arrays

    Merge nums2 into nums1 in place. nums1 has size m+n with extra space.

    Example:
        nums1 = [1, 2, 3, 0, 0, 0], m = 3
        nums2 = [2, 5, 6], n = 3
        After: nums1 = [1, 2, 2, 3, 5, 6]

    Solution: Fill from end to avoid overwriting
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


def exercise_5_best_time_to_buy_sell(prices: list[int]) -> int:
    """
    EASY: Best Time to Buy and Sell Stock

    Find maximum profit from one transaction.

    Example:
        prices = [7, 1, 5, 3, 6, 4]
        return 5 (buy at 1, sell at 6)

    Solution: Track minimum price and max profit
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# ============================================================================
# MEDIUM EXERCISES
# ============================================================================

def exercise_6_product_except_self(nums: list[int]) -> list[int]:
    """
    MEDIUM: Product of Array Except Self

    Return array where each element is product of all elements except self.
    Cannot use division.

    Example:
        nums = [1, 2, 3, 4]
        return [24, 12, 8, 6]

    Solution: Left and right product arrays
    Time Complexity: O(n)
    Space Complexity: O(1) extra space (output array doesn't count)
    """
    n = len(nums)
    result = [1] * n

    # Build left products in result
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Multiply by right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


def exercise_7_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    MEDIUM: Subarray Sum Equals K

    Count number of contiguous subarrays that sum to k.

    Example:
        nums = [1, 1, 1], k = 2
        return 2 ([1,1] at index 0 and [1,1] at index 1)

    Solution: Prefix sum with hash map
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_count: dict[int, int] = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count


def exercise_8_rotate_array(nums: list[int], k: int) -> None:
    """
    MEDIUM: Rotate Array

    Rotate array to the right by k steps in place.

    Example:
        nums = [1, 2, 3, 4, 5, 6, 7], k = 3
        After: nums = [5, 6, 7, 1, 2, 3, 4]

    Solution: Reverse three times
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    if n == 0:
        return
    k = k % n
    if k == 0:
        return

    def reverse(arr: list[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)


def exercise_9_container_with_most_water(height: list[int]) -> int:
    """
    MEDIUM: Container With Most Water

    Find two lines that together with x-axis form container holding most water.

    Example:
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        return 49

    Solution: Two pointers from ends
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        container_height = min(height[left], height[right])
        max_area = max(max_area, width * container_height)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def exercise_10_spiral_order(matrix: list[list[int]]) -> list[int]:
    """
    MEDIUM: Spiral Matrix

    Return all elements of matrix in spiral order.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        return [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Solution: Layer by layer traversal
    Time Complexity: O(m * n)
    Space Complexity: O(1) extra (excluding output)
    """
    if not matrix or not matrix[0]:
        return []

    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Traverse left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


# ============================================================================
# HARD EXERCISES
# ============================================================================

def exercise_11_trap_rain_water(height: list[int]) -> int:
    """
    HARD: Trapping Rain Water

    Calculate how much water can be trapped after raining.

    Example:
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        return 6

    Solution: Two pointers with max left/right tracking
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]
    water = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            water += max_right - height[right]

    return water


def exercise_12_find_median_sorted_arrays(
    nums1: list[int], nums2: list[int]
) -> float:
    """
    HARD: Median of Two Sorted Arrays

    Find median of two sorted arrays in O(log(m+n)) time.

    Example:
        nums1 = [1, 3], nums2 = [2]
        return 2.0

    Solution: Binary search on smaller array
    Time Complexity: O(log(min(m, n)))
    Space Complexity: O(1)
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half - partition1

        max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float("inf") if partition1 == m else nums1[partition1]

        max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float("inf") if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if total % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            return float(max(max_left1, max_left2))
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    return 0.0


def exercise_13_longest_consecutive(nums: list[int]) -> int:
    """
    HARD: Longest Consecutive Sequence

    Find length of longest consecutive elements sequence.
    Must run in O(n) time.

    Example:
        nums = [100, 4, 200, 1, 3, 2]
        return 4 ([1, 2, 3, 4])

    Solution: Hash set with sequence start detection
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting if this is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length


def exercise_14_first_missing_positive(nums: list[int]) -> int:
    """
    HARD: First Missing Positive

    Find smallest missing positive integer in O(n) time and O(1) space.

    Example:
        nums = [3, 4, -1, 1]
        return 2

    Solution: Place each number at its index (cyclic sort variant)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)

    # Place each number at its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    # Find first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


def exercise_15_sliding_window_maximum(
    nums: list[int], k: int
) -> list[int]:
    """
    HARD: Sliding Window Maximum

    Find max in each sliding window of size k.

    Example:
        nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
        return [3, 3, 5, 5, 6, 7]

    Solution: Deque to track indices of potential maximums
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if not nums or k == 0:
        return []

    from collections import deque

    dq: deque[int] = deque()
    result: list[int] = []

    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# ============================================================================
# UTILITY FUNCTIONS FOR TESTING
# ============================================================================

def run_all_exercises() -> dict[str, tuple[int | list[int] | float, str]]:
    """Run all exercises with test cases."""
    results: dict[str, tuple[int | list[int] | float, str]] = {}

    # Easy
    results["two_sum"] = (exercise_1_two_sum([2, 7, 11, 15], 9), "[0, 1]")
    results["max_consecutive_ones"] = (exercise_2_max_consecutive_ones([1, 1, 0, 1, 1, 1]), "3")
    results["remove_duplicates"] = (exercise_3_remove_duplicates([1, 1, 2]), "2")
    results["best_time"] = (exercise_5_best_time_to_buy_sell([7, 1, 5, 3, 6, 4]), "5")

    # Medium
    results["product_except_self"] = (exercise_6_product_except_self([1, 2, 3, 4]), "[24, 12, 8, 6]")
    results["subarray_sum"] = (exercise_7_subarray_sum_k([1, 1, 1], 2), "2")
    results["container"] = (exercise_9_container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), "49")

    # Hard
    results["trap_water"] = (exercise_11_trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), "6")
    results["longest_consecutive"] = (exercise_13_longest_consecutive([100, 4, 200, 1, 3, 2]), "4")
    results["first_missing"] = (exercise_14_first_missing_positive([3, 4, -1, 1]), "2")

    return results


if __name__ == "__main__":
    print("=== Exercise Results ===\n")

    results = run_all_exercises()
    for name, (result, expected) in results.items():
        print(f"{name}: {result} (expected: {expected})")
