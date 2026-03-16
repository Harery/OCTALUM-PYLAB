"""
Merge Sort Algorithm Module

Merge sort is a divide-and-conquer algorithm that divides the array into
halves, recursively sorts them, and then merges the sorted halves.

WHY IT'S CALLED "MERGE" SORT:
    It MERGES two sorted subarrays into one sorted array.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity:
    - O(n) for temporary arrays during merge
    - O(log n) for recursion stack

STABLE SORT: Yes - equal elements maintain relative order

WHEN TO USE:
    - Guaranteed O(n log n) needed (no worst case like quicksort)
    - Stable sorting required
    - Sorting linked lists (can be O(1) space)
    - External sorting (large files that don't fit in memory)

WHEN NOT TO USE:
    - Memory is very limited (uses O(n) extra space)
    - Small arrays (overhead not worth it)
"""

from typing import TypeVar, MutableSequence, Sequence

T = TypeVar('T')


def merge_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Basic merge sort using recursion (top-down approach).

    ALGORITHM:
    1. DIVIDE: Split array into two halves
    2. CONQUER: Recursively sort each half
    3. MERGE: Combine sorted halves into one sorted array

    VISUALIZATION:
    [38, 27, 43, 3, 9, 82, 10]
           ↓ divide
    [38, 27, 43, 3] | [9, 82, 10]
         ↓                ↓
    [38, 27] | [43, 3]  [9, 82] | [10]
       ↓         ↓        ↓
    [38][27]   [43][3]  [9][82]  [10]
       ↓         ↓        ↓
    [27, 38]  [3, 43]   [9, 82]  [10]
           ↓                ↓
    [3, 27, 38, 43] | [9, 10, 82]
           ↓ merge
    [3, 9, 10, 27, 38, 43, 82]

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Args:
        arr: Mutable sequence to sort

    Returns:
        Sorted sequence (may create new list)

    Example:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
    """
    if len(arr) <= 1:
        return arr

    # Divide: find midpoint
    mid = len(arr) // 2

    # Conquer: recursively sort halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combine: merge sorted halves
    return _merge(left, right)


def _merge(left: Sequence[T], right: Sequence[T]) -> list[T]:
    """
    Merge two sorted arrays into one sorted array.

    MERGE PROCESS:
    - Compare first elements of both arrays
    - Take smaller one, add to result
    - Repeat until one array is empty
    - Append remaining elements from other array

    Time Complexity: O(n + m) where n, m are lengths
    Space Complexity: O(n + m)
    """
    result = []
    i = j = 0

    # Compare and take smaller element
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (one of these will be non-empty)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_inplace(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Merge sort that modifies array in-place (uses helper array).

    OPTIMIZATION:
    Instead of creating new arrays for each merge, use a single
    temporary array passed through recursion.

    Time Complexity: O(n log n)
    Space Complexity: O(n) for temporary array

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    if len(arr) <= 1:
        return arr

    temp = [None] * len(arr)  # type: ignore
    _merge_sort_helper(arr, temp, 0, len(arr) - 1)
    return arr


def _merge_sort_helper(arr: MutableSequence[T], temp: list,
                       left: int, right: int) -> None:
    """Helper function for in-place merge sort."""
    if left >= right:
        return

    mid = (left + right) // 2
    _merge_sort_helper(arr, temp, left, mid)
    _merge_sort_helper(arr, temp, mid + 1, right)
    _merge_inplace(arr, temp, left, mid, right)


def _merge_inplace(arr: MutableSequence[T], temp: list,
                   left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays in-place using temporary array."""
    # Copy to temp
    for i in range(left, right + 1):
        temp[i] = arr[i]

    i = left      # Pointer for left subarray
    j = mid + 1   # Pointer for right subarray
    k = left      # Pointer for merged array

    while i <= mid and j <= right:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1

    # Copy remaining elements from left subarray
    while i <= mid:
        arr[k] = temp[i]
        i += 1
        k += 1

    # Right subarray elements are already in place


def merge_sort_iterative(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Iterative (bottom-up) merge sort.

    BOTTOM-UP APPROACH:
    - Start with subarrays of size 1 (already sorted)
    - Merge adjacent pairs into size 2
    - Merge adjacent pairs into size 4
    - Continue until whole array is merged

    WHY ITERATIVE:
    - Avoids recursion stack (O(log n) space saved)
    - Can be more cache-friendly
    - Sometimes faster in practice

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Args:
        arr: Mutable sequence to sort

    Returns:
        Sorted sequence
    """
    n = len(arr)
    if n <= 1:
        return arr

    temp = list(arr)  # Working array

    # Start with size 1, double each iteration
    width = 1
    while width < n:
        # Merge adjacent subarrays of size 'width'
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            # Merge arr[left:mid] and arr[mid:right]
            _merge_iterative(arr, temp, left, mid, right)

        width *= 2

    return arr


def _merge_iterative(arr: MutableSequence[T], temp: list,
                     left: int, mid: int, right: int) -> None:
    """Merge for iterative merge sort."""
    i, j, k = left, mid, left

    while i < mid and j < right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy back
    for i in range(left, right):
        arr[i] = temp[i]


def merge_sort_descending(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Merge sort in descending order.

    Reverse the comparison in merge operation.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_descending(arr[:mid])
    right = merge_sort_descending(arr[mid:])

    return _merge_descending(left, right)


def _merge_descending(left: Sequence[T], right: Sequence[T]) -> list[T]:
    """Merge in descending order."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:  # Changed to >= for descending
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_k_sorted(arrays: list[Sequence[T]]) -> list[T]:
    """
    Merge k sorted arrays into one sorted array.

    USE CASE:
    - External merge sort (merging sorted chunks)
    - Combining results from sorted sources

    APPROACH:
    Repeatedly merge pairs until one array remains.

    Time Complexity: O(n log k) where n = total elements, k = number of arrays
    Space Complexity: O(n)

    Args:
        arrays: List of sorted sequences

    Returns:
        Single merged sorted list
    """
    if not arrays:
        return []

    if len(arrays) == 1:
        return list(arrays[0])

    # Merge pairs repeatedly
    while len(arrays) > 1:
        merged = []
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                merged.append(_merge(arrays[i], arrays[i + 1]))
            else:
                merged.append(list(arrays[i]))
        arrays = merged

    return arrays[0]


def count_inversions(arr: Sequence[T]) -> int:
    """
    Count inversions in array using merge sort.

    INVERSION:
    Pair (i, j) where i < j but arr[i] > arr[j].
    Measures how "unsorted" an array is.

    MAXIMUM INVERSIONS: n(n-1)/2 (reverse sorted)
    MINIMUM INVERSIONS: 0 (already sorted)

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Args:
        arr: Sequence to analyze

    Returns:
        Number of inversions
    """
    return _count_inversions_helper(list(arr))[1]


def _count_inversions_helper(arr: list[T]) -> tuple[list[T], int]:
    """Helper that returns (sorted array, inversion count)."""
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = _count_inversions_helper(arr[:mid])
    right, right_inv = _count_inversions_helper(arr[mid:])
    merged, split_inv = _merge_count_inversions(left, right)

    return merged, left_inv + right_inv + split_inv


def _merge_count_inversions(left: list[T], right: list[T]) -> tuple[list[T], int]:
    """Merge while counting split inversions."""
    result = []
    i = j = 0
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # All remaining elements in left are inversions with right[j]
            inversions += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversions


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [38, 27, 43, 3, 9, 82, 10],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [12, 11, 13, 5, 6, 7],
    ]

    print("=" * 60)
    print("MERGE SORT DEMONSTRATION")
    print("=" * 60)

    # Test basic merge sort
    print("\n1. Basic Merge Sort (Top-Down)")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {merge_sort(arr)}")

    # Test in-place version
    print("\n2. In-Place Merge Sort")
    arr = test_arrays[3].copy()
    print(f"   Original: {test_arrays[3]}")
    print(f"   Sorted:   {merge_sort_inplace(arr)}")

    # Test iterative version
    print("\n3. Iterative Merge Sort (Bottom-Up)")
    arr = test_arrays[2].copy()
    print(f"   Original: {test_arrays[2]}")
    print(f"   Sorted:   {merge_sort_iterative(arr)}")

    # Test descending
    print("\n4. Descending Order")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Descending: {merge_sort_descending(arr)}")

    # Test k-way merge
    print("\n5. Merge K Sorted Arrays")
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(f"   Input: {arrays}")
    print(f"   Merged: {merge_k_sorted(arrays)}")

    # Count inversions
    print("\n6. Count Inversions")
    arr = [2, 4, 1, 3, 5]
    inversions = count_inversions(arr)
    print(f"   Array: {arr}")
    print(f"   Inversions: {inversions}")
    print(f"   Pairs: (2,1), (4,1), (4,3)")

    print("\n" + "=" * 60)
    print("All tests completed!")
