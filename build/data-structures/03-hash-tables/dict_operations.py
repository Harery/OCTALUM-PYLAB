"""
Python Dictionary Operations - Comprehensive Guide

This module covers all essential dictionary operations in Python including:
- Dictionary creation and access
- Adding, updating, and deleting entries
- Dictionary methods (keys, values, items)
- Dictionary comprehensions
- Merging dictionaries
"""

from __future__ import annotations


def demonstrate_dict_basics() -> None:
    """Demonstrate basic dictionary creation and access."""
    # Creating dictionaries
    person: dict[str, str | int] = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
    }

    empty: dict[str, int] = {}
    from_pairs = dict([("a", 1), ("b", 2)])

    print(f"Person: {person}")
    print(f"Empty: {empty}")
    print(f"From pairs: {from_pairs}")

    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age')}")

    # get() with default
    print(f"Country (default): {person.get('country', 'Unknown')}")


def demonstrate_adding_updating() -> None:
    """Demonstrate adding and updating dictionary entries."""
    scores: dict[str, int] = {"Alice": 85, "Bob": 90}

    print(f"Original: {scores}")

    # Add new entry
    scores["Charlie"] = 78
    print(f"After adding Charlie: {scores}")

    # Update existing entry
    scores["Alice"] = 95
    print(f"After updating Alice: {scores}")

    # update() with dict
    scores.update({"David": 88, "Eve": 92})
    print(f"After update(): {scores}")

    # update() with keyword args
    scores.update(Frank=75)
    print(f"After update(Frank=75): {scores}")

    # setdefault() - Set if key doesn't exist
    scores.setdefault("Alice", 0)  # No change, Alice exists
    scores.setdefault("Grace", 80)  # Grace added
    print(f"After setdefault(): {scores}")


def demonstrate_removing() -> None:
    """Demonstrate removing entries from dictionaries."""
    inventory: dict[str, int] = {"apple": 10, "banana": 20, "cherry": 15}

    print(f"Original: {inventory}")

    # del - Remove by key
    del inventory["apple"]
    print(f"After del: {inventory}")

    # pop() - Remove and return value
    removed = inventory.pop("banana")
    print(f"Popped 'banana': {removed}, Remaining: {inventory}")

    # pop() with default (no KeyError)
    inventory.pop("grape", None)

    # popitem() - Remove and return last item (LIFO in Python 3.7+)
    last = inventory.popitem()
    print(f"Popped last item: {last}")

    # clear() - Remove all
    inventory.clear()
    print(f"After clear(): {inventory}")


def demonstrate_iteration() -> None:
    """Demonstrate iterating over dictionaries."""
    person: dict[str, str] = {"name": "Alice", "city": "NYC", "job": "Engineer"}

    # Iterate over keys (default)
    print("Keys:")
    for key in person:
        print(f"  {key}")

    # Iterate over values
    print("Values:")
    for value in person.values():
        print(f"  {value}")

    # Iterate over items (key-value pairs)
    print("Items:")
    for key, value in person.items():
        print(f"  {key}: {value}")


def demonstrate_dict_methods() -> None:
    """Demonstrate useful dictionary methods."""
    scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 78}

    # keys(), values(), items()
    print(f"Keys: {list(scores.keys())}")
    print(f"Values: {list(scores.values())}")
    print(f"Items: {list(scores.items())}")

    # copy() - Shallow copy
    copy = scores.copy()
    print(f"Copy: {copy}")

    # fromkeys() - Create dict with same value
    defaults = dict.fromkeys(["a", "b", "c"], 0)
    print(f"fromkeys: {defaults}")


def demonstrate_merging() -> None:
    """Demonstrate merging dictionaries."""
    dict1: dict[str, int] = {"a": 1, "b": 2}
    dict2: dict[str, int] = {"b": 3, "c": 4}

    # Merge with ** unpacking
    merged = {**dict1, **dict2}
    print(f"Merge with **: {merged}")

    # Merge with | operator (Python 3.9+)
    merged_pipe = dict1 | dict2
    print(f"Merge with |: {merged_pipe}")

    # In-place merge with |=
    dict1 |= dict2
    print(f"dict1 |= dict2: {dict1}")


def demonstrate_comprehensions() -> None:
    """Demonstrate dictionary comprehensions."""
    numbers = list(range(1, 6))

    # Basic comprehension
    squares = {x: x**2 for x in numbers}
    print(f"Squares: {squares}")

    # With condition
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    print(f"Even squares: {even_squares}")

    # Swap keys and values
    swapped = {v: k for k, v in squares.items()}
    print(f"Swapped: {swapped}")


def exercise_count_occurrences() -> None:
    """Exercise: Count occurrences of elements in a list."""
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1

    print(f"Items: {items}")
    print(f"Counts: {counts}")

    # Using collections.Counter
    from collections import Counter

    counter = Counter(items)
    print(f"Counter: {dict(counter)}")


def exercise_unique_values() -> None:
    """Exercise: Get all values from dict into list without duplicates."""
    data: dict[str, int] = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

    unique_values = list(set(data.values()))
    print(f"Dictionary: {data}")
    print(f"Unique values: {sorted(unique_values)}")


def exercise_filter_by_dict_value() -> None:
    """Exercise: Filter list elements based on dictionary values."""
    lookup: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    items = ["a", "b", "x", "c", "y"]

    # Keep only items that exist as values in lookup
    valid_values = set(lookup.values())
    filtered = [item for item in items if item in lookup]

    print(f"Lookup: {lookup}")
    print(f"Items: {items}")
    print(f"Filtered (keys in lookup): {filtered}")


if __name__ == "__main__":
    print("=" * 50)
    print("Python Dictionary Operations Demo")
    print("=" * 50)

    demonstrate_dict_basics()
    print()

    demonstrate_adding_updating()
    print()

    demonstrate_removing()
    print()

    demonstrate_iteration()
    print()

    demonstrate_dict_methods()
    print()

    demonstrate_merging()
    print()

    demonstrate_comprehensions()
    print()

    print("=" * 50)
    print("Exercises")
    print("=" * 50)

    print("\nCount Occurrences:")
    exercise_count_occurrences()

    print("\nUnique Values:")
    exercise_unique_values()

    print("\nFilter by Dict Value:")
    exercise_filter_by_dict_value()
