"""
Control Flow: Loops in Python.

This module demonstrates for loops, while loops, break, continue,
and loop else clauses.

Time Complexity: O(n) for n iterations
Space Complexity: O(1) unless creating new collections
"""

from __future__ import annotations


def basic_for_loop() -> None:
    fruits: list[str] = ["apple", "banana", "cherry"]

    for fruit in fruits:
        print(f"Fruit: {fruit}")


def for_loop_with_range() -> None:
    print("range(5):")
    for i in range(5):
        print(f"  i = {i}")

    print("\nrange(2, 6):")
    for i in range(2, 6):
        print(f"  i = {i}")

    print("\nrange(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  i = {i}")

    print("\nrange(5, 0, -1):")
    for i in range(5, 0, -1):
        print(f"  i = {i}")


def for_loop_with_enumerate() -> None:
    fruits: list[str] = ["apple", "banana", "cherry"]

    print("With enumerate (index, value):")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")

    print("\nStarting enumerate at 1:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}: {fruit}")


def for_loop_with_zip() -> None:
    names: list[str] = ["Alice", "Bob", "Charlie"]
    ages: list[int] = [25, 30, 35]
    cities: list[str] = ["NYC", "LA", "Chicago"]

    print("Zipping two lists:")
    for name, age in zip(names, ages):
        print(f"  {name} is {age} years old")

    print("\nZipping three lists:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}, {age}, lives in {city}")


def iterating_dictionaries() -> None:
    scores: dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}

    print("Iterating keys (default):")
    for name in scores:
        print(f"  {name}")

    print("\nIterating keys explicitly:")
    for name in scores.keys():
        print(f"  {name}")

    print("\nIterating values:")
    for score in scores.values():
        print(f"  {score}")

    print("\nIterating items (key, value):")
    for name, score in scores.items():
        print(f"  {name}: {score}")


def basic_while_loop() -> None:
    count: int = 0

    while count < 5:
        print(f"Count: {count}")
        count += 1

    print(f"Final count: {count}")


def while_with_user_input() -> None:
    responses: list[str] = ["yes", "yes", "no"]
    index: int = 0

    while (response := responses[index]) != "no":
        print(f"Processing: {response}")
        index += 1
        if index >= len(responses):
            break

    print("Stopped at 'no' or end of list")


def break_statement() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target: int = 5

    for num in numbers:
        if num == target:
            print(f"Found {target}!")
            break
        print(f"Checking {num}...")


def continue_statement() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Printing only odd numbers:")
    for num in numbers:
        if num % 2 == 0:
            continue
        print(f"  {num}")


def loop_else_clause() -> None:
    print("For loop with else (no break):")
    for i in range(3):
        print(f"  i = {i}")
    else:
        print("  Loop completed normally")

    print("\nFor loop with else (with break):")
    for i in range(10):
        print(f"  i = {i}")
        if i == 2:
            print("  Breaking...")
            break
    else:
        print("  This won't print due to break")

    print("\nWhile loop with else:")
    count: int = 0
    while count < 3:
        print(f"  count = {count}")
        count += 1
    else:
        print("  While loop completed")


def finding_pattern() -> None:
    numbers: list[int] = [1, 3, 5, 7, 9]
    target: int = 4

    for num in numbers:
        if num == target:
            print(f"Found {target}!")
            break
    else:
        print(f"{target} not found in list")


def nested_loops() -> None:
    print("Multiplication table (3x3):")
    for i in range(1, 4):
        for j in range(1, 4):
            product: int = i * j
            print(f"  {i} x {j} = {product}")
        print()


def nested_loops_with_break() -> None:
    print("Searching in 2D grid:")
    grid: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    target: int = 5
    found: bool = False

    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value == target:
                print(f"  Found {target} at ({row_idx}, {col_idx})")
                found = True
                break
        if found:
            break

    if not found:
        print(f"  {target} not found")


def iterating_strings() -> None:
    text: str = "Python"

    print("Character by character:")
    for char in text:
        print(f"  '{char}'")

    print("\nWith index:")
    for idx, char in enumerate(text):
        print(f"  {idx}: '{char}'")


def reversed_and_sorted() -> None:
    numbers: list[int] = [3, 1, 4, 1, 5, 9]

    print("Reversed iteration:")
    for num in reversed(numbers):
        print(f"  {num}")

    print("\nSorted iteration:")
    for num in sorted(numbers):
        print(f"  {num}")

    print("\nReverse sorted:")
    for num in sorted(numbers, reverse=True):
        print(f"  {num}")


def early_termination_pattern(data: list[int]) -> int | None:
    for i, value in enumerate(data):
        if value < 0:
            print(f"Found negative at index {i}")
            return i
    return None


def processing_with_status() -> tuple[bool, str]:
    items: list[str] = ["valid", "valid", "skip", "valid"]
    processed: int = 0
    skipped: int = 0

    for item in items:
        if item == "skip":
            skipped += 1
            continue
        processed += 1

    return True, f"Processed: {processed}, Skipped: {skipped}"


def main() -> None:
    print("=" * 60)
    print("BASIC FOR LOOP")
    print("=" * 60)
    basic_for_loop()

    print("\n" + "=" * 60)
    print("FOR LOOP WITH RANGE")
    print("=" * 60)
    for_loop_with_range()

    print("\n" + "=" * 60)
    print("FOR LOOP WITH ENUMERATE")
    print("=" * 60)
    for_loop_with_enumerate()

    print("\n" + "=" * 60)
    print("FOR LOOP WITH ZIP")
    print("=" * 60)
    for_loop_with_zip()

    print("\n" + "=" * 60)
    print("ITERATING DICTIONARIES")
    print("=" * 60)
    iterating_dictionaries()

    print("\n" + "=" * 60)
    print("BASIC WHILE LOOP")
    print("=" * 60)
    basic_while_loop()

    print("\n" + "=" * 60)
    print("BREAK AND CONTINUE")
    print("=" * 60)
    break_statement()
    print()
    continue_statement()

    print("\n" + "=" * 60)
    print("LOOP ELSE CLAUSE")
    print("=" * 60)
    loop_else_clause()
    print()
    finding_pattern()

    print("\n" + "=" * 60)
    print("NESTED LOOPS")
    print("=" * 60)
    nested_loops()
    nested_loops_with_break()

    print("\n" + "=" * 60)
    print("SPECIAL ITERATIONS")
    print("=" * 60)
    iterating_strings()
    print()
    reversed_and_sorted()

    print("\n" + "=" * 60)
    print("PRACTICAL PATTERNS")
    print("=" * 60)
    result: int | None = early_termination_pattern([1, 2, -3, 4])
    print(f"early_termination_pattern result: {result}")

    success, message = processing_with_status()
    print(f"processing_with_status: success={success}, {message}")


if __name__ == "__main__":
    main()
