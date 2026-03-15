# Python Tips & Tricks for Interviews

Quick reference for Python features useful in coding interviews.

## One-Liners

### String Manipulation

```python
# Reverse a string
s_reversed = s[::-1]

# Check palindrome
is_palindrome = s == s[::-1]

# Check if alphanumeric
is_alnum = s.isalnum()

# Split and strip
words = s.strip().split()

# Join with separator
result = "-".join(words)

# Count character frequency
from collections import Counter
freq = Counter(s)
```

### List Operations

```python
# Reverse list in place
arr.reverse()

# Get reversed copy
reversed_arr = arr[::-1]

# Remove duplicates (loses order)
unique = list(set(arr))

# Remove duplicates (preserves order)
unique = list(dict.fromkeys(arr))

# Flatten 2D list
flat = [item for row in matrix for item in row]

# Transpose matrix
transposed = list(zip(*matrix))

# Get indices of sorted elements
indices = sorted(range(len(arr)), key=arr.__getitem__)

# Chunk list into size n
chunks = [arr[i:i+n] for i in range(0, len(arr), n)]
```

### Dictionary Operations

```python
# Default value
d.get(key, default)

# Set default
d.setdefault(key, default)

# Get or create
value = d[key] = d.get(key, default)

# Invert dictionary
inverted = {v: k for k, v in d.items()}

# Merge dictionaries (3.9+)
merged = d1 | d2

# Counter from list
from collections import Counter
c = Counter(arr)
most_common = c.most_common(3)
```

---

## Collections Module

### defaultdict

```python
from collections import defaultdict

# Auto-initialize values
d = defaultdict(list)
d[key].append(value)  # No KeyError

d = defaultdict(int)
d[key] += 1  # For counting

d = defaultdict(set)
d[key].add(value)
```

### Counter

```python
from collections import Counter

# Count elements
c = Counter(['a', 'b', 'a', 'c', 'a'])

# Most common
c.most_common(2)  # [('a', 3), ('b', 1)]

# Operations
c1 + c2   # Addition
c1 - c2   # Subtraction (keeps positive)
c1 & c2   # Intersection (min)
c1 | c2   # Union (max)
```

### deque

```python
from collections import deque

# O(1) operations on both ends
d = deque([1, 2, 3])
d.append(4)        # Right
d.appendleft(0)    # Left
d.pop()            # Right
d.popleft()        # Left

# Rotation
d.rotate(1)        # Right rotate
d.rotate(-1)       # Left rotate

# Max length (auto pop)
d = deque(maxlen=5)
```

### namedtuple

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2
```

---

## itertools Module

### infinite iterators

```python
from itertools import count, cycle, repeat

# Count forever
for i in count(10, 2):  # 10, 12, 14, ...
    if i > 20: break

# Cycle through
for item in cycle([1, 2, 3]):  # 1, 2, 3, 1, 2, 3, ...
    pass

# Repeat
for item in repeat(10, 3):  # 10, 10, 10
    pass
```

### Terminating iterators

```python
from itertools import accumulate, chain, compress

# Accumulate (prefix sums)
list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]

# Chain (flatten)
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# Compress (filter by boolean)
list(compress('ABCDEF', [1, 0, 1, 0, 1, 1]))  # ['A', 'C', 'E', 'F']
```

### Combinatoric iterators

```python
from itertools import product, permutations, combinations

# Cartesian product
list(product([1, 2], [3, 4]))  # [(1,3), (1,4), (2,3), (2,4)]

# Permutations (order matters)
list(permutations([1, 2, 3], 2))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# Combinations (order doesn't matter)
list(combinations([1, 2, 3, 4], 2))  # [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# Combinations with replacement
from itertools import combinations_with_replacement
```

---

## heapq Module

```python
import heapq

# Min heap
heap = []
heapq.heappush(heap, item)
smallest = heapq.heappop(heap)
peek = heap[0]  # Don't pop

# Heapify existing list
heapq.heapify(arr)

# Get n smallest/largest
heapq.nsmallest(3, arr)
heapq.nlargest(3, arr)

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -item)
largest = -heapq.heappop(max_heap)

# Merge sorted iterators
merged = heapq.merge(sorted1, sorted2)
```

---

## bisect Module

```python
import bisect

# Binary search in sorted list
arr = [1, 3, 3, 3, 5, 7]

# Find insertion point
bisect.bisect_left(arr, 3)   # 1 (leftmost)
bisect.bisect_right(arr, 3)  # 4 (rightmost)
bisect.bisect(arr, 3)        # 4 (alias for right)

# Insert maintaining order
bisect.insort(arr, 4)  # arr is now [1, 3, 3, 3, 4, 5, 7]

# Check if exists
index = bisect.bisect_left(arr, x)
exists = index < len(arr) and arr[index] == x
```

---

## functools Module

```python
from functools import lru_cache, reduce, partial

# Memoization
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# Reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24

# Partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
square(5)  # 25

# Compare for sorting
from functools import cmp_to_key
sorted_arr = sorted(arr, key=cmp_to_key(compare_function))
```

---

## Context Managers

```python
# Timer context
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")

with timer():
    # code to time
    pass
```

---

## Common Patterns

### Matrix Directions

```python
# 4-directional
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 8-directional
DIRS8 = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]

# Use
for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        # valid neighbor
```

### Grid BFS Template

```python
from collections import deque

def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set([start])

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc))
```

### Trie Template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
```

---

## Quick Reference

### Sorting with Key

```python
# Sort by second element
arr.sort(key=lambda x: x[1])

# Sort by multiple keys
arr.sort(key=lambda x: (x[0], -x[1]))

# Sort in reverse
arr.sort(reverse=True)

# Stable sort
arr = sorted(arr, key=lambda x: x[0])
```

### String Formatting

```python
# f-strings
f"{name}: {score:.2f}"

# Format with padding
f"{num:05d}"     # 00042
f"{num:+05d}"    # +0042
f"{num:.2f}"     # 42.00
f"{num:>10}"     # right align
f"{num:<10}"     # left align
f"{num:^10}"     # center align
```

---

*Master these and you'll write cleaner, faster interview code!*
