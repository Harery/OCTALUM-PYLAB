"""
Heap Sort Algorithm Module

Heap sort uses a binary heap data structure to sort elements. It first
builds a max-heap from the input, then repeatedly extracts the maximum
and places it at the end of the array.

WHY HEAP SORT WORKS:
    1. Build max-heap: largest element at root (index 0)
    2. Swap root with last element
    3. Reduce heap size and heapify
    4. Repeat until heap size is 1

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity: O(1) - in-place sorting

STABLE SORT: No - heap operations change relative order

WHEN TO USE:
    - Guaranteed O(n log n) needed
    - Memory is limited (in-place, no extra arrays)
    - Finding k largest/smallest elements efficiently

WHEN NOT TO USE:
    - Stability required
    - Small datasets (overhead not worth it)
    - When quick sort's average case is acceptable
"""

from typing import TypeVar, MutableSequence

T = TypeVar('T')


def heap_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Basic heap sort implementation using max-heap.

    ALGORITHM:
    1. BUILD MAX-HEAP: Convert array into max-heap
       - Start from last non-leaf node
       - Heapify each subtree bottom-up
    2. EXTRACT MAXIMUM repeatedly:
       - Swap root (max) with last unsorted element
       - Reduce heap size
       - Heapify new root

    VISUALIZATION:
    Array: [4, 10, 3, 5, 1]

    Build max-heap:
         10           10           10
        /  \   →     /  \   →     /  \
       4    3       5    3       5    3
      / \          / \          / \
     1   5       1   4        1   4

    Extract and heapify:
    [10, 5, 3, 1, 4] → [5, 4, 3, 1, | 10] → [4, 1, 3, | 5, 10]
    → ... → [1, | 3, 4, 5, 10] → [| 1, 3, 4, 5, 10]

    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> heap_sort([4, 10, 3, 5, 1])
        [1, 3, 4, 5, 10]
    """
    n = len(arr)

    if n <= 1:
        return arr

    # Step 1: Build max-heap
    # Start from last non-leaf node and heapify all subtrees
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (maximum) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify reduced heap
        _heapify(arr, i, 0)

    return arr


def _heapify(arr: MutableSequence[T], heap_size: int, root: int) -> None:
    """
    Maintain max-heap property starting from root.

    HEAP PROPERTY:
    For max-heap: parent >= children
    For node at index i:
        - Left child at 2*i + 1
        - Right child at 2*i + 2
        - Parent at (i-1)//2

    HEAPIFY PROCESS:
    1. Compare root with left and right children
    2. If child > root, swap with largest child
    3. Recursively heapify affected subtree

    Time Complexity: O(log n)
    Space Complexity: O(log n) for recursion
    """
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    # Check if left child exists and is greater than root
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _heapify(arr, heap_size, largest)


def heap_sort_iterative(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Heap sort with iterative heapify (no recursion).

    ITERATIVE HEAPIFY:
    Uses a loop instead of recursion to avoid stack overflow
    and improve performance for large arrays.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    if n <= 1:
        return arr

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_iterative(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify_iterative(arr, i, 0)

    return arr


def _heapify_iterative(arr: MutableSequence[T], heap_size: int, root: int) -> None:
    """Iterative version of heapify."""
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest


def heap_sort_descending(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Heap sort in descending order using min-heap.

    MIN-HEAP:
    Parent <= children, so root is minimum.
    Extracting minimum gives descending order.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    if n <= 1:
        return arr

    # Build min-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_min(arr, n, i)

    # Extract minimum to end
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify_min(arr, i, 0)

    return arr


def _heapify_min(arr: MutableSequence[T], heap_size: int, root: int) -> None:
    """Maintain min-heap property."""
    smallest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != root:
        arr[root], arr[smallest] = arr[smallest], arr[root]
        _heapify_min(arr, heap_size, smallest)


def heap_find_k_largest(arr: Sequence[T], k: int) -> list[T]:
    """
    Find k largest elements using max-heap.

    EFFICIENT K-SELECTION:
    Build max-heap once, then extract k times.
    O(n + k log n) vs O(n log n) for full sort.

    Time Complexity: O(n + k log n)
    Space Complexity: O(n) for heap copy

    Args:
        arr: Input sequence
        k: Number of largest elements to find

    Returns:
        List of k largest elements (largest first)
    """
    if k <= 0:
        return []

    n = len(arr)
    k = min(k, n)

    # Copy to avoid modifying original
    heap = list(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(heap, n, i)

    result = []
    for i in range(n - 1, n - k - 1, -1):
        result.append(heap[0])
        heap[0], heap[i] = heap[i], heap[0]
        _heapify(heap, i, 0)

    return result


def heap_find_k_smallest(arr: Sequence[T], k: int) -> list[T]:
    """
    Find k smallest elements using min-heap.

    Time Complexity: O(n + k log n)
    Space Complexity: O(n) for heap copy

    Args:
        arr: Input sequence
        k: Number of smallest elements to find

    Returns:
        List of k smallest elements (smallest first)
    """
    if k <= 0:
        return []

    n = len(arr)
    k = min(k, n)

    heap = list(arr)

    # Build min-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_min(heap, n, i)

    result = []
    for i in range(n - 1, n - k - 1, -1):
        result.append(heap[0])
        heap[0], heap[i] = heap[i], heap[0]
        _heapify_min(heap, i, 0)

    return result


# Heap operations for priority queue usage

def heap_push(heap: list[T], item: T) -> None:
    """
    Insert item into max-heap.

    PROCESS:
    1. Add item at end
    2. Bubble up until heap property restored

    Time Complexity: O(log n)
    """
    heap.append(item)
    _sift_up_max(heap, len(heap) - 1)


def _sift_up_max(heap: list[T], index: int) -> None:
    """Bubble up element at index to restore max-heap property."""
    while index > 0:
        parent = (index - 1) // 2
        if heap[index] <= heap[parent]:
            break
        heap[index], heap[parent] = heap[parent], heap[index]
        index = parent


def heap_pop(heap: list[T]) -> T:
    """
    Extract maximum from max-heap.

    PROCESS:
    1. Save root (maximum)
    2. Move last element to root
    3. Heapify from root

    Time Complexity: O(log n)

    Raises:
        IndexError if heap is empty
    """
    if not heap:
        raise IndexError("pop from empty heap")

    maximum = heap[0]
    last = heap.pop()

    if heap:
        heap[0] = last
        _heapify(heap, len(heap), 0)

    return maximum


def heap_peek(heap: list[T]) -> T:
    """
    Get maximum without removing it.

    Time Complexity: O(1)
    """
    if not heap:
        raise IndexError("peek from empty heap")
    return heap[0]


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [4, 10, 3, 5, 1],
        [12, 11, 13, 5, 6, 7],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("=" * 60)
    print("HEAP SORT DEMONSTRATION")
    print("=" * 60)

    # Test basic heap sort
    print("\n1. Basic Heap Sort")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {heap_sort(arr)}")

    # Test iterative version
    print("\n2. Iterative Heap Sort")
    arr = test_arrays[1].copy()
    print(f"   Original: {test_arrays[1]}")
    print(f"   Sorted:   {heap_sort_iterative(arr)}")

    # Test descending
    print("\n3. Heap Sort (Descending)")
    arr = test_arrays[1].copy()
    print(f"   Original: {test_arrays[1]}")
    print(f"   Descending: {heap_sort_descending(arr)}")

    # Test k largest
    print("\n4. Find K Largest Elements")
    arr = [3, 1, 6, 5, 2, 4]
    print(f"   Array: {arr}")
    print(f"   3 largest: {heap_find_k_largest(arr, 3)}")
    print(f"   3 smallest: {heap_find_k_smallest(arr, 3)}")

    # Test heap operations
    print("\n5. Heap Operations (Priority Queue)")
    heap = []
    for val in [3, 1, 6, 5, 2, 4]:
        heap_push(heap, val)
    print(f"   Built heap: {heap}")
    print(f"   Peek max: {heap_peek(heap)}")
    print(f"   Pop max: {heap_pop(heap)}")
    print(f"   After pop: {heap}")

    print("\n" + "=" * 60)
    print("All tests completed!")
