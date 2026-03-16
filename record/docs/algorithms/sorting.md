# Sorting Algorithms

Order elements efficiently based on criteria.

## Comparison Sorts

### Bubble Sort

Time: O(n²) | Space: O(1)

```python
def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Selection Sort

Time: O(n²) | Space: O(1)

```python
def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### Insertion Sort

Time: O(n²) | Space: O(1)

```python
def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### Merge Sort

Time: O(n log n) | Space: O(n)

```python
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
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
```

### Quick Sort

Time: O(n log n) avg | Space: O(log n)

```python
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

## Non-Comparison Sorts

### Counting Sort

Time: O(n + k) | Space: O(k)

```python
def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)

    return result
```

### Radix Sort

Time: O(d * (n + k)) | Space: O(n + k)

```python
def radix_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr
```

## Complexity Comparison

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) |
| Selection | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion | O(n) | O(n²) | O(n²) | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Counting | O(n + k) | O(n + k) | O(n + k) | O(k) |

## Python Built-in

```python
# Timsort (hybrid merge + insertion)
sorted_arr = sorted(arr)           # New list
arr.sort()                         # In-place

# Custom key
sorted(words, key=len)             # By length
sorted(words, key=lambda x: x[1])  # By second char

# Reverse
sorted(arr, reverse=True)
```

## Practice Files

- `build/algorithms/02-sorting/bubble_sort.py`
- `build/algorithms/02-sorting/merge_sort.py`
- `build/algorithms/02-sorting/quick_sort.py`

## Next Topic

Continue to [Recursion](recursion.md).
