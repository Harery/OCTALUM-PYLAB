"""
Top K Elements Pattern

Use when: Finding k largest/smallest/most frequent elements
Time: O(n log k) with heap, O(n) average with quickselect
Space: O(k) for heap, O(1) for quickselect
"""

import heapq
from typing import List, Tuple
from collections import Counter
import random

# ============================================================
# TEMPLATE 1: K Largest Elements (Min Heap)
# ============================================================

def k_largest_heap(nums: List[int], k: int) -> List[int]:
    """
    Find k largest using min heap of size k.
    Time: O(n log k), Space: O(k)
    """
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap


def k_largest_nlarget(nums: List[int], k: int) -> List[int]:
    """Using built-in nlargest. Time: O(n log k)"""
    return heapq.nlargest(k, nums)


# ============================================================
# TEMPLATE 2: K Smallest Elements (Max Heap)
# ============================================================

def k_smallest_heap(nums: List[int], k: int) -> List[int]:
    """
    Find k smallest using max heap of size k.
    Time: O(n log k), Space: O(k)
    """
    heap = []  # Store negatives for max behavior

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        elif num < -heap[0]:
            heapq.heapreplace(heap, -num)

    return [-x for x in heap]


# ============================================================
# TEMPLATE 3: Kth Largest/Smallest (QuickSelect)
# ============================================================

def kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest using min heap.
    Time: O(n log k), Space: O(k)
    """
    return heapq.nlargest(k, nums)[-1]


def kth_smallest(nums: List[int], k: int) -> int:
    """Find kth smallest using max heap."""
    return heapq.nsmallest(k, nums)[-1]


def quickselect(nums: List[int], k: int) -> int:
    """
    Find kth smallest using quickselect.
    Average: O(n), Worst: O(n²), Space: O(1)
    """
    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        store = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        nums[right], nums[store] = nums[store], nums[right]
        return store

    left, right = 0, len(nums) - 1
    k = k - 1  # 0-indexed

    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot = partition(left, right, pivot_idx)

        if new_pivot == k:
            return nums[new_pivot]
        elif new_pivot < k:
            left = new_pivot + 1
        else:
            right = new_pivot - 1

    return -1


# ============================================================
# TEMPLATE 4: Top K Frequent Elements
# ============================================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements.
    Time: O(n log k), Space: O(n)
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """Manual heap implementation."""
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))

    return [num for freq, num in heap]


# ============================================================
# TEMPLATE 5: K Closest Points
# ============================================================

def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin.
    Time: O(n log k), Space: O(k)
    """
    def distance(p: List[int]) -> int:
        return p[0] ** 2 + p[1] ** 2

    heap = []

    for point in points:
        d = distance(point)
        if len(heap) < k:
            heapq.heappush(heap, (-d, point))
        elif d < -heap[0][0]:
            heapq.heapreplace(heap, (-d, point))

    return [point for d, point in heap]


def k_closest_points_sorted(points: List[List[int]], k: int) -> List[List[int]]:
    """Using sort. Time: O(n log n)"""
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]


# ============================================================
# TEMPLATE 6: Sort Characters by Frequency
# ============================================================

def frequency_sort(s: str) -> str:
    """
    Sort characters by frequency.
    Time: O(n log k), Space: O(n)
    """
    count = Counter(s)
    chars = sorted(count.keys(), key=lambda x: -count[x])
    return ''.join(c * count[c] for c in chars)


# ============================================================
# TEMPLATE 7: K Pairs with Largest Sums
# ============================================================

def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    K pairs with smallest sums.
    Time: O(k log k), Space: O(k)
    """
    if not nums1 or not nums2:
        return []

    heap = [(nums1[0] + nums2[0], 0, 0)]
    result = []
    visited = {(0, 0)}

    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))

    return result


# ============================================================
# TEMPLATE 8: Reorganize String
# ============================================================

def reorganize_string(s: str) -> str:
    """
    Reorganize so no adjacent chars same.
    Time: O(n log k), Space: O(k)
    """
    count = Counter(s)
    max_heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(max_heap)

    result = []
    prev = None

    while max_heap or prev:
        if not max_heap and prev:
            return ""

        freq, char = heapq.heappop(max_heap)
        result.append(char)
        freq += 1  # Decrease negative (increase toward 0)

        if prev:
            heapq.heappush(max_heap, prev)
            prev = None

        if freq < 0:
            prev = (freq, char)

    return ''.join(result)


# ============================================================
# TEMPLATE 9: Task Scheduler
# ============================================================

def least_interval_heap(tasks: List[str], n: int) -> int:
    """
    Min time with cooldown using max heap.
    Time: O(n), Space: O(1)
    """
    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = []  # (count, available_time)

    while max_heap or queue:
        time += 1

        if max_heap:
            cnt = heapq.heappop(max_heap) + 1
            if cnt < 0:
                queue.append((cnt, time + n))

        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.pop(0)[0])

    return time


# ============================================================
# TEMPLATE 10: Find K Closest Elements
# ============================================================

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    """
    K closest integers to x in sorted array.
    Time: O(log n + k), Space: O(1)
    """
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    print("3 largest:", k_largest_heap(nums[:], 3))
    print("2nd largest:", kth_largest(nums[:], 2))

    nums2 = [1, 1, 1, 2, 2, 3]
    print("Top 2 frequent:", top_k_frequent(nums2, 2))

    points = [[3, 3], [5, -1], [-2, 4]]
    print("K closest:", k_closest_points(points, 2))

    print("Reorganize 'aab':", reorganize_string("aab"))

    arr = [1, 2, 3, 4, 5]
    print("4 closest to 3:", find_closest_elements(arr, 4, 3))
