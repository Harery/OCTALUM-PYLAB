"""
Tree BFS & DFS Pattern

Use when: Binary tree, n-ary tree traversal, level-order operations
DFS: O(n) time, O(h) space (h = height)
BFS: O(n) time, O(w) space (w = max width)
"""

from typing import List, Optional, Deque
from collections import deque
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


# ============================================================
# TEMPLATE 1: DFS - Recursive Traversals
# ============================================================

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Left -> Root -> Right. Time: O(n), Space: O(h)"""
    result = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Root -> Left -> Right. Time: O(n), Space: O(h)"""
    result = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Left -> Right -> Root. Time: O(n), Space: O(h)"""
    result = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


# ============================================================
# TEMPLATE 2: DFS - Iterative (with Stack)
# ============================================================

def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative inorder using stack."""
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Iterative preorder using stack."""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# ============================================================
# TEMPLATE 3: BFS - Level Order Traversal
# ============================================================

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level by level traversal.
    Time: O(n), Space: O(w) where w = max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


def level_order_values(root: Optional[TreeNode]) -> List[int]:
    """Simple BFS without level grouping."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# ============================================================
# TEMPLATE 4: Zigzag Level Order
# ============================================================

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Zigzag traversal (alternate directions).
    Time: O(n), Space: O(w)
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right

    return result


# ============================================================
# TEMPLATE 5: Right/Left Side View
# ============================================================

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    Nodes visible from right side.
    Time: O(n), Space: O(w)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:  # Last node in level
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# ============================================================
# TEMPLATE 6: Tree Depth and Properties
# ============================================================

def max_depth(root: Optional[TreeNode]) -> int:
    """Maximum depth of tree. Time: O(n), Space: O(h)"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root: Optional[TreeNode]) -> int:
    """Minimum depth to leaf. Time: O(n), Space: O(h)"""
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Check if tree is height-balanced. Time: O(n)"""
    def check(node: Optional[TreeNode]) -> int:
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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Check if two trees are identical. Time: O(n)"""
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


# ============================================================
# TEMPLATE 7: Path Problems
# ============================================================

def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """Check if root-to-leaf path sums to target."""
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))


def path_sum_all(root: Optional[TreeNode], target: int) -> List[List[int]]:
    """Find all root-to-leaf paths summing to target."""
    result = []

    def dfs(node: Optional[TreeNode], path: List[int], remaining: int) -> None:
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])
        else:
            dfs(node.left, path, remaining - node.val)
            dfs(node.right, path, remaining - node.val)

        path.pop()

    dfs(root, [], target)
    return result


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    Maximum path sum (path can start/end anywhere).
    Time: O(n), Space: O(h)
    """
    max_sum = float('-inf')

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        max_sum = max(max_sum, node.val + left_gain + right_gain)

        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum


# ============================================================
# TEMPLATE 8: Lowest Common Ancestor
# ============================================================

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA of two nodes in BST.
    Time: O(h), Space: O(h)
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return root


def lca_binary_tree(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Find LCA in regular binary tree.
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)

    if left and right:
        return root
    return left or right


# ============================================================
# TEMPLATE 9: Serialize/Deserialize
# ============================================================

def serialize(root: Optional[TreeNode]) -> str:
    """Serialize tree to string."""
    result = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            result.append('#')
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ','.join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    """Deserialize string to tree."""
    values = iter(data.split(','))

    def dfs() -> Optional[TreeNode]:
        val = next(values)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


# ============================================================
# Quick Test
# ============================================================
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5, 6, 7])

    print("Inorder:", inorder_traversal(root))
    print("Preorder:", preorder_traversal(root))
    print("Level order:", level_order(root))
    print("Zigzag:", zigzag_level_order(root))
    print("Right view:", right_side_view(root))
    print("Max depth:", max_depth(root))

    root2 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print("Path sum 22:", path_sum_all(root2, 22))
