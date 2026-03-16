"""
Priority Queue Module
=====================
Priority queue implementations using Python's heapq module.

Supports both min-heap and max-heap variants.

Time Complexity:
- push: O(log n)
- pop: O(log n)
- peek: O(1)
- is_empty: O(1)
- size: O(1)

Space Complexity: O(n)
"""

from __future__ import annotations
import heapq


class MinPriorityQueue:
    """
    Min-priority queue using heapq internally.

    Smallest element has highest priority (extracted first).
    heapq in Python implements a min-heap by default.

    Example:
        >>> pq = MinPriorityQueue()
        >>> pq.push(5)
        >>> pq.push(3)
        >>> pq.push(7)
        >>> pq.peek()  # 3 (smallest)
        >>> pq.pop()   # 3
        >>> pq.pop()   # 5
    """

    def __init__(self) -> None:
        self._heap: list[int] = []

    def __repr__(self) -> str:
        return f"MinPriorityQueue({self._heap})"

    def __str__(self) -> str:
        return f"MinPriorityQueue: {self._heap}"

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def push(self, value: int) -> None:
        """
        Insert value into the priority queue.

        Time Complexity: O(log n)
        """
        heapq.heappush(self._heap, value)

    def pop(self) -> int:
        """
        Remove and return the minimum element.

        Raises:
            IndexError: If queue is empty.

        Time Complexity: O(log n)
        """
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self._heap)

    def peek(self) -> int:
        """
        Return minimum element without removing.

        Raises:
            IndexError: If queue is empty.

        Time Complexity: O(1)
        """
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        return self._heap[0]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def push_pop(self, value: int) -> int:
        """
        Push value and pop minimum in one operation.

        More efficient than push then pop separately.
        Time Complexity: O(log n)
        """
        return heapq.heappushpop(self._heap, value)

    def replace(self, value: int) -> int:
        """
        Pop minimum and push value in one operation.

        More efficient than pop then push separately.
        Time Complexity: O(log n)
        """
        if not self._heap:
            raise IndexError("replace on empty priority queue")
        return heapq.heapreplace(self._heap, value)

    def heapify(self, data: list[int]) -> None:
        """
        Build heap from list in O(n) time.

        Replaces current contents.
        Time Complexity: O(n)
        """
        self._heap = data.copy()
        heapq.heapify(self._heap)

    def to_sorted_list(self) -> list[int]:
        """
        Return all elements in sorted order.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        return sorted(self._heap)

    def nsmallest(self, n: int) -> list[int]:
        """
        Return n smallest elements.

        Time Complexity: O(n log k) for k = min(n, len)
        """
        return heapq.nsmallest(n, self._heap)

    def nlargest(self, n: int) -> list[int]:
        """
        Return n largest elements.

        Time Complexity: O(n log k) for k = min(n, len)
        """
        return heapq.nlargest(n, self._heap)


class MaxPriorityQueue:
    """
    Max-priority queue using heapq internally.

    Largest element has highest priority (extracted first).
    Implemented by negating values since heapq is min-heap.

    Example:
        >>> pq = MaxPriorityQueue()
        >>> pq.push(5)
        >>> pq.push(3)
        >>> pq.push(7)
        >>> pq.peek()  # 7 (largest)
        >>> pq.pop()   # 7
        >>> pq.pop()   # 5
    """

    def __init__(self) -> None:
        self._heap: list[int] = []

    def __repr__(self) -> str:
        values = [-x for x in self._heap]
        return f"MaxPriorityQueue({values})"

    def __str__(self) -> str:
        values = [-x for x in self._heap]
        return f"MaxPriorityQueue: {values}"

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def push(self, value: int) -> None:
        """
        Insert value into the priority queue.

        Time Complexity: O(log n)
        """
        heapq.heappush(self._heap, -value)

    def pop(self) -> int:
        """
        Remove and return the maximum element.

        Raises:
            IndexError: If queue is empty.

        Time Complexity: O(log n)
        """
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        return -heapq.heappop(self._heap)

    def peek(self) -> int:
        """
        Return maximum element without removing.

        Raises:
            IndexError: If queue is empty.

        Time Complexity: O(1)
        """
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        return -self._heap[0]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def push_pop(self, value: int) -> int:
        """
        Push value and pop maximum in one operation.

        Time Complexity: O(log n)
        """
        return -heapq.heappushpop(self._heap, -value)

    def replace(self, value: int) -> int:
        """
        Pop maximum and push value in one operation.

        Time Complexity: O(log n)
        """
        if not self._heap:
            raise IndexError("replace on empty priority queue")
        return -heapq.heapreplace(self._heap, -value)

    def heapify(self, data: list[int]) -> None:
        """
        Build heap from list in O(n) time.

        Time Complexity: O(n)
        """
        self._heap = [-x for x in data]
        heapq.heapify(self._heap)

    def to_sorted_list(self, reverse: bool = True) -> list[int]:
        """
        Return all elements in sorted order.

        Time Complexity: O(n log n)
        """
        values = [-x for x in self._heap]
        return sorted(values, reverse=reverse)


class PriorityQueue:
    """
    Generic priority queue with custom items and priorities.

    Uses heapq internally. Lower priority number = higher priority.

    Example:
        >>> pq = PriorityQueue()
        >>> pq.push("task1", 3)
        >>> pq.push("task2", 1)  # Higher priority
        >>> pq.push("task3", 2)
        >>> pq.pop()  # "task2"
    """

    def __init__(self) -> None:
        self._heap: list[tuple[int, int, str]] = []
        self._counter = 0

    def __repr__(self) -> str:
        items = [(p, item) for p, _, item in self._heap]
        return f"PriorityQueue({items})"

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def push(self, item: str, priority: int) -> None:
        """
        Insert item with given priority.

        Lower priority number = extracted first.
        Ties broken by insertion order (FIFO).
        Time Complexity: O(log n)
        """
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> str:
        """
        Remove and return highest priority item.

        Raises:
            IndexError: If queue is empty.

        Time Complexity: O(log n)
        """
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> str:
        """
        Return highest priority item without removing.

        Time Complexity: O(1)
        """
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        return self._heap[0][2]

    def peek_priority(self) -> int:
        """Return priority of highest priority item. O(1)"""
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        return self._heap[0][0]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)


class IndexedPriorityQueue:
    """
    Indexed priority queue supporting key updates.

    Allows decreasing/increasing priority of existing items.
    Useful for Dijkstra's algorithm.

    Time Complexity:
    - push/update: O(log n)
    - pop: O(log n)
    - contains: O(1)
    """

    def __init__(self) -> None:
        self._heap: list[tuple[int, str]] = []
        self._index: dict[str, int] = {}

    def __len__(self) -> int:
        return len(self._heap)

    def __contains__(self, key: str) -> bool:
        return key in self._index

    def push_or_update(self, key: str, priority: int) -> None:
        """
        Insert new key or update existing key's priority.

        Time Complexity: O(log n)
        """
        if key in self._index:
            self._decrease_key(key, priority)
        else:
            heapq.heappush(self._heap, (priority, key))
            self._rebuild_index()

    def _decrease_key(self, key: str, new_priority: int) -> None:
        """Decrease priority of existing key."""
        for i, (p, k) in enumerate(self._heap):
            if k == key:
                if new_priority < p:
                    self._heap[i] = (new_priority, k)
                    heapq.heapify(self._heap)
                    self._rebuild_index()
                return

    def _rebuild_index(self) -> None:
        """Rebuild the key-to-position index."""
        self._index = {k: i for i, (_, k) in enumerate(self._heap)}

    def pop(self) -> tuple[str, int]:
        """
        Remove and return (key, priority) of minimum.

        Time Complexity: O(log n)
        """
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        priority, key = heapq.heappop(self._heap)
        self._rebuild_index()
        return key, priority

    def peek(self) -> tuple[str, int]:
        """Return (key, priority) of minimum without removing. O(1)"""
        if not self._heap:
            raise IndexError("peek from empty priority queue")
        return self._heap[0][1], self._heap[0][0]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def contains(self, key: str) -> bool:
        return key in self._index


def heap_sort(nums: list[int]) -> list[int]:
    """
    Sort using heap sort via heapq.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    h = nums.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def find_k_largest(nums: list[int], k: int) -> list[int]:
    """
    Find k largest elements using min-heap.

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k <= 0 or not nums:
        return []
    return heapq.nlargest(k, nums)


def find_k_smallest(nums: list[int], k: int) -> list[int]:
    """
    Find k smallest elements using max-heap technique.

    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k <= 0 or not nums:
        return []
    return heapq.nsmallest(k, nums)


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    """
    Merge k sorted lists using heapq.

    Time Complexity: O(n log k) where n = total elements
    Space Complexity: O(k)
    """
    result: list[int] = []
    heap: list[tuple[int, int, int]] = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


if __name__ == "__main__":
    print("=" * 50)
    print("MinPriorityQueue (using heapq)")
    print("=" * 50)

    mpq = MinPriorityQueue()
    mpq.push(5)
    mpq.push(3)
    mpq.push(7)
    mpq.push(1)
    print(f"Heap: {mpq}")
    print(f"Peek: {mpq.peek()}")
    print(f"Pop: {mpq.pop()}")
    print(f"After pop: {mpq}")
    print(f"3 smallest: {mpq.nsmallest(3)}")

    print("\n" + "=" * 50)
    print("MaxPriorityQueue (using heapq with negation)")
    print("=" * 50)

    xpq = MaxPriorityQueue()
    xpq.push(5)
    xpq.push(3)
    xpq.push(7)
    xpq.push(1)
    print(f"Heap: {xpq}")
    print(f"Peek: {xpq.peek()}")
    print(f"Pop: {xpq.pop()}")
    print(f"After pop: {xpq}")
    print(f"Sorted (desc): {xpq.to_sorted_list()}")

    print("\n" + "=" * 50)
    print("PriorityQueue (generic with priorities)")
    print("=" * 50)

    pq = PriorityQueue()
    pq.push("Low priority", 3)
    pq.push("High priority", 1)
    pq.push("Medium priority", 2)
    print(f"Pop: {pq.pop()} (priority 1)")
    print(f"Pop: {pq.pop()} (priority 2)")
    print(f"Pop: {pq.pop()} (priority 3)")

    print("\n" + "=" * 50)
    print("IndexedPriorityQueue")
    print("=" * 50)

    ipq = IndexedPriorityQueue()
    ipq.push_or_update("A", 5)
    ipq.push_or_update("B", 3)
    ipq.push_or_update("A", 1)  # Update A's priority
    print(f"Contains A: {'A' in ipq}")
    print(f"Peek: {ipq.peek()}")
    print(f"Pop: {ipq.pop()}")

    print("\n" + "=" * 50)
    print("Utility Functions")
    print("=" * 50)

    print(f"heap_sort([3,1,4,1,5,9,2,6]): {heap_sort([3,1,4,1,5,9,2,6])}")
    print(f"find_k_largest([3,1,4,1,5,9,2,6], 3): {find_k_largest([3,1,4,1,5,9,2,6], 3)}")
    print(f"merge_sorted_lists: {merge_sorted_lists([[1,4,7], [2,5,8], [3,6,9]])}")
