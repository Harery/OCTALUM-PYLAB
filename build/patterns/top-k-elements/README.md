# Top K Elements Pattern

## When to Use
- **K largest/smallest elements** - maintain heap of size k
- **K most frequent** - count + heap
- **K closest** - distance-based comparison
- **Top performers** - leaderboards, rankings

## Key Signals
| Signal | Example |
|--------|---------|
| "K largest/smallest" | Min/max heap of size k |
| "Top K frequent" | Counter + heap |
| "K closest to X" | Distance calculation + heap |
| "Kth element" | QuickSelect or heap |
| "K pairs with smallest/largest" | Multi-source merge |

## Template Variants

### 1. K Largest (Min Heap of Size K)
```python
heap = []
for num in nums:
    if len(heap) < k:
        heapq.heappush(heap, num)
    elif num > heap[0]:
        heapq.heapreplace(heap, num)
```

### 2. K Smallest (Max Heap - Negate Values)
```python
heap = []  # Store negatives
for num in nums:
    if len(heap) < k:
        heapq.heappush(heap, -num)
    elif num < -heap[0]:
        heapq.heapreplace(heap, -num)
return [-x for x in heap]
```

### 3. Top K Frequent
```python
count = Counter(nums)
return heapq.nlargest(k, count.keys(), key=count.get)
```

### 4. QuickSelect (Kth Element)
```python
def quickselect(nums, k):
    pivot = random.choice(nums)
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))
```

## Complexity
| Method | Time | Space |
|--------|------|-------|
| Heap (size k) | O(n log k) | O(k) |
| Sort | O(n log n) | O(1) or O(n) |
| QuickSelect | O(n) avg, O(n²) worst | O(1) |

## LeetCode Problems

| # | Problem | Difficulty | Method |
|---|---------|------------|--------|
| [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Kth Largest | Medium | Heap/QuickSelect |
| [347](https://leetcode.com/problems/top-k-frequent-elements/) | Top K Frequent | Medium | Counter + Heap |
| [973](https://leetcode.com/problems/k-closest-points-to-origin/) | K Closest Points | Medium | Heap |
| [451](https://leetcode.com/problems/sort-characters-by-frequency/) | Sort by Frequency | Medium | Counter + Sort |
| [373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | K Smallest Pairs | Medium | Multi-heap |
| [767](https://leetcode.com/problems/reorganize-string/) | Reorganize String | Medium | Max heap |
| [621](https://leetcode.com/problems/task-scheduler/) | Task Scheduler | Medium | Max heap |
| [703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Kth Largest Stream | Easy | Min heap |
| [658](https://leetcode.com/problems/find-k-closest-elements/) | K Closest Elements | Medium | Binary search |
| [692](https://leetcode.com/problems/top-k-frequent-words/) | Top K Frequent Words | Medium | Heap + Trie |

## Common Mistakes
1. **Wrong heap type** - Min heap for k largest, max heap for k smallest
2. **Heap size > k** - Always maintain size k
3. **QuickSelect worst case** - Randomize pivot
4. **Forgetting to negate** - Python has min heap only

## Quick Reference
```python
import heapq
from collections import Counter

# K largest - min heap
heap = []
for num in nums:
    heapq.heappushpop(heap, num) if len(heap) == k else heapq.heappush(heap, num)
    if len(heap) > k: heapq.heappop(heap)

# K smallest - use nlargest on negatives
k_smallest = heapq.nlargest(k, nums, key=lambda x: -x)

# Top K frequent
count = Counter(nums)
top_k = heapq.nlargest(k, count, key=count.get)

# Kth largest using heap
def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
```

## Heap vs Sort vs QuickSelect

| n size | k size | Best Method |
|--------|--------|-------------|
| Small | Any | Sort O(n log n) |
| Large | Small (k << n) | Heap O(n log k) |
| Large | Large (k ≈ n) | Sort O(n log n) |
| Any | Any | QuickSelect O(n) avg |

## Decision Tree
```
Need K elements?
├── K << N → Use heap of size K
├── K ≈ N → Just sort
└── Need only Kth → QuickSelect
```
