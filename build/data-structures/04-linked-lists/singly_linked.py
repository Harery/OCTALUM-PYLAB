"""
Singly Linked List Module
=========================
Complete implementation of a singly linked list with all common operations.

Time Complexity:
- Access by index: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(n) without tail pointer, O(1) with
- Insert at position: O(n)
- Delete at head: O(1)
- Delete at tail: O(n)
- Delete at position: O(n)

Space Complexity: O(n) for storing n nodes
"""

from __future__ import annotations


class Node:
    """
    A node in a singly linked list.

    Contains a value and a reference to the next node.
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    """
    A singly linked list implementation.

    Maintains a reference to the head node and tracks size.
    """

    def __init__(self) -> None:
        self.head: Node | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"LinkedList([{' -> '.join(values)}])"

    def __str__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Empty"

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __bool__(self) -> bool:
        return self.head is not None

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._size

    def prepend(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert(self, index: int, value: int) -> None:
        if index < 0:
            index = self._size + index
        if index <= 0:
            self.prepend(value)
            return
        if index >= self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def get(self, index: int) -> int:
        if index < 0:
            index = self._size + index
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index: int, value: int) -> None:
        if index < 0:
            index = self._size + index
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def pop_first(self) -> int:
        if not self.head:
            raise IndexError("Pop from empty list")
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def pop(self) -> int:
        if not self.head:
            raise IndexError("Pop from empty list")
        if not self.head.next:
            value = self.head.value
            self.head = None
            self._size -= 1
            return value

        current = self.head
        while current.next.next:
            current = current.next
        value = current.next.value
        current.next = None
        self._size -= 1
        return value

    def remove(self, index: int) -> int:
        if index < 0:
            index = self._size + index
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        if index == 0:
            return self.pop_first()

        current = self.head
        for _ in range(index - 1):
            current = current.next
        value = current.next.value
        current.next = current.next.next
        self._size -= 1
        return value

    def remove_value(self, value: int) -> bool:
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next
            self._size -= 1
            return True
        return False

    def find(self, value: int) -> int:
        """
        Find the index of a value in the list.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            value: Value to find

        Returns:
            Index of value if found, -1 otherwise
        """
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def search(self, value: int) -> bool:
        """
        Search for a value in the list.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            value: Value to search for

        Returns:
            True if value is found, False otherwise
        """
        return self.find(value) != -1

    def delete(self, value: int) -> bool:
        """
        Delete the first occurrence of a value from the list.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            value: Value to delete

        Returns:
            True if value was deleted, False if not found
        """
        return self.remove_value(value)

    def insert_at(self, index: int, value: int) -> None:
        """
        Insert a value at a specific index.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            index: Position to insert at
            value: Value to insert
        """
        self.insert(index, value)

    def print_list(self) -> None:
        """
        Print the linked list to stdout.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        print(str(self))

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
        self._size = 0

    def to_list(self) -> list[int]:
        result: list[int] = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    @classmethod
    def from_list(cls, values: list[int]) -> LinkedList:
        ll = cls()
        for value in values:
            ll.append(value)
        return ll

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reversed_copy(self) -> LinkedList:
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.prepend(current.value)
            current = current.next
        return new_list

    def get_middle(self) -> int | None:
        if not self.head:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value

    def has_cycle(self) -> bool:
        if not self.head:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def get_nth_from_end(self, n: int) -> int:
        if n <= 0 or not self.head:
            raise IndexError("Invalid index")

        fast = self.head
        slow = self.head

        for _ in range(n):
            if not fast:
                raise IndexError("Index out of range")
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.value

    def remove_duplicates(self) -> None:
        if not self.head:
            return

        seen: set[int] = {self.head.value}
        current = self.head

        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
                self._size -= 1
            else:
                seen.add(current.next.value)
                current = current.next

    def remove_duplicates_sorted(self) -> None:
        current = self.head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
                self._size -= 1
            else:
                current = current.next

    def merge_sorted(self, other: LinkedList) -> LinkedList:
        result = LinkedList()
        current1 = self.head
        current2 = other.head

        while current1 and current2:
            if current1.value <= current2.value:
                result.append(current1.value)
                current1 = current1.next
            else:
                result.append(current2.value)
                current2 = current2.next

        while current1:
            result.append(current1.value)
            current1 = current1.next

        while current2:
            result.append(current2.value)
            current2 = current2.next

        return result

    def is_palindrome(self) -> bool:
        if not self.head or not self.head.next:
            return True

        values: list[int] = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next

        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True

    def sort(self) -> None:
        if not self.head or not self.head.next:
            return
        values = self.to_list()
        values.sort()
        self.clear()
        for value in values:
            self.append(value)


class LinkedListIterator:
    """Iterator for LinkedList."""

    def __init__(self, head: Node | None) -> None:
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> int:
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print(f"List: {ll}")
    print(f"Size: {len(ll)}")

    ll.insert_at(2, 10)
    print(f"After insert_at index 2: {ll}")

    print(f"Get index 2: {ll.get(2)}")
    print(f"Search for 10: {ll.search(10)}")
    print(f"Find value 10: {ll.find(10)}")

    ll.delete(10)
    print(f"After delete(10): {ll}")

    ll.reverse()
    print(f"Reversed: {ll}")

    print(f"Middle element: {ll.get_middle()}")

    print(f"Nth from end (n=2): {ll.get_nth_from_end(2)}")

    ll2 = LinkedList.from_list([4, 5, 6])
    merged = ll.merge_sorted(ll2)
    ll.sort()
    print(f"Sorted: {ll}")
    print(f"Merged: {merged}")

    print("\nUsing print_list():")
    ll.print_list()
