"""
Two Heaps Pattern

Use when: Finding median, balancing elements, min/max of two halves
Time: O(n log n) for n insertions, O(log n) per operation
Space: O(n)
"""

import heapq
from typing import List, Optional

# ============================================================
# TEMPLATE 1: Find Median from Data Stream
# ============================================================

class MedianFinder:
    """
    Maintain two heaps to find median in O(log n).
    - max_heap (left): smaller half (use negative for max behavior)
    - min_heap (right): larger half

    Time: O(log n) per insertion, O(1) for median
    Space: O(n)
    """

    def __init__(self):
        self.max_heap = []  # Left half (smaller), stored as negatives
        self.min_heap = []  # Right half (larger)

    def addNum(self, num: int) -> None:
        # Add to max_heap first
        heapq.heappush(self.max_heap, -num)

        # Balance: move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has equal or one more element
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


# ============================================================
# TEMPLATE 2: Sliding Window Median
# ============================================================

def median_sliding_window(nums: List[int], k: int) -> List[float]:
    """
    Find median for each sliding window of size k.
    Time: O(n log k), Space: O(k)
    """
    import bisect

    window = sorted(nums[:k])
    result = []

    def get_median():
        if k % 2 == 1:
            return window[k // 2]
        return (window[k // 2 - 1] + window[k // 2]) / 2

    result.append(get_median())

    for i in range(k, len(nums)):
        # Remove old element
        window.pop(bisect.bisect_left(window, nums[i - k]))
        # Add new element
        bisect.insort(window, nums[i])
        result.append(get_median())

    return result


# ============================================================
# TEMPLATE 3: IPO / Maximize Capital
# ============================================================

def find_maximized_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    """
    Do at most k projects, need capital[i] to start, earn profits[i].
    Time: O(n log n), Space: O(n)
    """
    n = len(profits)
    projects = sorted(zip(capital, profits))  # Sort by capital needed

    max_profit_heap = []  # Max heap of available profits
    i = 0

    for _ in range(k):
        # Add all projects we can afford
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_profit_heap, -projects[i][1])
            i += 1

        if not max_profit_heap:
            break

        # Take the most profitable available project
        w += -heapq.heappop(max_profit_heap)

    return w


# ============================================================
# TEMPLATE 4: Sliding Window Maximum (with two heaps)
# ============================================================

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Find max in each sliding window using max heap with lazy removal.
    Time: O(n log n), Space: O(n)
    """
    result = []
    max_heap = [(-nums[i], i) for i in range(k)]
    heapq.heapify(max_heap)

    result.append(-max_heap[0][0])

    for i in range(k, len(nums)):
        heapq.heappush(max_heap, (-nums[i], i))

        # Remove elements outside window (lazy deletion)
        while max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)

        result.append(-max_heap[0][0])

    return result


# ============================================================
# TEMPLATE 5: Kth Smallest/Largest in Sorted Matrix
# ============================================================

def kth_smallest_matrix(matrix: List[List[int]], k: int) -> int:
    """
    Find kth smallest in sorted matrix.
    Time: O(k log k), Space: O(k)
    """
    n = len(matrix)
    min_heap = [(matrix[0][0], 0, 0)]
    visited = {(0, 0)}

    for _ in range(k - 1):
        val, r, c = heapq.heappop(min_heap)

        if r + 1 < n and (r + 1, c) not in visited:
            heapq.heappush(min_heap, (matrix[r + 1][c], r + 1, c))
            visited.add((r + 1, c))
        if c + 1 < n and (r, c + 1) not in visited:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            visited.add((r, c + 1))

    return min_heap[0][0]


# ============================================================
# TEMPLATE 6: Find Right Interval
# ============================================================

def find_right_interval(intervals: List[List[int]]) -> List[int]:
    """
    For each interval, find index of interval with start >= end.
    Time: O(n log n), Space: O(n)
    """
    n = len(intervals)

    # Max heap for starts (to process from largest start)
    max_start_heap = [(-intervals[i][0], i) for i in range(n)]
    heapq.heapify(max_start_heap)

    # Max heap for ends
    max_end_heap = [(-intervals[i][1], i) for i in range(n)]
    heapq.heapify(max_end_heap)

    result = [-1] * n

    for _ in range(n):
        end_val, end_idx = heapq.heappop(max_end_heap)
        end_val = -end_val

        # Find smallest start >= end
        while max_start_heap and -max_start_heap[0][0] >= end_val:
            start_val, start_idx = heapq.heappop(max_start_heap)
            result[end_idx] = start_idx

        if max_start_heap:
            result[end_idx] = max_start_heap[0][1]

    return result


# ============================================================
# TEMPLATE 7: Refuel Stops
# ============================================================

def min_refuel_stops(target: int, start_fuel: int, stations: List[List[int]]) -> int:
    """
    Minimum refuel stops to reach target.
    Time: O(n log n), Space: O(n)
    """
    max_heap = []  # Available fuel at passed stations
    stops = 0
    fuel = start_fuel
    prev = 0

    for pos, gas in stations + [[target, 0]]:
        distance = pos - prev
        # Use fuel from heap to cover distance
        while fuel < distance and max_heap:
            fuel += -heapq.heappop(max_heap)
            stops += 1

        if fuel < distance:
            return -1

        fuel -= distance
        prev = pos
        heapq.heappush(max_heap, -gas)

    return stops


# ============================================================
# TEMPLATE 8: Task Scheduler
# ============================================================

def least_interval(tasks: List[str], n: int) -> int:
    """
    Minimum time to complete tasks with cooldown n.
    Uses max heap for most frequent tasks.
    Time: O(n), Space: O(1) since 26 tasks max
    """
    from collections import Counter

    counts = Counter(tasks)
    max_heap = [-c for c in counts.values()]
    heapq.heapify(max_heap)

    time = 0

    while max_heap:
        cycle = []
        for _ in range(n + 1):
            if max_heap:
                cycle.append(-heapq.heappop(max_heap))

        for count in cycle:
            if count > 1:
                heapq.heappush(max_heap, -(count - 1))

        time += n + 1 if max_heap else len(cycle)

    return time


# ============================================================
# TEMPLATE 9: Meeting Rooms III
# ============================================================

def most_booked(n: int, meetings: List[List[int]]) -> int:
    """
    Find most booked room.
    Time: O(m log n), Space: O(n)
    """
    meetings.sort()

    available = list(range(n))  # Available room numbers
    heapq.heapify(available)

    busy = []  # (end_time, room_number)
    bookings = [0] * n

    for start, end in meetings:
        # Free up rooms that have finished
        while busy and busy[0][0] <= start:
            _, room = heapq.heappop(busy)
            heapq.heappush(available, room)

        if available:
            room = heapq.heappop(available)
            heapq.heappush(busy, (end, room))
        else:
            # Wait for earliest room
            earliest_end, room = heapq.heappop(busy)
            duration = end - start
            heapq.heappush(busy, (earliest_end + duration, room))

        bookings[busy[0][1]] += 1

    return bookings.index(max(bookings))


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    mf = MedianFinder()
    for num in [1, 2, 3]:
        mf.addNum(num)
        print(f"After {num}, median:", mf.findMedian())

    print("Sliding window median:", median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

    print("Sliding window max:", max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

    print("Least interval:", least_interval(["A", "A", "A", "B", "B", "B"], 2))

    print("Min refuel stops:", min_refuel_stops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
