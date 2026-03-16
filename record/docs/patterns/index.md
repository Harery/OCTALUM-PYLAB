# Coding Patterns Overview

Master patterns that solve 80% of interview problems.

## Why Patterns Matter

Most coding interview problems can be solved using a handful of patterns. Learning these patterns helps you:

- Recognize problem types quickly
- Apply proven solution templates
- Reduce interview anxiety
- Solve problems more efficiently

## Core Patterns

| Pattern | Use Case | Difficulty |
|---------|----------|------------|
| Sliding Window | Subarray/substring problems | Medium |
| Two Pointers | Sorted arrays, pairs | Easy |
| Fast & Slow Pointers | Cycles, middle element | Medium |
| Merge Intervals | Overlapping intervals | Medium |
| Cyclic Sort | Array in range [1, n] | Easy |
| Tree BFS/DFS | Tree traversals | Easy |
| Subsets | Combinations | Medium |
| Modified Binary Search | Rotated/bounded search | Medium |

## Quick Reference

### Sliding Window

```python
def sliding_window(arr: list[int], k: int) -> int:
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Two Pointers

```python
def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int]:
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return (left, right)
        elif current < target:
            left += 1
        else:
            right -= 1

    return (-1, -1)
```

### Fast & Slow Pointers

```python
def has_cycle(head: ListNode | None) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

## Learning Path

1. Start with **Two Pointers** - simplest pattern
2. Move to **Sliding Window** - very common
3. Learn **Fast & Slow Pointers** - linked list essential
4. Master **Merge Intervals** - interval problems
5. Practice **Cyclic Sort** - array tricks
6. Study **Tree patterns** - BFS/DFS variations
7. Understand **Subsets** - combinatorics

## Practice Files

All pattern implementations in `build/patterns/`:

```bash
python build/patterns/sliding-window/max_sum_subarray.py
python build/patterns/two-pointers/two_sum.py
python build/patterns/fast-slow-pointers/cycle_detection.py
```

## Interview Tips

1. **Identify the pattern** before coding
2. **Draw examples** to understand the problem
3. **Start with brute force**, then optimize
4. **Edge cases** matter - empty input, single element
5. **Time/space complexity** - always analyze

## Pattern Recognition

| Keywords | Likely Pattern |
|----------|----------------|
| "subarray", "contiguous" | Sliding Window |
| "sorted array", "pairs" | Two Pointers |
| "cycle", "middle" | Fast & Slow |
| "intervals", "merge" | Merge Intervals |
| "1 to n", "missing" | Cyclic Sort |
| "all combinations" | Subsets |
