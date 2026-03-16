"""
Queue Module
============
Queue implementations using list, linked list, and circular array.

FIFO (First In, First Out) data structure.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1) with proper implementation
- Peek: O(1)
- Is Empty: O(1)

Space Complexity: O(n)
"""

from __future__ import annotations


class QueueList:
    """
    Queue implementation using Python list.

    WARNING: dequeue() is O(n) because pop(0) shifts all elements.
    For production, use collections.deque.
    """

    def __init__(self) -> None:
        self._data: list[int] = []

    def __repr__(self) -> str:
        return f"QueueList({self._data})"

    def __str__(self) -> str:
        if not self._data:
            return "Queue: []"
        items = " -> ".join(str(x) for x in self._data)
        return f"Queue: [FRONT] {items} [REAR]"

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return bool(self._data)

    def enqueue(self, value: int) -> None:
        self._data.append(value)

    def dequeue(self) -> int:
        if not self._data:
            raise IndexError("Dequeue from empty queue")
        return self._data.pop(0)

    def peek(self) -> int:
        if not self._data:
            raise IndexError("Peek from empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()


class QueueNode:
    """Node for linked list queue."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: QueueNode | None = None


class QueueLinkedList:
    """
    Queue implementation using singly linked list with tail pointer.

    Enqueue at tail: O(1)
    Dequeue from head: O(1)
    """

    def __init__(self) -> None:
        self._head: QueueNode | None = None
        self._tail: QueueNode | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"QueueLinkedList([{', '.join(values)}])"

    def __str__(self) -> str:
        if not self._head:
            return "Queue: []"
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        items = " -> ".join(values)
        return f"Queue: [FRONT] {items} [REAR]"

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._head is not None

    def enqueue(self, value: int) -> None:
        new_node = QueueNode(value)
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self) -> int:
        if not self._head:
            raise IndexError("Dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if not self._head:
            self._tail = None
        self._size -= 1
        return value

    def peek(self) -> int:
        if not self._head:
            raise IndexError("Peek from empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        return self._size

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0


class CircularQueue:
    """
    Circular queue implementation using fixed-size array.

    Also known as Ring Buffer.
    All operations are O(1).
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data: list[int | None] = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0

    def __repr__(self) -> str:
        return f"CircularQueue(capacity={self._capacity}, size={self._size})"

    def __str__(self) -> str:
        if self._size == 0:
            return "CircularQueue: []"
        values = []
        for i in range(self._size):
            idx = (self._front + i) % self._capacity
            values.append(str(self._data[idx]))
        items = " -> ".join(values)
        return f"CircularQueue: [{items}]"

    def __len__(self) -> int:
        return self._size

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = value
        self._size += 1
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._data[self._front]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity


class Deque:
    """
    Double-ended queue implementation using doubly linked list.

    All operations are O(1).
    """

    def __init__(self) -> None:
        self._head: DequeNode | None = None
        self._tail: DequeNode | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"Deque([{', '.join(values)}])"

    def __len__(self) -> int:
        return self._size

    def add_front(self, value: int) -> None:
        new_node = DequeNode(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def add_rear(self, value: int) -> None:
        new_node = DequeNode(value)
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def remove_front(self) -> int:
        if not self._head:
            raise IndexError("Remove from empty deque")
        value = self._head.value
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        self._size -= 1
        return value

    def remove_rear(self) -> int:
        if not self._tail:
            raise IndexError("Remove from empty deque")
        value = self._tail.value
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None
        self._size -= 1
        return value

    def peek_front(self) -> int:
        if not self._head:
            raise IndexError("Peek from empty deque")
        return self._head.value

    def peek_rear(self) -> int:
        if not self._tail:
            raise IndexError("Peek from empty deque")
        return self._tail.value

    def is_empty(self) -> bool:
        return self._size == 0


class DequeNode:
    """Node for deque."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: DequeNode | None = None
        self.prev: DequeNode | None = None


def bfs_queue_demo() -> list[int]:
    """
    Demonstrate BFS using queue on a simple tree-like structure.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    graph: dict[int, list[int]] = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [], 5: [], 6: [], 7: []
    }

    queue = QueueLinkedList()
    visited: set[int] = set()
    result: list[int] = []

    queue.enqueue(1)
    visited.add(1)

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

    return result


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    """
    Find maximum in each sliding window using deque.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if not nums or k == 0:
        return []

    from collections import deque
    dq: deque[int] = deque()
    result: list[int] = []

    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print("=== QueueLinkedList ===")
    queue = QueueLinkedList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue: {queue}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Peek: {queue.peek()}")
    print(f"Size: {len(queue)}")

    print("\n=== CircularQueue ===")
    cq = CircularQueue(3)
    print(f"Enqueue 1: {cq.enqueue(1)}")
    print(f"Enqueue 2: {cq.enqueue(2)}")
    print(f"Enqueue 3: {cq.enqueue(3)}")
    print(f"Enqueue 4 (full): {cq.enqueue(4)}")
    print(f"Queue: {cq}")
    print(f"Dequeue: {cq.dequeue()}")
    print(f"Enqueue 4 again: {cq.enqueue(4)}")
    print(f"Queue: {cq}")

    print("\n=== Deque ===")
    d = Deque()
    d.add_front(1)
    d.add_rear(2)
    d.add_front(0)
    print(f"Deque: {d}")
    print(f"Remove front: {d.remove_front()}")
    print(f"Remove rear: {d.remove_rear()}")

    print("\n=== BFS Demo ===")
    print(f"BFS traversal: {bfs_queue_demo()}")

    print("\n=== Sliding Window Max ===")
    print(f"[1,3,-1,-3,5,3,6,7], k=3 -> {sliding_window_max([1,3,-1,-3,5,3,6,7], 3)}")
