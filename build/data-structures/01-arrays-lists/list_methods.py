"""
List Methods Module
===================
Comprehensive demonstration of all Python list methods with examples.

Python lists have 11 built-in methods for modification and querying.
"""

from __future__ import annotations


class ListMethodsDemo:
    """
    Demonstrates all Python list methods with clear examples.

    List methods can be categorized:
    - Adding elements: append, extend, insert
    - Removing elements: remove, pop, clear
    - Finding elements: index, count
    - Sorting/ordering: sort, reverse
    - Copying: copy
    """

    def __init__(self, initial_data: list[int] | None = None) -> None:
        self.data: list[int] = initial_data.copy() if initial_data else []

    def __repr__(self) -> str:
        return f"ListMethodsDemo({self.data})"

    def __str__(self) -> str:
        return str(self.data)


# ============================================================================
# ADDING ELEMENTS
# ============================================================================

def demo_append() -> tuple[list[int], int]:
    """
    list.append(x) - Add item to end of list.

    Time Complexity: O(1) amortized
    Space Complexity: O(1)
    Modifies list in place, returns None

    Equivalent to: lst[len(lst):] = [x]
    """
    lst = [1, 2, 3]
    result = lst.append(4)  # Returns None
    return lst, result if result is not None else 0  # 0 indicates None return


def demo_extend() -> tuple[list[int], int]:
    """
    list.extend(iterable) - Extend list by appending elements from iterable.

    Time Complexity: O(k) where k is length of iterable
    Space Complexity: O(1)
    Modifies list in place, returns None

    Equivalent to: lst[len(lst):] = iterable
    """
    lst = [1, 2, 3]
    result = lst.extend([4, 5, 6])  # Returns None
    return lst, 0


def demo_extend_various() -> dict[str, list[int | str]]:
    """
    extend() works with any iterable, not just lists.
    """
    results: dict[str, list[int | str]] = {}

    # With list
    lst1 = [1, 2]
    lst1.extend([3, 4])
    results["from_list"] = lst1

    # With tuple
    lst2 = [1, 2]
    lst2.extend((3, 4))
    results["from_tuple"] = lst2

    # With string (extends with characters)
    lst3 = ["a", "b"]
    lst3.extend("cd")
    results["from_string"] = lst3

    # With range
    lst4 = [1, 2]
    lst4.extend(range(3, 5))
    results["from_range"] = lst4

    # With set (order not guaranteed)
    lst5 = [1, 2]
    lst5.extend({3, 4})
    results["from_set"] = lst5

    return results


def demo_insert() -> list[int]:
    """
    list.insert(i, x) - Insert item at position i.

    Time Complexity: O(n) - elements after i must be shifted
    Space Complexity: O(1)
    Modifies list in place, returns None

    - If i >= len(lst): inserts at end (like append)
    - If i <= -len(lst): inserts at beginning
    - Negative indices are supported
    """
    lst = [1, 2, 3]
    lst.insert(0, 0)     # Insert at beginning
    lst.insert(2, 1.5)   # Insert in middle
    lst.insert(100, 99)  # Insert beyond end (appends)
    lst.insert(-1, 88)   # Insert before last element
    return lst


# ============================================================================
# REMOVING ELEMENTS
# ============================================================================

def demo_remove() -> tuple[list[int], int]:
    """
    list.remove(x) - Remove first occurrence of value x.

    Time Complexity: O(n) - search + shift
    Space Complexity: O(1)
    Modifies list in place, returns None
    Raises ValueError if x not in list
    """
    lst = [1, 2, 3, 2, 4]
    result = lst.remove(2)  # Removes first 2, not second
    return lst, 0


def demo_remove_error() -> str:
    """remove() raises ValueError if element not found."""
    lst = [1, 2, 3]
    try:
        lst.remove(99)
        return "Should not reach here"
    except ValueError as e:
        return f"ValueError: {e}"


def demo_pop() -> dict[str, int | list[int]]:
    """
    list.pop([i]) - Remove and return item at index i (default: last).

    Time Complexity: O(1) for last element, O(n) for others
    Space Complexity: O(1)
    Modifies list in place, returns the removed element
    Raises IndexError if list empty or index out of range
    """
    results: dict[str, int | list[int]] = {}

    lst = [1, 2, 3, 4, 5]

    # Pop last (default) - O(1)
    results["popped_last"] = lst.pop()
    results["after_pop_last"] = lst.copy()

    # Pop at index - O(n)
    results["popped_index_1"] = lst.pop(1)
    results["after_pop_index"] = lst.copy()

    # Pop with negative index
    results["popped_neg_1"] = lst.pop(-1)
    results["final"] = lst.copy()

    return results


def demo_pop_empty_error() -> str:
    """pop() on empty list raises IndexError."""
    lst: list[int] = []
    try:
        lst.pop()
        return "Should not reach here"
    except IndexError as e:
        return f"IndexError: {e}"


def demo_clear() -> tuple[list[int], int]:
    """
    list.clear() - Remove all items from list.

    Time Complexity: O(n) - decrements ref count for each element
    Space Complexity: O(1)
    Modifies list in place, returns None

    Equivalent to: del lst[:] or lst[:] = []
    """
    lst = [1, 2, 3, 4, 5]
    result = lst.clear()
    return lst, 0


# ============================================================================
# FINDING ELEMENTS
# ============================================================================

def demo_index() -> dict[str, int | tuple[int, ...]]:
    """
    list.index(x[, start[, end]]) - Return index of first occurrence of x.

    Time Complexity: O(n)
    Space Complexity: O(1)
    Raises ValueError if x not in list

    Parameters:
    - x: value to find
    - start: starting index for search (default 0)
    - end: ending index for search (default len(lst))
    """
    results: dict[str, int | tuple[int, ...]] = {}
    lst = [1, 2, 3, 2, 4, 2, 5]

    # Basic index
    results["index_of_2"] = lst.index(2)

    # With start parameter
    results["index_of_2_from_3"] = lst.index(2, 3)  # Start from index 3

    # With start and end parameters
    results["index_of_2_in_range"] = lst.index(2, 2, 5)  # Search indices 2-4

    return results


def demo_index_error() -> str:
    """index() raises ValueError if element not found."""
    lst = [1, 2, 3]
    try:
        lst.index(99)
        return "Should not reach here"
    except ValueError as e:
        return f"ValueError: {e}"


def demo_count() -> dict[str, int]:
    """
    list.count(x) - Return number of occurrences of x.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    lst = [1, 2, 3, 2, 4, 2, 5, 2]

    return {
        "count_2": lst.count(2),
        "count_1": lst.count(1),
        "count_99": lst.count(99),  # Returns 0 for non-existent
        "count_in_empty": [].count(1),
    }


# ============================================================================
# SORTING AND ORDERING
# ============================================================================

def demo_sort() -> dict[str, list[int]]:
    """
    list.sort(*, key=None, reverse=False) - Sort list in place.

    Time Complexity: O(n log n) - uses Timsort
    Space Complexity: O(n) - Timsort needs temporary storage
    Modifies list in place, returns None

    Timsort: Hybrid stable sorting algorithm derived from merge sort
    and insertion sort. Stable means equal elements keep original order.
    """
    results: dict[str, list[int]] = {}
    lst = [3, 1, 4, 1, 5, 9, 2, 6]

    # Basic sort
    sorted_lst = lst.copy()
    sorted_lst.sort()
    results["ascending"] = sorted_lst

    # Reverse sort
    reverse_lst = lst.copy()
    reverse_lst.sort(reverse=True)
    results["descending"] = reverse_lst

    return results


def demo_sort_key() -> dict[str, list[str] | list[tuple[int, str]]]:
    """
    sort() with key function for custom sorting.
    """
    results: dict[str, list[str] | list[tuple[int, str]]] = {}

    # Sort strings by length
    words = ["apple", "pie", "a", "longer", "hi"]
    words_sorted = words.copy()
    words_sorted.sort(key=len)
    results["by_length"] = words_sorted

    # Sort strings case-insensitive
    mixed = ["Banana", "apple", "Cherry", "date"]
    mixed_sorted = mixed.copy()
    mixed_sorted.sort(key=str.lower)
    results["case_insensitive"] = mixed_sorted

    # Sort by second element of tuple
    pairs = [(1, "b"), (2, "a"), (3, "c")]
    pairs_sorted = pairs.copy()
    pairs_sorted.sort(key=lambda x: x[1])
    results["by_second_element"] = pairs_sorted

    # Sort by absolute value
    nums = [-5, 2, -1, 8, -3]
    nums_sorted = nums.copy()
    nums_sorted.sort(key=abs)
    results["by_absolute_value"] = [str(n) for n in nums_sorted]
    results["by_absolute_value_actual"] = nums_sorted

    return results


def demo_sort_stable() -> list[tuple[str, int]]:
    """
    Demonstrate that sort() is stable - equal elements maintain relative order.
    """
    # Sort by first letter, 'a' and 'A' will be considered equal
    data = [("apple", 1), ("Apple", 2), ("banana", 3), ("apricot", 4)]
    data.sort(key=lambda x: x[0].lower())
    return data


def demo_reverse() -> list[int]:
    """
    list.reverse() - Reverse elements in place.

    Time Complexity: O(n)
    Space Complexity: O(1)
    Modifies list in place, returns None
    """
    lst = [1, 2, 3, 4, 5]
    lst.reverse()
    return lst


# ============================================================================
# COPYING
# ============================================================================

def demo_copy() -> dict[str, list[int]]:
    """
    list.copy() - Return a shallow copy of the list.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Equivalent to: lst[:] or list(lst)

    Note: This is a SHALLOW copy - nested mutable objects are shared.
    """
    original = [1, 2, 3, 4, 5]
    shallow = original.copy()

    # Modify copy doesn't affect original
    shallow.append(6)

    return {
        "original": original,
        "copy": shallow,
    }


def demo_copy_shallow_vs_deep() -> dict[str, list[list[int]]]:
    """
    Demonstrate shallow copy behavior with nested lists.
    """
    import copy

    original = [[1, 2], [3, 4]]

    # Shallow copy - nested lists are shared
    shallow = original.copy()
    shallow[0].append(99)  # Affects original!

    # Deep copy - nested lists are independent
    original2 = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original2)
    deep[0].append(99)  # Does NOT affect original2

    return {
        "original_after_shallow_mod": original,
        "original2_after_deep_mod": original2,
        "deep_copy": deep,
    }


# ============================================================================
# LIST OPERATORS (not methods, but commonly used)
# ============================================================================

def demo_operators() -> dict[str, list[int] | int | bool]:
    """
    Demonstrate list operators.
    """
    a = [1, 2, 3]
    b = [4, 5]

    return {
        # Concatenation - O(n+m)
        "concatenation": a + b,

        # Repetition - O(n*k)
        "repetition": a * 2,

        # Membership - O(n)
        "contains_2": 2 in a,
        "contains_4": 4 in a,

        # Comparison (lexicographic) - O(n)
        "less_than": [1, 2] < [1, 3],
        "equal": [1, 2] == [1, 2],

        # Length - O(1)
        "length": len(a),

        # Min/Max - O(n)
        "min": min(a),
        "max": max(a),

        # Sum - O(n)
        "sum": sum(a),
    }


# ============================================================================
# ADVANCED PATTERNS
# ============================================================================

def demo_list_comprehensions() -> dict[str, list[int]]:
    """
    List comprehensions for creating lists.
    """
    return {
        # Basic comprehension
        "squares": [x ** 2 for x in range(5)],

        # With condition
        "evens": [x for x in range(10) if x % 2 == 0],

        # With transformation
        "uppercased": [c.upper() for c in "hello"],

        # Nested comprehension (matrix transposition)
        "flattened": [x for row in [[1, 2], [3, 4]] for x in row],

        # Conditional expression
        "positive_or_zero": [x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]],
    }


def demo_stack_operations() -> dict[str, int | list[int]]:
    """
    Using list as a stack (LIFO - Last In, First Out).

    Operations:
    - push: append() - O(1)
    - pop: pop() - O(1)
    - peek: lst[-1] - O(1)
    - is_empty: len(lst) == 0 - O(1)
    """
    stack: list[int] = []
    results: dict[str, int | list[int]] = {}

    # Push
    stack.append(1)
    stack.append(2)
    stack.append(3)
    results["after_push"] = stack.copy()

    # Peek
    results["peek"] = stack[-1]

    # Pop
    results["popped"] = stack.pop()
    results["after_pop"] = stack.copy()

    # Check empty
    results["is_empty"] = len(stack) == 0

    return results


def demo_queue_operations_warning() -> str:
    """
    WARNING: Lists are NOT efficient for queues!

    Using list as queue (FIFO) is O(n) for pop(0).
    Use collections.deque instead for O(1) operations.
    """
    return "Use collections.deque for queues - list.pop(0) is O(n)!"


if __name__ == "__main__":
    print("=== ADDING ELEMENTS ===")
    lst, _ = demo_append()
    print(f"append: {lst}")

    lst, _ = demo_extend()
    print(f"extend: {lst}")

    print(f"insert: {demo_insert()}")

    print("\n=== REMOVING ELEMENTS ===")
    lst, _ = demo_remove()
    print(f"remove(2): {lst}")

    print(f"pop operations: {demo_pop()}")

    lst, _ = demo_clear()
    print(f"clear: {lst}")

    print("\n=== FINDING ELEMENTS ===")
    print(f"index: {demo_index()}")
    print(f"count: {demo_count()}")

    print("\n=== SORTING ===")
    print(f"sort: {demo_sort()}")
    print(f"sort with key: {demo_sort_key()}")
    print(f"reverse: {demo_reverse()}")

    print("\n=== COPYING ===")
    print(f"copy: {demo_copy()}")

    print("\n=== OPERATORS ===")
    print(f"operators: {demo_operators()}")

    print("\n=== STACK OPERATIONS ===")
    print(f"stack: {demo_stack_operations()}")
