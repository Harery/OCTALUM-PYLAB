"""
Binary Tree Module
==================
Binary tree implementation with traversal methods.

Time Complexity:
- Insert: O(n) for level order, O(h) for BST property
- Search: O(n) worst case, O(h) for BST
- Traversal: O(n)
- Height: O(n)

Space Complexity: O(n) for storage, O(h) for recursive operations
"""

from __future__ import annotations

from typing import Generator


class TreeNode:
    """Binary tree node."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __repr__(self) -> str:
        return f"TreeNode({self.value})"

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    """
    Binary tree with comprehensive traversal methods.
    """

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def __repr__(self) -> str:
        return f"BinaryTree(root={self.root})"

    def __str__(self) -> str:
        if not self.root:
            return "Empty Tree"
        return self._format_tree(self.root)

    def _format_tree(self, node: TreeNode | None, prefix: str = "", is_left: bool = True) -> str:
        if not node:
            return ""
        result = ""
        if node.right:
            result += self._format_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        result += prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"
        if node.left:
            result += self._format_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        return result

    def insert_level_order(self, value: int) -> None:
        if not self.root:
            self.root = TreeNode(value)
            return

        queue: list[TreeNode] = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(value)
                return
            queue.append(node.left)

            if not node.right:
                node.right = TreeNode(value)
                return
            queue.append(node.right)

    def inorder(self) -> list[int]:
        result: list[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: TreeNode | None, result: list[int]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def inorder_iterative(self) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode] = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def preorder(self) -> list[int]:
        result: list[int] = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: TreeNode | None, result: list[int]) -> None:
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def preorder_iterative(self) -> list[int]:
        if not self.root:
            return []

        result: list[int] = []
        stack: list[TreeNode] = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.value)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def postorder(self) -> list[int]:
        result: list[int] = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: TreeNode | None, result: list[int]) -> None:
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def postorder_iterative(self) -> list[int]:
        if not self.root:
            return []

        result: list[int] = []
        stack: list[TreeNode] = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.value)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return list(reversed(result))

    def level_order(self) -> list[list[int]]:
        if not self.root:
            return []

        result: list[list[int]] = []
        queue: list[TreeNode] = [self.root]

        while queue:
            level_size = len(queue)
            level: list[int] = []

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

    def level_order_flat(self) -> list[int]:
        result: list[int] = []
        for level in self.level_order():
            result.extend(level)
        return result

    def morris_inorder(self) -> list[int]:
        result: list[int] = []
        current = self.root

        while current:
            if not current.left:
                result.append(current.value)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.value)
                    current = current.right

        return result

    def height(self) -> int:
        return self._height_recursive(self.root)

    def _height_recursive(self, node: TreeNode | None) -> int:
        if not node:
            return -1
        return 1 + max(
            self._height_recursive(node.left),
            self._height_recursive(node.right)
        )

    def depth(self, value: int) -> int:
        return self._depth_recursive(self.root, value, 0)

    def _depth_recursive(self, node: TreeNode | None, value: int, depth: int) -> int:
        if not node:
            return -1
        if node.value == value:
            return depth

        left_depth = self._depth_recursive(node.left, value, depth + 1)
        if left_depth != -1:
            return left_depth

        return self._depth_recursive(node.right, value, depth + 1)

    def size(self) -> int:
        return self._size_recursive(self.root)

    def _size_recursive(self, node: TreeNode | None) -> int:
        if not node:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def count_leaves(self) -> int:
        return self._count_leaves_recursive(self.root)

    def _count_leaves_recursive(self, node: TreeNode | None) -> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self._count_leaves_recursive(node.left) + self._count_leaves_recursive(node.right)

    def is_complete(self) -> bool:
        if not self.root:
            return True

        queue: list[TreeNode | None] = [self.root]
        found_null = False

        while queue:
            node = queue.pop(0)

            if not node:
                found_null = True
            else:
                if found_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True

    def is_full(self) -> bool:
        return self._is_full_recursive(self.root)

    def _is_full_recursive(self, node: TreeNode | None) -> bool:
        if not node:
            return True
        if (node.left is None) != (node.right is None):
            return False
        return self._is_full_recursive(node.left) and self._is_full_recursive(node.right)

    def is_perfect(self) -> bool:
        height = self.height()
        expected_nodes = 2 ** (height + 1) - 1
        return self.size() == expected_nodes

    def is_balanced(self) -> bool:
        return self._check_balance(self.root) != -1

    def _check_balance(self, node: TreeNode | None) -> int:
        if not node:
            return 0

        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1

        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    def diameter(self) -> int:
        max_diameter = 0

        def get_height(node: TreeNode | None) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        get_height(self.root)
        return max_diameter

    def lowest_common_ancestor(self, p: int, q: int) -> int | None:
        def find_lca(node: TreeNode | None) -> TreeNode | None:
            if not node:
                return None
            if node.value == p or node.value == q:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            if left and right:
                return node
            return left if left else right

        lca = find_lca(self.root)
        return lca.value if lca else None

    def serialize(self) -> str:
        def serialize_node(node: TreeNode | None) -> str:
            if not node:
                return "#"
            return f"{node.value},{serialize_node(node.left)},{serialize_node(node.right)}"

        return serialize_node(self.root)

    @classmethod
    def deserialize(cls, data: str) -> BinaryTree:
        def deserialize_node(values: list[str]) -> TreeNode | None:
            if not values:
                return None
            val = values.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = deserialize_node(values)
            node.right = deserialize_node(values)
            return node

        tree = cls()
        values = data.split(",")
        tree.root = deserialize_node(values)
        return tree

    def mirror(self) -> None:
        def mirror_node(node: TreeNode | None) -> None:
            if node:
                node.left, node.right = node.right, node.left
                mirror_node(node.left)
                mirror_node(node.right)

        mirror_node(self.root)

    def to_list_level_order(self) -> list[int | None]:
        if not self.root:
            return []

        result: list[int | None] = []
        queue: list[TreeNode | None] = [self.root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    @classmethod
    def from_list(cls, values: list[int | None]) -> BinaryTree:
        if not values:
            return cls()

        tree = cls()
        tree.root = TreeNode(values[0])
        queue: list[TreeNode] = [tree.root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return tree


if __name__ == "__main__":
    tree = BinaryTree()
    for val in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert_level_order(val)

    print("Tree:")
    print(tree)

    print(f"\nInorder: {tree.inorder()}")
    print(f"Preorder: {tree.preorder()}")
    print(f"Postorder: {tree.postorder()}")
    print(f"Level order: {tree.level_order()}")

    print(f"\nHeight: {tree.height()}")
    print(f"Size: {tree.size()}")
    print(f"Leaves: {tree.count_leaves()}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Diameter: {tree.diameter()}")

    print(f"\nMorris inorder: {tree.morris_inorder()}")

    serialized = tree.serialize()
    print(f"\nSerialized: {serialized}")
    restored = BinaryTree.deserialize(serialized)
    print(f"Restored inorder: {restored.inorder()}")
