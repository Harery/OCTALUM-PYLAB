# Trees

## Overview

Trees are hierarchical data structures consisting of nodes connected by edges. Each tree has a root node, and every node can have child nodes. Trees are used to represent hierarchical relationships.

## Tree Types

| Type | Property | Use Case |
|------|----------|----------|
| **Binary Tree** | Each node has ≤2 children | Expression trees |
| **Binary Search Tree** | left < root < right | Searching, sorting |
| **Heap** | Complete binary tree with ordering | Priority queues |
| **Trie** | Prefix tree | Autocomplete, dictionary |
| **AVL Tree** | Self-balancing BST | Guaranteed O(log n) |
| **B-Tree** | Multi-way balanced | Databases, filesystems |

## Time Complexity

### Binary Tree Operations

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| **Insert** | O(log n) | O(n) | Depends on balance |
| **Search** | O(log n) | O(n) | Depends on balance |
| **Delete** | O(log n) | O(n) | Depends on balance |
| **Traversal** | O(n) | O(n) | Visit all nodes |
| **Height** | O(n) | O(n) | Recursive |

### BST Operations

| Operation | Average | Worst |
|-----------|---------|-------|
| **Insert** | O(log n) | O(n) |
| **Search** | O(log n) | O(n) |
| **Delete** | O(log n) | O(n) |
| **Min/Max** | O(log n) | O(n) |
| **Successor** | O(log n) | O(n) |

### Heap Operations

| Operation | Time | Notes |
|-----------|------|-------|
| **Insert** | O(log n) | Heapify up |
| **Extract** | O(log n) | Heapify down |
| **Peek** | O(1) | Root element |
| **Build** | O(n) | From array |

### Trie Operations

| Operation | Time | Notes |
|-----------|------|-------|
| **Insert** | O(m) | m = word length |
| **Search** | O(m) | m = word length |
| **Delete** | O(m) | m = word length |
| **StartsWith** | O(m) | m = prefix length |

## Tree Traversals

### Inorder (Left, Root, Right)
```
    4
   / \
  2   6
 / \ / \
1  3 5  7

Inorder: [1, 2, 3, 4, 5, 6, 7]
```
- Used for BST to get sorted order
- Left → Node → Right

### Preorder (Root, Left, Right)
```
Preorder: [4, 2, 1, 3, 6, 5, 7]
```
- Used for tree serialization
- Node → Left → Right

### Postorder (Left, Right, Root)
```
Postorder: [1, 3, 2, 5, 7, 6, 4]
```
- Used for tree deletion
- Left → Right → Node

### Level Order (BFS)
```
Level Order: [[4], [2, 6], [1, 3, 5, 7]]
```
- Level by level traversal
- Uses queue

## Tree Properties

```
Height = max distance from root to leaf
Depth = distance from root to node
Size = total number of nodes
Leaves = nodes with no children
```

### Height Calculation
```python
def height(node):
    if not node:
        return -1
    return 1 + max(height(node.left), height(node.right))
```

### Size Calculation
```python
def size(node):
    if not node:
        return 0
    return 1 + size(node.left) + size(node.right)
```

## Binary Heap Structure

```
Min-Heap:           Max-Heap:
      1                 9
     / \               / \
    3   2             7   8
   / \               / \
  7  4  5           5   6

Array: [1, 3, 2, 7, 4, 5]
Parent(i) = (i-1) // 2
Left(i)   = 2*i + 1
Right(i)  = 2*i + 2
```

## Trie Structure

```
Words: "app", "apple", "apt"

      (root)
       |
       a
       |
       p
      / \
     p   t
     |   |
     *   *
    / \
   l   *
   |
   e
   |
   (*)

* = end of word marker
```

## Common Tree Algorithms

### Lowest Common Ancestor
```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left or right
```

### Tree Diameter
```python
def diameter(root):
    max_diam = [0]
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        max_diam[0] = max(max_diam[0], left + right)
        return 1 + max(left, right)
    height(root)
    return max_diam[0]
```

### Check Balanced
```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check(root) != -1
```

## BST Properties

- Left subtree: all values < root
- Right subtree: all values > root
- Inorder traversal gives sorted sequence
- Min value: leftmost node
- Max value: rightmost node

## Best Practices

1. **Use recursion** for tree traversals (cleaner code)
   ```python
   def inorder(node, result):
       if node:
           inorder(node.left, result)
           result.append(node.value)
           inorder(node.right, result)
   ```

2. **Use iteration** when depth might cause stack overflow
   ```python
   def inorder_iterative(root):
       result, stack, current = [], [], root
       while current or stack:
           while current:
               stack.append(current)
               current = current.left
           current = stack.pop()
           result.append(current.value)
           current = current.right
       return result
   ```

3. **Use level-order (BFS)** for level-by-level processing
   ```python
   from collections import deque
   def bfs(root):
       if not root:
           return []
       result, queue = [], deque([root])
       while queue:
           node = queue.popleft()
           result.append(node.value)
           if node.left:
               queue.append(node.left)
           if node.right:
               queue.append(node.right)
       return result
   ```

4. **Consider self-balancing trees** when order matters (AVL, Red-Black)

5. **Use tries** for string prefix operations

## When to Use Trees

### Binary Search Tree
- Need sorted data with fast insert/delete
- Range queries
- Finding successor/predecessor

### Heap
- Priority queue
- K-th largest/smallest
- Merging sorted lists

### Trie
- Autocomplete
- Spell checker
- IP routing tables
- Dictionary implementation

### General Tree
- File system hierarchy
- Organization charts
- DOM structure
- Decision trees
