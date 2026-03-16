# Subsets / Backtracking Pattern

## When to Use
- **Generate all combinations** - subsets, permutations
- **Find all solutions** - with constraints
- **Combinatorial problems** - phone letters, parentheses
- **Partitioning problems** - palindrome, IP addresses

## Key Signals
| Signal | Example |
|--------|---------|
| "All possible subsets/combinations" | Power set |
| "All permutations" | Rearrangements |
| "All valid parentheses" | Balanced constraints |
| "Partition into X" | Backtracking with validation |
| "N-Queens / Sudoku" | Constraint satisfaction |

## Template Variants

### 1. Subsets (Include/Exclude)
```python
def backtrack(start, path):
    result.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()  # Backtrack
```

### 2. Permutations (Used Array)
```python
def backtrack(path, used):
    if len(path) == len(nums):
        result.append(path[:])
        return
    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True
        path.append(nums[i])
        backtrack(path, used)
        path.pop()
        used[i] = False
```

### 3. Combinations (Choose K)
```python
def backtrack(start, path):
    if len(path) == k:
        result.append(path[:])
        return
    for i in range(start, n + 1):
        path.append(i)
        backtrack(i + 1, path)
        path.pop()
```

### 4. Skip Duplicates
```python
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue  # Skip duplicates
    # ... rest of logic
```

## Complexity
| Problem | Time | Space |
|---------|------|-------|
| Subsets | O(n × 2^n) | O(n) |
| Permutations | O(n × n!) | O(n) |
| Combinations C(n,k) | O(k × C(n,k)) | O(k) |
| Letter combinations | O(4^n) | O(n) |
| N-Queens | O(n!) | O(n²) |

## LeetCode Problems

### Subsets & Permutations
| # | Problem | Difficulty |
|---|---------|------------|
| [78](https://leetcode.com/problems/subsets/) | Subsets | Medium |
| [90](https://leetcode.com/problems/subsets-ii/) | Subsets II | Medium |
| [46](https://leetcode.com/problems/permutations/) | Permutations | Medium |
| [47](https://leetcode.com/problems/permutations-ii/) | Permutations II | Medium |

### Combinations & Sum
| # | Problem | Difficulty |
|---|---------|------------|
| [77](https://leetcode.com/problems/combinations/) | Combinations | Medium |
| [39](https://leetcode.com/problems/combination-sum/) | Combination Sum | Medium |
| [40](https://leetcode.com/problems/combination-sum-ii/) | Combination Sum II | Medium |
| [216](https://leetcode.com/problems/combination-sum-iii/) | Combination Sum III | Medium |

### Strings
| # | Problem | Difficulty |
|---|---------|------------|
| [17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Letter Combinations | Medium |
| [22](https://leetcode.com/problems/generate-parentheses/) | Generate Parentheses | Medium |
| [131](https://leetcode.com/problems/palindrome-partitioning/) | Palindrome Partitioning | Medium |
| [79](https://leetcode.com/problems/word-search/) | Word Search | Medium |

### Constraint Satisfaction
| # | Problem | Difficulty |
|---|---------|------------|
| [51](https://leetcode.com/problems/n-queens/) | N-Queens | Hard |
| [37](https://leetcode.com/problems/sudoku-solver/) | Sudoku Solver | Hard |

## Common Mistakes
1. **Forgetting to backtrack** - Must pop/remove after recursion
2. **Not copying path** - Use `path[:]` not `path` reference
3. **Wrong duplicate handling** - Sort first, then skip
4. **Inefficient base case** - Check early to prune

## Quick Reference
```python
# Standard backtracking template
def backtrack(start, path, *args):
    if is_complete(path):
        result.append(path[:])
        return

    for i in range(start, n):
        if should_skip(i, path):
            continue

        path.append(choice[i])
        backtrack(next_start, path, *args)
        path.pop()  # BACKTRACK!

# Handle duplicates
nums.sort()  # Always sort first for duplicate handling
if i > start and nums[i] == nums[i-1]:
    continue  # Skip duplicate at same level
```

## Pruning Strategies
| Strategy | When to Use |
|----------|-------------|
| Early return | When remaining < 0 in sum |
| Sort + skip duplicates | When input has duplicates |
| Constraint check | N-Queens, Sudoku validity |
| Memoization | Repeated subproblems |

## Count Before Generating
- Subsets of n elements: 2^n
- Permutations of n: n!
- Combinations C(n,k): n! / (k!(n-k)!)
