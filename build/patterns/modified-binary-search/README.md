# Modified Binary Search Pattern

## When to Use
- **Sorted/rotated arrays** - search with modification
- **Finding boundaries** - first/last occurrence
- **Peak finding** - local maxima
- **Binary search on answer** - minimize/maximize result

## Key Signals
| Signal | Example |
|--------|---------|
| "Sorted array" | Standard binary search |
| "Rotated sorted" | One half always sorted |
| "Find first/last position" | Lower/upper bound |
| "O(log n) required" | Must use binary search |
| "Minimize maximum" | Binary search on answer |

## Template Variants

### 1. Standard Binary Search
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

### 2. Lower Bound (First >= target)
```python
left, right = 0, len(nums)
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left
```

### 3. Rotated Array
```python
if nums[left] <= nums[mid]:  # Left half sorted
    if nums[left] <= target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1
else:  # Right half sorted
    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```

### 4. Binary Search on Answer
```python
left, right = min_possible, max_possible
while left < right:
    mid = left + (right - left) // 2
    if feasible(mid):
        right = mid  # Or left = mid for max
    else:
        left = mid + 1
return left
```

## Complexity
| Variant | Time | Space |
|---------|------|-------|
| Standard | O(log n) | O(1) |
| Rotated | O(log n) | O(1) |
| With duplicates | O(n) worst | O(1) |
| 2D matrix | O(log(m×n)) | O(1) |
| Binary on answer | O(log(range) × check) | O(1) |

## LeetCode Problems

### Basic Binary Search
| # | Problem | Difficulty |
|---|---------|------------|
| [704](https://leetcode.com/problems/binary-search/) | Binary Search | Easy |
| [35](https://leetcode.com/problems/search-insert-position/) | Search Insert Position | Easy |
| [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Find First and Last | Medium |

### Rotated Arrays
| # | Problem | Difficulty |
|---|---------|------------|
| [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Search Rotated | Medium |
| [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | Search Rotated II | Medium |
| [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Find Min Rotated | Medium |
| [154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | Find Min II | Hard |

### Peak & Boundaries
| # | Problem | Difficulty |
|---|---------|------------|
| [162](https://leetcode.com/problems/find-peak-element/) | Find Peak Element | Medium |
| [69](https://leetcode.com/problems/sqrtx/) | Sqrt(x) | Easy |
| [367](https://leetcode.com/problems/valid-perfect-square/) | Valid Perfect Square | Easy |

### 2D Matrix
| # | Problem | Difficulty |
|---|---------|------------|
| [74](https://leetcode.com/problems/search-a-2d-matrix/) | Search 2D Matrix | Medium |
| [240](https://leetcode.com/problems/search-a-2d-matrix-ii/) | Search 2D Matrix II | Medium |

### Binary Search on Answer
| # | Problem | Difficulty |
|---|---------|------------|
| [410](https://leetcode.com/problems/split-array-largest-sum/) | Split Array Largest Sum | Hard |
| [875](https://leetcode.com/problems/koko-eating-bananas/) | Koko Eating Bananas | Medium |
| [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Ship Packages | Medium |
| [69](https://leetcode.com/problems/sqrtx/) | Sqrt(x) | Easy |

## Common Mistakes
1. **Integer overflow** - Use `mid = left + (right - left) // 2`
2. **Infinite loop** - Check loop condition and pointer updates
3. **Off by one** - `<=` vs `<`, `mid` vs `mid ± 1`
4. **Missing edge cases** - Empty array, single element

## Quick Reference
```python
# Most common template
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Find insertion point (lower bound)
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

## Loop Invariants
| Template | Invariant | Return |
|----------|-----------|--------|
| `left <= right` | Search space includes all | Index or -1 |
| `left < right` | At least 2 elements | left (or right) |
| `left < right - 1` | At least 3 elements | Compare left, right |

## When to Use Which Template
| Need | Template |
|------|----------|
| Find exact match | `left <= right` |
| Find first >= | `left < right`, shrink right |
| Find last <= | `left < right`, shrink left |
| Minimize result | Binary on answer |
