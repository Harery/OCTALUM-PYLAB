"""
Functions: Basics in Python.

This module demonstrates function definitions, parameters, return types,
and various argument patterns using Python 3.12+ syntax.

Time Complexity: O(1) for function call overhead
Space Complexity: O(n) for call stack depth n
"""

from __future__ import annotations


def basic_function() -> str:
    return "Hello from basic function!"


def function_with_params(name: str, age: int) -> str:
    return f"{name} is {age} years old"


def function_with_return_tuple(x: int, y: int) -> tuple[int, int]:
    return x + y, x * y


def function_with_return_dict(name: str, score: int) -> dict[str, int | str]:
    return {"name": name, "score": score, "passed": score >= 60}


def default_parameters(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def multiple_defaults(a: int, b: int = 10, c: int = 20) -> int:
    return a + b + c


def keyword_arguments(name: str, age: int, city: str) -> str:
    return f"{name}, {age}, from {city}"


def positional_only(a: int, b: int, /, c: int) -> int:
    return a + b + c


def keyword_only(a: int, *, b: int, c: int) -> int:
    return a + b + c


def mixed_parameters(a: int, b: int, /, c: int, *, d: int) -> int:
    return a + b + c + d


def variable_positional(*args: int) -> int:
    return sum(args)


def variable_keyword(**kwargs: str) -> dict[str, str]:
    return kwargs


def combined_variable(a: int, *args: int, **kwargs: str) -> dict[str, int | str | list[int]]:
    return {
        "first": a,
        "rest": list(args),
        "named": kwargs
    }


def all_parameter_types(
    a: int,
    b: int,
    /,
    c: int,
    d: int = 10,
    *args: int,
    e: int = 20,
    f: int,
    **kwargs: str
) -> dict[str, int | str | list[int]]:
    return {
        "pos_only": a + b,
        "pos_or_keyword": c + d,
        "var_positional": list(args),
        "keyword_only": e + f,
        "var_keyword": kwargs
    }


def return_none(value: int) -> None:
    print(f"Processing: {value}")


def return_optional(value: int | None) -> int | None:
    if value is None:
        return None
    return value * 2


def return_multiple_types(value: int) -> int | str:
    if value < 0:
        return "negative"
    return value * 2


def type_alias_example() -> None:
    type Vector = tuple[float, float, float]
    type PointDict = dict[str, Vector]

    def create_point(name: str, coords: Vector) -> PointDict:
        return {name: coords}

    result: PointDict = create_point("origin", (0.0, 0.0, 0.0))
    print(f"Point: {result}")


def callback_function(numbers: list[int], transform: Callable[[int], int]) -> list[int]:
    return [transform(n) for n in numbers]


def function_as_argument() -> None:
    def double(x: int) -> int:
        return x * 2

    def square(x: int) -> int:
        return x * x

    nums: list[int] = [1, 2, 3, 4, 5]

    doubled: list[int] = callback_function(nums, double)
    print(f"Doubled: {doubled}")

    squared: list[int] = callback_function(nums, square)
    print(f"Squared: {squared}")


def returning_function(multiplier: int) -> Callable[[int], int]:
    def multiply(x: int) -> int:
        return x * multiplier
    return multiply


def closure_example() -> None:
    double: Callable[[int], int] = returning_function(2)
    triple: Callable[[int], int] = returning_function(3)

    print(f"double(5): {double(5)}")
    print(f"triple(5): {triple(5)}")


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def tail_recursive_sum(n: int, accumulator: int = 0) -> int:
    if n == 0:
        return accumulator
    return tail_recursive_sum(n - 1, accumulator + n)


def early_return_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


def guard_clause_pattern(data: list[int] | None) -> str:
    if data is None:
        return "No data"

    if not data:
        return "Empty data"

    if len(data) > 100:
        return "Data too large"

    return f"Processed {len(data)} items"


def main() -> None:
    print("=" * 60)
    print("BASIC FUNCTIONS")
    print("=" * 60)
    print(basic_function())
    print(function_with_params("Alice", 30))
    sum_val, product = function_with_return_tuple(5, 3)
    print(f"Sum: {sum_val}, Product: {product}")

    print("\n" + "=" * 60)
    print("DEFAULT PARAMETERS")
    print("=" * 60)
    print(default_parameters("Alice"))
    print(default_parameters("Alice", "Hi"))
    print(f"multiple_defaults(1): {multiple_defaults(1)}")
    print(f"multiple_defaults(1, 2): {multiple_defaults(1, 2)}")
    print(f"multiple_defaults(1, 2, 3): {multiple_defaults(1, 2, 3)}")

    print("\n" + "=" * 60)
    print("KEYWORD ARGUMENTS")
    print("=" * 60)
    print(keyword_arguments("Alice", 30, "NYC"))
    print(keyword_arguments(name="Bob", city="LA", age=25))

    print("\n" + "=" * 60)
    print("POSITIONAL-ONLY AND KEYWORD-ONLY")
    print("=" * 60)
    print(f"positional_only(1, 2, 3): {positional_only(1, 2, 3)}")
    print(f"keyword_only(1, b=2, c=3): {keyword_only(1, b=2, c=3)}")
    print(f"mixed_parameters(1, 2, 3, d=4): {mixed_parameters(1, 2, 3, d=4)}")

    print("\n" + "=" * 60)
    print("VARIABLE ARGUMENTS (*args, **kwargs)")
    print("=" * 60)
    print(f"variable_positional(1, 2, 3, 4, 5): {variable_positional(1, 2, 3, 4, 5)}")
    print(f"variable_keyword(a=1, b=2, c=3): {variable_keyword(a='1', b='2', c='3')}")
    print(f"combined_variable(1, 2, 3, x='a', y='b'): {combined_variable(1, 2, 3, x='a', y='b')}")

    print("\n" + "=" * 60)
    print("RETURN TYPES")
    print("=" * 60)
    return_none(42)
    print(f"return_optional(5): {return_optional(5)}")
    print(f"return_optional(None): {return_optional(None)}")
    print(f"return_multiple_types(5): {return_multiple_types(5)}")
    print(f"return_multiple_types(-5): {return_multiple_types(-5)}")

    print("\n" + "=" * 60)
    print("FUNCTIONS AS OBJECTS")
    print("=" * 60)
    function_as_argument()
    closure_example()

    print("\n" + "=" * 60)
    print("RECURSION")
    print("=" * 60)
    print(f"factorial(5): {factorial(5)}")
    print(f"fibonacci(10): {fibonacci(10)}")
    print(f"tail_recursive_sum(10): {tail_recursive_sum(10)}")

    print("\n" + "=" * 60)
    print("PRACTICAL PATTERNS")
    print("=" * 60)
    print(f"early_return_divide(10, 2): {early_return_divide(10, 2)}")
    print(f"early_return_divide(10, 0): {early_return_divide(10, 0)}")
    print(f"guard_clause_pattern([1, 2, 3]): {guard_clause_pattern([1, 2, 3])}")
    print(f"guard_clause_pattern(None): {guard_clause_pattern(None)}")


from typing import Callable


if __name__ == "__main__":
    main()
