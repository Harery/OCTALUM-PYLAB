"""
Merge Intervals Pattern

Use when: Problems involving overlapping intervals, meetings, ranges
Time: O(n log n) for sorting, O(n) for merging
Space: O(n) for result
"""

from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class Interval:
    start: int
    end: int

    def overlaps(self, other: 'Interval') -> bool:
        return self.start <= other.end and other.start <= self.end


# ============================================================
# TEMPLATE 1: Merge Overlapping Intervals
# ============================================================

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge all overlapping intervals.
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


def merge_intervals_class(intervals: List[Interval]) -> List[Interval]:
    """Alternative using Interval class."""
    if not intervals:
        return []

    intervals.sort(key=lambda x: x.start)
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current.start <= last.end:
            last.end = max(last.end, current.end)
        else:
            merged.append(current)

    return merged


# ============================================================
# TEMPLATE 2: Insert Interval
# ============================================================

def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Insert new interval and merge if needed.
    Time: O(n), Space: O(n)
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # Add remaining intervals
    result.extend(intervals[i:])

    return result


# ============================================================
# TEMPLATE 3: Check If Intervals Overlap
# ============================================================

def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Check if person can attend all meetings (no overlaps).
    Time: O(n log n), Space: O(1)
    """
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


def has_overlap(intervals: List[List[int]]) -> bool:
    """Check if any two intervals overlap."""
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return True

    return False


# ============================================================
# TEMPLATE 4: Find Overlapping Intervals
# ============================================================

def interval_intersection(first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
    """
    Find intersection of two interval lists (already sorted).
    Time: O(n + m), Space: O(n + m)
    """
    result = []
    i = j = 0

    while i < len(first) and j < len(second):
        start = max(first[i][0], second[j][0])
        end = min(first[i][1], second[j][1])

        if start <= end:
            result.append([start, end])

        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1

    return result


# ============================================================
# TEMPLATE 5: Meeting Rooms Variants
# ============================================================

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Find minimum meeting rooms needed.
    Time: O(n log n), Space: O(n)

    Uses two pointers with sorted start/end times.
    """
    if not intervals:
        return 0

    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    rooms = 0
    end_ptr = 0

    for start in starts:
        if start >= ends[end_ptr]:
            end_ptr += 1  # Free a room
        else:
            rooms += 1  # Need new room

    return rooms


def min_meeting_rooms_heap(intervals: List[List[int]]) -> int:
    """
    Alternative using min heap.
    Time: O(n log n), Space: O(n)
    """
    import heapq

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = [intervals[0][1]]  # Min heap of end times

    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


# ============================================================
# TEMPLATE 6: Non-overlapping Intervals
# ============================================================

def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Minimum number of intervals to remove to make non-overlapping.
    Greedy: keep intervals with earliest end times.
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            count += 1  # Remove current interval
        else:
            prev_end = intervals[i][1]

    return count


# ============================================================
# TEMPLATE 7: Cover Interval with Points
# ============================================================

def find_min_arrow_shots(points: List[List[int]]) -> int:
    """
    Find minimum arrows to burst all balloons (intervals).
    Arrow at point x bursts all balloons containing x.
    Time: O(n log n), Space: O(1)
    """
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrows = 1
    prev_end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > prev_end:
            arrows += 1
            prev_end = points[i][1]

    return arrows


# ============================================================
# TEMPLATE 8: Employee Free Time
# ============================================================

def employee_free_time(schedule: List[List[List[int]]]) -> List[List[int]]:
    """
    Find common free time across all employees.
    schedule[i] = list of intervals for employee i.
    Time: O(n log n), Space: O(n)
    """
    all_intervals = []
    for emp_schedule in schedule:
        all_intervals.extend(emp_schedule)

    all_intervals.sort(key=lambda x: x[0])
    merged = [all_intervals[0]]

    for interval in all_intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    free_time = []
    for i in range(1, len(merged)):
        if merged[i][0] > merged[i - 1][1]:
            free_time.append([merged[i - 1][1], merged[i][0]])

    return free_time


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Merged:", merge_intervals(intervals))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    print("Insert [4, 8]:", insert_interval(intervals, [4, 8]))

    meetings = [[0, 30], [5, 10], [15, 20]]
    print("Can attend all:", can_attend_meetings(meetings))
    print("Min rooms:", min_meeting_rooms(meetings))

    first = [[0, 2], [5, 10], [13, 23], [24, 25]]
    second = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print("Intersection:", interval_intersection(first, second))

    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print("Erase to non-overlap:", erase_overlap_intervals(intervals))
