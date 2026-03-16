# Two Pointers Pattern

## When to Use
- **Sorted arrays** - looking for pairs/triplets with sum conditions
- **Palindrome problems** - comparing from both ends
- **In-place array modifications** - moving/removing elements
- **Container/water problems** - area calculations
- **Merging sorted arrays** - comparing elements from two sources

## Key Signals
| Signal | Example |
|--------|---------|
| "Find pair with sum X" | Sorted array + target sum |
| "Remove/move elements in-place" | O(1) space constraint |
| "Palindrome/valid string" | Compare characters from both ends |
| "Container/trap water" | Area between boundaries |

## Template Variants

### 1. Opposite Direction (Start → ← End)
```python
left, right = 0, len(nums) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

### 2. Same Direction (Fast/Slow)
```python
write = 0  # slow pointer
for read in range(len(nums)):  # fast pointer
    if condition:
        nums[write] = nums[read]
        write += 1
```

### 3. Two Arrays
```python
i, j = 0, 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
```

## Complexity
| Variant | Time | Space |
|---------|------|-------|
| Opposite direction | O(n) | O(1) |
| Same direction | O(n) | O(1) |
| Two arrays | O(n + m) | O(1) |
| Three sum (sorted) | O(n²) | O(1)* |

*excluding output space

## LeetCode Problems

| # | Problem | Difficulty | Pattern |
|---|---------|------------|---------|
| [125](https://leetcode.com/problems/valid-palindrome/) | Valid Palindrome | Easy | Opposite |
| [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Sum II | Easy | Opposite |
| [283](https://leetcode.com/problems/move-zeroes/) | Move Zeroes | Easy | Same direction |
| [26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Remove Duplicates | Easy | Same direction |
| [11](https://leetcode.com/problems/container-with-most-water/) | Container With Most Water | Medium | Opposite |
| [15](https://leetcode.com/problems/3sum/) | 3Sum | Medium | Triple pointers |
| [42](https://leetcode.com/problems/trapping-rain-water/) | Trapping Rain Water | Hard | Opposite |
| [16](https://leetcode.com/problems/3sum-closest/) | 3Sum Closest | Medium | Triple pointers |

## Common Mistakes
1. **Forgetting to sort** - Two sum requires sorted array
2. **Wrong pointer movement** - Move smaller height in container, not both
3. **Off-by-one errors** - Use `while left < right` not `<=`
4. **Duplicate handling** - Skip duplicates in three sum variants

## Quick Reference
```python
# Standard two pointers
left, right = 0, len(arr) - 1
while left < right:
    # process
    if nums[left] + nums[right] == target:
        return [left, right]
    elif nums[left] + nums[right] < target:
        left += 1
    else:
        right -= 1
```
