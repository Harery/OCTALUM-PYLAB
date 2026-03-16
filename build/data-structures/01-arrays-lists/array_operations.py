"""
Array Operations Module
=======================
Demonstrates array manipulation, slicing, and common patterns in Python.

Python lists are dynamic arrays that can grow and shrink.
They provide O(1) access time by index but O(n) insertion/deletion in the middle.
"""

from __future__ import annotations


def create_arrays() -> dict[str, list[int] | list[str] | list[float]]:
    """
    Demonstrate various ways to create arrays (lists) in Python.

    Time Complexity: O(n) where n is the size of the created array
    Space Complexity: O(n) for storing the array
    """
    # Empty array
    empty: list[int] = []

    # Literal creation
    numbers: list[int] = [1, 2, 3, 4, 5]

    # Using list() constructor
    from_string: list[str] = list("hello")  # ['h', 'e', 'l', 'l', 'o']

    # List comprehension
    squares: list[int] = [x ** 2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

    # Using * operator for repetition
    repeated: list[int] = [0] * 5  # [0, 0, 0, 0, 0]

    # Range to list
    range_list: list[int] = list(range(5))  # [0, 1, 2, 3, 4]

    # Mixed types (not recommended for arrays)
    mixed: list[int | str | float] = [1, "hello", 3.14]

    return {
        "empty": empty,
        "numbers": numbers,
        "from_string": from_string,
        "squares": squares,
        "repeated": repeated,
        "range_list": range_list,
        "mixed": mixed,
    }


def slicing_operations(arr: list[int]) -> dict[str, list[int]]:
    """
    Demonstrate array slicing operations.

    Slice syntax: arr[start:stop:step]
    - start: inclusive, defaults to 0
    - stop: exclusive, defaults to len(arr)
    - step: defaults to 1

    Time Complexity: O(k) where k is the size of the slice
    Space Complexity: O(k) for the new sliced list
    """
    results: dict[str, list[int]] = {}

    # Basic slicing
    results["first_three"] = arr[0:3]  # Elements at index 0, 1, 2
    results["last_three"] = arr[-3:]  # Last three elements
    results["middle"] = arr[2:5]  # Elements at index 2, 3, 4

    # Step slicing
    results["every_second"] = arr[::2]  # Every second element
    results["every_third"] = arr[::3]  # Every third element

    # Negative indexing
    results["last_element"] = arr[-1:]  # Last element as list
    results["all_except_last"] = arr[:-1]  # All except last

    # Reverse
    results["reversed"] = arr[::-1]  # Reverse the array

    # Reverse with step
    results["reversed_every_second"] = arr[::-2]  # Every second, reversed

    # Copy
    results["copy"] = arr[:]  # Shallow copy

    return results


def access_patterns(arr: list[int]) -> dict[str, int | list[int]]:
    """
    Demonstrate various array access patterns.

    Time Complexity: O(1) for index access, O(n) for search
    Space Complexity: O(1) for single access
    """
    results: dict[str, int | list[int]] = {}

    # Direct index access - O(1)
    results["first"] = arr[0]
    results["last"] = arr[-1]
    results["third"] = arr[2]

    # Safe access with bounds checking
    def safe_get(lst: list[int], index: int, default: int = -1) -> int:
        """Safely get element at index, return default if out of bounds."""
        if 0 <= index < len(lst):
            return lst[index]
        return default

    results["safe_index_100"] = safe_get(arr, 100)  # Returns -1

    return results


def modification_patterns(arr: list[int]) -> dict[str, list[int]]:
    """
    Demonstrate array modification patterns.

    Time Complexity: O(1) for end operations, O(n) for middle operations
    Space Complexity: O(1) for in-place modifications
    """
    # Create copies to avoid modifying original
    results: dict[str, list[int]] = {}

    # Append - O(1) amortized
    append_arr = arr.copy()
    append_arr.append(100)
    results["after_append"] = append_arr

    # Insert at position - O(n)
    insert_arr = arr.copy()
    insert_arr.insert(2, 99)  # Insert 99 at index 2
    results["after_insert"] = insert_arr

    # Extend with another list - O(k) where k is length of extension
    extend_arr = arr.copy()
    extend_arr.extend([10, 20, 30])
    results["after_extend"] = extend_arr

    # Modify by index - O(1)
    modify_arr = arr.copy()
    modify_arr[0] = 999
    results["after_modify"] = modify_arr

    # Remove by value - O(n)
    remove_arr = arr.copy()
    if 3 in remove_arr:
        remove_arr.remove(3)  # Removes first occurrence
    results["after_remove"] = remove_arr

    # Pop from end - O(1)
    pop_arr = arr.copy()
    popped = pop_arr.pop()
    results["after_pop_end"] = pop_arr

    # Pop from middle - O(n)
    pop_middle_arr = arr.copy()
    pop_middle_arr.pop(2)  # Remove element at index 2
    results["after_pop_middle"] = pop_middle_arr

    # Delete slice - O(n)
    del_arr = arr.copy()
    del del_arr[1:3]  # Delete elements at index 1 and 2
    results["after_del_slice"] = del_arr

    return results


def common_patterns() -> dict[str, list[int] | int | tuple[int, int]]:
    """
    Demonstrate common array manipulation patterns.

    Various time complexities noted for each pattern.
    """
    results: dict[str, list[int] | int | tuple[int, int]] = {}

    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # Two pointers pattern - O(n)
    def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
        """Find two numbers that sum to target in sorted array."""
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return (left, right)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

    sorted_arr = sorted(arr)
    result = two_sum_sorted(sorted_arr, 7)
    results["two_sum_result"] = result if result else (-1, -1)

    # Sliding window - O(n)
    def max_sum_subarray(nums: list[int], k: int) -> int:
        """Find maximum sum of any k consecutive elements."""
        if len(nums) < k:
            return 0
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        return max_sum

    results["max_sum_k_3"] = max_sum_subarray(arr, 3)

    # Prefix sum - O(n) preprocessing, O(1) query
    def build_prefix_sum(nums: list[int]) -> list[int]:
        """Build prefix sum array."""
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        return prefix

    prefix = build_prefix_sum(arr)
    results["prefix_sum"] = prefix

    # Range sum query - O(1)
    def range_sum(prefix: list[int], left: int, right: int) -> int:
        """Get sum of elements from index left to right (inclusive)."""
        return prefix[right + 1] - prefix[left]

    results["range_sum_2_to_5"] = range_sum(prefix, 2, 5)

    # Frequency counting - O(n)
    def count_frequency(nums: list[int]) -> dict[int, int]:
        """Count frequency of each element."""
        freq: dict[int, int] = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return freq

    results["most_frequent"] = max(count_frequency(arr).items(), key=lambda x: x[1])[0]

    # Rotate array - O(n)
    def rotate_right(nums: list[int], k: int) -> list[int]:
        """Rotate array to the right by k positions."""
        n = len(nums)
        if n == 0:
            return nums
        k = k % n
        return nums[-k:] + nums[:-k]

    results["rotated_3"] = rotate_right(arr, 3)

    return results


def search_patterns(arr: list[int]) -> dict[str, int | bool]:
    """
    Demonstrate search patterns in arrays.

    Linear search: O(n)
    Binary search: O(log n) - requires sorted array
    """
    results: dict[str, int | bool] = {}

    # Linear search - O(n)
    def linear_search(nums: list[int], target: int) -> int:
        """Find index of target, return -1 if not found."""
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

    results["linear_search_5"] = linear_search(arr, 5)
    results["linear_search_100"] = linear_search(arr, 100)

    # Binary search - O(log n), array must be sorted
    def binary_search(nums: list[int], target: int) -> int:
        """Binary search on sorted array, return index or -1."""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    sorted_arr = sorted(arr)
    results["binary_search_5"] = binary_search(sorted_arr, 5)

    # Find min/max - O(n)
    results["min"] = min(arr)
    results["max"] = max(arr)

    # Check existence - O(n)
    results["contains_5"] = 5 in arr
    results["contains_100"] = 100 in arr

    # Find index - O(n)
    results["index_of_5"] = arr.index(5) if 5 in arr else -1

    return results


def sorting_patterns(arr: list[int]) -> dict[str, list[int]]:
    """
    Demonstrate sorting patterns.

    Python's sorted() uses Timsort: O(n log n) average/worst, O(n) best
    """
    results: dict[str, list[int]] = {}

    # Basic sort - O(n log n)
    results["ascending"] = sorted(arr)
    results["descending"] = sorted(arr, reverse=True)

    # Sort by key
    words = ["apple", "pie", "a", "longer"]
    results["by_length"] = sorted(words, key=len)
    results["by_last_char"] = sorted(words, key=lambda x: x[-1])

    # Sort in place - modifies original
    in_place = arr.copy()
    in_place.sort()
    results["in_place_sorted"] = in_place

    # Stable sort example
    pairs = [(3, "c"), (1, "a"), (2, "b"), (1, "d")]
    results["stable_by_first"] = sorted(pairs, key=lambda x: x[0])

    return results


def transformation_patterns(arr: list[int]) -> dict[str, list[int] | int]:
    """
    Demonstrate array transformation patterns using map, filter, reduce.

    Time Complexity: O(n) for each transformation
    """
    results: dict[str, list[int] | int] = {}

    # Map - transform each element
    results["doubled"] = [x * 2 for x in arr]
    results["squared"] = [x ** 2 for x in arr]

    # Filter - keep elements matching condition
    results["evens"] = [x for x in arr if x % 2 == 0]
    results["greater_than_3"] = [x for x in arr if x > 3]

    # Reduce - combine elements
    results["sum"] = sum(arr)
    results["product"] = 1
    for x in arr:
        results["product"] *= x

    # Flatten nested lists
    nested = [[1, 2], [3, 4], [5, 6]]
    results["flattened"] = [x for sublist in nested for x in sublist]

    # Zip - combine multiple lists
    names = ["a", "b", "c"]
    values = [1, 2, 3]
    results["zipped"] = list(zip(names, values))

    # Enumerate - get index and value
    results["enumerated"] = [(i, x) for i, x in enumerate(arr[:5])]

    return results


if __name__ == "__main__":
    # Example usage
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("=== Array Creation ===")
    arrays = create_arrays()
    for name, arr in arrays.items():
        print(f"{name}: {arr}")

    print("\n=== Slicing Operations ===")
    slices = slicing_operations(test_arr)
    for name, arr in slices.items():
        print(f"{name}: {arr}")

    print("\n=== Common Patterns ===")
    patterns = common_patterns()
    for name, result in patterns.items():
        print(f"{name}: {result}")

    print("\n=== Search Patterns ===")
    searches = search_patterns([3, 1, 4, 1, 5, 9, 2, 6, 5])
    for name, result in searches.items():
        print(f"{name}: {result}")
