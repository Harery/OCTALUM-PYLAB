"""
Python Set Operations - Comprehensive Guide

This module covers all essential set operations in Python including:
- Set creation and modification
- Set operations (union, intersection, difference)
- Set comparisons (subset, superset)
- Set comprehensions
"""

from __future__ import annotations


def demonstrate_set_basics() -> None:
    """Demonstrate basic set creation and properties."""
    # Creating sets
    fruits: set[str] = {"apple", "banana", "cherry"}
    numbers = set([1, 2, 3, 3, 3])  # Duplicates removed
    empty: set[int] = set()  # NOT {} - that's an empty dict

    print(f"Fruits: {fruits}")
    print(f"Numbers (duplicates removed): {numbers}")
    print(f"Empty set: {empty}")

    # Set properties
    print(f"Unique items only: {len(fruits)} items")


def demonstrate_adding_removing() -> None:
    """Demonstrate adding and removing elements from sets."""
    s: set[int] = {1, 2, 3}
    print(f"Original: {s}")

    # add() - Add single element
    s.add(4)
    print(f"After add(4): {s}")

    # Adding duplicate has no effect
    s.add(4)
    print(f"After add(4) again: {s}")

    # remove() - Raises KeyError if not found
    s.remove(4)
    print(f"After remove(4): {s}")

    # discard() - No error if not found
    s.discard(100)
    print(f"After discard(100) (not in set): {s}")

    # pop() - Remove and return arbitrary element
    popped = s.pop()
    print(f"Popped: {popped}, Remaining: {s}")

    # clear() - Remove all
    s.clear()
    print(f"After clear(): {s}")


def demonstrate_union() -> None:
    """Demonstrate set union operations."""
    a: set[int] = {1, 2, 3}
    b: set[int] = {3, 4, 5}

    # Union using | operator
    union_pipe = a | b
    print(f"a | b: {union_pipe}")

    # Union using union() method
    union_method = a.union(b)
    print(f"a.union(b): {union_method}")

    # Update using |=
    a |= b
    print(f"a |= b: {a}")


def demonstrate_intersection() -> None:
    """Demonstrate set intersection operations."""
    a: set[int] = {1, 2, 3, 4}
    b: set[int] = {3, 4, 5, 6}

    # Intersection using & operator
    inter_amp = a & b
    print(f"a & b: {inter_amp}")

    # Intersection using intersection() method
    inter_method = a.intersection(b)
    print(f"a.intersection(b): {inter_method}")

    # Intersection update
    result = a.copy()
    result &= b
    print(f"a &= b: {result}")


def demonstrate_difference() -> None:
    """Demonstrate set difference operations."""
    a: set[int] = {1, 2, 3, 4}
    b: set[int] = {3, 4, 5, 6}

    # Difference using - operator
    diff_minus = a - b
    print(f"a - b: {diff_minus}")

    # Difference using difference() method
    diff_method = a.difference(b)
    print(f"a.difference(b): {diff_method}")

    # Symmetric difference (elements in either, but not both)
    sym_diff = a ^ b
    print(f"a ^ b (symmetric): {sym_diff}")

    sym_diff_method = a.symmetric_difference(b)
    print(f"a.symmetric_difference(b): {sym_diff_method}")


def demonstrate_subset_superset() -> None:
    """Demonstrate subset and superset operations."""
    a: set[int] = {1, 2}
    b: set[int] = {1, 2, 3, 4}

    # Subset check
    print(f"a subset of b: {a.issubset(b)}")
    print(f"a <= b: {a <= b}")
    print(f"a < b (proper subset): {a < b}")

    # Superset check
    print(f"b superset of a: {b.issuperset(a)}")
    print(f"b >= a: {b >= a}")
    print(f"b > a (proper superset): {b > a}")

    # Disjoint check
    c: set[int] = {5, 6}
    print(f"a disjoint c: {a.isdisjoint(c)}")


def exercise_intersection_and_remove() -> None:
    """
    Exercise: Find intersection of two sets and remove those elements from first set.
    """
    set1: set[int] = {1, 2, 3, 4, 5}
    set2: set[int] = {4, 5, 6, 7, 8}

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")

    # Find intersection
    intersection = set1 & set2
    print(f"Intersection: {intersection}")

    # Remove intersection from set1
    set1 -= intersection
    print(f"Set 1 after removing intersection: {set1}")


def exercise_subset_delete() -> None:
    """
    Exercise: Check if one set is subset/superset of another.
    If subset found, delete all elements from that set.
    """
    set1: set[int] = {1, 2, 3}
    set2: set[int] = {1, 2, 3, 4, 5}

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")

    if set1.issubset(set2):
        print("Set 1 is subset of Set 2")
        set1.clear()
        print(f"Set 1 cleared: {set1}")
    elif set2.issubset(set1):
        print("Set 2 is subset of Set 1")
        set2.clear()
        print(f"Set 2 cleared: {set2}")
    else:
        print("Neither is subset of the other")


def exercise_create_pairs() -> None:
    """Exercise: Create set of pairs from two lists."""
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]

    pairs = set(zip(list1, list2))
    print(f"Pairs from lists: {pairs}")


if __name__ == "__main__":
    print("=" * 50)
    print("Python Set Operations Demo")
    print("=" * 50)

    demonstrate_set_basics()
    print()

    demonstrate_adding_removing()
    print()

    demonstrate_union()
    print()

    demonstrate_intersection()
    print()

    demonstrate_difference()
    print()

    demonstrate_subset_superset()
    print()

    print("=" * 50)
    print("Exercises")
    print("=" * 50)

    print("\nIntersection and Remove:")
    exercise_intersection_and_remove()

    print("\nSubset Check and Delete:")
    exercise_subset_delete()

    print("\nCreate Pairs from Lists:")
    exercise_create_pairs()
