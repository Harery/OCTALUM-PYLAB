"""
Radix Sort Algorithm Module

Radix sort is a non-comparison-based sorting algorithm that sorts numbers
digit by digit, from least significant to most significant (LSD) or vice
versa (MSD), using a stable sort as a subroutine.

WHY IT WORKS:
    Uses the positional notation of numbers.
    Sorts by each digit position, with stable sort ensuring
    previous ordering is preserved for equal digits.

Time Complexity: O(d * (n + b))
    - d = number of digits
    - n = number of elements
    - b = base (10 for decimal)

Space Complexity: O(n + b)

STABLE SORT: Yes (when using stable subroutine like counting sort)

WHEN TO USE:
    - Fixed-length integer keys
    - Strings (lexicographic order)
    - When O(n) sorting is needed and keys are integers

WHEN NOT TO USE:
    - Floating-point numbers (requires special handling)
    - Very large numbers with many digits
    - Variable-length keys without padding
"""

from typing import MutableSequence, Sequence
from counting_sort import counting_sort_by_digit


def radix_sort_lsd(arr: Sequence[int]) -> list[int]:
    """
    Radix sort using Least Significant Digit (LSD) approach.

    ALGORITHM:
    1. Find maximum number to determine number of digits
    2. For each digit position (units, tens, hundreds...):
       a. Sort by that digit using stable sort (counting sort)
       b. Result preserves order from previous sorts for same digit
    3. After all digits processed, array is sorted

    WHY LSD:
    - Natural left-to-right processing
    - No need to know total digits beforehand for sorting
    - Works well with counting sort subroutine

    VISUALIZATION:
    [170, 45, 75, 90, 802, 24, 2, 66]

    Sort by units (exp=1):
    [170, 90, 802, 2, 24, 45, 75, 66]

    Sort by tens (exp=10):
    [802, 2, 24, 45, 66, 170, 75, 90]

    Sort by hundreds (exp=100):
    [2, 24, 45, 66, 75, 90, 170, 802]

    Time Complexity: O(d * n) where d = number of digits
    Space Complexity: O(n)

    Args:
        arr: Sequence of non-negative integers

    Returns:
        New sorted list

    Example:
        >>> radix_sort_lsd([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    if not arr:
        return []

    # Handle empty after filtering
    non_neg = [x for x in arr if x >= 0]
    if not non_neg:
        return []

    result = list(non_neg)

    # Find maximum to know number of digits
    max_val = max(result)

    # Process each digit
    exp = 1
    while max_val // exp > 0:
        result = counting_sort_by_digit(result, exp)
        exp *= 10

    return result


def radix_sort_lsd_with_negatives(arr: Sequence[int]) -> list[int]:
    """
    Radix sort handling negative integers.

    NEGATIVE NUMBER STRATEGY:
    1. Separate into negative and non-negative arrays
    2. Sort non-negative normally
    3. Sort negative by absolute value, then reverse
    4. Combine: sorted_negatives + sorted_non_negatives

    WHY REVERSE NEGATIVES:
    - In absolute terms, -1 > -5
    - But in actual value, -1 > -5
    - After sorting by absolute value: [1, 5] (negative of these)
    - Reversed: [5, 1] → [-5, -1] which is correct order

    Time Complexity: O(d * n)
    Space Complexity: O(n)
    """
    if not arr:
        return []

    negatives = [-x for x in arr if x < 0]
    non_negatives = [x for x in arr if x >= 0]

    # Sort negatives by absolute value
    sorted_negatives = []
    if negatives:
        max_neg = max(negatives)
        exp = 1
        while max_neg // exp > 0:
            negatives = counting_sort_by_digit(negatives, exp)
            exp *= 10
        # Reverse and negate
        sorted_negatives = [-x for x in reversed(negatives)]

    # Sort non-negatives
    sorted_non_neg = []
    if non_negatives:
        max_val = max(non_negatives)
        exp = 1
        while max_val // exp > 0:
            non_negatives = counting_sort_by_digit(non_negatives, exp)
            exp *= 10
        sorted_non_neg = non_negatives

    return sorted_negatives + sorted_non_neg


def radix_sort_msd(arr: Sequence[int]) -> list[int]:
    """
    Radix sort using Most Significant Digit (MSD) approach.

    MSD VS LSD:
    - MSD: Start from most significant digit
    - Allows early termination for different-length numbers
    - More natural for string sorting

    ALGORITHM:
    1. Find maximum digit position
    2. Sort by most significant digit first
    3. Recursively sort each bucket by remaining digits

    Time Complexity: O(d * n) average
    Space Complexity: O(n + d) for recursion stack
    """
    if not arr:
        return []

    non_neg = [x for x in arr if x >= 0]
    if not non_neg:
        return []

    if len(non_neg) <= 1:
        return non_neg

    max_val = max(non_neg)

    # Find highest digit position
    exp = 1
    while max_val // exp > 0:
        exp *= 10
    exp //= 10  # Back off to highest digit position

    return _radix_msd_helper(list(non_neg), exp)


def _radix_msd_helper(arr: list[int], exp: int) -> list[int]:
    """MSD radix sort helper."""
    if exp == 0 or len(arr) <= 1:
        return arr

    # Create buckets for each digit (0-9)
    buckets: list[list[int]] = [[] for _ in range(10)]

    for num in arr:
        digit = (num // exp) % 10
        buckets[digit].append(num)

    # Recursively sort each bucket and concatenate
    result = []
    for bucket in buckets:
        if bucket:
            sorted_bucket = _radix_msd_helper(bucket, exp // 10)
            result.extend(sorted_bucket)

    return result


def radix_sort_strings(strings: Sequence[str]) -> list[str]:
    """
    Radix sort for strings using LSD approach.

    STRING RADIX SORT:
    - Each character is a "digit" in base 256 (ASCII)
    - Pad shorter strings to equal length
    - Sort from last character to first

    WHY PADDING:
    "an" should come before "and"
    Padding: "an\0\0" vs "and\0" - sorting correctly places shorter first

    Time Complexity: O(d * n) where d = max string length
    Space Complexity: O(n)
    """
    if not strings:
        return []

    # Find maximum length
    max_len = max(len(s) for s in strings)

    result = list(strings)

    # Sort from last character to first
    for pos in range(max_len - 1, -1, -1):
        result = _counting_sort_by_char(result, pos)

    return result


def _counting_sort_by_char(strings: list[str], pos: int) -> list[str]:
    """Counting sort by character at position."""
    # 256 ASCII characters + 1 for "no character" (sorts first)
    count = [0] * 257

    for s in strings:
        char_val = ord(s[pos]) + 1 if pos < len(s) else 0
        count[char_val] += 1

    # Cumulative count
    for i in range(1, 257):
        count[i] += count[i - 1]

    # Build output (stable)
    output = [''] * len(strings)
    for s in reversed(strings):
        char_val = ord(s[pos]) + 1 if pos < len(s) else 0
        count[char_val] -= 1
        output[count[char_val]] = s

    return output


def radix_sort_inplace(arr: MutableSequence[int]) -> MutableSequence[int]:
    """
    In-place radix sort (uses minimal extra space).

    IN-PLACE OPTIMIZATION:
    Uses a single auxiliary array instead of creating new arrays
    at each digit pass.

    Time Complexity: O(d * n)
    Space Complexity: O(n) for auxiliary array
    """
    if len(arr) <= 1:
        return arr

    # Filter non-negative for simplicity
    result = [x for x in arr if x >= 0]
    if not result:
        return []

    max_val = max(result)
    aux = [0] * len(result)

    exp = 1
    while max_val // exp > 0:
        _radix_pass_inplace(result, aux, exp)
        exp *= 10

    # Copy back to original
    for i, val in enumerate(result):
        if i < len(arr):
            arr[i] = val

    return arr


def _radix_pass_inplace(arr: list[int], aux: list[int], exp: int) -> None:
    """Single pass of radix sort using auxiliary array."""
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for num in reversed(arr):
        digit = (num // exp) % 10
        count[digit] -= 1
        aux[count[digit]] = num

    arr[:] = aux[:]


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("RADIX SORT DEMONSTRATION")
    print("=" * 60)

    # Test LSD radix sort
    print("\n1. Radix Sort LSD (Non-negative)")
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"   Original: {arr}")
    print(f"   Sorted:   {radix_sort_lsd(arr)}")

    # Test with negatives
    print("\n2. Radix Sort (With Negatives)")
    arr = [170, -45, 75, -90, 802, 24, -2, 66]
    print(f"   Original: {arr}")
    print(f"   Sorted:   {radix_sort_lsd_with_negatives(arr)}")

    # Test MSD
    print("\n3. Radix Sort MSD")
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"   Original: {arr}")
    print(f"   Sorted:   {radix_sort_msd(arr)}")

    # Test string sorting
    print("\n4. Radix Sort for Strings")
    words = ["apple", "banana", "grape", "blueberry", "cherry", "an"]
    print(f"   Original: {words}")
    print(f"   Sorted:   {radix_sort_strings(words)}")

    # Test in-place
    print("\n5. In-Place Radix Sort")
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"   Original: {arr}")
    radix_sort_inplace(arr)
    print(f"   Sorted:   {arr}")

    print("\n" + "=" * 60)
    print("All tests completed!")
