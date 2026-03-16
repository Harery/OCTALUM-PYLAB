"""
Selection Sort Algorithm Module

Selection sort works by repeatedly finding the minimum element from the
unsorted portion and putting it at the beginning.

WHY IT'S CALLED "SELECTION" SORT:
    It SELECTS the smallest element from the unsorted portion
    and places it in its correct position.

Time Complexity:
    - Best Case: O(n²) - even if sorted, still finds minimum each pass
    - Average Case: O(n²)
    - Worst Case: O(n²)

Space Complexity: O(1) - in-place sorting

STABLE SORT: No - equal elements may change relative order

WHEN TO USE:
    - Memory is extremely limited (minimizes writes)
    - Small datasets
    - When swap cost is high (minimizes swaps to O(n))

WHEN NOT TO USE:
    - Large datasets (use merge/quick/heap sort instead)
    - When stability is required
"""

from typing import TypeVar, MutableSequence, Callable

T = TypeVar('T')


def selection_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Basic selection sort implementation.

    ALGORITHM:
    1. Divide array into sorted (left) and unsorted (right) portions
    2. Find minimum element in unsorted portion
    3. Swap it with first element of unsorted portion
    4. Expand sorted portion by one
    5. Repeat until entire array is sorted

    VISUALIZATION:
    [64, 25, 12, 22, 11]  → Find min(11), swap with 64
    [11, 25, 12, 22, 64]  → Find min(12), swap with 25
    [11, 12, 25, 22, 64]  → Find min(22), swap with 25
    [11, 12, 22, 25, 64]  → Find min(25), swap with 25 (no change)
    [11, 12, 22, 25, 64]  → Sorted!

    KEY INSIGHT:
    After i passes, first i elements are in final sorted position.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    """
    n = len(arr)

    # Iterate through array, growing sorted portion
    for i in range(n - 1):
        # Assume current position has minimum
        min_idx = i

        # Find actual minimum in unsorted portion [i+1, n-1]
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum with first unsorted element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def selection_sort_descending(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Selection sort in descending order.

    Find MAXIMUM instead of minimum in each pass.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in descending order)
    """
    n = len(arr)

    for i in range(n - 1):
        max_idx = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:  # Find maximum
                max_idx = j

        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


def selection_sort_with_key(arr: MutableSequence[T],
                            key: Callable[[T], int | float] = lambda x: x) -> MutableSequence[T]:
    """
    Selection sort with custom key function.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place
        key: Function to extract comparison value

    Returns:
        Same sequence (sorted in-place)
    """
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def selection_sort_count_swaps(arr: MutableSequence[T]) -> tuple[MutableSequence[T], int]:
    """
    Selection sort that counts swaps.

    KEY ADVANTAGE OF SELECTION SORT:
    Maximum of n-1 swaps (one per position).
    Useful when swap operations are expensive (e.g., writing to flash memory).

    Compare to bubble sort which can have O(n²) swaps.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Tuple of (sorted array, swap count)
    """
    n = len(arr)
    swap_count = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1

    return arr, swap_count


def selection_sort_recursive(arr: MutableSequence[T], start: int = 0) -> MutableSequence[T]:
    """
    Recursive implementation of selection sort.

    RECURSIVE LOGIC:
    1. Base case: start >= n-1 (only one element left)
    2. Find minimum in unsorted portion
    3. Swap to position start
    4. Recursively sort from start+1

    Time Complexity: O(n²)
    Space Complexity: O(n) for recursion stack

    Args:
        arr: Mutable sequence to sort in-place
        start: Starting index of unsorted portion

    Returns:
        Same sequence (sorted in-place)
    """
    n = len(arr)

    # Base case: single element or empty
    if start >= n - 1:
        return arr

    # Find minimum in unsorted portion
    min_idx = start
    for j in range(start + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    # Swap minimum to correct position
    if min_idx != start:
        arr[start], arr[min_idx] = arr[min_idx], arr[start]

    # Recursively sort remaining elements
    return selection_sort_recursive(arr, start + 1)


def selection_sort_stable(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Stable version of selection sort.

    WHY STANDARD SELECTION SORT IS UNSTABLE:
    When we swap the minimum to position i, we might move an equal
    element past other equal elements, changing their relative order.

    EXAMPLE OF INSTABILITY:
    [(5, 'a'), (5, 'b'), (2, 'c')]
    After swap: [(2, 'c'), (5, 'b'), (5, 'a')]
    (5, 'a') and (5, 'b') changed order!

    STABLE SOLUTION:
    Instead of swapping, shift elements right and insert minimum.
    This preserves relative order of equal elements.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place, stable)
    """
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            # Instead of swap, shift and insert (stable)
            min_value = arr[min_idx]
            # Shift all elements from i to min_idx-1 right by one
            for k in range(min_idx, i, -1):
                arr[k] = arr[k - 1]
            # Insert minimum at position i
            arr[i] = min_value

    return arr


def selection_sort_bidirectional(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Bidirectional selection sort (Cocktail Selection Sort).

    OPTIMIZATION:
    Find both min AND max in each pass.
    Place min at left, max at right.
    Reduces passes by half.

    Time Complexity: O(n²) but with smaller constant
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        # Find min and max in current unsorted portion
        min_idx = left
        max_idx = left

        for i in range(left + 1, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i

        # Swap min to left
        if min_idx != left:
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            # If max was at left, it's now at min_idx
            if max_idx == left:
                max_idx = min_idx

        # Swap max to right
        if max_idx != right:
            arr[right], arr[max_idx] = arr[max_idx], arr[right]

        left += 1
        right -= 1

    return arr


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [64, 25, 12, 22, 11],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 3, 3, 1, 1],
    ]

    print("=" * 60)
    print("SELECTION SORT DEMONSTRATION")
    print("=" * 60)

    # Test basic selection sort
    print("\n1. Basic Selection Sort")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {selection_sort(arr)}")

    # Test descending
    print("\n2. Descending Order")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Descending: {selection_sort_descending(arr)}")

    # Count swaps
    print("\n3. Count Swaps (Key Advantage: At Most n-1 Swaps)")
    arr = test_arrays[1].copy()
    _, swaps = selection_sort_count_swaps(arr)
    print(f"   Already sorted array needs {swaps} swaps")

    arr = test_arrays[2].copy()
    sorted_arr, swaps = selection_sort_count_swaps(arr)
    print(f"   Reverse sorted needs {swaps} swaps")
    print(f"   (Compare to bubble sort which would need ~n²/2 swaps)")

    # Test bidirectional
    print("\n4. Bidirectional Selection Sort")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {selection_sort_bidirectional(arr)}")
    print("   (Finds min and max in each pass)")

    # Test stable version
    print("\n5. Stable Selection Sort")
    # Using tuples to demonstrate stability
    data = [(5, 'a'), (2, 'b'), (5, 'c'), (1, 'd')]
    print(f"   Original: {data}")
    result = selection_sort_stable(data.copy())
    print(f"   Sorted:   {result}")
    print("   (Equal elements 5a and 5c maintain relative order)")

    print("\n" + "=" * 60)
    print("All tests completed!")
