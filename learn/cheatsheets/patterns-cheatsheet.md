# Coding Patterns Cheatsheet

Quick reference for recognizing and applying coding patterns.

## Pattern Recognition Guide

| Signal | Pattern |
|--------|---------|
| Sorted array → | Binary Search, Two Pointers |
| Subarray/Substring → | Sliding Window |
| Cycle detection → | Fast & Slow Pointers |
| Overlapping intervals → | Merge Intervals |
| Array in range [1, n] → | Cyclic Sort |
| Matrix traversal → | Island (DFS/BFS) |
| Tree level-by-level → | Tree BFS |
| Tree path problems → | Tree DFS |
| Median/running median → | Two Heaps |
| Permutations/Subsets → | Subsets (Backtracking) |
| Unknown array size → | Modified Binary Search |
| Top K elements → | Top K (Heap) |

---

## 1. Two Pointers

### When to Use
- Sorted array/string
- Need to find pair/triplet
- Palindrome problems
- Container with most water type

### Template

```python
def two_pointers(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Two Sum II | Easy | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| 3Sum | Medium | [LeetCode](https://leetcode.com/problems/3sum/) |
| Container With Most Water | Medium | [LeetCode](https://leetcode.com/problems/container-with-most-water/) |

---

## 2. Sliding Window

### When to Use
- Subarray/substring problems
- Contiguous elements
- "Longest", "Shortest", "Maximum" subarray
- Fixed or variable window size

### Template (Variable Window)

```python
def sliding_window(s: str, k: int) -> int:
    char_count: dict[str, int] = {}
    left = max_length = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        # Shrink window while invalid
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

### Complexity
- **Time:** O(n)
- **Space:** O(k) where k is character set

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Maximum Sum Subarray | Easy | [LeetCode](https://leetcode.com/problems/maximum-subarray/) |
| Longest Substring Without Repeating | Medium | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Minimum Window Substring | Hard | [LeetCode](https://leetcode.com/problems/minimum-window-substring/) |

---

## 3. Fast & Slow Pointers

### When to Use
- Cycle detection
- Find middle of linked list
- Find start of cycle

### Template

```python
def has_cycle(head: ListNode | None) -> bool:
    if not head or not head.next:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Linked List Cycle | Easy | [LeetCode](https://leetcode.com/problems/linked-list-cycle/) |
| Find Middle of Linked List | Easy | [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/) |
| Happy Number | Easy | [LeetCode](https://leetcode.com/problems/happy-number/) |

---

## 4. Merge Intervals

### When to Use
- Overlapping intervals
- Meeting rooms
- Insert/merge intervals

### Template

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
```

### Complexity
- **Time:** O(n log n)
- **Space:** O(n)

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Merge Intervals | Medium | [LeetCode](https://leetcode.com/problems/merge-intervals/) |
| Insert Interval | Medium | [LeetCode](https://leetcode.com/problems/insert-interval/) |
| Meeting Rooms II | Medium | [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) |

---

## 5. Cyclic Sort

### When to Use
- Array elements in range [1, n] or [0, n-1]
- Find missing/duplicate numbers
- In-place sorting required

### Template

```python
def cyclic_sort(arr: list[int]) -> list[int]:
    i = 0
    n = len(arr)

    while i < n:
        correct_pos = arr[i] - 1  # For [1, n] range

        if arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
        else:
            i += 1

    return arr
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Missing Number | Easy | [LeetCode](https://leetcode.com/problems/missing-number/) |
| Find All Duplicates | Medium | [LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/) |
| First Missing Positive | Hard | [LeetCode](https://leetcode.com/problems/first-missing-positive/) |

---

## 6. Island Pattern (Matrix DFS/BFS)

### When to Use
- Count connected components
- Flood fill
- Matrix traversal

### Template (DFS)

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            grid[r][c] != '1'):
            return

        grid[r][c] = '#'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

### Complexity
- **Time:** O(m × n)
- **Space:** O(m × n) recursion stack

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Number of Islands | Medium | [LeetCode](https://leetcode.com/problems/number-of-islands/) |
| Max Area of Island | Medium | [LeetCode](https://leetcode.com/problems/max-area-of-island/) |
| Surrounded Regions | Medium | [LeetCode](https://leetcode.com/problems/surrounded-regions/) |

---

## 7. Two Heaps

### When to Use
- Find median
- Sliding window median
- Schedule tasks

### Template

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negated)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

### Complexity
- **Time:** O(log n) per insertion
- **Space:** O(n)

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Find Median from Data Stream | Hard | [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) |
| Sliding Window Median | Hard | [LeetCode](https://leetcode.com/problems/sliding-window-median/) |

---

## 8. Subsets (Backtracking)

### When to Use
- Generate all permutations/combinations
- Power set
- All possible paths

### Template

```python
def subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

### Complexity
- **Time:** O(2^n)
- **Space:** O(n) recursion

### Practice Problems
| Problem | Difficulty | Link |
|---------|------------|------|
| Subsets | Medium | [LeetCode](https://leetcode.com/problems/subsets/) |
| Permutations | Medium | [LeetCode](https://leetcode.com/problems/permutations/) |
| Combination Sum | Medium | [LeetCode](https://leetcode.com/problems/combination-sum/) |

---

## Quick Reference Card

| Pattern | Key Signal | Time | Space |
|---------|------------|------|-------|
| Two Pointers | Sorted, pair finding | O(n) | O(1) |
| Sliding Window | Subarray, contiguous | O(n) | O(k) |
| Fast/Slow | Cycle, middle | O(n) | O(1) |
| Merge Intervals | Overlapping | O(n log n) | O(n) |
| Cyclic Sort | Range [1,n] | O(n) | O(1) |
| Island | Matrix, connected | O(mn) | O(mn) |
| Two Heaps | Median, balance | O(log n) | O(n) |
| Subsets | Permute/combine | O(2^n) | O(n) |

---

*Memorize the signals. Recognize the pattern. Apply the template.*
