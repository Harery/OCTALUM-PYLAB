# Pattern Reference

Quick reference for common coding patterns.

## 1. Sliding Window

**Use when:** Contiguous subarray/substring problems

```python
def max_sum_subarray(arr: list[int], k: int) -> int:
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

**Problems:** Max sum subarray, Longest substring, Min window

## 2. Two Pointers

**Use when:** Sorted array, finding pairs

```python
def two_sum(arr: list[int], target: int) -> tuple[int, int]:
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

**Problems:** Two sum, 3Sum, Container with most water

## 3. Fast & Slow Pointers

**Use when:** Cycle detection, find middle

```python
def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Problems:** Cycle detection, Find middle, Happy number

## 4. Merge Intervals

**Use when:** Overlapping intervals

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)

    return result
```

**Problems:** Merge intervals, Insert interval, Meeting rooms

## 5. Cyclic Sort

**Use when:** Array contains 1 to n

```python
def cyclic_sort(arr: list[int]) -> list[int]:
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    return arr
```

**Problems:** Missing number, Duplicate number, First missing positive

## 6. Tree BFS

**Use when:** Level-by-level traversal

```python
from collections import deque

def level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

**Problems:** Level order, Right side view, Zigzag traversal

## 7. Tree DFS

**Use when:** Path problems, depth

```python
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Problems:** Max depth, Path sum, Diameter of tree

## 8. Subsets

**Use when:** All combinations

```python
def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result
```

**Problems:** Subsets, Permutations, Combinations

## 9. Modified Binary Search

**Use when:** Rotated array, bounded search

```python
def search_rotated(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

**Problems:** Search rotated array, Find minimum, Peak element

## Pattern Recognition

| Keywords | Pattern |
|----------|---------|
| "subarray", "contiguous" | Sliding Window |
| "sorted", "pair" | Two Pointers |
| "cycle", "loop" | Fast & Slow |
| "intervals", "merge" | Merge Intervals |
| "1 to n", "missing" | Cyclic Sort |
| "level", "width" | Tree BFS |
| "path", "depth" | Tree DFS |
| "all combinations" | Subsets |
| "rotated", "bound" | Modified Binary |
