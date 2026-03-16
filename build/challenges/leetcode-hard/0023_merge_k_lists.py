#!/usr/bin/env python3
"""
LeetCode Hard #23: Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order. Merge all the linked-lists into one sorted linked-list
and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

Time Complexity: O(N log k) where N = total nodes, k = number of lists
Space Complexity: O(k) for the heap
"""

from __future__ import annotations

import heapq


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next_node: ListNode | None = None):
        self.val = val
        self.next = next_node

    def __lt__(self, other: ListNode) -> bool:
        return self.val < other.val

    def to_list(self) -> list[int]:
        """Convert linked list to Python list."""
        result = []
        current: ListNode | None = self
        while current:
            result.append(current.val)
            current = current.next
        return result


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """
    Merge k sorted linked lists using a min-heap.

    Uses a min-heap to efficiently select the smallest element
    from all k lists at each step.

    Args:
        lists: Array of k sorted linked list heads

    Returns:
        Head of the merged sorted linked list
    """
    if not lists:
        return None

    # Min-heap to track the smallest element from each list
    min_heap: list[ListNode] = []

    # Add the first node of each non-empty list to the heap
    for node in lists:
        if node:
            heapq.heappush(min_heap, node)

    # Dummy head for easier list construction
    dummy = ListNode(0)
    current = dummy

    while min_heap:
        # Get the smallest node
        smallest = heapq.heappop(min_heap)

        # Add it to the result list
        current.next = smallest
        current = current.next

        # Add the next node from the same list to the heap
        if smallest.next:
            heapq.heappush(min_heap, smallest.next)

    return dummy.next


def list_to_linked(lst: list[int]) -> ListNode | None:
    """Convert Python list to linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test() -> None:
    """Test cases for merge k sorted lists."""
    # Test case 1: [[1,4,5],[1,3,4],[2,6]]
    lists1 = [
        list_to_linked([1, 4, 5]),
        list_to_linked([1, 3, 4]),
        list_to_linked([2, 6]),
    ]
    result1 = merge_k_lists(lists1)
    assert result1 is not None
    assert result1.to_list() == [1, 1, 2, 3, 4, 4, 5, 6]

    # Test case 2: Empty list
    result2 = merge_k_lists([])
    assert result2 is None

    # Test case 3: Single list
    lists3 = [list_to_linked([1, 2, 3])]
    result3 = merge_k_lists(lists3)
    assert result3 is not None
    assert result3.to_list() == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test()
