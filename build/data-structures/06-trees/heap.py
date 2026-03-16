"""
Heap Module
===========
Min-heap and Max-heap implementations.

Time Complexity:
- Insert: O(log n)
- Extract: O(log n)
- Peek: O(1)
- Build heap: O(n)

Space Complexity: O(n)
"""

from __future__ import annotations


class MinHeap:
    """
    Min-heap where the smallest element is at the root.

    Parent <= Children
    """

    def __init__(self) -> None:
        self.heap: list[int] = []

    def __repr__(self) -> str:
        return f"MinHeap({self.heap})"

    def __str__(self) -> str:
        return f"MinHeap: {self.heap}"

    def __len__(self) -> int:
        return len(self.heap)

    def __bool__(self) -> bool:
        return bool(self.heap)

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i: int) -> None:
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i: int) -> None:
        size = len(self.heap)
        smallest = i

        left = self._left(i)
        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left

        right = self._right(i)
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest)

    def insert(self, value: int) -> None:
        """
        Insert a value into the heap.

        Args:
            value: Value to insert

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> heap = MinHeap()
            >>> heap.insert(5)
            >>> heap.peek()  # 5
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # Alias for insert
    push = insert

    def extract_min(self) -> int:
        """
        Remove and return the minimum element.

        Returns:
            The minimum value in the heap

        Raises:
            IndexError: If heap is empty

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> heap = MinHeap()
            >>> heap.insert(3)
            >>> heap.extract_min()  # 3
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return min_val

    # Alias for extract_min
    pop = extract_min

    def peek(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

    def build_heap(self, arr: list[int]) -> None:
        self.heap = arr.copy()
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def heapify(self, arr: list[int]) -> None:
        self.build_heap(arr)


class MaxHeap:
    """
    Max-heap where the largest element is at the root.

    Parent >= Children
    """

    def __init__(self) -> None:
        self.heap: list[int] = []

    def __repr__(self) -> str:
        return f"MaxHeap({self.heap})"

    def __str__(self) -> str:
        return f"MaxHeap: {self.heap}"

    def __len__(self) -> int:
        return len(self.heap)

    def __bool__(self) -> bool:
        return bool(self.heap)

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i: int) -> None:
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i: int) -> None:
        size = len(self.heap)
        largest = i

        left = self._left(i)
        if left < size and self.heap[left] > self.heap[largest]:
            largest = left

        right = self._right(i)
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self._swap(i, largest)
            self._heapify_down(largest)

    def push(self, value: int) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")

        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return max_val

    def peek(self) -> int:
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

    def build_heap(self, arr: list[int]) -> None:
        self.heap = arr.copy()
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)


def heap_sort_ascending(arr: list[int]) -> list[int]:
    """
    Sort in ascending order using max-heap.

    Time Complexity: O(n log n)
    Space Complexity: O(1) in-place
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_max(arr, i, 0)

    return arr


def heap_sort_descending(arr: list[int]) -> list[int]:
    """
    Sort in descending order using min-heap.

    Time Complexity: O(n log n)
    Space Complexity: O(1) in-place
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_min(arr, i, 0)

    return arr


def heapify_max(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)


def heapify_min(arr: list[int], n: int, i: int) -> None:
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)


def heap_sort(arr: list[int], reverse: bool = False) -> list[int]:
    """
    Sort array using heap sort algorithm.

    Args:
        arr: List of integers to sort
        reverse: If True, sort in descending order

    Returns:
        Sorted list

    Time Complexity: O(n log n)
    Space Complexity: O(n) for the copy

    Example:
        >>> heap_sort([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
        >>> heap_sort([3, 1, 4], reverse=True)
        [4, 3, 1]
    """
    result = arr.copy()
    if reverse:
        return heap_sort_descending(result)
    return heap_sort_ascending(result)


if __name__ == "__main__":
    print("=== MinHeap ===")
    mh = MinHeap()
    for v in [5, 3, 7, 1, 9, 2]:
        mh.push(v)
    print(f"Heap: {mh}")
    print(f"Peek: {mh.peek()}")

    result = []
    while mh:
        result.append(mh.pop())
    print(f"Sorted (ascending): {result}")

    print("\n=== MaxHeap ===")
    mxh = MaxHeap()
    mxh.build_heap([5, 3, 7, 1, 9, 2])
    print(f"Built heap: {mxh}")

    result = []
    while mxh:
        result.append(mxh.pop())
    print(f"Sorted (descending): {result}")

    print("\n=== Heap Sort ===")
    arr = [5, 3, 7, 1, 9, 2]
    print(f"Original: {arr}")
    print(f"Ascending: {heap_sort_ascending(arr.copy())}")
    print(f"Descending: {heap_sort_descending(arr.copy())}")
