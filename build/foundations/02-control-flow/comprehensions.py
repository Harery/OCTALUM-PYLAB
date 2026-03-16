"""
Control Flow: Comprehensions in Python.

This module demonstrates list, dict, set, and generator comprehensions
with Python 3.12+ syntax.

Time Complexity: O(n) for n elements
Space Complexity: O(n) for list/dict/set, O(1) for generators
"""

from __future__ import annotations


def basic_list_comprehension() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]

    squares: list[int] = [x ** 2 for x in numbers]
    print(f"Squares: {squares}")

    cubes: list[int] = [x ** 3 for x in numbers]
    print(f"Cubes: {cubes}")


def list_comprehension_with_condition() -> None:
    numbers: list[int] = range(1, 11)

    evens: list[int] = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {evens}")

    odds: list[int] = [x for x in numbers if x % 2 != 0]
    print(f"Odd numbers: {odds}")

    squares_of_evens: list[int] = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"Squares of evens: {squares_of_evens}")


def list_comprehension_with_if_else() -> None:
    numbers: list[int] = range(1, 6)

    labels: list[str] = ["even" if x % 2 == 0 else "odd" for x in numbers]
    print(f"Labels: {labels}")

    positives: list[int | str] = [x if x > 0 else "negative" for x in [-2, -1, 0, 1, 2]]
    print(f"Positives or label: {positives}")


def nested_list_comprehension() -> None:
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    flattened: list[int] = [item for row in matrix for item in row]
    print(f"Flattened matrix: {flattened}")

    transposed: list[list[int]] = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"Transposed: {transposed}")

    pairs: list[tuple[int, int]] = [(x, y) for x in range(3) for y in range(3)]
    print(f"All pairs (3x3): {pairs}")


def basic_dict_comprehension() -> None:
    names: list[str] = ["alice", "bob", "charlie"]

    name_lengths: dict[str, int] = {name: len(name) for name in names}
    print(f"Name lengths: {name_lengths}")

    numbers: list[int] = [1, 2, 3, 4, 5]
    squares_dict: dict[int, int] = {x: x ** 2 for x in numbers}
    print(f"Squares dict: {squares_dict}")


def dict_comprehension_with_condition() -> None:
    numbers: list[int] = range(1, 11)

    even_squares: dict[int, int] = {x: x ** 2 for x in numbers if x % 2 == 0}
    print(f"Even squares: {even_squares}")

    scores: dict[str, int] = {"Alice": 95, "Bob": 67, "Charlie": 82, "David": 45}

    passing: dict[str, int] = {name: score for name, score in scores.items() if score >= 70}
    print(f"Passing scores: {passing}")


def dict_from_two_lists() -> None:
    keys: list[str] = ["a", "b", "c"]
    values: list[int] = [1, 2, 3]

    mapping: dict[str, int] = {k: v for k, v in zip(keys, values)}
    print(f"Mapping from two lists: {mapping}")


def dict_comprehension_with_transformation() -> None:
    words: list[str] = ["Hello", "WORLD", "Python"]

    lowercase: dict[str, str] = {word: word.lower() for word in words}
    print(f"Lowercase mapping: {lowercase}")

    word_lengths: dict[str, int] = {word.lower(): len(word) for word in words}
    print(f"Word lengths: {word_lengths}")


def basic_set_comprehension() -> None:
    numbers: list[int] = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    unique: set[int] = {x for x in numbers}
    print(f"Unique from {numbers}: {unique}")

    squares_set: set[int] = {x ** 2 for x in range(1, 6)}
    print(f"Squares set: {squares_set}")


def set_comprehension_with_condition() -> None:
    numbers: list[int] = range(-5, 6)

    positive_squares: set[int] = {x ** 2 for x in numbers if x > 0}
    print(f"Positive squares: {positive_squares}")

    words: list[str] = ["apple", "banana", "cherry", "apricot"]

    first_letters: set[str] = {word[0] for word in words}
    print(f"First letters: {first_letters}")


def basic_generator_expression() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]

    squares_gen = (x ** 2 for x in numbers)
    print(f"Generator object: {squares_gen}")
    print(f"Squares as list: {list(squares_gen)}")

    sum_of_squares: int = sum(x ** 2 for x in numbers)
    print(f"Sum of squares: {sum_of_squares}")


def generator_vs_list_memory() -> None:
    import sys

    list_comp: list[int] = [x for x in range(1000)]
    gen_expr = (x for x in range(1000))

    print(f"List size: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")


def generator_with_functions() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]

    total: int = sum(x for x in numbers)
    print(f"Sum: {total}")

    maximum: int = max(x ** 2 for x in numbers)
    print(f"Max square: {maximum}")

    minimum: int = min(x for x in numbers if x > 2)
    print(f"Min > 2: {minimum}")

    as_string: str = ", ".join(str(x) for x in numbers)
    print(f"Joined: {as_string}")


def generator_with_any_all() -> None:
    numbers: list[int] = [2, 4, 6, 8, 10]

    has_even: bool = any(x % 2 == 0 for x in numbers)
    print(f"Has even: {has_even}")

    all_positive: bool = all(x > 0 for x in numbers)
    print(f"All positive: {all_positive}")

    all_even: bool = all(x % 2 == 0 for x in numbers)
    print(f"All even: {all_even}")


def walrus_in_comprehension() -> None:
    data: list[str] = ["hello", "world", "python", "programming"]

    lengths: list[int] = [length for item in data if (length := len(item)) > 5]
    print(f"Lengths > 5: {lengths}")

    results: list[tuple[str, int]] = [(item, length) for item in data if (length := len(item)) > 5]
    print(f"Items with length > 5: {results}")


def filtering_with_comprehension() -> list[int]:
    numbers: list[int] = range(1, 21)

    divisible_by_3_or_5: list[int] = [
        x for x in numbers
        if x % 3 == 0 or x % 5 == 0
    ]
    return divisible_by_3_or_5


def transforming_data() -> dict[str, float]:
    products: list[dict[str, str | float]] = [
        {"name": "apple", "price": 1.50},
        {"name": "banana", "price": 0.75},
        {"name": "cherry", "price": 2.00}
    ]

    price_lookup: dict[str, float] = {
        str(item["name"]): float(item["price"])
        for item in products
    }
    return price_lookup


def nested_filtering() -> list[int]:
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    even_numbers: list[int] = [
        item for row in matrix
        for item in row
        if item % 2 == 0
    ]
    return even_numbers


def main() -> None:
    print("=" * 60)
    print("LIST COMPREHENSIONS")
    print("=" * 60)
    basic_list_comprehension()
    print()
    list_comprehension_with_condition()
    print()
    list_comprehension_with_if_else()
    print()
    nested_list_comprehension()

    print("\n" + "=" * 60)
    print("DICT COMPREHENSIONS")
    print("=" * 60)
    basic_dict_comprehension()
    print()
    dict_comprehension_with_condition()
    print()
    dict_from_two_lists()
    print()
    dict_comprehension_with_transformation()

    print("\n" + "=" * 60)
    print("SET COMPREHENSIONS")
    print("=" * 60)
    basic_set_comprehension()
    print()
    set_comprehension_with_condition()

    print("\n" + "=" * 60)
    print("GENERATOR EXPRESSIONS")
    print("=" * 60)
    basic_generator_expression()
    print()
    generator_vs_list_memory()
    print()
    generator_with_functions()
    print()
    generator_with_any_all()

    print("\n" + "=" * 60)
    print("ADVANCED PATTERNS")
    print("=" * 60)
    walrus_in_comprehension()
    print()
    print(f"Filtering result: {filtering_with_comprehension()}")
    print(f"Transforming result: {transforming_data()}")
    print(f"Nested filtering result: {nested_filtering()}")


if __name__ == "__main__":
    main()
