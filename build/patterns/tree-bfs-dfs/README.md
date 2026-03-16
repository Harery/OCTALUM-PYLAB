# Tree BFS & DFS Pattern

## When to Use
- **Binary tree traversal** - inorder, preorder, postorder
- **Level-based operations** - level order, zigzag, right view
- **Path problems** - sum, existence, all paths
- **Tree properties** - depth, balance, symmetry

## Key Signals
| Signal | Example |
|--------|---------|
| "Level order" | BFS with level grouping |
| "Inorder/preorder/postorder" | DFS with specific order |
| "Path from root to leaf" | DFS with path tracking |
| "Nodes visible from right" | BFS, take last of each level |
| "Maximum/minimum depth" | Recursive DFS |

## Template Variants

### 1. DFS Recursive (Inorder)
```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    process(node.val)
    inorder(node.right)
```

### 2. BFS Level Order
```python
def level_order(root):
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
```

### 3. Path with Backtracking
```python
def dfs(node, path, target):
    path.append(node.val)
    if is_leaf and sum(path) == target:
        result.append(path[:])
    dfs(node.left, path, target)
    dfs(node.right, path, target)
    path.pop()  # Backtrack
```

## Traversal Orders
| Order | Sequence | Use Case |
|-------|----------|----------|
| Preorder | Root → Left → Right | Copy tree, prefix expr |
| Inorder | Left → Root → Right | BST sorted order |
| Postorder | Left → Right → Root | Delete tree, postfix expr |
| Level | Level by level | Shortest path, level ops |

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Any traversal | O(n) | O(h) DFS / O(w) BFS |
| Max depth | O(n) | O(h) |
| Path sum | O(n) | O(h) |
| LCA (BST) | O(h) | O(1) iterative |

h = height, w = max width, n = nodes

## LeetCode Problems

### Basic Traversals
| # | Problem | Difficulty |
|---|---------|------------|
| [94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Inorder Traversal | Easy |
| [144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Preorder Traversal | Easy |
| [145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Postorder Traversal | Easy |
| [102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Level Order | Medium |

### Level-Based
| # | Problem | Difficulty |
|---|---------|------------|
| [103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Zigzag Level Order | Medium |
| [199](https://leetcode.com/problems/binary-tree-right-side-view/) | Right Side View | Medium |
| [107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | Level Order II | Medium |

### Path Problems
| # | Problem | Difficulty |
|---|---------|------------|
| [112](https://leetcode.com/problems/path-sum/) | Path Sum | Easy |
| [113](https://leetcode.com/problems/path-sum-ii/) | Path Sum II | Medium |
| [124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Max Path Sum | Hard |
| [257](https://leetcode.com/problems/binary-tree-paths/) | Binary Tree Paths | Easy |

### Properties
| # | Problem | Difficulty |
|---|---------|------------|
| [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Max Depth | Easy |
| [111](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Min Depth | Easy |
| [110](https://leetcode.com/problems/balanced-binary-tree/) | Balanced Tree | Easy |
| [100](https://leetcode.com/problems/same-tree/) | Same Tree | Easy |
| [101](https://leetcode.com/problems/symmetric-tree/) | Symmetric Tree | Easy |
| [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | LCA | Medium |

## Common Mistakes
1. **Not handling None** - Always check for null nodes
2. **Mutable default args** - Don't use `[]` as default
3. **Forgetting backtrack** - Pop from path after recursion
4. **Wrong level tracking** - Capture `len(queue)` before iterating

## Quick Reference
```python
# DFS - any order
def dfs(node):
    if not node: return
    # preorder: process here
    dfs(node.left)
    # inorder: process here
    dfs(node.right)
    # postorder: process here

# BFS - level by level
def bfs(root):
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            # process node
            for child in [node.left, node.right]:
                if child: queue.append(child)
```

## DFS vs BFS Decision
| Use DFS | Use BFS |
|---------|---------|
| Path to leaf | Level operations |
| Tree depth | Shortest path |
| Backtracking | Right/left view |
| Recursive natural | Iterative natural |
