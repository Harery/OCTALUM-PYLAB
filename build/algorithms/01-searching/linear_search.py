"""
Linear Search Algorithm Module

Linear search is the simplest searching algorithm that checks each element
in a collection sequentially until the target is found or the entire collection
is traversed.

Time Complexity:
    - Best Case: O(1) - target is at the first position
    - Average Case: O(n) - target is somewhere in the middle
    - Worst Case: O(n) - target is at the end or not present

Space Complexity: O(1) - only uses a few variables

WHY USE LINEAR SEARCH?
    - Works on unsorted data
    - Works on any data structure that can be iterated
    - Simple to implement and understand
    - Good for small datasets
    - Useful when you need to find ALL occurrences
"""

from typing import TypeVar, Sequence

T = TypeVar('T')


def linear_search(arr: Sequence[T], target: T) -> int:
    """
    Perform linear search to find the first occurrence of target.

    ALGORITHM:
    1. Start from the first element
    2. Compare each element with the target
    3. If found, return the index
    4. If end is reached without finding, return -1

    Args:
        arr: Sequence to search through
        target: Value to find

    Returns:
        Index of first occurrence, or -1 if not found

    Example:
        >>> linear_search([4, 2, 7, 1, 9], 7)
        2
    """
    # Step 1: Iterate through each element with its index
    for i, element in enumerate(arr):
        # Step 2: Check if current element matches target
        if element == target:
            # Step 3: Return index when found
            return i

    # Step 4: Target not found after checking all elements
    return -1


def linear_search_all(arr: Sequence[T], target: T) -> list[int]:
    """
    Find all occurrences of target in the sequence.

    This variation is useful when duplicates are present and you need
    to know all positions where the target appears.

    Time Complexity: O(n) - must check every element
    Space Complexity: O(k) - where k is the number of matches

    Args:
        arr: Sequence to search through
        target: Value to find

    Returns:
        List of all indices where target appears (empty if not found)

    Example:
        >>> linear_search_all([1, 3, 2, 3, 4, 3], 3)
        [1, 3, 5]
    """
    # Collect all indices where target is found
    indices = []

    for i, element in enumerate(arr):
        if element == target:
            indices.append(i)

    return indices


def linear_search_last(arr: Sequence[T], target: T) -> int:
    """
    Find the last occurrence of target in the sequence.

    This is more efficient than finding all occurrences when you only
    need the last one, as it can traverse from the end.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Sequence to search through
        target: Value to find

    Returns:
        Index of last occurrence, or -1 if not found

    Example:
        >>> linear_search_last([1, 3, 2, 3, 4], 3)
        3
    """
    # Traverse from end to find last occurrence
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i

    return -1


def linear_search_with_sentinel(arr: list[T], target: T) -> int:
    """
    Linear search with sentinel optimization.

    SENTINEL CONCEPT:
    By appending the target to the end, we guarantee finding it.
    This eliminates the need to check if we've reached the end
    of the array in each iteration, reducing comparisons.

    WHY IT'S SLIGHTLY FASTER:
    - Standard linear search: 2 comparisons per iteration
      (element check + boundary check)
    - Sentinel search: 1 comparison per iteration (element check only)

    Time Complexity: O(n) - but with smaller constant factor
    Space Complexity: O(1) - but modifies the list temporarily

    Args:
        arr: List to search (will be temporarily modified)
        target: Value to find

    Returns:
        Index of first occurrence, or -1 if not found

    Example:
        >>> linear_search_with_sentinel([4, 2, 7, 1], 7)
        2
    """
    n = len(arr)

    # Handle empty array
    if n == 0:
        return -1

    # Step 1: Store last element and place sentinel
    last = arr[-1]
    arr[-1] = target

    # Step 2: Search without boundary checking
    i = 0
    while arr[i] != target:
        i += 1

    # Step 3: Restore last element
    arr[-1] = last

    # Step 4: Check if we found the actual target or just reached sentinel
    if i < n - 1 or target == last:
        return i

    return -1


def linear_search_ordered(arr: Sequence[T], target: T) -> int:
    """
    Linear search optimized for ordered/sorted sequences.

    OPTIMIZATION FOR ORDERED DATA:
    If we encounter an element larger than the target (in ascending order),
    we can stop early because the target won't appear later.

    This is a hybrid approach - not as fast as binary search for
    sorted data, but better than standard linear search.

    Time Complexity:
        - Best Case: O(1)
        - Average Case: O(n/2) = O(n)
        - Worst Case: O(n)
    Space Complexity: O(1)

    Args:
        arr: Sorted sequence (ascending order)
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Example:
        >>> linear_search_ordered([1, 2, 4, 7, 9], 7)
        3
        >>> linear_search_ordered([1, 2, 4, 7, 9], 5)
        -1
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
        # Early termination: if current > target, target can't be later
        # (only works for ascending order)
        if element > target:
            break

    return -1


def linear_search_min(arr: Sequence[T]) -> tuple[int, T]:
    """
    Find the minimum element and its index using linear search.

    This is a fundamental operation that demonstrates why linear search
    is sometimes necessary - there's no faster way to find the minimum
    in an unsorted array without additional data structures.

    Time Complexity: O(n) - must check every element
    Space Complexity: O(1)

    Args:
        arr: Non-empty sequence to search

    Returns:
        Tuple of (index, minimum_value)

    Raises:
        ValueError: If sequence is empty

    Example:
        >>> linear_search_min([5, 2, 8, 1, 9])
        (3, 1)
    """
    if not arr:
        raise ValueError("Cannot find minimum of empty sequence")

    min_index = 0
    min_value = arr[0]

    for i, element in enumerate(arr[1:], start=1):
        if element < min_value:
            min_index = i
            min_value = element

    return min_index, min_value


def linear_search_max(arr: Sequence[T]) -> tuple[int, T]:
    """
    Find the maximum element and its index using linear search.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Non-empty sequence to search

    Returns:
        Tuple of (index, maximum_value)

    Raises:
        ValueError: If sequence is empty

    Example:
        >>> linear_search_max([5, 2, 8, 1, 9])
        (4, 9)
    """
    if not arr:
        raise ValueError("Cannot find maximum of empty sequence")

    max_index = 0
    max_value = arr[0]

    for i, element in enumerate(arr[1:], start=1):
        if element > max_value:
            max_index = i
            max_value = element

    return max_index, max_value


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Test data
    numbers = [4, 2, 7, 1, 9, 5, 7]
    sorted_numbers = [1, 2, 4, 5, 7, 7, 9]
    words = ["apple", "banana", "cherry", "date"]

    print("=" * 60)
    print("LINEAR SEARCH DEMONSTRATION")
    print("=" * 60)

    # Test basic linear search
    print("\n1. Basic Linear Search")
    print(f"   Array: {numbers}")
    print(f"   Search for 7: index {linear_search(numbers, 7)}")
    print(f"   Search for 3: index {linear_search(numbers, 3)}")

    # Test find all occurrences
    print("\n2. Find All Occurrences")
    print(f"   Array: {numbers}")
    print(f"   All positions of 7: {linear_search_all(numbers, 7)}")

    # Test find last occurrence
    print("\n3. Find Last Occurrence")
    print(f"   Array: {numbers}")
    print(f"   Last position of 7: {linear_search_last(numbers, 7)}")

    # Test sentinel search
    print("\n4. Sentinel Search")
    test_list = [4, 2, 7, 1, 9]
    print(f"   Array: {test_list}")
    print(f"   Search for 7: index {linear_search_with_sentinel(test_list, 7)}")

    # Test ordered search
    print("\n5. Ordered Search (Early Termination)")
    print(f"   Sorted array: {sorted_numbers}")
    print(f"   Search for 6 (not present): {linear_search_ordered(sorted_numbers, 6)}")
    print(f"   Search for 5: {linear_search_ordered(sorted_numbers, 5)}")

    # Test min/max
    print("\n6. Find Min and Max")
    print(f"   Array: {numbers}")
    min_idx, min_val = linear_search_min(numbers)
    max_idx, max_val = linear_search_max(numbers)
    print(f"   Min: value {min_val} at index {min_idx}")
    print(f"   Max: value {max_val} at index {max_idx}")

    # Test with strings
    print("\n7. Search with Strings")
    print(f"   Array: {words}")
    print(f"   Search for 'cherry': index {linear_search(words, 'cherry')}")

    print("\n" + "=" * 60)
    print("All tests completed!")
