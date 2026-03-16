# Two Heaps Pattern

## When to Use
- **Finding median** - balance two halves of data
- **Sliding window median/max** - maintain heap for window
- **Scheduling with priority** - most frequent/urgent first
- **Resource allocation** - maximize profit with constraints

## Key Signals
| Signal | Example |
|--------|---------|
| "Median of data stream" | Two heaps (max + min) |
| "Maximum profit with constraints" | Max heap for available |
| "K projects with limited capital" | Available vs affordable |
| "Task scheduling with cooldown" | Most frequent first |
| "Minimum refuel stops" | Greedy with max heap |

## Template Variants

### 1. Two Heaps for Median
```python
max_heap = []  # Smaller half (negated for max behavior)
min_heap = []  # Larger half

# Balance invariant: len(max) == len(min) or len(max) == len(min) + 1
def add(num):
    heapq.heappush(max_heap, -num)
    heapq.heappush(min_heap, -heapq.heappop(max_heap))
    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
```

### 2. Max Heap with Lazy Removal
```python
max_heap = [(-value, index) for ...]
while max_heap and max_heap[0][1] < valid_start:
    heapq.heappop(max_heap)  # Remove stale entries
```

### 3. Multi-heap Scheduling
```python
available = list(range(n))  # Available resources
busy = []  # (end_time, resource)
while busy and busy[0][0] <= current_time:
    _, resource = heapq.heappop(busy)
    heapq.heappush(available, resource)
```

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Add to heap | O(log n) | O(n) |
| Get median | O(1) | - |
| K operations | O(k log n) | O(n) |

## Python Heap Notes
- `heapq` is min-heap only
- For max-heap: negate values (`-value`)
- Heapify existing list: `heapq.heapify(lst)`
- Push: `heapq.heappush(heap, item)`
- Pop: `heapq.heappop(heap)`
- Push + Pop: `heapq.heappushpop(heap, item)`
- N largest/smallest: `heapq.nlargest(n, iterable)`

## LeetCode Problems

| # | Problem | Difficulty | Key Insight |
|---|---------|------------|-------------|
| [295](https://leetcode.com/problems/find-median-from-data-stream/) | Median from Data Stream | Hard | Two heaps |
| [480](https://leetcode.com/problems/sliding-window-median/) | Sliding Window Median | Hard | Two heaps + lazy delete |
| [502](https://leetcode.com/problems/ipo/) | IPO | Hard | Min + Max heap |
| [239](https://leetcode.com/problems/sliding-window-maximum/) | Sliding Window Max | Hard | Max heap / Deque |
| [378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Kth Smallest in Matrix | Medium | Min heap |
| [621](https://leetcode.com/problems/task-scheduler/) | Task Scheduler | Medium | Max heap + cooldown |
| [871](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | Min Refuel Stops | Hard | Max heap greedy |
| [253](https://leetcode.com/problems/meeting-rooms-ii/) | Meeting Rooms II | Medium | Min heap for end times |
| [2402](https://leetcode.com/problems/meeting-rooms-iii/) | Meeting Rooms III | Hard | Two heaps |

## Common Mistakes
1. **Wrong heap type** - Python only has min-heap, negate for max
2. **Lazy removal needed** - Don't remove immediately, mark for deletion
3. **Balance invariant** - Keep heaps balanced for median
4. **Overflow in math** - Use long for large sums

## Quick Reference
```python
import heapq

# Min heap
min_h = [3, 1, 2]
heapq.heapify(min_h)
heapq.heappush(min_h, 0)
smallest = heapq.heappop(min_h)  # 0

# Max heap (negate values)
max_h = [-3, -1, -2]
heapq.heapify(max_h)
heapq.heappush(max_h, -5)
largest = -heapq.heappop(max_h)  # 5

# Two heaps for median
class MedianFinder:
    def __init__(self):
        self.lo = []  # max heap (negated)
        self.hi = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

## Decision: When to Use Two Heaps
- Need to track both min and max of changing set
- Need to balance two halves (median)
- Need to choose from available vs pending items
