# Arrays and Lists

## Overview

Python lists are dynamic arrays that can grow and shrink. They are implemented as arrays of pointers to objects, allowing them to hold heterogeneous data types.

## Time Complexity Table

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| **Index Access** | O(1) | O(1) | Direct memory access |
| **Index Assignment** | O(1) | O(1) | Direct memory access |
| **Append** | O(1) | O(n) | Amortized O(1), occasionally O(n) for resize |
| **Pop (last)** | O(1) | O(1) | Remove from end |
| **Pop (index)** | O(n) | O(n) | Elements must shift |
| **Insert** | O(n) | O(n) | Elements must shift |
| **Remove** | O(n) | O(n) | Search + shift |
| **Contains (in)** | O(n) | O(n) | Linear search |
| **Index** | O(n) | O(n) | Linear search |
| **Count** | O(n) | O(n) | Must check all elements |
| **Sort** | O(n log n) | O(n log n) | Timsort algorithm |
| **Reverse** | O(n) | O(n) | Swap elements |
| **Copy** | O(n) | O(n) | Shallow copy |
| **Extend** | O(k) | O(k) | k = length of iterable |
| **Len** | O(1) | O(1) | Stored as attribute |
| **Min/Max** | O(n) | O(n) | Must check all elements |
| **Sum** | O(n) | O(n) | Must check all elements |

## Space Complexity

| Operation | Space | Notes |
|-----------|-------|-------|
| **Creation** | O(n) | n = number of elements |
| **Copy** | O(n) | New list with same references |
| **Slice** | O(k) | k = size of slice |
| **Concatenation (+)** | O(n+m) | Creates new list |
| **Repetition (*)** | O(n*k) | k = repeat count |

## Dynamic Array Resizing

Python lists automatically resize when they grow:

- **Growth factor**: Approximately 1.125x (implementation-dependent)
- **Over-allocation**: Extra space reserved for future growth
- **Shrinking**: Occurs when list becomes much smaller

This makes append operations **amortized O(1)**:
- Most appends are O(1)
- Occasional resize is O(n)
- Average over many operations is O(1)

## Slicing Operations

| Slice | Result | Description |
|-------|--------|-------------|
| `lst[a:b]` | Elements from a to b-1 | Start inclusive, end exclusive |
| `lst[a:]` | Elements from a to end | From index a to end |
| `lst[:b]` | Elements from start to b-1 | From beginning to b-1 |
| `lst[:]` | All elements | Shallow copy |
| `lst[::k]` | Every k-th element | Step of k |
| `lst[::-1]` | Reversed list | Negative step reverses |
| `lst[a:b:k]` | Combined | All parameters together |

## Common Patterns

### Two Pointers

```python
def two_pointers(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        # Process elements
        left += 1
        right -= 1
```
**Time**: O(n), **Space**: O(1)

### Sliding Window

```python
def sliding_window(arr: list[int], k: int) -> int:
    window_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        # Process window
```
**Time**: O(n), **Space**: O(1)

### Prefix Sum

```python
def build_prefix(arr: list[int]) -> list[int]:
    prefix = [0] * (len(arr) + 1)
    for i, val in enumerate(arr):
        prefix[i + 1] = prefix[i] + val
    return prefix

def range_sum(prefix: list[int], l: int, r: int) -> int:
    return prefix[r + 1] - prefix[l]
```
**Build**: O(n), **Query**: O(1)

## List vs Other Structures

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Mutable | Yes | No | Yes | Yes |
| Ordered | Yes | Yes | No* | No* |
| Duplicates | Yes | Yes | No | Keys: No |
| Index Access | O(1) | O(1) | No | Keys: O(1) |
| Lookup | O(n) | O(n) | O(1) | O(1) |

*Python 3.7+ preserves insertion order for sets and dicts

## Memory Layout

```
List Object
┌─────────────────┐
│ ob_refcnt       │  Reference count
│ ob_type         │  Type pointer
│ ob_size         │  Number of elements
│ allocated       │  Allocated slots
│ items           │──→ Array of pointers
└─────────────────┘    ┌───┬───┬───┬───┐
                       │ * │ * │ * │...│  Pointers to objects
                       └─┬─┴─┬─┴─┬─┴───┘
                         │   │   │
                         ▼   ▼   ▼
                        [1] [2] [3]  Actual objects
```

## Best Practices

1. **Use list comprehension** for simple transformations
   ```python
   squares = [x**2 for x in range(10)]
   ```

2. **Use extend()** instead of multiple append() calls
   ```python
   lst.extend([1, 2, 3])  # Better than three append() calls
   ```

3. **Preallocate size** if you know it (for performance)
   ```python
   lst = [0] * n  # Creates list of n zeros
   ```

4. **Avoid pop(0)** for queues - use collections.deque
   ```python
   from collections import deque
   queue = deque([1, 2, 3])
   queue.popleft()  # O(1) instead of O(n)
   ```

5. **Use in-place sort** when you don't need original
   ```python
   lst.sort()  # In-place, returns None
   # vs
   new_lst = sorted(lst)  # Creates new list
   ```

## When to Use Arrays/Lists

**Good for:**
- Sequential access patterns
- Known size (mostly)
- Frequent index access
- Ordered data requirements

**Poor for:**
- Frequent insertions at beginning
- Frequent deletions at beginning
- Membership testing (use set instead)
- Key-value lookups (use dict instead)
