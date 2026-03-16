"""
Binary Search Algorithm Module

Binary search is a divide-and-conquer algorithm that finds the position of a target
value within a SORTED array. It compares the target to the middle element and
eliminates half of the search space in each iteration.

PREREQUISITE: The array MUST be sorted (ascending order assumed).

Time Complexity:
    - Best Case: O(1) - target is at the middle
    - Average Case: O(log n)
    - Worst Case: O(log n)

Space Complexity:
    - Iterative: O(1)
    - Recursive: O(log n) due to call stack

WHY BINARY SEARCH IS FAST:
    Each comparison eliminates HALF of the remaining elements.
    For 1 million elements: ~20 comparisons vs 500,000 average for linear search.
"""

from typing import TypeVar, Sequence, Callable

T = TypeVar('T')


def binary_search_iterative(arr: Sequence[T], target: T) -> int:
    """
    Binary search using iterative approach.

    ALGORITHM:
    1. Set left and right pointers to array bounds
    2. While left <= right:
       a. Calculate middle index
       b. If middle element equals target, return index
       c. If target < middle, search left half (right = mid - 1)
       d. If target > middle, search right half (left = mid + 1)
    3. If loop ends, target not found

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order)
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Example:
        >>> binary_search_iterative([1, 3, 5, 7, 9, 11], 7)
        3
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Calculate middle index (avoiding overflow for very large arrays)
        # Using (left + right) // 2 can overflow in some languages
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # Target is in left half, exclude mid and everything right
            right = mid - 1
        else:
            # Target is in right half, exclude mid and everything left
            left = mid + 1

    return -1


def binary_search_recursive(arr: Sequence[T], target: T,
                            left: int = 0, right: int | None = None) -> int:
    """
    Binary search using recursive approach.

    RECURSIVE LOGIC:
    - Base case: left > right means target not found
    - Recursive case: search appropriate half based on comparison

    Time Complexity: O(log n)
    Space Complexity: O(log n) - recursion depth is log(n)

    Args:
        arr: Sorted sequence (ascending order)
        target: Value to find
        left: Left boundary (default 0)
        right: Right boundary (default len(arr) - 1)

    Returns:
        Index of target, or -1 if not found

    Example:
        >>> binary_search_recursive([1, 3, 5, 7, 9], 5)
        2
    """
    if right is None:
        right = len(arr) - 1

    # Base case: search space exhausted
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        # Search left half
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        # Search right half
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search_first(arr: Sequence[T], target: T) -> int:
    """
    Find the FIRST occurrence of target (handles duplicates).

    WHY THIS VARIATION EXISTS:
    Standard binary search may return any occurrence of duplicates.
    This variation ensures we find the leftmost one.

    KEY INSIGHT:
    When we find target, we don't immediately return. Instead, we
    continue searching in the left half to see if there's an earlier
    occurrence, but we remember this position.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order, may have duplicates)
        target: Value to find

    Returns:
        Index of first occurrence, or -1 if not found

    Example:
        >>> binary_search_first([1, 2, 2, 2, 3, 4], 2)
        1
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Found target, but continue searching left for earlier occurrence
            result = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result


def binary_search_last(arr: Sequence[T], target: T) -> int:
    """
    Find the LAST occurrence of target (handles duplicates).

    SIMILAR TO FIRST OCCURRENCE:
    When we find target, we continue searching right to find
    a later occurrence.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order, may have duplicates)
        target: Value to find

    Returns:
        Index of last occurrence, or -1 if not found

    Example:
        >>> binary_search_last([1, 2, 2, 2, 3, 4], 2)
        3
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Found target, but continue searching right for later occurrence
            result = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result


def binary_search_insert_position(arr: Sequence[T], target: T) -> int:
    """
    Find the position where target should be inserted to maintain sorted order.

    USEFUL FOR:
    - Inserting into a sorted array
    - Finding rank of an element
    - Ceiling/floor problems

    DIFFERENCE FROM STANDARD SEARCH:
    - Returns left pointer when not found (insert position)
    - Always returns a valid index in range [0, len(arr)]

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order)
        target: Value to find/insert

    Returns:
        Index where target is or should be inserted

    Example:
        >>> binary_search_insert_position([1, 3, 5, 7], 4)
        2  # 4 should be inserted at index 2
        >>> binary_search_insert_position([1, 3, 5, 7], 5)
        2  # 5 is already at index 2
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # Left is the insertion position
    return left


def binary_search_range(arr: Sequence[T], target: T) -> tuple[int, int]:
    """
    Find the range of indices containing target.

    COMBINES FIRST AND LAST:
    Returns [first_occurrence, last_occurrence] for duplicates.

    Time Complexity: O(log n) - two binary searches
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order)
        target: Value to find

    Returns:
        Tuple of (first_index, last_index), or (-1, -1) if not found

    Example:
        >>> binary_search_range([1, 2, 2, 2, 3, 4], 2)
        (1, 3)
        >>> binary_search_range([1, 2, 3, 4], 5)
        (-1, -1)
    """
    first = binary_search_first(arr, target)
    if first == -1:
        return -1, -1
    last = binary_search_last(arr, target)
    return first, last


def binary_search_closest(arr: Sequence[T], target: T) -> int:
    """
    Find the index of element closest to target.

    WHEN TARGET NOT FOUND:
    Returns the index of the element with minimum absolute difference
    from target.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order)
        target: Value to find or approximate

    Returns:
        Index of closest element

    Example:
        >>> binary_search_closest([1, 4, 6, 8], 5)
        2  # 6 is closest to 5
    """
    if not arr:
        raise ValueError("Cannot search empty array")

    left = 0
    right = len(arr) - 1

    # If target is outside array bounds, return closest endpoint
    if target <= arr[left]:
        return left
    if target >= arr[right]:
        return right

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # At this point, left > right
    # The closest is either at 'left' or 'right'
    # Compare which is closer to target
    if abs(arr[left] - target) < abs(arr[right] - target):
        return left
    return right


def binary_search_generic(arr: Sequence[T], target: T,
                          compare: Callable[[T, T], int]) -> int:
    """
    Binary search with custom comparison function.

    CUSTOM COMPARISON:
    compare(a, b) returns:
    - negative if a < b
    - 0 if a == b
    - positive if a > b

    This allows binary search on custom sorted orders or complex objects.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence according to compare function
        target: Value to find
        compare: Comparison function

    Returns:
        Index of target, or -1 if not found
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        cmp_result = compare(arr[mid], target)

        if cmp_result == 0:
            return mid
        elif cmp_result > 0:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_rotated(arr: Sequence[T], target: T) -> int:
    """
    Binary search in a rotated sorted array.

    ROTATED ARRAY:
    Original: [1, 2, 3, 4, 5]
    Rotated:  [4, 5, 1, 2, 3] (rotated 3 positions)

    KEY INSIGHT:
    One half of the array is always sorted. We determine which half,
    check if target is in that sorted half, and eliminate accordingly.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Rotated sorted sequence (no duplicates for simplicity)
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Example:
        >>> binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 0)
        4
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                # Target is in sorted left half
                right = mid - 1
            else:
                # Target is in right half
                left = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                # Target is in sorted right half
                left = mid + 1
            else:
                # Target is in left half
                right = mid - 1

    return -1


def find_rotation_point(arr: Sequence[T]) -> int:
    """
    Find the index of the minimum element (rotation point) in rotated sorted array.

    ROTATION POINT:
    In [4, 5, 1, 2, 3], the rotation point is index 2 (value 1).

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Args:
        arr: Rotated sorted sequence

    Returns:
        Index of minimum element (rotation point)

    Example:
        >>> find_rotation_point([4, 5, 6, 1, 2, 3])
        3
    """
    left = 0
    right = len(arr) - 1

    # If not rotated (or single element)
    if arr[left] <= arr[right]:
        return left

    while left < right:
        mid = left + (right - left) // 2

        # If mid element > right element, rotation point is in right half
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return left


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    duplicates = [1, 2, 2, 2, 3, 4, 5]
    rotated = [4, 5, 6, 7, 0, 1, 2]

    print("=" * 60)
    print("BINARY SEARCH DEMONSTRATION")
    print("=" * 60)

    # Test iterative search
    print("\n1. Iterative Binary Search")
    print(f"   Array: {sorted_arr}")
    print(f"   Search 7: index {binary_search_iterative(sorted_arr, 7)}")
    print(f"   Search 11: index {binary_search_iterative(sorted_arr, 11)}")

    # Test recursive search
    print("\n2. Recursive Binary Search")
    print(f"   Search 5: index {binary_search_recursive(sorted_arr, 5)}")

    # Test first/last occurrence
    print("\n3. First and Last Occurrence (duplicates)")
    print(f"   Array: {duplicates}")
    print(f"   First '2': index {binary_search_first(duplicates, 2)}")
    print(f"   Last '2': index {binary_search_last(duplicates, 2)}")
    print(f"   Range of '2': {binary_search_range(duplicates, 2)}")

    # Test insert position
    print("\n4. Insert Position")
    print(f"   Array: {sorted_arr}")
    print(f"   Insert 5.5: position {binary_search_insert_position(sorted_arr[:], 5.5)}")
    print(f"   Insert 0: position {binary_search_insert_position(sorted_arr[:], 0)}")

    # Test closest element
    print("\n5. Closest Element")
    arr = [1, 4, 6, 8]
    print(f"   Array: {arr}")
    print(f"   Closest to 5: index {binary_search_closest(arr, 5)} (value {arr[binary_search_closest(arr, 5)]})")

    # Test rotated array search
    print("\n6. Rotated Array Search")
    print(f"   Array: {rotated}")
    print(f"   Search 0: index {binary_search_rotated(rotated, 0)}")
    print(f"   Search 5: index {binary_search_rotated(rotated, 5)}")
    print(f"   Rotation point: index {find_rotation_point(rotated)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
