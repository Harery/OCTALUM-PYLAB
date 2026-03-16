"""
Python List Operations - Comprehensive Guide

This module covers all essential list operations in Python including:
- Adding elements (append, extend, insert)
- Removing elements (remove, pop, clear)
- Searching and counting
- Sorting and reversing
"""

from __future__ import annotations


def demonstrate_list_basics() -> None:
    """Demonstrate basic list creation and operations."""
    names: list[str] = ["Mohamed", "Ahmed", "Yahia"]

    print(f"Type: {type(names)}")
    print(f"Initial list: {names}")


def demonstrate_adding_elements() -> None:
    """Demonstrate different ways to add elements to a list."""
    names: list[str] = ["Mohamed", "Ahmed", "Yahia"]

    # append() - Add single element to end
    names.append("Jad")
    print(f"After append('Jad'): {names}")

    # += operator - Add multiple elements
    names += ["lola", "m", "azzma"]
    print(f"After += ['lola', 'm', 'azzma']: {names}")

    # extend() - Add iterable elements
    names.extend(["Gihad"])
    print(f"After extend(['Gihad']): {names}")

    # extend() with string - adds each character
    names.extend("medo")
    print(f"After extend('medo'): {names}")

    # insert() - Add at specific index
    names.insert(1, "ali ya ali")
    print(f"After insert(1, 'ali ya ali'): {names}")


def demonstrate_removing_elements() -> None:
    """Demonstrate different ways to remove elements from a list."""
    names: list[str] = ["Mohamed", "Ahmed", "Yahia", "Ali", "Sara"]

    # remove() - Remove by value
    names.remove("Mohamed")
    print(f"After remove('Mohamed'): {names}")

    # pop() - Remove by index (default: last element)
    removed = names.pop(0)
    print(f"After pop(0), removed '{removed}': {names}")

    # clear() - Remove all elements
    names.clear()
    print(f"After clear(): {names}")


def demonstrate_sorting() -> None:
    """Demonstrate list sorting operations."""
    numbers: list[int] = [64, 34, 25, 12, 22, 11, 90]

    # sort() - In-place sorting
    numbers.sort()
    print(f"Sorted ascending: {numbers}")

    numbers.sort(reverse=True)
    print(f"Sorted descending: {numbers}")

    # sorted() - Returns new sorted list
    original = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_copy = sorted(original)
    print(f"Original: {original}")
    print(f"Sorted copy: {sorted_copy}")


def demonstrate_searching() -> None:
    """Demonstrate searching operations in lists."""
    names: list[str] = ["Ahmed", "Yahia", "Ali", "Sara", "m", "m"]

    # count() - Count occurrences
    count_m = names.count("m")
    print(f"Count of 'm': {count_m}")

    # in operator - Check membership
    print(f"'Yahia' in names: {'Yahia' in names}")
    print(f"'f' in names: {'f' in names}")

    # index() - Find index of element
    try:
        idx = names.index("Ali")
        print(f"Index of 'Ali': {idx}")
    except ValueError:
        print("'Ali' not found in list")


def demonstrate_other_operations() -> None:
    """Demonstrate other useful list operations."""
    numbers: list[int] = [1, 2, 3, 4, 5]

    # len() - Get length
    print(f"Length: {len(numbers)}")

    # reverse() - Reverse in place
    numbers.reverse()
    print(f"Reversed: {numbers}")

    # copy() - Create shallow copy
    copy = numbers.copy()
    print(f"Copy: {copy}")

    # min, max, sum
    print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")


def demonstrate_list_comprehensions() -> None:
    """Demonstrate list comprehension patterns."""
    numbers = list(range(10))

    # Basic comprehension
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")

    # With condition
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    # Nested comprehension
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"Matrix: {matrix}")


def fizzbuzz() -> None:
    """Classic FizzBuzz problem demonstrating control flow with lists."""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num}: FizzBuzz")
        elif num % 3 == 0:
            print(f"{num}: Fizz")
        elif num % 5 == 0:
            print(f"{num}: Buzz")
        else:
            print(num)


def exercise_move_element() -> None:
    """
    Exercise: Given a list, remove element at index 4,
    add it to position 2, and also append it to the end.
    """
    data: list[int] = [34, 54, 67, 89, 11, 43, 94]
    print(f"Original list: {data}")

    # Remove element at index 4
    element = data.pop(4)
    print(f"After pop(4): {data}, removed: {element}")

    # Insert at position 2
    data.insert(2, element)
    print(f"After insert(2, {element}): {data}")

    # Append to end
    data.append(element)
    print(f"After append({element}): {data}")


if __name__ == "__main__":
    print("=" * 50)
    print("Python List Operations Demo")
    print("=" * 50)

    demonstrate_list_basics()
    print()

    demonstrate_adding_elements()
    print()

    demonstrate_removing_elements()
    print()

    demonstrate_sorting()
    print()

    demonstrate_searching()
    print()

    demonstrate_other_operations()
    print()

    demonstrate_list_comprehensions()
    print()

    print("=" * 50)
    print("Exercise: Move Element")
    print("=" * 50)
    exercise_move_element()
