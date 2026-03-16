"""
Insertion Sort Algorithm Module

Insertion sort builds the sorted array one element at a time by repeatedly
picking the next element and inserting it into its correct position among
the previously sorted elements.

WHY IT'S CALLED "INSERTION" SORT:
    It INSERTS each element into its correct position in the sorted portion.

Time Complexity:
    - Best Case: O(n) - already sorted (no shifts needed)
    - Average Case: O(n²)
    - Worst Case: O(n²) - reverse sorted (maximum shifts)

Space Complexity: O(1) - in-place sorting

STABLE SORT: Yes - equal elements maintain relative order

WHEN TO USE:
    - Small datasets
    - Nearly sorted data (very efficient, O(n))
    - Online sorting (sorting as data arrives)
    - Hybrid with other algorithms (e.g., Timsort uses insertion sort)

WHEN NOT TO USE:
    - Large unsorted datasets
"""

from typing import TypeVar, MutableSequence, Callable

T = TypeVar('T')


def insertion_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Basic insertion sort implementation.

    ALGORITHM:
    1. Start with second element (first is trivially sorted)
    2. Compare current element with elements in sorted portion
    3. Shift larger elements right
    4. Insert current element in correct position
    5. Repeat for remaining elements

    VISUALIZATION:
    [5, 2, 4, 6, 1, 3]
     ↑ sorted

    [5, | 2, 4, 6, 1, 3]  → Insert 2
    [2, 5, | 4, 6, 1, 3]  → Insert 4
    [2, 4, 5, | 6, 1, 3]  → Insert 6 (already in place)
    [2, 4, 5, 6, | 1, 3]  → Insert 1
    [1, 2, 4, 5, 6, | 3]  → Insert 3
    [1, 2, 3, 4, 5, 6]    → Sorted!

    KEY INSIGHT:
    Elements before current index are always sorted.
    We just need to find where to insert current element.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        [1, 2, 3, 4, 5, 6]
    """
    # Start from second element (index 1)
    for i in range(1, len(arr)):
        # Element to be inserted
        key = arr[i]

        # Find position to insert by shifting larger elements right
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift right
            j -= 1

        # Insert element at correct position
        arr[j + 1] = key

    return arr


def insertion_sort_binary(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Insertion sort with binary search for insertion position.

    OPTIMIZATION:
    Instead of linear search to find insertion position, use binary search.
    This reduces comparisons from O(n) to O(log n) per element.

    HOWEVER:
    Total complexity remains O(n²) because shifting elements is still O(n).
    Useful when comparisons are expensive but shifts are cheap.

    Time Complexity: O(n²) - still dominated by shifts
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    for i in range(1, len(arr)):
        key = arr[i]

        # Binary search for insertion position in arr[0:i]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1

        # left is the insertion position
        # Shift elements from left to i-1 right by one
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]

        # Insert at correct position
        arr[left] = key

    return arr


def insertion_sort_descending(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Insertion sort in descending order.

    Reverse the comparison: arr[j] < key instead of arr[j] > key

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in descending order)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements smaller than key right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def insertion_sort_with_key(arr: MutableSequence[T],
                            key: Callable[[T], int | float] = lambda x: x) -> MutableSequence[T]:
    """
    Insertion sort with custom key function.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place
        key: Function to extract comparison value

    Returns:
        Same sequence (sorted in-place)
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and key(arr[j]) > key(current):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


def insertion_sort_recursive(arr: MutableSequence[T], n: int | None = None) -> MutableSequence[T]:
    """
    Recursive implementation of insertion sort.

    RECURSIVE LOGIC:
    1. Base case: n <= 1 (single element is sorted)
    2. Recursively sort first n-1 elements
    3. Insert nth element into sorted portion

    Time Complexity: O(n²)
    Space Complexity: O(n) for recursion stack

    Args:
        arr: Mutable sequence to sort in-place
        n: Number of elements to sort (default: len(arr))

    Returns:
        Same sequence (sorted in-place)
    """
    if n is None:
        n = len(arr)

    # Base case: single element is sorted
    if n <= 1:
        return arr

    # Sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)

    # Insert last element into sorted portion
    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

    return arr


def insertion_sort_count_shifts(arr: MutableSequence[T]) -> tuple[MutableSequence[T], int]:
    """
    Insertion sort that counts element shifts.

    USEFUL FOR:
    - Analyzing how "unsorted" an array is
    - Understanding insertion sort behavior

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Tuple of (sorted array, shift count)
    """
    shift_count = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shift_count += 1
            j -= 1

        arr[j + 1] = key

    return arr, shift_count


def insertion_sort_for_linked_list(values: list[T]) -> list[T]:
    """
    Insertion sort optimized conceptually for linked lists.

    LINKED LIST ADVANTAGE:
    Insertions are O(1) (no shifting needed).
    This makes insertion sort much more efficient for linked lists.

    This implementation works on a list but demonstrates the concept.

    Time Complexity: O(n²) comparisons, O(1) insertions per element
    Space Complexity: O(n) for new list

    Args:
        values: List of values to sort

    Returns:
        New sorted list
    """
    if not values:
        return []

    # Build sorted list from scratch
    sorted_list = [values[0]]

    for i in range(1, len(values)):
        value = values[i]
        inserted = False

        # Find insertion point
        for j in range(len(sorted_list)):
            if value < sorted_list[j]:
                sorted_list.insert(j, value)
                inserted = True
                break

        # If not inserted, append at end
        if not inserted:
            sorted_list.append(value)

    return sorted_list


def shell_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Shell sort - optimized insertion sort with gap sequence.

    SHELL SORT CONCEPT:
    - Start with large gap (elements far apart)
    - Perform insertion sort on elements separated by gap
    - Gradually reduce gap until gap=1 (regular insertion sort)

    WHY IT'S FASTER:
    - Large gaps allow elements to move quickly to correct region
    - By the time gap=1, array is nearly sorted, making insertion sort O(n)

    GAP SEQUENCE:
    Using n//2, n//4, n//8, ... (Shell's original sequence)
    Better sequences exist (Knuth, Sedgewick) but this is simple.

    Time Complexity: O(n²) worst, O(n log n) to O(n^(3/2)) average
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    n = len(arr)
    gap = n // 2

    # Reduce gap until it becomes 1
    while gap > 0:
        # Perform insertion sort for this gap
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Shift elements that are gap apart
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [5, 2, 4, 6, 1, 3],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [2, 3, 4, 5, 1],  # Small element at end
    ]

    print("=" * 60)
    print("INSERTION SORT DEMONSTRATION")
    print("=" * 60)

    # Test basic insertion sort
    print("\n1. Basic Insertion Sort")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {insertion_sort(arr)}")

    # Test binary search variant
    print("\n2. Binary Insertion Sort")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {insertion_sort_binary(arr)}")

    # Test on already sorted (best case)
    print("\n3. Already Sorted (Best Case)")
    arr = test_arrays[1].copy()
    _, shifts = insertion_sort_count_shifts(arr)
    print(f"   Array: {test_arrays[1]}")
    print(f"   Shifts needed: {shifts} (O(n) best case)")

    # Test on reverse sorted (worst case)
    print("\n4. Reverse Sorted (Worst Case)")
    arr = test_arrays[2].copy()
    _, shifts = insertion_sort_count_shifts(arr)
    print(f"   Array: {test_arrays[2]}")
    print(f"   Shifts needed: {shifts} (O(n²) worst case)")

    # Test Shell sort
    print("\n5. Shell Sort (Gap-Optimized Insertion)")
    arr = test_arrays[2].copy()
    print(f"   Original: {test_arrays[2]}")
    print(f"   Sorted:   {shell_sort(arr)}")
    print("   (Uses gaps to move elements faster)")

    # Test descending
    print("\n6. Descending Order")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Descending: {insertion_sort_descending(arr)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
