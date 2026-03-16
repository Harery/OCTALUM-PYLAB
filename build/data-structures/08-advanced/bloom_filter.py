"""
Bloom Filter Module
=====================
Probabilistic data structure for set membership testing.

Bloom filters provide space-efficient membership testing with a configurable false positive rate.

Space Complexity: O(m) where m is number of hash functions
Time Complexity:
- Add: O(k) where k is number of hash functions
- Contains: O(k)
- No false negatives (always returns True if item might be in set)
- Can have false positives (returns True even if item is NOT in set)

Probability of false positive ≈ (1 - (1 - e^(-k/m))^n where:
- n = number of elements added
- m = size of bit array
- k = number of hash functions
"""

from __future__ import annotations

import hashlib


class BloomFilter:
    """
    Bloom filter implementation with configurable size and hash functions.
    """

    def __init__(self, size: int = 1000, num_hashes: int = 3) -> None:
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array: list[bool] = [False] * size
        self._count: int = 0

    def __repr__(self) -> str:
        return f"BloomFilter(size={self.size}, hashes={self.num_hashes}, items={self._count})"

    def __str__(self) -> str:
        return f"BloomFilter with {self._count} items"

    def __len__(self) -> int:
        return self._count

    def _hashes(self, item: int | str) -> Generator[int, None]:
        for i in range(self.num_hashes):
            hash_val = int(hashlib.md5(f"{item}{i}".encode()))
            yield hash_val % self.size

    def add(self, item: int | str) -> None:
        for hash_val in self._hashes(item):
            if not self.bit_array[hash_val]:
                self.bit_array[hash_val] = True
                self._count += 1

    def contains(self, item: int | str) -> bool:
        for hash_val in self._hashes(item):
            if not self.bit_array[hash_val]:
                return False
        return True

    def union(self, other: BloomFilter) -> None:
        for i in range(self.size):
            if other.bit_array[i]:
                self.bit_array[i] = True

    def intersection(self, other: BloomFilter) -> None:
        for i in range(self.size):
            if not (other.bit_array[i]):
                self.bit_array[i] = False

    def false_positive_rate(self) -> float:
        return 1 - (1 - (1 - 1/self.size)) ** self.num_hashes


class CountingBloomFilter:
    """
    Counting Bloom Filter that can estimate the count of elements.
    """

    def __init__(self, size: int = 1000, num_hashes: int = 3) -> None:
        super().__init__(size, num_hashes)
        self.counts: list[int] = [0] * size

    def __repr__(self) -> str:
        return f"CountingBloomFilter(size={self.size}, hashes={self.num_hashes})"

    def add(self, item: int | str) -> None:
        for hash_val in self._hashes(item):
            self.counts[hash_val] += 1
            self.bit_array[hash_val] = True
        self._count += 1

    def count(self, item: int | str) -> int:
        min_count = float("inf")
        for hash_val in self._hashes(item):
            if not self.bit_array[hash_val]:
                return 0
            min_count = min(min_count, self.counts[hash_val])
        return int(min_count)


class ScalableBloomFilter:
    """
    Scalable Bloom Filter that can grow as needed.
    """

    def __init__(self, initial_size: int = 1000, error_rate: float = 0.01) -> None:
        self.initial_size = initial_size
        self.error_rate = error_rate
        self.filters: list[BloomFilter] = [BloomFilter(initial_size)]
        self._count: int = 0
        self._scale_factor = 2

    def __repr__(self) -> str:
        return f"ScalableBloomFilter(filters={len(self.filters)}, items={self._count})"

    def __str__(self) -> str:
        return f"ScalableBloomFilter with {self._count} items in {len(self.filters)} filters"

    def __len__(self) -> int:
        return self._count

    def _current_filter(self) -> BloomFilter:
        return self.filters[-1]

    def add(self, item: int | str) -> None:
        if self._current_filter().contains(item):
            return

        self._current_filter().add(item)
        self._count += 1

        if self._current_filter()._count > self.initial_size * self._scale_factor:
            new_size = self.initial_size * (self._scale_factor ** len(self.filters))
            self.filters.append(BloomFilter(new_size))

    def contains(self, item: int | str) -> bool:
        return all(f.contains(item) for f in self.filters)


if __name__ == "__main__":
    print("=== Bloom Filter ===")
    bf = BloomFilter(size=100, num_hashes=3)

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in items:
        bf.add(item)

    print(f"Added {bf._count} items")

    print(f"\nContains 5: {bf.contains(5)}")
    print(f"Contains 11 (not added): {bf.contains(11)}")

    print(f"\nFalse positive rate: {bf.false_positive_rate():.4f}")

    print("\n=== Set Operations ===")
    bf1 = BloomFilter(size=50, num_hashes=2)
    bf2 = BloomFilter(size=50, num_hashes=2)

    for i in range(1, 11):
        bf1.add(i)
    for i in range(6, 16):
        bf2.add(i)

    print(f"bf1 contains 5: {bf1.contains(5)}")
    print(f"bf2 contains 5: {bf2.contains(5)}")
    print(f"bf1 contains 15: {bf1.contains(15)}")
    print(f"bf2 contains 15: {bf2.contains(15)}")

    print("\n=== Counting Bloom Filter ===")
    cbf = CountingBloomFilter(size=100, num_hashes=3)

    for _ in range(5):
        cbf.add("item1")
    for _ in range(3):
        cbf.add("item2")
    for _ in range(7):
        cbf.add("item3")

    print(f"Count of item1: {cbf.count('item1')}")
    print(f"Count of item2: {cbf.count('item2')}")
    print(f"Count of item3: {cbf.count('item3')}")
    print(f"Count of item4: {cbf.count('item4')}")

    print("\n=== Scalable Bloom Filter ===")
    sbf = ScalableBloomFilter(initial_size=50)

    for i in range(100):
        sbf.add(i)

    print(f"Added {len(sbf)} items")
    print(f"Number of filters: {len(sbf.filters)}")
    print(f"Contains 50: {sbf.contains(50)}")
    print(f"Contains 150: {sbf.contains(150)}")
