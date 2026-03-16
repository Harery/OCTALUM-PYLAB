"""
Interpolation Search Algorithm Module

Interpolation search is an improved variant of binary search for uniformly
distributed sorted data. Instead of always probing the middle, it estimates
the position of the target based on the values at the boundaries.

KEY DIFFERENCE FROM BINARY SEARCH:
    Binary search: Always checks middle: mid = (left + right) // 2
    Interpolation search: Estimates position using value distribution

THE FORMULA:
    pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

    This estimates where target likely is based on its relative value.

Time Complexity:
    - Best/Average Case: O(log log n) - for uniformly distributed data
    - Worst Case: O(n) - when data is not uniformly distributed

Space Complexity: O(1)

WHEN TO USE:
    - Data is SORTED and UNIFORMLY DISTRIBUTED
    - Large datasets where binary search log(n) is still too slow
    - Examples: phone books, dictionaries with uniform word distribution

WHEN NOT TO USE:
    - Non-uniform distribution (e.g., exponential growth)
    - Small datasets (overhead not worth it)
    - Data where arr[right] - arr[left] could be 0
"""

from typing import TypeVar, Sequence

T = TypeVar('T', int, float)  # Numeric types for interpolation formula


def interpolation_search(arr: Sequence[T], target: T) -> int:
    """
    Interpolation search for uniformly distributed sorted data.

    ALGORITHM:
    1. Calculate probe position using interpolation formula
    2. If probe value equals target, return probe index
    3. If probe value < target, search right portion
    4. If probe value > target, search left portion
    5. Repeat until found or search space exhausted

    THE MATH BEHIND IT:
    Think of it as estimating where target falls on a number line:
    - If target is 25% of the way from arr[left] to arr[right],
      then it should be around 25% of the index range from left to right.

    Time Complexity:
        - Best/Average: O(log log n) for uniform distribution
        - Worst: O(n) for non-uniform distribution
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending) with uniformly distributed values
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Example:
        >>> interpolation_search([1, 3, 5, 7, 9, 11, 13, 15], 7)
        3
    """
    left = 0
    right = len(arr) - 1

    while left <= right and target >= arr[left] and target <= arr[right]:
        # Guard against division by zero when left and right have same value
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            break

        # INTERPOLATION FORMULA
        # Estimate position based on value distribution
        # pos is weighted by where target falls between arr[left] and arr[right]
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

        # Safety check: ensure pos is within bounds
        if pos < left or pos > right:
            break

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            # Target is in right portion, move left boundary
            left = pos + 1
        else:
            # Target is in left portion, move right boundary
            right = pos - 1

    return -1


def interpolation_search_recursive(arr: Sequence[T], target: T,
                                   left: int = 0, right: int | None = None) -> int:
    """
    Recursive implementation of interpolation search.

    Same logic as iterative, but expressed recursively.

    Time Complexity: O(log log n) average, O(n) worst
    Space Complexity: O(log log n) average due to recursion stack

    Args:
        arr: Sorted sequence with uniform distribution
        target: Value to find
        left: Left boundary (default 0)
        right: Right boundary (default len(arr) - 1)

    Returns:
        Index of target, or -1 if not found
    """
    if right is None:
        right = len(arr) - 1

    # Base cases: search space exhausted or target outside range
    if left > right or target < arr[left] or target > arr[right]:
        return -1

    # Handle case where all elements are the same
    if arr[left] == arr[right]:
        return left if arr[left] == target else -1

    # Calculate probe position using interpolation
    pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

    # Bounds check
    if pos < left or pos > right:
        return -1

    if arr[pos] == target:
        return pos
    elif arr[pos] < target:
        return interpolation_search_recursive(arr, target, pos + 1, right)
    else:
        return interpolation_search_recursive(arr, target, left, pos - 1)


def interpolation_search_first(arr: Sequence[T], target: T) -> int:
    """
    Find first occurrence using interpolation search.

    After finding target, continues searching left to find
    the first occurrence (handles duplicates).

    Time Complexity: O(log log n) average for uniform distribution
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence with uniform distribution
        target: Value to find

    Returns:
        Index of first occurrence, or -1 if not found
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right and target >= arr[left] and target <= arr[right]:
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            break

        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

        if pos < left or pos > right:
            break

        if arr[pos] == target:
            result = pos
            # Continue searching left for first occurrence
            right = pos - 1
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return result


def interpolation_search_last(arr: Sequence[T], target: T) -> int:
    """
    Find last occurrence using interpolation search.

    After finding target, continues searching right to find
    the last occurrence (handles duplicates).

    Time Complexity: O(log log n) average for uniform distribution
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence with uniform distribution
        target: Value to find

    Returns:
        Index of last occurrence, or -1 if not found
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right and target >= arr[left] and target <= arr[right]:
        if arr[left] == arr[right]:
            if arr[left] == target:
                return right
            break

        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

        if pos < left or pos > right:
            break

        if arr[pos] == target:
            result = pos
            # Continue searching right for last occurrence
            left = pos + 1
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return result


def interpolation_search_insert_position(arr: Sequence[T], target: T) -> int:
    """
    Find insertion position using interpolation search.

    Returns the index where target should be inserted to maintain
    sorted order. Uses interpolation for faster convergence.

    Time Complexity: O(log log n) average
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence with uniform distribution
        target: Value to find/insert

    Returns:
        Index where target is or should be inserted

    Example:
        >>> interpolation_search_insert_position([1, 3, 5, 7, 9], 4)
        2
    """
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1

    # Handle edge cases where target is outside array range
    if target <= arr[left]:
        return 0
    if target >= arr[right]:
        return len(arr) if target > arr[right] else right

    while left <= right:
        if arr[left] == arr[right]:
            if arr[left] >= target:
                return left
            return left + 1

        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        pos = max(left, min(right, pos))  # Clamp to bounds

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return left


def compare_search_performance():
    """
    Compare interpolation search vs binary search for different distributions.

    This demonstrates WHY distribution matters:
    - Uniform distribution: Interpolation search excels
    - Non-uniform: Binary search may be better

    Returns dict with comparison insights.
    """
    return {
        "uniform_distribution": {
            "example": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
            "interpolation": "O(log log n) - very fast",
            "binary": "O(log n) - good",
            "winner": "Interpolation search"
        },
        "non_uniform_distribution": {
            "example": "[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]",
            "interpolation": "O(n) worst case - degrades",
            "binary": "O(log n) - stable",
            "winner": "Binary search"
        },
        "recommendation": (
            "Use interpolation search when data is known to be uniformly "
            "distributed. Otherwise, binary search is safer."
        )
    }


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Uniformly distributed data (ideal for interpolation search)
    uniform_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

    # Non-uniformly distributed data (binary search better)
    non_uniform = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    # Array with duplicates
    duplicates = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]

    print("=" * 60)
    print("INTERPOLATION SEARCH DEMONSTRATION")
    print("=" * 60)

    # Test basic interpolation search
    print("\n1. Basic Interpolation Search (Uniform Data)")
    print(f"   Array: {uniform_arr}")
    print(f"   Search for 15: index {interpolation_search(uniform_arr, 15)}")
    print(f"   Search for 1: index {interpolation_search(uniform_arr, 1)}")
    print(f"   Search for 29: index {interpolation_search(uniform_arr, 29)}")
    print(f"   Search for 14 (not in array): {interpolation_search(uniform_arr, 14)}")

    # Test with non-uniform data
    print("\n2. Interpolation Search (Non-Uniform Data)")
    print(f"   Array: {non_uniform}")
    print(f"   Search for 64: index {interpolation_search(non_uniform, 64)}")
    print(f"   (Note: May take more iterations on non-uniform data)")

    # Test recursive version
    print("\n3. Recursive Interpolation Search")
    print(f"   Search for 11: index {interpolation_search_recursive(uniform_arr, 11)}")

    # Test first/last occurrence
    print("\n4. First and Last Occurrence (Duplicates)")
    print(f"   Array: {duplicates}")
    print(f"   First '2': index {interpolation_search_first(duplicates, 2)}")
    print(f"   Last '2': index {interpolation_search_last(duplicates, 2)}")
    print(f"   First '5': index {interpolation_search_first(duplicates, 5)}")
    print(f"   Last '5': index {interpolation_search_last(duplicates, 5)}")

    # Test insert position
    print("\n5. Insert Position")
    print(f"   Array: {uniform_arr}")
    print(f"   Insert 10: position {interpolation_search_insert_position(uniform_arr, 10)}")
    print(f"   Insert 0: position {interpolation_search_insert_position(uniform_arr, 0)}")
    print(f"   Insert 30: position {interpolation_search_insert_position(uniform_arr, 30)}")

    # Performance comparison
    print("\n6. Performance Comparison")
    comparison = compare_search_performance()
    print(f"   Uniform data winner: {comparison['uniform_distribution']['winner']}")
    print(f"   Non-uniform winner: {comparison['non_uniform_distribution']['winner']}")
    print(f"   Recommendation: {comparison['recommendation']}")

    print("\n" + "=" * 60)
    print("All tests completed!")
