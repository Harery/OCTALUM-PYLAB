"""
LeetCode 56: Merge Intervals

Given array of intervals, merge all overlapping intervals.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]

Pattern: Merge Intervals
Time: O(n log n) - sorting
Space: O(n) - output
"""

from __future__ import annotations


class Solution:
    def solve(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
    ]

    for intervals, expected in test_cases:
        result = solution.solve(intervals)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {intervals} | Output: {result}")
