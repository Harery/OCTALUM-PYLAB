# Cyclic Sort Pattern

## When to Use
- **Array contains numbers 1 to n** (or 0 to n-1)
- **Finding missing/duplicate numbers** in range
- **In-place sorting** with O(1) space constraint
- **Problems with "array of n integers from 1 to n"**

## Key Signals
| Signal | Example |
|--------|---------|
| "Array of n numbers from 1 to n" | Classic cyclic sort |
| "Find missing number" | Place each number at its index |
| "Find duplicate" | Collision when placing |
| "Find all missing/duplicates" | Scan after placement |
| "First missing positive" | Ignore out-of-range values |

## Template Variants

### 1. Basic Cyclic Sort (1 to n)
```python
i = 0
while i < len(nums):
    correct = nums[i] - 1  # 1-indexed
    if nums[i] != nums[correct]:
        nums[i], nums[correct] = nums[correct], nums[i]
    else:
        i += 1
```

### 2. Find Missing Number
```python
# After sorting, find where index != value
for i in range(n):
    if nums[i] != i + 1:
        return i + 1
return n + 1
```

### 3. Find Duplicate
```python
# After sorting, duplicate is at wrong position
for i in range(n):
    if nums[i] != i + 1:
        return nums[i]
```

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Cyclic sort | O(n) | O(1) |
| Find missing | O(n) | O(1) |
| Find duplicate | O(n) | O(1) |
| First missing positive | O(n) | O(1) |

## LeetCode Problems

| # | Problem | Difficulty | Variant |
|---|---------|------------|---------|
| [268](https://leetcode.com/problems/missing-number/) | Missing Number | Easy | 0 to n |
| [448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Find All Disappeared | Easy | Multiple missing |
| [287](https://leetcode.com/problems/find-the-duplicate-number/) | Find Duplicate | Medium | Floyd's or cyclic |
| [442](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Find All Duplicates | Medium | Multiple dupes |
| [645](https://leetcode.com/problems/set-mismatch/) | Set Mismatch | Easy | Missing + duplicate |
| [41](https://leetcode.com/problems/first-missing-positive/) | First Missing Positive | Hard | Ignore negatives |
| [765](https://leetcode.com/problems/couples-holding-hands/) | Couples Holding Hands | Hard | Cyclic sort variant |

## Common Mistakes
1. **Wrong index calculation** - Use `nums[i] - 1` for 1-indexed, `nums[i]` for 0-indexed
2. **Infinite loop** - Only increment `i` when not swapping
3. **Ignoring bounds** - Check if value is within valid range before placing
4. **Modifying when shouldn't** - For some problems, use XOR or math instead

## Quick Reference
```python
# Core pattern: place value v at index v-1
def cyclic_sort_core(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

# After sorting, mismatched positions reveal missing/duplicates
for i in range(len(nums)):
    if nums[i] != i + 1:
        # i+1 is missing, nums[i] is duplicate
```

## Index Mapping
| Range | Correct Index for value v |
|-------|---------------------------|
| 1 to n | `v - 1` |
| 0 to n-1 | `v` |
| Any range [a, b] | `v - a` |

## Alternative for Duplicate Without Modification
When array must not be modified, use Floyd's cycle detection:
```python
slow = fast = nums[0]
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
# Find cycle start (duplicate)
```
