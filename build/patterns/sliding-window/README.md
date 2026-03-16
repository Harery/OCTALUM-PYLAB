# Sliding Window Pattern

## When to Use
- **Contiguous subarray/substring problems** - must be consecutive elements
- **Finding minimum/maximum length** - with some constraint
- **Problems with "window" or "range"** - explicit size constraints
- **String matching patterns** - anagrams, character counts
- **Running calculations** - sum, average over segments

## Key Signals
| Signal | Example |
|--------|---------|
| "Subarray of size K" | Fixed window |
| "Longest/shortest subarray with property X" | Variable window |
| "At most K distinct/unique" | Counter-based shrinking |
| "Contains all characters" | Min window substring |
| "Exactly K" | Use atMost(K) - atMost(K-1) |

## Template Variants

### 1. Fixed Size Window
```python
window_sum = sum(nums[:k])
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]  # Slide
```

### 2. Variable Size (Shrink from Left)
```python
left = 0
for right in range(len(nums)):
    # Expand: add nums[right]
    while invalid_condition:
        # Shrink: remove nums[left]
        left += 1
```

### 3. Counter-Based (Anagrams/Characters)
```python
need = Counter(target)
have = defaultdict(int)
for right, char in enumerate(s):
    have[char] += 1
    # Check if have == need or formed == required
```

## Complexity
| Type | Time | Space |
|------|------|-------|
| Fixed size | O(n) | O(1) |
| Variable shrink | O(n)* | O(k) |
| Counter-based | O(n) | O(charset) |

*Each element added and removed at most once

## LeetCode Problems

### Fixed Window
| # | Problem | Difficulty |
|---|---------|------------|
| [643](https://leetcode.com/problems/maximum-average-subarray-i/) | Maximum Average Subarray I | Easy |
| [1343](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Subarrays of Size K | Medium |

### Variable Window
| # | Problem | Difficulty |
|---|---------|------------|
| [209](https://leetcode.com/problems/minimum-size-subarray-sum/) | Minimum Size Subarray Sum | Medium |
| [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating | Medium |
| [424](https://leetcode.com/problems/longest-repeating-character-replacement/) | Longest Repeating Character Replacement | Medium |
| [438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Find All Anagrams | Medium |
| [567](https://leetcode.com/problems/permutation-in-string/) | Permutation in String | Medium |
| [76](https://leetcode.com/problems/minimum-window-substring/) | Minimum Window Substring | Hard |
| [992](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Subarrays with K Different Integers | Hard |

## Common Mistakes
1. **Off-by-one in window size** - Window size = `right - left + 1`
2. **Not handling empty input** - Check edge cases
3. **Wrong shrink condition** - Should shrink while invalid, not if
4. **Counter comparison** - Use `formed` counter for efficiency

## Quick Reference
```python
# Generic sliding window
def sliding_window(nums, condition):
    left = 0
    state = initial_state()

    for right in range(len(nums)):
        # Expand window
        add_to_state(state, nums[right])

        # Shrink while invalid
        while not condition(state):
            remove_from_state(state, nums[left])
            left += 1

        # Update answer
        update_result(right - left + 1)

    return result
```

## Decision Tree
```
Is window size fixed?
├── Yes → Use fixed template with sum += new - old
└── No → Variable window
    ├── Need min length? → Shrink when condition met
    ├── Need max length? → Shrink when invalid
    └── Count matches? → Counter + compare
```
