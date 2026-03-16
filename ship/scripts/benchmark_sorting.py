#!/usr/bin/env python3
"""
OCTALUM-PYLAB Sorting Benchmark

Compare performance of different sorting algorithms.

Usage:
    python ship/scripts/benchmark_sorting.py
    python ship/scripts/benchmark_sorting.py --size 10000
    python ship/scripts/benchmark_sorting.py --algorithms quick,merge,heap
"""

from __future__ import annotations

import argparse
import random
import timeit
from typing import Callable

type SortFunction = Callable[[list[int]], list[int]]


def bubble_sort(arr: list[int]) -> list[int]:
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(arr: list[int]) -> list[int]:
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def insertion_sort(arr: list[int]) -> list[int]:
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr: list[int]) -> list[int]:
    import heapq

    result = arr.copy()
    heapq.heapify(result)
    return [heapq.heappop(result) for _ in range(len(result))]


def python_sort(arr: list[int]) -> list[int]:
    return sorted(arr)


ALGORITHMS: dict[str, SortFunction] = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "python": python_sort,
}


def benchmark(algorithm: str, data: list[int], repeats: int = 3) -> float:
    """Run benchmark and return average time in milliseconds."""
    func = ALGORITHMS[algorithm]
    timer = timeit.Timer(lambda: func(data))
    times = timer.repeat(repeat=repeats, number=1)
    return min(times) * 1000


def main() -> None:
    parser = argparse.ArgumentParser(description="Sorting Algorithm Benchmark")
    parser.add_argument(
        "--size",
        "-s",
        type=int,
        default=1000,
        help="Size of array to sort (default: 1000)",
    )
    parser.add_argument(
        "--algorithms",
        "-a",
        type=str,
        default="all",
        help="Comma-separated algorithms to test (default: all)",
    )
    parser.add_argument(
        "--repeats",
        "-r",
        type=int,
        default=3,
        help="Number of repeats (default: 3)",
    )
    parser.add_argument(
        "--sorted",
        action="store_true",
        help="Use pre-sorted data (best case)",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Use reverse-sorted data (worst case)",
    )

    args = parser.parse_args()

    if args.algorithms == "all":
        algorithms = list(ALGORITHMS.keys())
    else:
        algorithms = [a.strip() for a in args.algorithms.split(",") if a.strip() in ALGORITHMS]

    if args.sorted:
        data = list(range(args.size))
        data_type = "Sorted"
    elif args.reverse:
        data = list(range(args.size, 0, -1))
        data_type = "Reverse Sorted"
    else:
        data = list(range(args.size))
        random.shuffle(data)
        data_type = "Random"

    print(f"\n{'=' * 60}")
    print(f"Sorting Benchmark - {args.size:,} elements ({data_type})")
    print(f"{'=' * 60}\n")

    print(f"{'Algorithm':<15} {'Time (ms)':<12} {'Ops/sec':<15}")
    print("-" * 45)

    results = []
    for algo in algorithms:
        try:
            time_ms = benchmark(algo, data.copy(), args.repeats)
            ops_per_sec = args.size / (time_ms / 1000)
            results.append((algo, time_ms, ops_per_sec))
            print(f"{algo:<15} {time_ms:>10.2f}   {ops_per_sec:>12,.0f}")
        except RecursionError:
            print(f"{algo:<15} {'RECURSION ERROR':<12}")
        except Exception as e:
            print(f"{algo:<15} {f'ERROR: {e}'[:30]}")

    print("\n" + "=" * 60)

    if results:
        fastest = min(results, key=lambda x: x[1])
        print(f"Fastest: {fastest[0]} ({fastest[1]:.2f} ms)")


if __name__ == "__main__":
    main()
