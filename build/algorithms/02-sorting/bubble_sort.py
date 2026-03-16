"""
Bubble Sort Algorithm Module

Bubble sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they're in the wrong order. The pass through the list is
repeated until no swaps are needed.

WHY IT'S CALLED "BUBBLE" SORT:
    Smaller elements "bubble" to the top (beginning) of the list,
    while larger elements sink to the bottom (end).

Time Complexity:
    - Best Case: O(n) - already sorted (with optimization)
    - Average Case: O(n²)
    - Worst Case: O(n²) - reverse sorted

Space Complexity: O(1) - in-place sorting

STABLE SORT: Yes - equal elements maintain relative order

WHEN TO USE:
    - Educational purposes (understanding sorting fundamentals)
    - Nearly sorted data (with early termination)
    - Very small datasets

WHEN NOT TO USE:
    - Production code with large datasets
    - When performance matters
"""

from typing import TypeVar, MutableSequence, Callable

T = TypeVar('T')


def bubble_sort(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Basic bubble sort implementation.

    ALGORITHM:
    1. For each pass through the array:
    2. Compare each pair of adjacent elements
    3. Swap if they're in wrong order
    4. After n-1 passes, array is sorted

    VISUALIZATION:
    Pass 1: [5,3,8,4,2] → [3,5,4,2,8]  (8 bubbles to end)
    Pass 2: [3,5,4,2,8] → [3,4,2,5,8]  (5 bubbles to position)
    Pass 3: [3,4,2,5,8] → [3,2,4,5,8]  (4 bubbles to position)
    Pass 4: [3,2,4,5,8] → [2,3,4,5,8]  (sorted!)

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> bubble_sort([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]
    """
    n = len(arr)

    # Outer loop: n-1 passes needed
    for i in range(n - 1):
        # Inner loop: compare adjacent pairs
        # After i passes, last i elements are already sorted
        for j in range(n - 1 - i):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_optimized(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Bubble sort with early termination optimization.

    OPTIMIZATION:
    If no swaps occur during a pass, the array is already sorted.
    We can terminate early, achieving O(n) for already sorted data.

    Time Complexity: O(n) best, O(n²) average/worst
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> bubble_sort_optimized([1, 2, 3, 4, 5])  # Already sorted
        [1, 2, 3, 4, 5]  # Only one pass needed!
    """
    n = len(arr)

    for i in range(n - 1):
        swapped = False  # Track if any swap occurred this pass

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Early termination: if no swaps, array is sorted
        if not swapped:
            break

    return arr


def bubble_sort_flag_position(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Bubble sort with last-swap position optimization.

    ADVANCED OPTIMIZATION:
    Track where the last swap occurred. Elements after this position
    are already sorted, so we don't need to check them again.

    WHY THIS HELPS:
    If the last swap was at position k, everything after k is sorted.
    Next pass only needs to go up to k.

    Time Complexity: O(n) best, O(n²) average/worst
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    n = len(arr)
    last_swap = n - 1  # Position of last swap

    while last_swap > 0:
        current_last_swap = 0

        for j in range(last_swap):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                current_last_swap = j  # Remember where swap happened

        # Next pass only needs to go up to last swap position
        last_swap = current_last_swap

    return arr


def bubble_sort_bidirectional(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Bidirectional (cocktail shaker) bubble sort.

    COCKTAIL SHAKER SORT:
    Instead of only bubbling up, we alternate:
    - Forward pass: bubble largest to end
    - Backward pass: bubble smallest to beginning

    WHY THIS HELPS:
    Regular bubble sort is slow when small elements are at the end
    (turtles problem). Cocktail sort handles this better.

    EXAMPLE:
    [2, 3, 4, 5, 1] - Regular bubble sort needs 4 passes
    Cocktail sort moves 1 to front in just 2 passes!

    Time Complexity: O(n) best, O(n²) average/worst
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in-place)
    """
    n = len(arr)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass: bubble largest to right
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        right -= 1  # Rightmost element is now sorted
        swapped = False

        # Backward pass: bubble smallest to left
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True

        left += 1  # Leftmost element is now sorted

    return arr


def bubble_sort_with_key(arr: MutableSequence[T],
                         key: Callable[[T], int | float] = lambda x: x) -> MutableSequence[T]:
    """
    Bubble sort with custom key function for comparison.

    KEY FUNCTION:
    Extract a comparison value from each element.
    Useful for sorting objects by a specific attribute.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place
        key: Function to extract comparison value

    Returns:
        Same sequence (sorted in-place)

    Example:
        >>> data = [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
        >>> bubble_sort_with_key(data, key=lambda x: x['age'])
        # Sorts by age
    """
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def bubble_sort_descending(arr: MutableSequence[T]) -> MutableSequence[T]:
    """
    Bubble sort in descending order.

    Simply reverse the comparison: arr[j] < arr[j+1] instead of >

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Same sequence (sorted in descending order)
    """
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:  # Reversed comparison
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def count_bubble_sort_swaps(arr: MutableSequence[T]) -> tuple[MutableSequence[T], int]:
    """
    Bubble sort that counts total swaps.

    USEFUL FOR:
    - Analyzing how "unsorted" an array is
    - Understanding bubble sort behavior

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Args:
        arr: Mutable sequence to sort in-place

    Returns:
        Tuple of (sorted array, total swap count)
    """
    n = len(arr)
    total_swaps = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                total_swaps += 1

    return arr, total_swaps


def bubble_sort_recursive(arr: MutableSequence[T], n: int | None = None) -> MutableSequence[T]:
    """
    Recursive implementation of bubble sort.

    RECURSIVE LOGIC:
    1. Base case: n == 1, single element is sorted
    2. One pass moves largest to end
    3. Recursively sort first n-1 elements

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
    if n == 1:
        return arr

    # One pass: bubble largest element to position n-1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursively sort remaining n-1 elements
    return bubble_sort_recursive(arr, n - 1)


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [2, 3, 4, 5, 1],  # Small element at end (cocktail sort advantage)
    ]

    print("=" * 60)
    print("BUBBLE SORT DEMONSTRATION")
    print("=" * 60)

    # Test basic bubble sort
    print("\n1. Basic Bubble Sort")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {bubble_sort(arr)}")

    # Test optimized version
    print("\n2. Optimized Bubble Sort (Early Termination)")
    arr = test_arrays[1].copy()
    print(f"   Already sorted: {test_arrays[1]}")
    print(f"   Result: {bubble_sort_optimized(arr)}")
    print("   (Only one pass needed due to early termination)")

    # Test bidirectional
    print("\n3. Bidirectional (Cocktail Shaker) Sort")
    arr = test_arrays[3].copy()
    print(f"   Input: {test_arrays[3]}")
    print(f"   Sorted: {bubble_sort_bidirectional(arr)}")
    print("   (Handles 'turtles' - small elements at end)")

    # Test descending order
    print("\n4. Descending Order")
    arr = test_arrays[0].copy()
    print(f"   Original: {test_arrays[0]}")
    print(f"   Descending: {bubble_sort_descending(arr)}")

    # Count swaps
    print("\n5. Count Swaps")
    arr = test_arrays[2].copy()
    sorted_arr, swaps = count_bubble_sort_swaps(arr)
    print(f"   Reverse sorted: {test_arrays[2]}")
    print(f"   Total swaps needed: {swaps}")

    # Test with key function
    print("\n6. Sort with Key Function")
    people = [
        {"name": "Bob", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Charlie", "age": 20}
    ]
    print(f"   Original: {people}")
    bubble_sort_with_key(people, key=lambda x: x["age"])
    print(f"   Sorted by age: {[p['name'] for p in people]}")

    print("\n" + "=" * 60)
    print("All tests completed!")
