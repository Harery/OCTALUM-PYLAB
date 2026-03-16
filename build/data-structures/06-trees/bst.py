"""
Binary Search Tree Module
=========================
BST implementation with insert, delete, search, and utility methods.

Time Complexity (average case, balanced):
- Insert: O(log n)
- Delete: O(log n)
- Search: O(log n)
- Min/Max: O(log n)

Time Complexity (worst case, skewed):
- All operations: O(n)

Space Complexity: O(n)
"""

from __future__ import annotations


class BSTNode:
    """Binary search tree node."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

    def __repr__(self) -> str:
        return f"BSTNode({self.value})"

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
    """
    Binary Search Tree with standard operations.

    Property: left.value < node.value < right.value
    """

    def __init__(self) -> None:
        self.root: BSTNode | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        return f"BinarySearchTree(size={self._size})"

    def __str__(self) -> str:
        if not self.root:
            return "Empty BST"
        return self._format_tree(self.root)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, value: int) -> bool:
        return self.search(value) is not None

    def _format_tree(self, node: BSTNode | None, prefix: str = "", is_left: bool = True) -> str:
        if not node:
            return ""
        result = ""
        if node.right:
            result += self._format_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        result += prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"
        if node.left:
            result += self._format_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        return result

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = BSTNode(value)
            self._size += 1
            return

        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: BSTNode, value: int) -> None:
        if value < node.value:
            if not node.left:
                node.left = BSTNode(value)
                self._size += 1
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = BSTNode(value)
                self._size += 1
            else:
                self._insert_recursive(node.right, value)

    def insert_iterative(self, value: int) -> None:
        if not self.root:
            self.root = BSTNode(value)
            self._size += 1
            return

        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = BSTNode(value)
                    self._size += 1
                    return
                current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = BSTNode(value)
                    self._size += 1
                    return
                current = current.right
            else:
                return

    def search(self, value: int) -> BSTNode | None:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: BSTNode | None, value: int) -> BSTNode | None:
        if not node or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def search_iterative(self, value: int) -> BSTNode | None:
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, value: int) -> bool:
        if not self.root:
            return False

        result = self._delete_recursive(self.root, None, value)
        if result:
            self._size -= 1
        return result

    def _delete_recursive(self, node: BSTNode | None, parent: BSTNode | None, value: int) -> bool:
        if not node:
            return False

        if value < node.value:
            return self._delete_recursive(node.left, node, value)
        elif value > node.value:
            return self._delete_recursive(node.right, node, value)
        else:
            if not node.left and not node.right:
                self._replace_node(parent, node, None)
            elif not node.left:
                self._replace_node(parent, node, node.right)
            elif not node.right:
                self._replace_node(parent, node, node.left)
            else:
                successor = self._find_min_node(node.right)
                node.value = successor.value
                self._delete_recursive(node.right, node, successor.value)
            return True

    def _replace_node(self, parent: BSTNode | None, old_node: BSTNode, new_node: BSTNode | None) -> None:
        if not parent:
            self.root = new_node
        elif parent.left is old_node:
            parent.left = new_node
        else:
            parent.right = new_node

    def _find_min_node(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left:
            current = current.left
        return current

    def find_min(self) -> int | None:
        if not self.root:
            return None
        return self._find_min_node(self.root).value

    def find_max(self) -> int | None:
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.value

    def inorder(self) -> list[int]:
        result: list[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: BSTNode | None, result: list[int]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder(self) -> list[int]:
        result: list[int] = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: BSTNode | None, result: list[int]) -> None:
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self) -> list[int]:
        result: list[int] = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: BSTNode | None, result: list[int]) -> None:
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def successor(self, value: int) -> int | None:
        node = self.search(value)
        if not node:
            return None

        if node.right:
            return self._find_min_node(node.right).value

        successor = None
        current = self.root

        while current:
            if value < current.value:
                successor = current.value
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                break

        return successor

    def predecessor(self, value: int) -> int | None:
        node = self.search(value)
        if not node:
            return None

        if node.left:
            current = node.left
            while current.right:
                current = current.right
            return current.value

        predecessor = None
        current = self.root

        while current:
            if value > current.value:
                predecessor = current.value
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                break

        return predecessor

    def floor(self, value: int) -> int | None:
        return self._floor_recursive(self.root, value)

    def _floor_recursive(self, node: BSTNode | None, value: int) -> int | None:
        if not node:
            return None

        if value == node.value:
            return value

        if value < node.value:
            return self._floor_recursive(node.left, value)

        floor_right = self._floor_recursive(node.right, value)
        if floor_right is not None:
            return floor_right
        return node.value

    def ceil(self, value: int) -> int | None:
        return self._ceil_recursive(self.root, value)

    def _ceil_recursive(self, node: BSTNode | None, value: int) -> int | None:
        if not node:
            return None

        if value == node.value:
            return value

        if value > node.value:
            return self._ceil_recursive(node.right, value)

        ceil_left = self._ceil_recursive(node.left, value)
        if ceil_left is not None:
            return ceil_left
        return node.value

    def range_query(self, low: int, high: int) -> list[int]:
        result: list[int] = []
        self._range_query_recursive(self.root, low, high, result)
        return result

    def _range_query_recursive(self, node: BSTNode | None, low: int, high: int, result: list[int]) -> None:
        if not node:
            return

        if low < node.value:
            self._range_query_recursive(node.left, low, high, result)

        if low <= node.value <= high:
            result.append(node.value)

        if high > node.value:
            self._range_query_recursive(node.right, low, high, result)

    def is_valid_bst(self) -> bool:
        return self._is_valid_recursive(self.root, float("-inf"), float("inf"))

    def _is_valid_recursive(self, node: BSTNode | None, min_val: float, max_val: float) -> bool:
        if not node:
            return True

        if node.value <= min_val or node.value >= max_val:
            return False

        return (self._is_valid_recursive(node.left, min_val, node.value) and
                self._is_valid_recursive(node.right, node.value, max_val))

    def height(self) -> int:
        return self._height_recursive(self.root)

    def _height_recursive(self, node: BSTNode | None) -> int:
        if not node:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def lowest_common_ancestor(self, v1: int, v2: int) -> int | None:
        if v1 not in self or v2 not in self:
            return None
        return self._lca_recursive(self.root, v1, v2)

    def _lca_recursive(self, node: BSTNode | None, v1: int, v2: int) -> int | None:
        if not node:
            return None

        if v1 < node.value and v2 < node.value:
            return self._lca_recursive(node.left, v1, v2)
        if v1 > node.value and v2 > node.value:
            return self._lca_recursive(node.right, v1, v2)
        return node.value

    def clear(self) -> None:
        self.root = None
        self._size = 0

    @classmethod
    def from_sorted_array(cls, arr: list[int]) -> BinarySearchTree:
        bst = cls()
        bst.root = cls._build_balanced(arr, 0, len(arr) - 1)
        bst._size = len(arr)
        return bst

    @classmethod
    def _build_balanced(cls, arr: list[int], start: int, end: int) -> BSTNode | None:
        if start > end:
            return None

        mid = (start + end) // 2
        node = BSTNode(arr[mid])
        node.left = cls._build_balanced(arr, start, mid - 1)
        node.right = cls._build_balanced(arr, mid + 1, end)
        return node


if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("BST:")
    print(bst)

    print(f"\nInorder (sorted): {bst.inorder()}")
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 100: {bst.search(100)}")

    print(f"\nMin: {bst.find_min()}")
    print(f"Max: {bst.find_max()}")

    print(f"\nSuccessor of 40: {bst.successor(40)}")
    print(f"Predecessor of 40: {bst.predecessor(40)}")

    print(f"\nFloor of 45: {bst.floor(45)}")
    print(f"Ceil of 45: {bst.ceil(45)}")

    print(f"\nRange query [30, 60]: {bst.range_query(30, 60)}")

    print(f"\nIs valid BST: {bst.is_valid_bst()}")
    print(f"LCA of 20 and 40: {bst.lowest_common_ancestor(20, 40)}")

    print(f"\nDelete 30")
    bst.delete(30)
    print(f"Inorder after delete: {bst.inorder()}")

    sorted_arr = [1, 2, 3, 4, 5, 6, 7]
    balanced = BinarySearchTree.from_sorted_array(sorted_arr)
    print(f"\nBalanced from {sorted_arr}:")
    print(f"Inorder: {balanced.inorder()}")
    print(f"Height: {balanced.height()}")
