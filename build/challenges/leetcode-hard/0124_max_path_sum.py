#!/usr/bin/env python3
"""
LeetCode Hard #124: Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes has an edge connecting them. Find the maximum path sum.

The path does not need to pass through the root.

Example 1:
    Input: root = [1,2,3]
    Output: 6 (path: 2 -> 1 -> 3)

Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""

from __future__ import annotations


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode | None) -> int:
    """
    Find maximum path sum using DFS.

    For each node, calculate:
    1. Maximum path sum through this node (can be global max)
    2. Maximum path sum that can be extended upward to parent

    Args:
        root: Root of binary tree

    Returns:
        Maximum path sum
    """
    max_sum = float("-inf")

    def max_gain(node: TreeNode | None) -> int:
        """Return max path sum starting from node going downward."""
        nonlocal max_sum

        if not node:
            return 0

        # Max gain from left and right subtrees (ignore negative paths)
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Max path sum with current node as "peak" of the path
        current_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)

        # Return max gain if continuing this path upward
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return int(max_sum)


def build_tree(values: list[int | None], index: int = 0) -> TreeNode | None:
    """Build tree from level-order list."""
    if index >= len(values) or values[index] is None:
        return None

    node = TreeNode(values[index])  # type: ignore
    node.left = build_tree(values, 2 * index + 1)
    node.right = build_tree(values, 2 * index + 2)
    return node


def test() -> None:
    """Test cases for max path sum."""
    # Test case 1: [1,2,3]
    root1 = build_tree([1, 2, 3])
    assert max_path_sum(root1) == 6

    # Test case 2: [-10,9,20,None,None,15,7]
    root2 = build_tree([-10, 9, 20, None, None, 15, 7])
    assert max_path_sum(root2) == 42  # 15 -> 20 -> 7

    # Test case 3: Single node
    root3 = TreeNode(-3)
    assert max_path_sum(root3) == -3

    print("All tests passed!")


if __name__ == "__main__":
    test()
