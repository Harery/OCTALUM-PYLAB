#!/usr/bin/env python3
"""
System Design: LRU Cache

Design a Least Recently Used (LRU) cache with O(1) get and put operations.

Requirements:
- get(key): Return value if exists, else -1
- put(key, value): Insert/update value
- Evict least recently used when at capacity
- All operations in O(1) time

Key Components:
1. Hash map for O(1) lookups
2. Doubly linked list for O(1) reordering

Time Complexity: O(1) for get and put
Space Complexity: O(capacity)
"""

from __future__ import annotations


class Node:
    """Doubly linked list node."""

    __slots__ = ["key", "value", "prev", "next"]

    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """
    LRU Cache using hash map + doubly linked list.

    - Hash map provides O(1) access
    - Linked list provides O(1) reordering
    - Head = most recently used, Tail = least recently used
    """

    def __init__(self, capacity: int) -> None:
        """
        Initialize LRU cache.

        Args:
            capacity: Maximum number of items to store
        """
        self._capacity = capacity
        self._cache: dict[int, Node] = {}

        # Dummy head and tail for easier manipulation
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: Node) -> None:
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        """Add node right after head (most recently used)."""
        node.prev = self._head
        node.next = self._head.next
        if self._head.next:
            self._head.next.prev = node
        self._head.next = node

    def get(self, key: int) -> int:
        """
        Get value by key and mark as recently used.

        Args:
            key: Key to look up

        Returns:
            Value if found, -1 if not found
        """
        if key not in self._cache:
            return -1

        node = self._cache[key]

        # Move to front (most recently used)
        self._remove(node)
        self._add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.

        Args:
            key: Key to insert/update
            value: Value to store
        """
        if key in self._cache:
            # Update existing
            node = self._cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Insert new
            if len(self._cache) >= self._capacity:
                # Evict LRU (node before tail)
                lru = self._tail.prev
                if lru:
                    self._remove(lru)
                    del self._cache[lru.key]

            new_node = Node(key, value)
            self._cache[key] = new_node
            self._add_to_front(new_node)

    def size(self) -> int:
        """Return current number of items."""
        return len(self._cache)


def test() -> None:
    """Test cases for LRU cache."""
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Returns 1

    cache.put(3, 3)  # Evicts key 2
    assert cache.get(2) == -1  # Returns -1 (not found)

    cache.put(4, 4)  # Evicts key 1
    assert cache.get(1) == -1  # Returns -1
    assert cache.get(3) == 3  # Returns 3
    assert cache.get(4) == 4  # Returns 4

    # Test update
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(1, 2)  # Update, not evict
    assert cache2.get(1) == 2
    assert cache2.size() == 1

    print("All LRU cache tests passed!")


if __name__ == "__main__":
    test()
