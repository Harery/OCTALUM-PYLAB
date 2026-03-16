# Linked Lists

## Overview

Linked lists are linear data structures where elements are stored in nodes. Each node contains data and a reference (pointer) to the next node. Unlike arrays, elements are not stored in contiguous memory locations.

## Types of Linked Lists

| Type | Structure | Use Case |
|------|-----------|----------|
| **Singly** | Node → Next | Simple forward traversal |
| **Doubly** | Node ↔ Next/Prev | Bidirectional traversal |
| **Circular** | Last → First | Round-robin scheduling |

## Time Complexity Comparison

### Singly Linked List

| Operation | Time | Notes |
|-----------|------|-------|
| **Access by index** | O(n) | Must traverse from head |
| **Search** | O(n) | Linear search |
| **Insert at head** | O(1) | Just update head pointer |
| **Insert at tail** | O(n)* | O(1) with tail pointer |
| **Insert at position** | O(n) | Must find position |
| **Delete at head** | O(1) | Just update head pointer |
| **Delete at tail** | O(n) | Must find second-to-last |
| **Delete at position** | O(n) | Must find position |
| **Reverse** | O(n) | Single pass |
| **Detect cycle** | O(n) | Floyd's algorithm |

### Doubly Linked List

| Operation | Time | Notes |
|-----------|------|-------|
| **Access by index** | O(n/2) | Can start from closer end |
| **Search** | O(n) | Linear search |
| **Insert at head** | O(1) | Update head and next's prev |
| **Insert at tail** | O(1) | Update tail and prev's next |
| **Insert at position** | O(n) | Must find position |
| **Delete at head** | O(1) | Update head |
| **Delete at tail** | O(1) | Update tail |
| **Delete at position** | O(n) | Must find position |
| **Reverse** | O(n) | Swap all prev/next |

## Space Complexity

| Type | Space | Notes |
|------|-------|-------|
| **Singly** | O(n) | n nodes + n pointers |
| **Doubly** | O(n) | n nodes + 2n pointers |
| **Extra overhead** | - | Doubly needs ~2x memory |

## Linked List vs Array

| Feature | Linked List | Array |
|---------|-------------|-------|
| **Memory** | Non-contiguous | Contiguous |
| **Access by index** | O(n) | O(1) |
| **Insert at beginning** | O(1) | O(n) |
| **Insert at end** | O(n) / O(1)* | O(1) amortized |
| **Insert in middle** | O(n) | O(n) |
| **Delete at beginning** | O(1) | O(n) |
| **Memory overhead** | High (pointers) | Low |
| **Cache locality** | Poor | Excellent |
| **Size flexibility** | Dynamic | Fixed / Dynamic |

*With tail pointer

## Node Structure

### Singly Linked Node
```
┌──────────────┐
│  Data  │ Next │──→
└──────────────┘
```

### Doubly Linked Node
```
        ┌────────────────────┐
   ←─── │ Prev │ Data │ Next │ ───→
        └────────────────────┘
```

## Common Operations Visualization

### Insert at Head (Singly)
```
Before: Head → [1] → [2] → None
New Node: [0]
After:  Head → [0] → [1] → [2] → None
```

### Delete at Head (Singly)
```
Before: Head → [1] → [2] → [3] → None
After:  Head → [2] → [3] → None
```

### Reverse (Singly)
```
Before: Head → [1] → [2] → [3] → None
After:  Head → [3] → [2] → [1] → None
```

## Key Algorithms

### Floyd's Cycle Detection
```python
def has_cycle(head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```
Time: O(n), Space: O(1)

### Find Middle Element
```python
def get_middle(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```
Time: O(n), Space: O(1)

### Merge Two Sorted Lists
```python
def merge(l1: Node, l2: Node) -> Node:
    dummy = Node(0)
    current = dummy
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
```
Time: O(n+m), Space: O(1)

## When to Use Linked Lists

### Good For
- Frequent insertions/deletions at beginning
- Unknown or highly variable size
- No random access needed
- Implementing stacks/queues
- Hash table collision handling (chaining)

### Poor For
- Random access by index
- Memory-constrained environments
- Cache-sensitive applications
- Binary search operations

## Common Interview Problems

| Problem | Technique | Time |
|---------|-----------|------|
| Reverse list | Two pointers | O(n) |
| Detect cycle | Floyd's algorithm | O(n) |
| Find middle | Fast/slow pointers | O(n) |
| Merge sorted lists | Two pointers | O(n+m) |
| Remove nth from end | Two pointers | O(n) |
| Palindrome check | Reverse half | O(n) |
| Remove duplicates | Hash set | O(n) |
| Sort list | Merge sort | O(n log n) |

## Memory Layout

### Array (Contiguous)
```
Address: 1000  1004  1008  1012  1016
Data:    [ 1  ] [ 2  ] [ 3  ] [ 4  ] [ 5  ]
```

### Linked List (Scattered)
```
Node 1: Addr 1000, Data 1, Next 2050
Node 2: Addr 2050, Data 2, Next 3000
Node 3: Addr 3000, Data 3, Next 1500
Node 4: Addr 1500, Data 4, Next NULL
```

## Best Practices

1. **Always check for None/null** before accessing next
   ```python
   if head and head.next:
       # Safe to access
   ```

2. **Use dummy node** for operations that might change head
   ```python
   dummy = Node(0)
   dummy.next = head
   # ... operations ...
   return dummy.next
   ```

3. **Track previous node** in singly linked list for deletions
   ```python
   prev = None
   current = head
   while current:
       if condition:
           if prev:
               prev.next = current.next
           else:
               head = current.next
       prev = current
       current = current.next
   ```

4. **Use doubly linked** when frequent backward traversal needed

5. **Consider circular** for round-robin scenarios

## Sentinel Nodes

Using dummy/sentinel nodes simplifies edge cases:

```python
class LinkedListWithSentinel:
    def __init__(self):
        self.sentinel = Node(None)  # Dummy node
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
```

Benefits:
- No null checks needed
- Simplifies insertion/deletion logic
- Head and tail always exist
