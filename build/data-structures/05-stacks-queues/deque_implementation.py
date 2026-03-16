"""
Deque (Double-Ended Queue) Module
=================================
Deque implementation using doubly linked list.

Supports insertion and removal at both ends in O(1) time.

Time Complexity:
- add_front: O(1)
- add_rear: O(1)
- remove_front: O(1)
- remove_rear: O(1)
- peek_front: O(1)
- peek_rear: O(1)
- is_empty: O(1)
- size: O(1)

Space Complexity: O(n)
"""

from __future__ import annotations


class DequeNode:
    """
    Node for doubly linked list deque.

    Contains value and pointers to next/prev nodes.
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: DequeNode | None = None
        self.prev: DequeNode | None = None

    def __repr__(self) -> str:
        return f"DequeNode({self.value})"


class Deque:
    """
    Double-ended queue implementation using doubly linked list.

    All operations are O(1) since we maintain head and tail pointers.

    Example:
        >>> d = Deque()
        >>> d.add_rear(1)
        >>> d.add_rear(2)
        >>> d.add_front(0)
        >>> d.to_list()  # [0, 1, 2]
        >>> d.remove_front()  # 0
        >>> d.remove_rear()   # 2
    """

    def __init__(self) -> None:
        self._head: DequeNode | None = None
        self._tail: DequeNode | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        return f"Deque({self.to_list()})"

    def __str__(self) -> str:
        if self.is_empty():
            return "Deque: [] (empty)"
        values = " <-> ".join(str(x) for x in self.to_list())
        return f"Deque: [{values}] (size={self._size})"

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0

    def __iter__(self) -> DequeIterator:
        return DequeIterator(self._head)

    def add_front(self, value: int) -> None:
        """
        Add element to the front of the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DequeNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1

    def add_rear(self, value: int) -> None:
        """
        Add element to the rear of the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DequeNode(value)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def remove_front(self) -> int:
        """
        Remove and return element from the front.

        Raises:
            IndexError: If deque is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("remove_front from empty deque")

        value = self._head.value
        self._head = self._head.next

        if self._head:
            self._head.prev = None
        else:
            self._tail = None

        self._size -= 1
        return value

    def remove_rear(self) -> int:
        """
        Remove and return element from the rear.

        Raises:
            IndexError: If deque is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")

        value = self._tail.value
        self._tail = self._tail.prev

        if self._tail:
            self._tail.next = None
        else:
            self._head = None

        self._size -= 1
        return value

    def peek_front(self) -> int:
        """
        Return front element without removing.

        Raises:
            IndexError: If deque is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek_front from empty deque")
        return self._head.value

    def peek_rear(self) -> int:
        """
        Return rear element without removing.

        Raises:
            IndexError: If deque is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek_rear from empty deque")
        return self._tail.value

    def is_empty(self) -> bool:
        """Check if deque is empty. O(1)"""
        return self._size == 0

    def size(self) -> int:
        """Return number of elements. O(1)"""
        return self._size

    def clear(self) -> None:
        """Remove all elements. O(1)"""
        self._head = None
        self._tail = None
        self._size = 0

    def to_list(self) -> list[int]:
        """Convert deque to list (front to rear). O(n)"""
        result: list[int] = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def rotate_left(self, k: int = 1) -> None:
        """
        Rotate deque left by k positions.

        Moves k elements from front to rear.
        Time Complexity: O(k)
        """
        k = k % self._size if self._size else 0
        for _ in range(k):
            self.add_rear(self.remove_front())

    def rotate_right(self, k: int = 1) -> None:
        """
        Rotate deque right by k positions.

        Moves k elements from rear to front.
        Time Complexity: O(k)
        """
        k = k % self._size if self._size else 0
        for _ in range(k):
            self.add_front(self.remove_rear())


class DequeIterator:
    """Iterator for Deque."""

    def __init__(self, head: DequeNode | None) -> None:
        self._current = head

    def __iter__(self) -> DequeIterator:
        return self

    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next
        return value


class CircularDeque:
    """
    Circular deque implementation using fixed-size array.

    More memory efficient for bounded deques.
    All operations are O(1).
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data: list[int | None] = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def __repr__(self) -> str:
        return f"CircularDeque(capacity={self._capacity}, size={self._size})"

    def __str__(self) -> str:
        if self.is_empty():
            return "CircularDeque: [] (empty)"
        values = [str(self._data[(self._front + i) % self._capacity])
                  for i in range(self._size)]
        return f"CircularDeque: [{', '.join(values)}]"

    def __len__(self) -> int:
        return self._size

    def _prev_index(self, idx: int) -> int:
        return (idx - 1 + self._capacity) % self._capacity

    def _next_index(self, idx: int) -> int:
        return (idx + 1) % self._capacity

    def add_front(self, value: int) -> bool:
        """
        Add element to front.

        Returns False if at capacity.
        Time Complexity: O(1)
        """
        if self.is_full():
            return False

        self._front = self._prev_index(self._front)
        self._data[self._front] = value
        self._size += 1
        return True

    def add_rear(self, value: int) -> bool:
        """
        Add element to rear.

        Returns False if at capacity.
        Time Complexity: O(1)
        """
        if self.is_full():
            return False

        self._data[self._rear] = value
        self._rear = self._next_index(self._rear)
        self._size += 1
        return True

    def remove_front(self) -> int:
        """
        Remove element from front.

        Raises IndexError if empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("remove_front from empty circular deque")

        value = self._data[self._front]
        self._data[self._front] = None
        self._front = self._next_index(self._front)
        self._size -= 1
        return value

    def remove_rear(self) -> int:
        """
        Remove element from rear.

        Raises IndexError if empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("remove_rear from empty circular deque")

        self._rear = self._prev_index(self._rear)
        value = self._data[self._rear]
        self._data[self._rear] = None
        self._size -= 1
        return value

    def peek_front(self) -> int:
        """Return front element without removing. O(1)"""
        if self.is_empty():
            raise IndexError("peek_front from empty circular deque")
        return self._data[self._front]

    def peek_rear(self) -> int:
        """Return rear element without removing. O(1)"""
        if self.is_empty():
            raise IndexError("peek_rear from empty circular deque")
        rear_idx = self._prev_index(self._rear)
        return self._data[rear_idx]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity


def is_palindrome_deque(s: str) -> bool:
    """
    Check if string is palindrome using deque.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    deque = Deque()

    # Add all characters to deque
    for char in s.lower():
        if char.isalnum():
            deque.add_rear(ord(char))

    # Compare front and rear
    while deque.size() > 1:
        if deque.remove_front() != deque.remove_rear():
            return False

    return True


def max_sliding_window_deque(nums: list[int], k: int) -> list[int]:
    """
    Find maximum in each sliding window using deque.

    Deque stores indices of elements in decreasing order.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if not nums or k == 0:
        return []

    from collections import deque as PyDeque

    dq: PyDeque[int] = PyDeque()
    result: list[int] = []

    for i, num in enumerate(nums):
        # Remove indices outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Record maximum when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print("=" * 50)
    print("Deque (Doubly Linked List)")
    print("=" * 50)

    d = Deque()
    print(f"Empty deque: {d}")

    # Add elements
    d.add_rear(1)
    d.add_rear(2)
    d.add_front(0)
    print(f"After add_rear(1,2) and add_front(0): {d}")

    # Peek operations
    print(f"peek_front(): {d.peek_front()}")
    print(f"peek_rear(): {d.peek_rear()}")

    # Remove operations
    print(f"remove_front(): {d.remove_front()}")
    print(f"remove_rear(): {d.remove_rear()}")
    print(f"After removals: {d}")

    # Rotation
    d.add_rear(3)
    d.add_rear(4)
    print(f"\nBefore rotation: {d.to_list()}")
    d.rotate_left(1)
    print(f"After rotate_left(1): {d.to_list()}")
    d.rotate_right(2)
    print(f"After rotate_right(2): {d.to_list()}")

    # Iteration
    print(f"\nIteration: {[x for x in d]}")

    print("\n" + "=" * 50)
    print("CircularDeque")
    print("=" * 50)

    cd = CircularDeque(5)
    print(f"Created with capacity 5: {cd}")

    cd.add_rear(1)
    cd.add_rear(2)
    cd.add_front(0)
    print(f"After adds: {cd}")
    print(f"add_front(-1) when full: {cd.add_front(-1)}")  # False - not full yet

    cd.add_rear(3)
    cd.add_rear(4)
    print(f"After more adds: {cd}")
    print(f"add_rear(5) when full: {cd.add_rear(5)}")  # False - full

    print(f"remove_front(): {cd.remove_front()}")
    print(f"After removal: {cd}")

    print("\n" + "=" * 50)
    print("Applications")
    print("=" * 50)

    # Palindrome check
    test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello"]
    print("\nPalindrome check:")
    for s in test_strings:
        print(f"  '{s}' -> {is_palindrome_deque(s)}")

    # Sliding window max
    print("\nSliding window maximum:")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"  nums={nums}, k={k}")
    print(f"  result={max_sliding_window_deque(nums, k)}")
