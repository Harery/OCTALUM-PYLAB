# Arrays & Lists

Arrays and lists are sequential collections that store elements in order.

## Overview

Arrays store elements contiguously in memory, providing O(1) access by index.

## Python Lists

Python lists are dynamic arrays that grow/shrink automatically.

```python
# Creation
arr: list[int] = [1, 2, 3, 4, 5]

# Access
first = arr[0]    # 1
last = arr[-1]    # 5

# Modify
arr[0] = 10       # [10, 2, 3, 4, 5]
arr.append(6)     # [10, 2, 3, 4, 5, 6]
arr.insert(0, 0)  # [0, 10, 2, 3, 4, 5, 6]
arr.pop()         # Removes 6
arr.remove(10)    # Removes first 10

# Slicing
sub = arr[1:4]    # Elements at index 1, 2, 3
rev = arr[::-1]   # Reversed copy
```

## Common Operations

### Two Pointers

```python
def reverse_array(arr: list[int]) -> list[int]:
    """Reverse array in-place using two pointers."""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

### Sliding Window

```python
def max_subarray_sum(arr: list[int], k: int) -> int:
    """Find max sum of subarray of size k."""
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Prefix Sum

```python
def prefix_sum(arr: list[int]) -> list[int]:
    """Build prefix sum array for range queries."""
    prefix = [0] * (len(arr) + 1)
    for i, num in enumerate(arr):
        prefix[i + 1] = prefix[i] + num
    return prefix

# Range sum from i to j: prefix[j + 1] - prefix[i]
```

## Time Complexity

| Operation | Time |
|-----------|------|
| Access by index | O(1) |
| Search | O(n) |
| Insert at end | O(1) amortized |
| Insert at start | O(n) |
| Delete | O(n) |
| Update | O(1) |

## Common Interview Problems

- Two Sum
- Best Time to Buy/Sell Stock
- Contains Duplicate
- Product of Array Except Self
- Maximum Subarray

## Practice Files

- `build/data-structures/01-arrays-lists/array_basics.py`
- `build/data-structures/01-arrays-lists/array_operations.py`
- `build/challenges/leetcode-easy/0001_two_sum.py`

## Next Topic

Continue to [Strings](strings.md).
