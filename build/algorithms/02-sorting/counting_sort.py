"""
Counting Sort Algorithm Module

Counting sort is a non-comparison-based sorting algorithm that counts
the occurrences of each distinct element, then reconstructs the sorted array.

WHY IT'S FAST:
    It doesn't compare elements - it counts them!
    Trade-off: Works only on integers (or objects with integer keys)

Time Complexity: O(n + k)
    - n = number of elements
    - k = range of input (max - min)

Space Complexity: O(k) for count array

STABLE SORT: Yes (when implemented correctly)

WHEN TO USE:
    - Integer keys with limited range (k << n log n)
    - Sorting objects by integer attribute
    - Radix sort subroutine

WHEN NOT TO USE:
    - Large range of values (k >> n)
    - Non-integer data without integer keys
    - Memory is very limited
"""

from typing import TypeVar, MutableSequence, Sequence

T = TypeVar('T')


def counting_sort(arr: Sequence[int]) -> list[int]:
    """
    Basic counting sort for non-negative integers.

    ALGORITHM:
    1. Find range of input (min to max)
    2. Count occurrences of each value
    3. Convert counts to cumulative counts (positions)
    4. Place each element in its sorted position

    VISUALIZATION:
    Input: [4, 2, 2, 8, 3, 3, 1]

    Count array (indices represent values):
    Index: 0  1  2  3  4  5  6  7  8
    Count: 0  1  2  2  1  0  0  0  1

    Cumulative (position after last occurrence):
    Index: 0  1  2  3  4  5  6  7  8
    Cumu:  0  1  3  5  6  6  6  6  7

    Output: [1, 2, 2, 3, 3, 4, 8]

    Time Complexity: O(n + k) where k = max - min
    Space Complexity: O(k) for count array

    Args:
        arr: Sequence of non-negative integers

    Returns:
        New sorted list

    Example:
        >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]
    """
    if not arr:
        return []

    # Find range
    min_val = min(arr)
    max_val = max(arr)

    # Create count array
    range_size = max_val - min_val + 1
    count = [0] * range_size

    # Count occurrences
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct sorted array
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)

    return result


def counting_sort_stable(arr: Sequence[int]) -> list[int]:
    """
    Stable counting sort that preserves relative order of equal elements.

    WHY STABLE:
    Instead of just extending with counts, we:
    1. Convert counts to cumulative positions
    2. Process input in reverse, placing each element at its position
    3. Decrement position counter

    STABILITY MATTERS WHEN:
    - Sorting objects by one key among many
    - Multiple sorting passes on different keys

    Time Complexity: O(n + k)
    Space Complexity: O(n + k)
    """
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    range_size = max_val - min_val + 1
    count = [0] * range_size

    # Count occurrences
    for num in arr:
        count[num - min_val] += 1

    # Convert to cumulative count (position of last occurrence + 1)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output array from right to left (for stability)
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


def counting_sort_with_negative(arr: Sequence[int]) -> list[int]:
    """
    Counting sort that handles negative integers.

    HANDLING NEGATIVES:
    Shift all values by -min_val to make them non-negative,
    then shift back when reconstructing.

    Time Complexity: O(n + k)
    Space Complexity: O(k)
    """
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    # Shift to handle negatives
    shift = -min_val
    range_size = max_val - min_val + 1
    count = [0] * range_size

    for num in arr:
        count[num + shift] += 1

    result = []
    for i, c in enumerate(count):
        if c > 0:
            result.extend([i - shift] * c)

    return result


def counting_sort_objects(arr: Sequence[T], key_func) -> list[T]:
    """
    Counting sort for objects with integer keys.

    KEY FUNCTION:
    Extracts integer key from each object for counting.
    Objects are sorted by their keys while preserving original objects.

    Time Complexity: O(n + k)
    Space Complexity: O(n + k)

    Args:
        arr: Sequence of objects
        key_func: Function that extracts integer key from object

    Returns:
        New sorted list of objects

    Example:
        >>> students = [('Alice', 85), ('Bob', 92), ('Carol', 78)]
        >>> counting_sort_objects(students, lambda x: x[1])
        [('Carol', 78), ('Alice', 85), ('Bob', 92)]
    """
    if not arr:
        return []

    # Extract keys
    keys = [key_func(item) for item in arr]
    min_key = min(keys)
    max_key = max(keys)

    range_size = max_key - min_key + 1
    count = [0] * range_size

    for key in keys:
        count[key - min_key] += 1

    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output (stable)
    output = [None] * len(arr)  # type: ignore
    for i in range(len(arr) - 1, -1, -1):
        key = keys[i] - min_key
        count[key] -= 1
        output[count[key]] = arr[i]

    return output


def counting_sort_by_digit(arr: Sequence[int], exp: int) -> list[int]:
    """
    Counting sort by specific digit (for radix sort).

    RADIX SORT SUBROUTINE:
    Sorts by a single digit position.
    exp = 1 for units, 10 for tens, 100 for hundreds, etc.

    Time Complexity: O(n + 10) = O(n)
    Space Complexity: O(n + 10) = O(n)
    """
    if not arr:
        return []

    # Digits are 0-9, so k = 10
    count = [0] * 10

    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (stable, right to left)
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    return output


def counting_sort_frequency(arr: Sequence[int]) -> list[int]:
    """
    Sort by frequency (most frequent first), then by value.

    USE CASE:
    - Frequency-based sorting
    - Finding most common elements

    Time Complexity: O(n + k)
    Space Complexity: O(n + k)
    """
    if not arr:
        return []

    # Count frequencies
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Sort by frequency (desc) then value (asc)
    return sorted(arr, key=lambda x: (-freq[x], x))


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    test_arrays = [
        [4, 2, 2, 8, 3, 3, 1],
        [1, 4, 1, 2, 7, 5, 2],
        [5, 5, 5, 5],
        [-3, 1, -2, 4, 0],  # With negatives
    ]

    print("=" * 60)
    print("COUNTING SORT DEMONSTRATION")
    print("=" * 60)

    # Test basic counting sort
    print("\n1. Basic Counting Sort")
    print(f"   Original: {test_arrays[0]}")
    print(f"   Sorted:   {counting_sort(test_arrays[0])}")

    # Test stable version
    print("\n2. Stable Counting Sort")
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"   Original: {arr}")
    print(f"   Sorted:   {counting_sort_stable(arr)}")

    # Test with negatives
    print("\n3. Counting Sort (With Negatives)")
    print(f"   Original: {test_arrays[3]}")
    print(f"   Sorted:   {counting_sort_with_negative(test_arrays[3])}")

    # Test object sorting
    print("\n4. Sort Objects by Integer Key")
    students = [('Alice', 85), ('Bob', 92), ('Carol', 78), ('Dave', 85)]
    print(f"   Original: {students}")
    sorted_students = counting_sort_objects(students, lambda x: x[1])
    print(f"   Sorted by score: {sorted_students}")
    print("   (Note: Alice and Dave maintain relative order - stable)")

    # Test digit sort (for radix)
    print("\n5. Sort by Specific Digit (Units Place)")
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"   Original: {arr}")
    sorted_by_units = counting_sort_by_digit(arr, 1)
    print(f"   By units digit: {sorted_by_units}")

    print("\n" + "=" * 60)
    print("All tests completed!")
