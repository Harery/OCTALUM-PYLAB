# Stacks & Queues

Linear data structures with restricted access patterns.

## Stack (LIFO)

Last In, First Out - like a stack of plates.

```python
# Using list
stack: list[int] = []
stack.append(1)   # Push
stack.append(2)
stack.pop()       # Pop -> 2
stack[-1]         # Peek -> 1

# Using collections.deque (more efficient)
from collections import deque
stack: deque[int] = deque()
stack.append(1)
stack.append(2)
stack.pop()       # -> 2
```

### Stack Implementation

```python
class Stack:
    def __init__(self):
        self._items: list[int] = []

    def push(self, item: int) -> None:
        self._items.append(item)

    def pop(self) -> int | None:
        return self._items.pop() if self._items else None

    def peek(self) -> int | None:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0
```

### Common Stack Problems

- Valid Parentheses
- Evaluate Expression
- Next Greater Element
- Min Stack

## Queue (FIFO)

First In, First Out - like a line at a store.

```python
from collections import deque

queue: deque[int] = deque()
queue.append(1)   # Enqueue
queue.append(2)
queue.popleft()   # Dequeue -> 1
queue[0]          # Peek -> 2
```

### Queue Implementation

```python
from collections import deque

class Queue:
    def __init__(self):
        self._items: deque[int] = deque()

    def enqueue(self, item: int) -> None:
        self._items.append(item)

    def dequeue(self) -> int | None:
        return self._items.popleft() if self._items else None

    def peek(self) -> int | None:
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0
```

## Priority Queue

```python
import heapq

# Min heap (default)
pq: list[int] = []
heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)
heapq.heappop(pq)  # -> 1 (smallest)

# Max heap (negate values)
max_pq: list[int] = []
heapq.heappush(max_pq, -3)
heapq.heappush(max_pq, -1)
-heapq.heappop(max_pq)  # -> 3 (largest)
```

## Deque (Double-Ended Queue)

```python
from collections import deque

d: deque[int] = deque()
d.append(1)       # Add to right
d.appendleft(0)   # Add to left
d.pop()           # Remove from right
d.popleft()       # Remove from left
```

## Time Complexity

| Operation | Stack | Queue | Deque |
|-----------|-------|-------|-------|
| Push/Enqueue | O(1) | O(1) | O(1) |
| Pop/Dequeue | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(n) |

## When to Use

- **Stack**: Undo operations, expression evaluation, DFS
- **Queue**: BFS, task scheduling, buffer
- **Deque**: Sliding window problems

## Practice Files

- `build/data-structures/05-stacks-queues/stack.py`
- `build/data-structures/05-stacks-queues/queue.py`
- `build/data-structures/05-stacks-queues/deque_demo.py`

## Next Topic

Continue to [Trees](trees.md).
