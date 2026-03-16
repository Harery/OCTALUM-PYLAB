"""
Python String Operations - Comprehensive Guide

This module covers all essential string operations in Python including:
- String creation and formatting
- String methods (upper, lower, strip, split, join)
- String slicing and indexing
- Pattern matching basics
"""

from __future__ import annotations


def demonstrate_string_basics() -> None:
    """Demonstrate basic string creation and properties."""
    # Different ways to create strings
    single = "Hello"
    double = "World"
    triple = """Multi-line
    string"""

    print(f"Single quotes: {single}")
    print(f"Double quotes: {double}")
    print(f"Triple quotes: {triple}")

    # String properties
    text = "Python"
    print(f"Length: {len(text)}")
    print(f"First char: {text[0]}")
    print(f"Last char: {text[-1]}")


def demonstrate_string_immutability() -> None:
    """Demonstrate that strings are immutable."""
    text = "Hello"
    print(f"Original: {text}")
    print(f"ID: {id(text)}")

    # This creates a NEW string, doesn't modify the original
    text = text + " World"
    print(f"After concatenation: {text}")
    print(f"New ID: {id(text)}")


def demonstrate_string_formatting() -> None:
    """Demonstrate different string formatting methods."""
    name = "Alice"
    age = 30
    score = 95.5678

    # f-strings (Python 3.6+) - Preferred
    print(f"Name: {name}, Age: {age}")
    print(f"Score: {score:.2f}")

    # format() method
    print("Name: {}, Age: {}".format(name, age))
    print("Name: {n}, Age: {a}".format(n=name, a=age))

    # % formatting (old style)
    print("Name: %s, Age: %d" % (name, age))


def demonstrate_case_methods() -> None:
    """Demonstrate string case conversion methods."""
    text = "Hello World"

    print(f"Original: {text}")
    print(f"upper(): {text.upper()}")
    print(f"lower(): {text.lower()}")
    print(f"title(): {text.title()}")
    print(f"capitalize(): {text.capitalize()}")
    print(f"swapcase(): {text.swapcase()}")


def demonstrate_search_methods() -> None:
    """Demonstrate string search methods."""
    text = "Hello, World! Hello, Python!"

    # find() - Returns index or -1
    print(f"find('World'): {text.find('World')}")
    print(f"find('xyz'): {text.find('xyz')}")

    # index() - Returns index or raises ValueError
    try:
        print(f"index('World'): {text.index('World')}")
    except ValueError:
        print("'World' not found")

    # count() - Count occurrences
    print(f"count('Hello'): {text.count('Hello')}")

    # startswith(), endswith()
    print(f"startswith('Hello'): {text.startswith('Hello')}")
    print(f"endswith('!'): {text.endswith('!')}")


def demonstrate_strip_methods() -> None:
    """Demonstrate string stripping methods."""
    text = "   Hello World   "

    print(f"Original: '{text}'")
    print(f"strip(): '{text.strip()}'")
    print(f"lstrip(): '{text.lstrip()}'")
    print(f"rstrip(): '{text.rstrip()}'")

    # Strip specific characters
    custom = "xxHello Worldxx"
    print(f"strip('x'): '{custom.strip('x')}'")


def demonstrate_split_join() -> None:
    """Demonstrate string split and join methods."""
    sentence = "Hello World Python Programming"

    # split() - Split into list
    words = sentence.split()
    print(f"split(): {words}")

    # split with delimiter
    csv = "apple,banana,cherry"
    items = csv.split(",")
    print(f"split(','): {items}")

    # join() - Join list into string
    joined = " ".join(words)
    print(f"' '.join(): {joined}")

    joined_csv = ",".join(items)
    print(f"','.join(): {joined_csv}")


def demonstrate_replace() -> None:
    """Demonstrate string replace method."""
    text = "Hello World, World is beautiful"

    # Replace all occurrences
    replaced = text.replace("World", "Python")
    print(f"replace('World', 'Python'): {replaced}")

    # Replace with count
    limited = text.replace("World", "Python", 1)
    print(f"replace with count=1: {limited}")


def demonstrate_slicing() -> None:
    """Demonstrate string slicing operations."""
    text = "Python Programming"

    print(f"Original: {text}")

    # Basic slicing [start:end]
    print(f"[0:6]: {text[0:6]}")
    print(f"[7:]: {text[7:]}")
    print(f"[:6]: {text[:6]}")

    # Negative slicing
    print(f"[-11:]: {text[-11:]}")
    print(f"[:-1]: {text[:-1]}")

    # Step slicing [start:end:step]
    print(f"[::2]: {text[::2]}")
    print(f"[1::2]: {text[1::2]}")

    # Reverse
    print(f"[::-1]: {text[::-1]}")


def demonstrate_validation_methods() -> None:
    """Demonstrate string validation methods."""
    print(f"'123'.isdigit(): {'123'.isdigit()}")
    print(f"'abc'.isalpha(): {'abc'.isalpha()}")
    print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
    print(f"'   '.isspace(): {'   '.isspace()}")
    print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")
    print(f"'hello'.islower(): {'hello'.islower()}")
    print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")


def exercise_grab_hello() -> None:
    """Exercise: Extract 'hello' from a nested structure."""
    data = {"k1": [1, 2, {"k2": ["this is tricky", {"tough": [1, 2, ["hello"]]}]}]}

    result = data["k1"][2]["k2"][1]["tough"][2][0]
    print(f"Extracted: {result}")


def exercise_incremental_stars() -> None:
    """Exercise: Print incremental star pattern."""
    for i in range(1, 6):
        print("*" * i)


if __name__ == "__main__":
    print("=" * 50)
    print("Python String Operations Demo")
    print("=" * 50)

    demonstrate_string_basics()
    print()

    demonstrate_string_immutability()
    print()

    demonstrate_string_formatting()
    print()

    demonstrate_case_methods()
    print()

    demonstrate_search_methods()
    print()

    demonstrate_strip_methods()
    print()

    demonstrate_split_join()
    print()

    demonstrate_replace()
    print()

    demonstrate_slicing()
    print()

    demonstrate_validation_methods()
    print()

    print("=" * 50)
    print("Exercises")
    print("=" * 50)

    print("\nGrab 'hello' from nested structure:")
    exercise_grab_hello()

    print("\nIncremental stars:")
    exercise_incremental_stars()
