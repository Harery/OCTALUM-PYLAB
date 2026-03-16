#!/usr/bin/env python3
"""
LeetCode Hard #295: Find Median from Data Stream

The median is the middle value in an ordered integer list.
If the size is even, the median is the mean of the two middle values.

Design a data structure that supports:
- addNum(num): Add integer to data structure
- findMedian(): Return median of all elements

Example:
    addNum(1), addNum(2), findMedian() -> 1.5
    addNum(3), findMedian() -> 2

Time Complexity: O(log n) for addNum, O(1) for findMedian
Space Complexity: O(n)
"""

from __future__ import annotations

import heapq


class MedianFinder:
    """
    Find median using two heaps.

    - max_heap: stores the smaller half (as negatives for max behavior)
    - min_heap: stores the larger half

    Keep them balanced so median can be found in O(1).
    """

    def __init__(self) -> None:
        self.max_heap: list[int] = []  # Smaller half (negated for max heap)
        self.min_heap: list[int] = []  # Larger half

    def add_num(self, num: int) -> None:
        """Add number to the data structure."""
        # Add to max_heap first
        heapq.heappush(self.max_heap, -num)

        # Move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Balance: max_heap should have >= elements than min_heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        """Return the median of all added numbers."""
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])

        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


def test() -> None:
    """Test cases for median finder."""
    mf = MedianFinder()

    # Add 1, 2 -> median should be 1.5
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5

    # Add 3 -> median should be 2
    mf.add_num(3)
    assert mf.find_median() == 2.0

    # Test with more numbers
    mf2 = MedianFinder()
    for i in [5, 15, 1, 3]:
        mf2.add_num(i)
    # Sorted: [1, 3, 5, 15] -> median = (3 + 5) / 2 = 4
    assert mf2.find_median() == 4.0

    print("All tests passed!")


if __name__ == "__main__":
    test()
