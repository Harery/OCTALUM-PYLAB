# Data Structures Overview

Master the fundamental data structures used in software development and interviews.

## What You'll Learn

Understanding data structures is crucial for writing efficient code and acing technical interviews.

## Topics

| Topic | Description | Difficulty |
|-------|-------------|------------|
| [Arrays & Lists](arrays-lists.md) | Sequential collections | Easy |
| [Strings](strings.md) | Text manipulation | Easy |
| [Hash Tables](hash-tables.md) | Key-value storage | Easy |
| [Linked Lists](linked-lists.md) | Chain of nodes | Medium |
| [Stacks & Queues](stacks-queues.md) | LIFO and FIFO | Easy |
| [Trees](trees.md) | Hierarchical structures | Medium |
| [Graphs](graphs.md) | Network structures | Medium |

## Complexity Overview

| Operation | Array | Linked List | Hash Table | BST |
|-----------|-------|-------------|------------|-----|
| Access | O(1) | O(n) | O(1) avg | O(log n) |
| Search | O(n) | O(n) | O(1) avg | O(log n) |
| Insert | O(n) | O(1) | O(1) avg | O(log n) |
| Delete | O(n) | O(1) | O(1) avg | O(log n) |

## Practice Files

All implementations are in `build/data-structures/`:

```bash
# Arrays
python build/data-structures/01-arrays-lists/array_basics.py

# Linked Lists
python build/data-structures/04-linked-lists/singly_linked.py

# Trees
python build/data-structures/06-trees/binary_tree.py
```

## Learning Path

1. Start with [Arrays & Lists](arrays-lists.md) - the foundation
2. Progress to [Strings](strings.md) and [Hash Tables](hash-tables.md)
3. Master [Linked Lists](linked-lists.md) - common interview topic
4. Understand [Stacks & Queues](stacks-queues.md)
5. Dive into [Trees](trees.md) - essential for advanced problems
6. Explore [Graphs](graphs.md) - powerful modeling tool

## Interview Tips

- Know time/space complexity for all operations
- Practice implementing from scratch
- Understand when to use each structure
- Be able to explain trade-offs
