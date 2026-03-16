# Stacks and Queues

## Overview

Stacks and queues are linear data structures with restricted access patterns. They are fundamental abstract data types used throughout computer science.

## Stack: LIFO (Last In, First Out)

```
    ┌───┐
    │ 3 │ ← TOP (push/pop here)
    ├───┤
    │ 2 │
    ├───┤
    │ 1 │ ← BOTTOM
    └───┘
```

### Stack Operations

| Operation | Time | Description |
|-----------|------|-------------|
| **push(x)** | O(1) | Add element to top |
| **pop()** | O(1) | Remove and return top element |
| **peek()/top()** | O(1) | Return top element without removing |
| **is_empty()** | O(1) | Check if stack is empty |
| **size()** | O(1) | Return number of elements |

## Queue: FIFO (First In, First Out)

```
DEQUEUE ← [ 1 | 2 | 3 | 4 ] ← ENQUEUE
(front)                      (rear)
```

### Queue Operations

| Operation | Time | Description |
|-----------|------|-------------|
| **enqueue(x)** | O(1) | Add element to rear |
| **dequeue()** | O(1) | Remove and return front element |
| **peek()/front()** | O(1) | Return front element without removing |
| **is_empty()** | O(1) | Check if queue is empty |
| **size()** | O(1) | Return number of elements |

## Time Complexity Comparison

### Stack Implementations

| Implementation | Push | Pop | Peek | Space |
|----------------|------|-----|------|-------|
| **Array/List** | O(1)* | O(1) | O(1) | O(n) |
| **Linked List** | O(1) | O(1) | O(1) | O(n) |

*Amortized - may trigger resize

### Queue Implementations

| Implementation | Enqueue | Dequeue | Peek | Space |
|----------------|---------|---------|------|-------|
| **Array (naive)** | O(1) | O(n) | O(1) | O(n) |
| **Linked List** | O(1) | O(1) | O(1) | O(n) |
| **Circular Array** | O(1) | O(1) | O(1) | O(n) |
| **Deque** | O(1) | O(1) | O(1) | O(n) |

## Priority Queue

| Operation | Binary Heap | Sorted Array | Unsorted Array |
|-----------|-------------|--------------|----------------|
| **Insert** | O(log n) | O(n) | O(1) |
| **Extract Min/Max** | O(log n) | O(1) | O(n) |
| **Peek** | O(1) | O(1) | O(n) |
| **Build** | O(n) | O(n log n) | O(n) |

## Stack vs Queue Comparison

| Feature | Stack | Queue |
|---------|-------|-------|
| **Order** | LIFO | FIFO |
| **Access point** | One end (top) | Two ends (front/rear) |
| **Real-world analogy** | Stack of plates | Line at store |
| **Common uses** | Recursion, undo | BFS, scheduling |

## Common Applications

### Stack Applications
- Function call stack (recursion)
- Undo/Redo operations
- Expression evaluation
- Parentheses matching
- Backtracking algorithms
- Browser history
- Syntax parsing

### Queue Applications
- BFS traversal
- Task scheduling
- Print job queue
- Message queues
- Buffering
- CPU scheduling
- IO buffers

## Visualization

### Stack Operations
```
push(1): [1]
push(2): [1, 2]
push(3): [1, 2, 3]
pop():   [1, 2]    → returns 3
peek():  [1, 2]    → returns 2
```

### Queue Operations
```
enqueue(1): [1]
enqueue(2): [1, 2]
enqueue(3): [1, 2, 3]
dequeue():  [2, 3]  → returns 1
peek():     [2, 3]  → returns 2
```

## Circular Queue

A circular queue (ring buffer) reuses empty slots:

```
Initial:     [_, _, _, _, _]
             front=rear=0

After add:   [A, B, C, _, _]
             front=0, rear=2

After wrap:  [D, _, _, B, C]
             front=3, rear=0
```

Benefits:
- Fixed size
- No shifting needed
- O(1) for all operations
- Memory efficient

## Deque (Double-Ended Queue)

Supports operations at both ends:

| Operation | Description |
|-----------|-------------|
| add_front(x) | Add to front |
| add_rear(x) | Add to rear |
| remove_front() | Remove from front |
| remove_rear() | Remove from rear |

## Common Algorithms

### Valid Parentheses (Stack)
```python
def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif not stack or stack.pop() != pairs[c]:
            return False
    return not stack
```
Time: O(n), Space: O(n)

### Next Greater Element (Stack)
```python
def next_greater(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result
```
Time: O(n), Space: O(n)

### Sliding Window Maximum (Deque)
```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    from collections import deque
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```
Time: O(n), Space: O(k)

## Heap Structure

Binary heap visualization:
```
        1
       / \
      3   2
     / \  / \
    7  4 5  6

Array: [1, 3, 2, 7, 4, 5, 6]
Parent(i) = (i-1) // 2
Left(i)   = 2*i + 1
Right(i)  = 2*i + 2
```

## Best Practices

1. **Use list for stack** - Simple and efficient
   ```python
   stack = []
   stack.append(x)  # push
   stack.pop()      # pop
   ```

2. **Use deque for queue** - Avoid O(n) dequeue
   ```python
   from collections import deque
   q = deque()
   q.append(x)  # enqueue
   q.popleft()  # dequeue
   ```

3. **Use heapq for priority queue**
   ```python
   import heapq
   heap = []
   heapq.heappush(heap, (priority, item))
   heapq.heappop(heap)
   ```

4. **Consider circular queue** for fixed-size buffering

5. **Use MinStack** when you need O(1) minimum queries

## When to Use

### Use Stack When:
- Need LIFO behavior
- Implementing recursion iteratively
- Parsing expressions
- Backtracking

### Use Queue When:
- Need FIFO behavior
- BFS traversal
- Task scheduling
- Producer-consumer patterns

### Use Priority Queue When:
- Need to process by priority
- Dijkstra's algorithm
- Huffman coding
- Event simulation
