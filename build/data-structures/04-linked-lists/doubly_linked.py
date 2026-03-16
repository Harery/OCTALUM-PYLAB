"""
Doubly Linked List Module
=========================
Complete implementation of a doubly linked list with all common operations.

Time Complexity:
- Access by index: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(1)
- Insert at position: O(n)
- Delete at head: O(1)
- Delete at tail: O(1)
- Delete at position: O(n)

Space Complexity: O(n) for storing n nodes (more than singly linked due to prev pointers)
"""

from __future__ import annotations


class DoublyNode:
    """
    A node in a doubly linked list.

    Contains a value and references to both next and previous nodes.
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: DoublyNode | None = None
        self.prev: DoublyNode | None = None

    def __repr__(self) -> str:
        return f"DoublyNode({self.value})"

    def __str__(self) -> str:
        return str(self.value)


class DoublyLinkedList:
    """
    A doubly linked list implementation.

    Maintains references to both head and tail nodes for O(1)
    operations at both ends.
    """

    def __init__(self) -> None:
        self.head: DoublyNode | None = None
        self.tail: DoublyNode | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"DoublyLinkedList([{' <-> '.join(values)}])"

    def __str__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values) if values else "Empty"

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> DoublyLinkedListIterator:
        return DoublyLinkedListIterator(self.head)

    def __reversed__(self) -> DoublyLinkedListReverseIterator:
        return DoublyLinkedListReverseIterator(self.tail)

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __bool__(self) -> bool:
        return self.head is not None

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._size

    def _get_node_at(self, index: int) -> DoublyNode:
        if index < 0:
            index = self._size + index
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")

        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        return current

    def prepend(self, value: int) -> None:
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def append(self, value: int) -> None:
        new_node = DoublyNode(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def insert(self, index: int, value: int) -> None:
        if index <= 0:
            self.prepend(value)
            return
        if index >= self._size:
            self.append(value)
            return

        current = self._get_node_at(index)
        new_node = DoublyNode(value)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self._size += 1

    def get(self, index: int) -> int:
        return self._get_node_at(index).value

    def set(self, index: int, value: int) -> None:
        self._get_node_at(index).value = value

    def pop_first(self) -> int:
        if not self.head:
            raise IndexError("Pop from empty list")

        value = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return value

    def pop(self) -> int:
        if not self.tail:
            raise IndexError("Pop from empty list")

        value = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return value

    def remove(self, index: int) -> int:
        if index == 0:
            return self.pop_first()
        if index == self._size - 1:
            return self.pop()

        current = self._get_node_at(index)
        current.prev.next = current.next
        current.next.prev = current.prev
        self._size -= 1
        return current.value

    def remove_value(self, value: int) -> bool:
        current = self.head
        while current:
            if current.value == value:
                if current is self.head:
                    self.pop_first()
                elif current is self.tail:
                    self.pop()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self._size -= 1
                return True
            current = current.next
        return False

    def find(self, value: int) -> int:
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, value: int) -> bool:
        return self.find(value) != -1

    def count(self, value: int) -> int:
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def to_list(self) -> list[int]:
        result: list[int] = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def to_list_reversed(self) -> list[int]:
        result: list[int] = []
        current = self.tail
        while current:
            result.append(current.value)
            current = current.prev
        return result

    @classmethod
    def from_list(cls, values: list[int]) -> DoublyLinkedList:
        dll = cls()
        for value in values:
            dll.append(value)
        return dll

    def reverse(self) -> None:
        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

    def swap(self, index1: int, index2: int) -> None:
        if index1 == index2:
            return

        node1 = self._get_node_at(index1)
        node2 = self._get_node_at(index2)
        node1.value, node2.value = node2.value, node1.value

    def move_to_front(self, index: int) -> None:
        if index == 0:
            return

        node = self._get_node_at(index)
        if node is self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def move_to_end(self, index: int) -> None:
        if index == self._size - 1:
            return

        node = self._get_node_at(index)
        if node is self.head:
            self.head = node.next
            node.next.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def insert_after(self, node_value: int, new_value: int) -> bool:
        current = self.head
        while current:
            if current.value == node_value:
                new_node = DoublyNode(new_value)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self._size += 1
                return True
            current = current.next
        return False

    def insert_before(self, node_value: int, new_value: int) -> bool:
        current = self.head
        while current:
            if current.value == node_value:
                new_node = DoublyNode(new_value)
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                self._size += 1
                return True
            current = current.next
        return False

    def remove_duplicates(self) -> None:
        seen: set[int] = set()
        current = self.head
        while current:
            if current.value in seen:
                next_node = current.next
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current is self.head:
                    self.head = current.next
                if current is self.tail:
                    self.tail = current.prev
                self._size -= 1
                current = next_node
            else:
                seen.add(current.value)
                current = current.next

    def sort(self) -> None:
        if not self.head or not self.head.next:
            return
        values = self.to_list()
        values.sort()
        self.clear()
        for value in values:
            self.append(value)


class DoublyLinkedListIterator:
    """Forward iterator for DoublyLinkedList."""

    def __init__(self, head: DoublyNode | None) -> None:
        self.current = head

    def __iter__(self) -> DoublyLinkedListIterator:
        return self

    def __next__(self) -> int:
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class DoublyLinkedListReverseIterator:
    """Reverse iterator for DoublyLinkedList."""

    def __init__(self, tail: DoublyNode | None) -> None:
        self.current = tail

    def __iter__(self) -> DoublyLinkedListReverseIterator:
        return self

    def __next__(self) -> int:
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.prev
        return value


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print(f"List: {dll}")
    print(f"Size: {len(dll)}")

    print(f"Forward: {list(dll)}")
    print(f"Backward: {list(reversed(dll))}")

    dll.insert(2, 10)
    print(f"After insert at index 2: {dll}")

    print(f"Pop first: {dll.pop_first()}")
    print(f"Pop last: {dll.pop()}")
    print(f"After pops: {dll}")

    dll.reverse()
    print(f"Reversed: {dll}")

    dll2 = DoublyLinkedList.from_list([5, 6, 7])
    print(f"From list: {dll2}")
