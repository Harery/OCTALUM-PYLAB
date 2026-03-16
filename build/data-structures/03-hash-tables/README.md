# Hash Tables

## Overview

Hash tables (dictionaries in Python) provide O(1) average-case performance for insertions, deletions, and lookups. They use a hash function to map keys to array indices.

## Time Complexity Table

### Dictionary Operations

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| **Get/Access** | O(1) | O(n) | Worst case: all keys hash to same bucket |
| **Insert/Set** | O(1) | O(n) | May trigger resize |
| **Delete** | O(1) | O(n) | - |
| **Contains (in)** | O(1) | O(n) | - |
| **Len** | O(1) | O(1) | Stored as attribute |
| **Keys/Values/Items** | O(1) | O(1) | Returns view object |
| **Copy** | O(n) | O(n) | Shallow copy |
| **Clear** | O(1) | O(1) | - |

### Set Operations

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| **Add** | O(1) | O(n) | - |
| **Remove/Discard** | O(1) | O(n) | - |
| **Contains (in)** | O(1) | O(n) | - |
| **Union (|)** | O(len(s)+len(t)) | - | - |
| **Intersection (&)** | O(min(len(s), len(t))) | - | - |
| **Difference (-)** | O(len(s)) | - | - |
| **Symmetric Diff (^)** | O(len(s)+len(t)) | - | - |
| **Subset (<=)** | O(len(s)) | - | - |

## Space Complexity

| Structure | Space | Notes |
|-----------|-------|-------|
| **Dictionary** | O(n) | Plus overhead for hash table |
| **Set** | O(n) | Same as dictionary (keys only) |
| **Load Factor** | n/capacity | Typically 0.66-0.75 threshold |

## Hash Function

A good hash function should:
1. **Deterministic**: Same input always gives same output
2. **Uniform distribution**: Keys spread evenly across buckets
3. **Fast to compute**: O(1) ideally

```python
def simple_hash(key: str, size: int) -> int:
    return sum(ord(c) for c in key) % size
```

## Collision Resolution

### Chaining (Used by Python)
- Each bucket contains a linked list of entries
- Collisions append to the list
- Simple but requires extra memory

```
Bucket 0: [(key1, val1)]
Bucket 1: [(key2, val2)] -> [(key3, val3)] -> [(key4, val4)]
Bucket 2: [(key5, val5)]
```

### Open Addressing
- Find next empty slot on collision
- Probing strategies:
  - Linear: i+1, i+2, i+3...
  - Quadratic: i+1², i+2², i+3²...
  - Double hashing: i + h2(k)

## Dictionary vs Set vs List

| Feature | Dict | Set | List |
|---------|------|-----|------|
| Key-Value | Yes | No | No |
| Unique Keys | Yes | Yes | No |
| Ordered* | Yes | No | Yes |
| Mutable | Yes | Yes | Yes |
| Hashable | No | No | Yes |
| Lookup | O(1) | O(1) | O(n) |

*Python 3.7+ preserves insertion order for dicts

## Common Patterns

### Counting
```python
counts: dict[str, int] = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

### Grouping
```python
groups: dict[int, list[str]] = {}
for item in items:
    key = get_key(item)
    groups.setdefault(key, []).append(item)
```

### Caching (Memoization)
```python
cache: dict[int, int] = {}
def fib(n: int) -> int:
    if n in cache:
        return cache[n]
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result
```

### Two Sum (Hash Table)
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

## Set Theory Operations

| Operation | Python | Mathematical | Result |
|-----------|--------|--------------|--------|
| Union | `a | b` | A ∪ B | Elements in A or B |
| Intersection | `a & b` | A ∩ B | Elements in both |
| Difference | `a - b` | A \ B | In A, not in B |
| Symmetric Diff | `a ^ b` | A △ B | In A or B, not both |
| Subset | `a <= b` | A ⊆ B | All of A in B |
| Proper Subset | `a < b` | A ⊂ B | A ⊆ B and A ≠ B |
| Superset | `a >= b` | A ⊇ B | All of B in A |
| Disjoint | `a.isdisjoint(b)` | A ∩ B = ∅ | No common elements |

## Venn Diagram Representation

```
    ┌─────────┬─────────┐
    │    A    │  A ∩ B  │
    │  A \ B  │         │
    ├─────────┼─────────┤
    │  B \ A  │    B    │
    │         │         │
    └─────────┴─────────┘

A | B = A ∪ B (union)
A & B = A ∩ B (intersection)
A - B = A \ B (difference)
A ^ B = A △ B (symmetric difference)
```

## Load Factor and Resizing

- **Load Factor** = n / capacity (filled slots / total slots)
- Python resizes when load factor > 2/3
- Resize doubles the capacity
- All entries must be rehashed

## Best Practices

1. **Use dict for key-value storage**
   ```python
   user = {"name": "Alice", "age": 30}
   ```

2. **Use set for uniqueness**
   ```python
   unique_items = set(items)
   ```

3. **Use get() for safe access**
   ```python
   value = d.get(key, default)
   ```

4. **Use setdefault for initialization**
   ```python
   d.setdefault(key, []).append(value)
   ```

5. **Use comprehension for transformation**
   ```python
   squares = {x: x**2 for x in range(10)}
   ```

## When to Use Hash Tables

**Good for:**
- Fast lookups by key
- Removing duplicates
- Counting occurrences
- Caching/memoization
- Set operations

**Poor for:**
- Ordered data (use list or OrderedDict)
- Range queries (use tree)
- Memory-constrained (overhead)
- Unknown key types (must be hashable)

## Hashable Types

**Hashable (can be dict keys):**
- int, float, str, bytes
- tuple (if all elements hashable)
- frozenset
- None, bool

**Not Hashable:**
- list, dict, set
- bytearray
- Custom classes (unless __hash__ defined)
