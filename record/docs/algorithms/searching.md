# Searching Algorithms

Find elements efficiently in collections.

## Linear Search

Time: O(n) | Space: O(1)

```python
def linear_search(arr: list[int], target: int) -> int:
    """Find target, return index or -1."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

## Binary Search

Time: O(log n) | Space: O(1)

**Prerequisite: Sorted array**

```python
def binary_search(arr: list[int], target: int) -> int:
    """Find target in sorted array."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## Binary Search Variants

### Find First Occurrence

```python
def find_first(arr: list[int], target: int) -> int:
    """Find first occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### Find Last Occurrence

```python
def find_last(arr: list[int], target: int) -> int:
    """Find last occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### Search in Rotated Array

```python
def search_rotated(arr: list[int], target: int) -> int:
    """Search in rotated sorted array."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

## When to Use

| Algorithm | When to Use |
|-----------|-------------|
| Linear Search | Unsorted data, small datasets |
| Binary Search | Sorted data, large datasets |

## Practice Files

- `build/algorithms/01-searching/binary_search.py`
- `build/algorithms/01-searching/interpolation_search.py`
- `build/challenges/leetcode-easy/0704_binary_search.py`

## Next Topic

Continue to [Sorting](sorting.md).
