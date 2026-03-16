"""
Quick Sort Algorithm Module

Quick sort is a divide-and-conquer algorithm that selects a 'pivot' element
and partitions the array around it, then recursively sorts the partitions.

WHY IT'S CALLED "QUICK" SORT:
    It's typically faster in practice than other O(n log n) algorithms
    due to better cache performance and lower constant factors.

Time Complexity:
    - Best Case: O(n log n) - balanced partitions
    - Average Case: O(n log n)
    - Worst Case: O(n²) - already sorted with poor pivot choice

Space Complexity:
    - O(log n) for recursion stack (best/average)
    - O(n) for recursion stack (worst case)

STABLE SORT: No - partition process changes relative order of equal elements

WHEN TO USE:
    - General-purpose sorting (most common choice)
    - Average case performance matters more than worst case
    - In-place sorting required

WHEN NOT TO USE:
    - Worst case O(n²) unacceptable (use merge sort)
    - Stability required (use merge sort)
    - Nearly sorted data with poor pivot selection
"""

from typing import TypeVar, MutableSequence
import random

T = TypeVar('T')


def quick_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Basic quick sort using Lomuto partition scheme.

    ALGORITHM:
    1. Choose pivot (last element in Lomuto scheme)
    2. Partition: elements < pivot go left, >= pivot go right
    3. Recursively sort left and right partitions

    LOMUTO PARTITION SCHEME:
    - Simple to understand and implement
    - Uses last element as pivot
    - Single pass through array
    - More swaps than Hoare's scheme

    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n) average for recursion

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
    """
    _quick_sort_lomuto(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_lomuto(arr: MutableSequence[T], low: int, high: int) -> None:
    """Recursive helper for Lomuto quick sort."""
    if low < high:
        # Partition and get pivot's final position
        pivot_idx = _partition_lomuto(arr, low, high)

        # Recursively sort elements before and after pivot
        _quick_sort_lomuto(arr, low, pivot_idx - 1)
        _quick_sort_lomuto(arr, pivot_idx + 1, high)


def _partition_lomuto(arr: MutableSequence[T], low: int, high: int) -> int:
    """
    Lomuto partition scheme.

    PROCESS:
    1. Choose last element as pivot
    2. Maintain pointer i for boundary of smaller elements
    3. Scan through array, swap smaller elements to front
    4. Finally place pivot in correct position

    VISUALIZATION (pivot = 5):
    [3, 7, 2, 8, 5]  →  [3, 2, 5, 8, 7]
            pivot        elements < 5 | pivot | elements >= 5
    """
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element boundary

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_hoare(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Quick sort using Hoare partition scheme.

    HOARE VS LOMUTO:
    - Hoare's scheme is more efficient (fewer swaps)
    - Uses first element as pivot
    - Two pointers moving toward each other
    - More complex but better performance

    TIME ADVANTAGE:
    - 3x fewer swaps on average
    - Better for arrays with many equal elements

    Time Complexity: O(n log n) average
    Space Complexity: O(log n) for recursion

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    _quick_sort_hoare(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_hoare(arr: MutableSequence[T], low: int, high: int) -> None:
    """Recursive helper for Hoare quick sort."""
    if low < high:
        pivot_idx = _partition_hoare(arr, low, high)
        _quick_sort_hoare(arr, low, pivot_idx)      # Note: includes pivot
        _quick_sort_hoare(arr, pivot_idx + 1, high)


def _partition_hoare(arr: MutableSequence[T], low: int, high: int) -> int:
    """
    Hoare partition scheme.

    PROCESS:
    1. Choose first element as pivot
    2. Move i from left, j from right
    3. Stop when arr[i] >= pivot and arr[j] <= pivot
    4. Swap if i < j
    5. Return j as partition point

    KEY DIFFERENCE FROM LOMUTO:
    - Returns position where left partition ends
    - Pivot may not be at returned position
    - More efficient due to fewer swaps
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # Find element >= pivot from left
        i += 1
        while arr[i] < pivot:
            i += 1

        # Find element <= pivot from right
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers crossed, partition complete
        if i >= j:
            return j

        # Swap elements on wrong sides
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_randomized(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Quick sort with randomized pivot selection.

    WHY RANDOMIZE:
    - Worst case O(n²) occurs when array is sorted/nearly sorted
    - Random pivot selection makes worst case very unlikely
    - Expected runtime is O(n log n) regardless of input order

    Time Complexity: O(n log n) expected, O(n²) with tiny probability
    Space Complexity: O(log n) expected

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    _quick_sort_randomized(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_randomized(arr: MutableSequence[T], low: int, high: int) -> None:
    """Randomized quick sort helper."""
    if low < high:
        pivot_idx = _partition_randomized(arr, low, high)
        _quick_sort_randomized(arr, low, pivot_idx - 1)
        _quick_sort_randomized(arr, pivot_idx + 1, high)


def _partition_randomized(arr: MutableSequence[T], low: int, high: int) -> int:
    """Partition with random pivot selection."""
    # Choose random pivot and swap with last element
    random_idx = random.randint(low, high)
    arr[random_idx], arr[high] = arr[high], arr[random_idx]

    # Use Lomuto scheme with randomly chosen pivot
    return _partition_lomuto(arr, low, high)


def quick_sort_median_of_three(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Quick sort with median-of-three pivot selection.

    MEDIAN OF THREE:
    - Choose pivot as median of first, middle, last elements
    - Better than random for many real-world inputs
    - Helps avoid worst case on nearly sorted data

    Time Complexity: O(n log n) average
    Space Complexity: O(log n)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    _quick_sort_median3(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_median3(arr: MutableSequence[T], low: int, high: int) -> None:
    """Median-of-three quick sort helper."""
    if low < high:
        # For small subarrays, use insertion sort (optimization)
        if high - low < 10:
            _insertion_sort_range(arr, low, high)
            return

        pivot_idx = _partition_median3(arr, low, high)
        _quick_sort_median3(arr, low, pivot_idx - 1)
        _quick_sort_median3(arr, pivot_idx + 1, high)


def _partition_median3(arr: MutableSequence[T], low: int, high: int) -> int:
    """Partition using median-of-three pivot."""
    mid = (low + high) // 2

    # Sort low, mid, high and use middle as pivot
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]

    # Place pivot at high-1 position for Lomuto
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]

    return _partition_lomuto(arr, low, high)


def _insertion_sort_range(arr: MutableSequence[T], low: int, high: int) -> None:
    """Insertion sort for small subarrays."""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort_3way(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Three-way (Dutch National Flag) quick sort.

    THREE-WAY PARTITION:
    - Elements < pivot
    - Elements == pivot
    - Elements > pivot

    WHY USE IT:
    - Highly efficient for arrays with many duplicate elements
    - Avoids redundant comparisons of equal elements
    - Used in Java's Arrays.sort() for primitives

    Time Complexity: O(n log n) average, O(n) for all equal elements
    Space Complexity: O(log n)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    _quick_sort_3way(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_3way(arr: MutableSequence[T], low: int, high: int) -> None:
    """Three-way quick sort helper."""
    if low >= high:
        return

    # Three-way partition
    pivot = arr[low]
    lt = low       # arr[low..lt-1] < pivot
    gt = high      # arr[gt+1..high] > pivot
    i = low + 1    # current element

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    # Recursively sort < and > partitions
    _quick_sort_3way(arr, low, lt - 1)
    _quick_sort_3way(arr, gt + 1, high)


def quick_sort_iterative(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Iterative quick sort using explicit stack.

    WHY ITERATIVE:
    - Avoids recursion stack overflow for large arrays
    - Can be more efficient in some cases
    - Useful when recursion is not available

    Time Complexity: O(n log n) average
    Space Complexity: O(log n) for explicit stack

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    if len(arr) <= 1:
        return arr

    # Use list as stack
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_idx = _partition_lomuto(arr, low, high)

            # Push larger partition first (minimizes stack size)
            if pivot_idx - low > high - pivot_idx:
                stack.append((low, pivot_idx - 1))
                stack.append((pivot_idx + 1, high))
            else:
                stack.append((pivot_idx + 1, high))
                stack.append((low, pivot_idx - 1))

    return arr


def quick_select(arr: MutableSequence[T], k: int) -> T:
    """
    Find k-th smallest element using quick sort partitioning.

    QUICK SELECT:
    - Similar to quick sort but only recurse into one partition
    - Average O(n) time vs O(n log n) for full sort
    - Used to find median, percentiles efficiently

    Time Complexity: O(n) average, O(n²) worst
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence (will be partially modified)
        k: 0-indexed position (0 = smallest, n-1 = largest)

    Returns:
        k-th smallest element

    Example:
        >>> quick_select([3, 2, 1, 5, 4], 2)
        3  # 3rd smallest (0-indexed)
    """
    return _quick_select(arr, 0, len(arr) - 1, k)


def _quick_select(arr: MutableSequence[T], low: int, high: int, k: int) -> T:
    """Quick select helper."""
    if low == high:
        return arr[low]

    pivot_idx = _partition_lomuto(arr, low, high)

    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return _quick_select(arr, low, pivot_idx - 1, k)
    else:
        return _quick_select(arr, pivot_idx + 1, high, k)


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [3, 6, 8, 10, 1, 2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 4, 4, 4, 4],  # All duplicates
        [38, 27, 43, 3, 9, 82, 10],
    ]

    print("=" * 60)
    print("QUICK SORT DEMONSTRATION")
    print("=" * 60)

    # Test Lomuto scheme
    print("\n1. Quick Sort (Lomuto Partition)")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {quick_sort(arr)}")

    # Test Hoare scheme
    print("\n2. Quick Sort (Hoare Partition)")
    arr = test_arrays[1].copy()
    print(f"   Original: {test_arrays[1]}")
    print(f"   Sorted:   {quick_sort_hoare(arr)}")

    # Test randomized
    print("\n3. Quick Sort (Randomized Pivot)")
    arr = test_arrays[4].copy()
    print(f"   Original: {test_arrays[4]}")
    print(f"   Sorted:   {quick_sort_randomized(arr)}")

    # Test three-way (duplicates)
    print("\n4. Quick Sort (Three-Way) - For Duplicates")
    arr = test_arrays[3].copy()
    print(f"   Original: {test_arrays[3]}")
    print(f"   Sorted:   {quick_sort_3way(arr)}")

    # Test median-of-three
    print("\n5. Quick Sort (Median-of-Three Pivot)")
    arr = test_arrays[2].copy()
    print(f"   Original: {test_arrays[2]}")
    print(f"   Sorted:   {quick_sort_median_of_three(arr)}")

    # Test iterative
    print("\n6. Quick Sort (Iterative)")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {quick_sort_iterative(arr)}")

    # Test quick select
    print("\n7. Quick Select (Find k-th smallest)")
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"   Array: {arr}")
    print(f"   0th smallest (min): {quick_select(arr.copy(), 0)}")
    print(f"   3rd smallest: {quick_select(arr.copy(), 3)}")
    print(f"   6th smallest (max): {quick_select(arr.copy(), 6)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
