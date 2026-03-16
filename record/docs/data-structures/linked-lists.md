# Linked Lists

Linked lists store elements in nodes connected by pointers.

## Overview

Each node contains data and a reference to the next node.

```python
class Node:
    """Singly linked list node."""
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    """Singly linked list."""
    def __init__(self):
        self.head: Node | None = None

    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
```

## Types

### Singly Linked List

```
[A] -> [B] -> [C] -> None
```

### Doubly Linked List

```
None <- [A] <-> [B] <-> [C] -> None
```

### Circular Linked List

```
[A] -> [B] -> [C] -> [A] (back to head)
```

## Common Operations

### Reverse

```python
def reverse(head: Node | None) -> Node | None:
    """Reverse a linked list."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

### Detect Cycle

```python
def has_cycle(head: Node | None) -> bool:
    """Detect cycle using Floyd's algorithm."""
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

### Find Middle

```python
def find_middle(head: Node | None) -> Node | None:
    """Find middle node using slow/fast pointers."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### Merge Two Sorted Lists

```python
def merge_sorted(l1: Node | None, l2: Node | None) -> Node | None:
    """Merge two sorted linked lists."""
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

## Time Complexity

| Operation | Time |
|-----------|------|
| Access by index | O(n) |
| Search | O(n) |
| Insert at head | O(1) |
| Insert at tail | O(n) |
| Delete at head | O(1) |
| Delete by value | O(n) |

## When to Use

- Need O(1) insertions/deletions at known positions
- Don't need random access
- Memory is fragmented
- Size changes frequently

## Practice Files

- `build/data-structures/04-linked-lists/singly_linked.py`
- `build/data-structures/04-linked-lists/doubly_linked.py`
- `build/data-structures/04-linked-lists/circular_linked.py`

## Next Topic

Continue to [Stacks & Queues](stacks-queues.md).
