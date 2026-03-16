#!/usr/bin/env python3
"""
LeetCode Hard #297: Serialize and Deserialize Binary Tree

Design an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting a data structure into a
sequence of bits. Deserialization reconstructs the data structure.

Example:
    Input: root = [1,2,3,null,null,4,5]
    Serialize: "1,2,3,null,null,4,5,null,null,null,null"
    Deserialize: Back to original tree

Time Complexity: O(n) for both operations
Space Complexity: O(n)
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


class Codec:
    """Serializer/Deserializer for binary trees."""

    def serialize(self, root: TreeNode | None) -> str:
        """Encode a tree to a single string."""
        result: list[str] = []

        def dfs(node: TreeNode | None) -> None:
            if not node:
                result.append("null")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """Decode encoded string to tree."""
        if not data:
            return None

        values = iter(data.split(","))

        def dfs() -> TreeNode | None:
            val = next(values)
            if val == "null":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


def test() -> None:
    """Test cases for serialize/deserialize."""
    codec = Codec()

    # Test case 1: [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)  # type: ignore
    root.right.right = TreeNode(5)  # type: ignore

    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)

    # Re-serialize to verify
    reserialized = codec.serialize(deserialized)
    assert serialized == reserialized

    # Test case 2: Empty tree
    assert codec.serialize(None) == "null"
    assert codec.deserialize("null") is None

    print("All tests passed!")


if __name__ == "__main__":
    test()
