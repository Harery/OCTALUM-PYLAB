# Big-O Reference

Quick reference for algorithm complexity analysis.

## Complexity Classes

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

## Common Complexities

### O(1) - Constant

```python
def first_element(arr: list[int]) -> int:
    return arr[0]  # Always one operation
```

### O(log n) - Logarithmic

```python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # Halves search space each iteration
```

### O(n) - Linear

```python
def find_max(arr: list[int]) -> int:
    max_val = arr[0]
    for num in arr:  # One pass through array
        max_val = max(max_val, num)
    return max_val
```

### O(n log n) - Linearithmic

```python
def merge_sort(arr: list[int]) -> list[int]:
    # Divide: O(log n) levels
    # Merge: O(n) work per level
    # Total: O(n log n)
```

### O(n²) - Quadratic

```python
def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):  # Nested loops
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

## Data Structure Operations

| Operation | Array | Linked List | Hash Table | BST | Heap |
|-----------|-------|-------------|------------|-----|------|
| Access | O(1) | O(n) | O(1)* | O(log n) | O(1) |
| Search | O(n) | O(n) | O(1)* | O(log n) | O(n) |
| Insert | O(n) | O(1) | O(1)* | O(log n) | O(log n) |
| Delete | O(n) | O(1) | O(1)* | O(log n) | O(log n) |

*Average case

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

## Space Complexity

| Code Pattern | Space |
|--------------|-------|
| Variables | O(1) |
| Fixed array | O(1) |
| Dynamic array | O(n) |
| Recursion depth | O(depth) |
| Hash table | O(n) |

## Common Patterns

| Pattern | Time | Space |
|---------|------|-------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) or O(k) |
| Binary Search | O(log n) | O(1) |
| DFS (recursive) | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |
| DP (tabulation) | O(states) | O(states) |

## Amortized Analysis

| Operation | Amortized | Reason |
|-----------|-----------|--------|
| ArrayList.append() | O(1) | Doubling spreads cost |
| HashMap.put() | O(1) | Resize spreads cost |

## Rules of Thumb

1. **Drop constants**: O(2n) → O(n)
2. **Drop lower terms**: O(n² + n) → O(n²)
3. **Different inputs**: O(a + b) not O(n + n)
4. **Nested vs sequential**: Nested multiplies, sequential adds

## Quick Estimation

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
|---|------|----------|------|------------|-------|
| 10 | 1 | 3 | 10 | 33 | 100 |
| 100 | 1 | 7 | 100 | 664 | 10,000 |
| 1,000 | 1 | 10 | 1,000 | 9,966 | 1M |
| 1M | 1 | 20 | 1M | 20M | 1T |

## Practice

- Always state complexity before coding
- Consider both time AND space
- Worst case matters for interviews
- Amortized for dynamic structures
