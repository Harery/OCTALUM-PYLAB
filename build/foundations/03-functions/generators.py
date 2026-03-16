"""
Functions: Generators in Python.

This module demonstrates generators, yield statements, generator expressions,
and itertools basics using Python 3.12+ syntax.

Time Complexity: O(1) per yielded element
Space Complexity: O(1) for generators (lazy evaluation)
"""

from __future__ import annotations
from typing import Generator, Iterator
from itertools import (
    count, cycle, repeat, islice,
    chain, compress, filterfalse,
    starmap, takewhile, dropwhile,
    groupby, combinations, permutations,
    product
)
import time


def basic_generator() -> Generator[int, None, None]:
    n: int = 0
    while n < 5:
        yield n
        n += 1


def generator_with_yield_from() -> Generator[int, None, None]:
    yield from range(3)
    yield from range(10, 13)


def generator_with_send() -> Generator[int, int, None]:
    value: int = 0
    while True:
        received: int = yield value
        if received is not None:
            value = received
        else:
            value += 1


def generator_with_throw() -> Generator[int, None, None]:
    try:
        yield 1
        yield 2
        yield 3
    except ValueError as e:
        yield f"Caught: {e}"
    yield 4


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def infinite_fibonacci() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def countdown(n: int) -> Generator[int, None, None]:
    while n > 0:
        yield n
        n -= 1
    yield 0


def read_lines_simulation() -> Generator[str, None, None]:
    lines: list[str] = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]
    for line in lines:
        yield line


def chunk_generator(data: list[int], chunk_size: int) -> Generator[list[int], None, None]:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def pair_generator(items: list[int]) -> Generator[tuple[int, int], None, None]:
    for i in range(len(items) - 1):
        yield (items[i], items[i + 1])


def tree_traversal_simulation() -> Generator[int, None, None]:
    tree: dict[int, list[int]] = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: []
    }

    def dfs(node: int) -> None:
        yield node
        for child in tree.get(node, []):
            yield from dfs(child)

    yield from dfs(1)


def generator_expression_basics() -> None:
    squares = (x ** 2 for x in range(5))
    print(f"Squares generator: {squares}")
    print(f"As list: {list(squares)}")

    filtered = (x for x in range(20) if x % 3 == 0)
    print(f"Divisible by 3: {list(filtered)}")


def memory_comparison() -> None:
    import sys

    list_data: list[int] = [x for x in range(10000)]
    gen_data = (x for x in range(10000))

    print(f"List size: {sys.getsizeof(list_data)} bytes")
    print(f"Generator size: {sys.getsizeof(gen_data)} bytes")


def pipeline_example() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    step1 = (x for x in numbers)
    step2 = (x * 2 for x in step1)
    step3 = (x for x in step2 if x > 10)

    print(f"Pipeline result: {list(step3)}")


def demonstrate_count() -> None:
    counter = count(start=10, step=2)
    print(f"count(10, 2) first 5: {list(islice(counter, 5))}")


def demonstrate_cycle() -> None:
    colors = cycle(['red', 'green', 'blue'])
    print(f"cycle first 7: {list(islice(colors, 7))}")


def demonstrate_repeat() -> None:
    repeater = repeat('hello', times=3)
    print(f"repeat('hello', 3): {list(repeater)}")


def demonstrate_chain() -> None:
    chained = chain([1, 2], [3, 4], [5, 6])
    print(f"chain([1,2], [3,4], [5,6]): {list(chained)}")


def demonstrate_compress() -> None:
    data: list[str] = ['a', 'b', 'c', 'd']
    selectors: list[bool] = [True, False, True, False]
    result = compress(data, selectors)
    print(f"compress: {list(result)}")


def demonstrate_filterfalse() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    odds = filterfalse(lambda x: x % 2 == 0, numbers)
    print(f"filterfalse (odds): {list(odds)}")


def demonstrate_takewhile_dropwhile() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 1, 2]

    taken = takewhile(lambda x: x < 4, numbers)
    print(f"takewhile x < 4: {list(taken)}")

    dropped = dropwhile(lambda x: x < 4, numbers)
    print(f"dropwhile x < 4: {list(dropped)}")


def demonstrate_groupby() -> None:
    from itertools import groupby

    data: list[str] = ['aaa', 'bb', 'ccc', 'dd', 'eee']
    grouped = groupby(data, key=len)

    print("groupby by length:")
    for key, group in grouped:
        print(f"  Length {key}: {list(group)}")


def demonstrate_starmap() -> None:
    pairs: list[tuple[int, int]] = [(2, 3), (4, 5), (6, 7)]
    result = starmap(pow, pairs)
    print(f"starmap(pow, pairs): {list(result)}")


def demonstrate_combinations() -> None:
    items: list[str] = ['A', 'B', 'C']
    combs = combinations(items, 2)
    print(f"combinations(2): {list(combs)}")


def demonstrate_permutations() -> None:
    items: list[str] = ['A', 'B']
    perms = permutations(items, 2)
    print(f"permutations(2): {list(perms)}")


def demonstrate_product() -> None:
    result = product(['A', 'B'], [1, 2])
    print(f"product: {list(result)}")


class CountdownIterator:
    def __init__(self, start: int) -> None:
        self.current: int = start

    def __iter__(self) -> "CountdownIterator":
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value: int = self.current
        self.current -= 1
        return value


def generator_state_example() -> None:
    def accumulator(initial: int = 0) -> Generator[int, int, None]:
        total: int = initial
        while True:
            received: int = yield total
            if received is not None:
                total += received

    gen = accumulator(10)
    next(gen)
    print(f"Initial: 10")
    print(f"After sending 5: {gen.send(5)}")
    print(f"After sending 3: {gen.send(3)}")


def lazy_file_reader_simulation() -> Generator[dict[str, str | int], None, None]:
    records: list[dict[str, str | int]] = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 87},
        {"id": 3, "name": "Charlie", "score": 92}
    ]

    for record in records:
        yield record


def batch_processor(items: list[int], batch_size: int) -> Generator[list[int], None, None]:
    batch: list[int] = []
    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def main() -> None:
    print("=" * 60)
    print("BASIC GENERATORS")
    print("=" * 60)
    print(f"basic_generator(): {list(basic_generator())}")
    print(f"generator_with_yield_from(): {list(generator_with_yield_from())}")

    print("\n" + "=" * 60)
    print("PRACTICAL GENERATORS")
    print("=" * 60)
    print(f"fibonacci(10): {list(fibonacci_generator(10))}")
    print(f"countdown(5): {list(countdown(5))}")
    print(f"chunks of [1..10] by 3: {list(chunk_generator(list(range(1, 11)), 3))}")

    print("\n" + "=" * 60)
    print("GENERATOR EXPRESSIONS")
    print("=" * 60)
    generator_expression_basics()
    memory_comparison()
    pipeline_example()

    print("\n" + "=" * 60)
    print("ITERTOOLS: INFINITE")
    print("=" * 60)
    demonstrate_count()
    demonstrate_cycle()
    demonstrate_repeat()

    print("\n" + "=" * 60)
    print("ITERTOOLS: COMBINATORIC")
    print("=" * 60)
    demonstrate_combinations()
    demonstrate_permutations()
    demonstrate_product()

    print("\n" + "=" * 60)
    print("ITERTOOLS: FILTERING")
    print("=" * 60)
    demonstrate_chain()
    demonstrate_compress()
    demonstrate_filterfalse()
    demonstrate_takewhile_dropwhile()

    print("\n" + "=" * 60)
    print("ITERTOOLS: GROUPING")
    print("=" * 60)
    demonstrate_groupby()
    demonstrate_starmap()

    print("\n" + "=" * 60)
    print("CUSTOM ITERATOR CLASS")
    print("=" * 60)
    countdown_iter: CountdownIterator = CountdownIterator(5)
    print(f"CountdownIterator(5): {list(countdown_iter)}")

    print("\n" + "=" * 60)
    print("GENERATOR STATE")
    print("=" * 60)
    generator_state_example()


if __name__ == "__main__":
    main()
