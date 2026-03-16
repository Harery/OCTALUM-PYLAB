# Trees

Hierarchical data structures with root, branches, and leaves.

## Overview

```
        1 (root)
       / \
      2   3
     / \   \
    4   5   6
   (leaves)
```

## Binary Tree

```python
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
```

## Tree Traversals

### Depth-First (DFS)

```python
def inorder(root: TreeNode | None) -> list[int]:
    """Left -> Root -> Right"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root: TreeNode | None) -> list[int]:
    """Root -> Left -> Right"""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root: TreeNode | None) -> list[int]:
    """Left -> Right -> Root"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Breadth-First (BFS)

```python
from collections import deque

def level_order(root: TreeNode | None) -> list[list[int]]:
    """Level by level traversal"""
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

## Binary Search Tree (BST)

Left subtree < root < Right subtree

```python
def search(root: TreeNode | None, target: int) -> TreeNode | None:
    if not root or root.val == target:
        return root
    if target < root.val:
        return search(root.left, target)
    return search(root.right, target)

def insert(root: TreeNode | None, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
```

## Common Operations

### Height

```python
def height(root: TreeNode | None) -> int:
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
```

### Is Balanced

```python
def is_balanced(root: TreeNode | None) -> bool:
    def check(node: TreeNode | None) -> int:
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1
```

### Lowest Common Ancestor

```python
def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root.val > p.val and root.val > q.val:
        return lca(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return lca(root.right, p, q)
    return root
```

## Time Complexity

| Operation | BST Average | BST Worst | Balanced |
|-----------|-------------|-----------|----------|
| Search | O(log n) | O(n) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |

## Practice Files

- `build/data-structures/06-trees/binary_tree.py`
- `build/data-structures/06-trees/bst.py`
- `build/data-structures/06-trees/tree_traversals.py`

## Next Topic

Continue to [Graphs](graphs.md).
