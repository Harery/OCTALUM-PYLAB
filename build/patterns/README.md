# Problem-Solving Patterns Overview

Master these 12 patterns to solve most coding interview problems.

## Quick Reference

| Pattern | When to Use | Time | Key Problems |
|---------|-------------|------|--------------|
| [Two Pointers](./two-pointers/) | Sorted arrays, pairs, palindrome | O(n) | Two Sum, 3Sum, Container |
| [Sliding Window](./sliding-window/) | Subarrays, contiguous sequences | O(n) | Longest Substring, Min Window |
| [Fast/Slow Pointers](./fast-slow-pointers/) | Linked list, cycle detection | O(n) | Cycle, Middle, Happy Number |
| [Merge Intervals](./merge-intervals/) | Overlapping ranges, meetings | O(n log n) | Merge, Meeting Rooms |
| [Cyclic Sort](./cyclic-sort/) | Numbers 1 to n, missing/duplicate | O(n) | Missing Number, First Missing |
| [Island/Matrix](./island-matrix/) | 2D grid, connected components | O(m×n) | Islands, Flood Fill |
| [Tree BFS/DFS](./tree-bfs-dfs/) | Binary tree traversal | O(n) | Level Order, Path Sum |
| [Two Heaps](./two-heaps/) | Median, scheduling, max/min | O(log n) | Median Finder, IPO |
| [Subsets](./subsets/) | Combinations, permutations | O(2^n) or O(n!) | Subsets, Permutations |
| [Modified Binary Search](./modified-binary-search/) | Rotated arrays, boundaries | O(log n) | Search Rotated, Peak |
| [Top K Elements](./top-k-elements/) | K largest/smallest/frequent | O(n log k) | Kth Largest, Top Frequent |

## Pattern Selection Guide

### By Input Type

| Input Type | Patterns to Consider |
|------------|---------------------|
| Array (sorted) | Two Pointers, Binary Search |
| Array (unsorted) | Sliding Window, Cyclic Sort, Heap |
| String | Two Pointers, Sliding Window |
| Linked List | Fast/Slow Pointers |
| Tree | BFS/DFS |
| Matrix/Grid | Island Pattern (DFS/BFS) |
| Intervals | Merge Intervals |
| Numbers 1-n | Cyclic Sort |

### By Problem Type

| Problem Type | Patterns to Consider |
|--------------|---------------------|
| Find pair/triplet | Two Pointers |
| Find subarray | Sliding Window |
| Detect cycle | Fast/Slow Pointers |
| Generate all | Subsets/Backtracking |
| Find K elements | Top K Elements (Heap) |
| Search sorted | Binary Search |
| Overlap/merge | Merge Intervals |
| Connected regions | Island Pattern |

### By Time Constraint

| Required Time | Suitable Patterns |
|---------------|-------------------|
| O(log n) | Binary Search |
| O(n) | Two Pointers, Sliding Window, Fast/Slow, Cyclic Sort, DFS/BFS |
| O(n log n) | Merge Intervals, Heap operations |
| O(n²) | Nested loops (avoid if possible) |
| O(2^n) | Subsets (small n only) |

## Pattern Combinations

Many problems combine multiple patterns:

| Combination | Example Problem |
|-------------|-----------------|
| Two Pointers + Sorting | 3Sum |
| Sliding Window + Hash Map | Longest Substring |
| Binary Search + Greedy | Split Array |
| DFS + Backtracking | Word Search |
| Heap + Greedy | Task Scheduler |
| BFS + Queue | Shortest Path in Grid |

## Difficulty Distribution

| Pattern | Easy | Medium | Hard |
|---------|------|--------|------|
| Two Pointers | 3 | 4 | 1 |
| Sliding Window | 1 | 5 | 1 |
| Fast/Slow Pointers | 3 | 2 | 0 |
| Merge Intervals | 1 | 5 | 1 |
| Cyclic Sort | 2 | 3 | 1 |
| Island/Matrix | 1 | 6 | 1 |
| Tree BFS/DFS | 6 | 4 | 1 |
| Two Heaps | 0 | 3 | 3 |
| Subsets | 0 | 6 | 2 |
| Binary Search | 3 | 5 | 2 |
| Top K Elements | 1 | 6 | 1 |

## Study Order (Recommended)

1. **Two Pointers** - Foundation for many patterns
2. **Sliding Window** - Extension of two pointers
3. **Fast/Slow Pointers** - Linked list basics
4. **Binary Search** - Essential for sorted data
5. **Tree BFS/DFS** - Fundamental tree operations
6. **Island/Matrix** - Grid traversal
7. **Merge Intervals** - Range problems
8. **Cyclic Sort** - Array manipulation
9. **Subsets** - Combinatorics
10. **Top K Elements** - Heap usage
11. **Two Heaps** - Advanced heap patterns

## Common Mistakes to Avoid

1. **Wrong pattern selection** - Analyze problem before coding
2. **Edge cases** - Empty input, single element, duplicates
3. **Off-by-one errors** - Check loop bounds carefully
4. **Time limit** - Verify complexity before implementing
5. **Space limit** - Consider in-place solutions

## Quick Templates

```python
# Two Pointers
left, right = 0, len(nums) - 1
while left < right:
    if condition(nums[left], nums[right]):
        # process
    left += 1 or right -= 1

# Sliding Window
left = 0
for right in range(len(nums)):
    # expand
    while invalid:
        # shrink from left
        left += 1

# Binary Search
left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: left = mid + 1
    else: right = mid - 1

# DFS (Tree)
def dfs(node):
    if not node: return
    # process
    dfs(node.left)
    dfs(node.right)

# BFS (Tree)
queue = deque([root])
while queue:
    node = queue.popleft()
    # process
    for child in children:
        queue.append(child)

# Backtracking
def backtrack(path, choices):
    if done: result.append(path[:])
    for choice in choices:
        path.append(choice)
        backtrack(path, next_choices)
        path.pop()
```

## Resources

- Each pattern folder contains:
  - `pattern.py` - Working template code
  - `README.md` - Explanation and LeetCode links
- `learn/cheatsheets/` - Quick reference materials
