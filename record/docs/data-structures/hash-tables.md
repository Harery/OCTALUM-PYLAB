# Hash Tables

Hash tables provide O(1) average-time access using key-value pairs.

## Overview

Python dictionaries are hash tables with automatic resizing.

```python
# Creation
hash_table: dict[str, int] = {"apple": 1, "banana": 2}

# Access
value = hash_table["apple"]       # 1
value = hash_table.get("cherry", 0)  # 0 (default)

# Modify
hash_table["cherry"] = 3          # Add/update
del hash_table["apple"]           # Delete
hash_table.pop("banana", None)    # Pop with default

# Iterate
for key, value in hash_table.items():
    print(f"{key}: {value}")
```

## Hash Collision Handling

Python uses open addressing with probing.

```python
# Two keys with same hash (rare, but possible)
class BadKey:
    def __hash__(self):
        return 1  # All instances collide

    def __eq__(self, other):
        return isinstance(other, BadKey)
```

## Common Use Cases

### Frequency Counter

```python
from collections import Counter

def char_frequency(s: str) -> dict[str, int]:
    """Count character occurrences."""
    return dict(Counter(s))

# Or manually
def char_frequency_manual(s: str) -> dict[str, int]:
    freq: dict[str, int] = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
```

### Two Sum Problem

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Find indices of two numbers that add to target."""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Group Anagrams

```python
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams."""
    groups: dict[str, list[str]] = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
```

## DefaultDict & Counter

```python
from collections import defaultdict, Counter

# defaultdict - auto-creates missing keys
word_count: defaultdict[str, int] = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1

# Counter - specialized frequency dict
counts = Counter(["a", "b", "a", "c", "b", "a"])
counts.most_common(2)  # [("a", 3), ("b", 2)]
```

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Access | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |

## Practice Files

- `build/data-structures/03-hash-tables/hash_basics.py`
- `build/data-structures/03-hash-tables/collision_handling.py`
- `build/challenges/leetcode-easy/0001_two_sum.py`

## Next Topic

Continue to [Linked Lists](linked-lists.md).
