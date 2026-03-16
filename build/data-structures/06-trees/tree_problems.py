"""
Tree Problems Module
====================
Common tree problems and solutions for interview preparation.

Problems included:
- max_depth: Find maximum depth of binary tree
- invert_tree: Mirror/invert a binary tree
- is_same_tree: Check if two trees are identical
- has_path_sum: Check if root-to-leaf path equals target sum
- lowest_common_ancestor: Find LCA of two nodes

Time Complexity: O(n) for all problems (visit each node once)
Space Complexity: O(h) for recursive solutions (h = height)
"""

from __future__ import annotations


class TreeNode:
    """Binary tree node for problems."""

    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def max_depth(root: TreeNode | None) -> int:
    """
    Find the maximum depth of a binary tree.

    Args:
        root: Root node of the tree

    Returns:
        Maximum depth (0 for empty tree, 1 for single node)

    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> max_depth(root)
        2
    """
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """
    Invert/mirror a binary tree.

    Args:
        root: Root node of the tree

    Returns:
        Root of the inverted tree

    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> inverted = invert_tree(root)
        >>> inverted.left.val  # Was 2, now 3
        3
    """
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Check if two binary trees are identical.

    Args:
        p: Root of first tree
        q: Root of second tree

    Returns:
        True if trees are identical, False otherwise

    Time Complexity: O(min(n, m)) where n, m are sizes
    Space Complexity: O(min(h1, h2))

    Example:
        >>> t1 = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> t2 = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> is_same_tree(t1, t2)
        True
    """
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    """
    Check if there exists a root-to-leaf path with given sum.

    Args:
        root: Root node of the tree
        target_sum: Target sum to find

    Returns:
        True if such path exists, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Example:
        >>> root = TreeNode(5, TreeNode(4, TreeNode(11)), TreeNode(8))
        >>> has_path_sum(root, 20)  # 5 + 4 + 11 = 20
        True
    """
    if root is None:
        return False

    if root.left is None and root.right is None:
        return root.val == target_sum

    remaining = target_sum - root.val

    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    Find the lowest common ancestor of two nodes in a binary tree.

    Args:
        root: Root node of the tree
        p: First node
        q: Second node

    Returns:
        The lowest common ancestor node, or None if not found

    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Example:
        >>> root = TreeNode(3, TreeNode(5), TreeNode(1))
        >>> lca = lowest_common_ancestor(root, root.left, root.right)
        >>> lca.val
        3
    """
    if root is None:
        return None

    if root is p or root is q:
        return root

    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)

    if left_lca is not None and right_lca is not None:
        return root

    return left_lca if left_lca is not None else right_lca


def is_balanced(root: TreeNode | None) -> bool:
    """
    Check if a binary tree is height-balanced.

    A tree is balanced if the height difference between
    left and right subtrees is at most 1 for every node.

    Args:
        root: Root node of the tree

    Returns:
        True if tree is balanced, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(h)

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> is_balanced(root)
        True
    """
    def check_height(node: TreeNode | None) -> int:
        if node is None:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1


def diameter_of_tree(root: TreeNode | None) -> int:
    """
    Find the diameter of a binary tree.

    The diameter is the length of the longest path between
    any two nodes (may or may not pass through root).

    Args:
        root: Root node of the tree

    Returns:
        Diameter length (number of edges)

    Time Complexity: O(n)
    Space Complexity: O(h)

    Example:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        >>> diameter_of_tree(root)
        3
    """
    max_diameter = 0

    def height(node: TreeNode | None) -> int:
        nonlocal max_diameter
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return max_diameter


def level_order_traversal(root: TreeNode | None) -> list[list[int]]:
    """
    Return level order traversal as list of lists.

    Args:
        root: Root node of the tree

    Returns:
        List of levels, each level is a list of values

    Time Complexity: O(n)
    Space Complexity: O(w) where w is max width

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> level_order_traversal(root)
        [[1], [2, 3]]
    """
    if root is None:
        return []

    from collections import deque

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(level)

    return result


def build_tree_from_array(arr: list[int | None]) -> TreeNode | None:
    """
    Build a binary tree from array representation.

    Args:
        arr: Array where None represents missing nodes

    Returns:
        Root of the constructed tree

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> root = build_tree_from_array([1, 2, 3, None, 4])
        >>> root.val
        1
    """
    if not arr or arr[0] is None:
        return None

    from collections import deque

    root = TreeNode(arr[0])
    queue: deque[TreeNode] = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    print("=== Tree Problems Demo ===\n")

    # Build tree:
    #       1
    #      / \\
    #     2   3
    #    / \\
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Tree structure:")
    print("      1")
    print("     / \\")
    print("    2   3")
    print("   / \\")
    print("  4   5")
    print()

    print(f"Max depth: {max_depth(root)}")
    print(f"Is balanced: {is_balanced(root)}")
    print(f"Diameter: {diameter_of_tree(root)}")
    print(f"Level order: {level_order_traversal(root)}")

    # Test invert
    inverted = invert_tree(build_tree_from_array([1, 2, 3, 4, 5]))
    print(f"\nInverted level order: {level_order_traversal(inverted)}")

    # Test is_same_tree
    t1 = build_tree_from_array([1, 2, 3])
    t2 = build_tree_from_array([1, 2, 3])
    t3 = build_tree_from_array([1, 2, 4])
    print(f"\nSame trees [1,2,3] and [1,2,3]: {is_same_tree(t1, t2)}")
    print(f"Same trees [1,2,3] and [1,2,4]: {is_same_tree(t1, t3)}")

    # Test has_path_sum
    path_tree = build_tree_from_array([5, 4, 8, 11, None, 13, 4])
    print(f"\nPath sum 20 exists: {has_path_sum(path_tree, 20)}")
    print(f"Path sum 26 exists: {has_path_sum(path_tree, 26)}")

    # Test LCA
    lca_root = TreeNode(3)
    lca_root.left = TreeNode(5)
    lca_root.right = TreeNode(1)
    lca_root.left.left = TreeNode(6)
    lca_root.left.right = TreeNode(2)

    lca_result = lowest_common_ancestor(lca_root, lca_root.left, lca_root.right)
    print(f"\nLCA of 5 and 1: {lca_result.val if lca_result else None}")
