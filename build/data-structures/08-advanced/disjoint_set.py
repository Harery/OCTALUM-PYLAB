"""
Disjoint Set (Union-Find) Module
================================
Data structure for tracking connected components efficiently.

Operations:
- Make-Set: Create a new set containing a single element - O(1)
- Union: Merge two sets - O(α(n)) amortized, ~O(1)
- Find: Find which set an element belongs to - O(α(n)) amortized, ~O(1)
- Connected: Check if two elements are in the same set - O(α(n))

Space Complexity: O(n)
"""

from __future__ import annotations


class DisjointSet:
    """
    Disjoint Set data structure with union by rank and path compression.
    """

    def __init__(self, size: int) -> None:
        self.parent: list[int] = list(range(size))
        self.rank: list[int] = [0] * size
        self._count: int = size

    def __repr__(self) -> str:
        return f"DisjointSet(size={len(self.parent)}, sets={self.set_count()})"

    def __str__(self) -> str:
        return f"DisjointSet with {self.set_count()} disjoint sets"

    def __len__(self) -> int:
        return len(self.parent)

    @property
    def set_count(self) -> int:
        count = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                count += 1
        return count

    def find(self, x: int) -> int:
        if x < 0 or x >= len(self.parent):
            raise IndexError(f"Element {x} out of range")

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def get_sets(self) -> dict[int, list[int]]:
        sets: dict[int, list[int]] = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in sets:
                sets[root] = []
            sets[root].append(i)
        return sets


class WeightedDisjointSet:
    """
    Disjoint Set with weighted union (union by size).
    """

    def __init__(self, size: int) -> None:
        self.parent: list[int] = list(range(size))
        self.size: list[int] = [1] * size
        self._count: int = size

    def __repr__(self) -> str:
        return f"WeightedDisjointSet(size={len(self.parent)})"

    def find(self, x: int) -> int:
        if x < 0 or x >= len(self.parent):
            raise IndexError(f"Element {x} out of range")

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]


def count_islands(grid: list[list[str]]) -> int:
    """
    Count number of islands in a grid using Disjoint Set.

    An island is a group of '1's connected horizontally or vertically.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    ds = DisjointSet(rows * cols)

    def index(r: int, c: int) -> int:
        return r * cols + c

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue

            if c > 0 and grid[r][c - 1] == "1":
                ds.union(index(r, c), index(r, c - 1))

            if r > 0 and grid[r - 1][c] == "1":
                ds.union(index(r, c), index(r - 1, c))

    land_roots: set[int] = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                land_roots.add(ds.find(index(r, c)))

    return len(land_roots)


def min_spanning_tree_kruskal(edges: list[tuple[int, int, int]], n: int) -> list[tuple[int, int, int]]:
    """
    Find minimum spanning tree using Kruskal's algorithm.

    Args:
        edges: List of (u, v, weight) tuples
        n: Number of vertices

    Returns:
        List of edges in the MST
    """
    edges = sorted(edges, key=lambda x: x[2])
    ds = DisjointSet(n)
    mst: list[tuple[int, int, int]] = []

    for u, v, weight in edges:
        if not ds.connected(u, v):
            ds.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break

    return mst


if __name__ == "__main__":
    print("=== Disjoint Set ===")
    ds = DisjointSet(10)

    print(f"Initial sets: {ds.set_count}")

    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(0, 2)

    print(f"After unions: {ds.set_count}")
    print(f"0 and 1 connected: {ds.connected(0, 1)}")
    print(f"0 and 2 connected: {ds.connected(0, 2)}")
    print(f"0 and 4 connected: {ds.connected(0, 4)}")

    print("\nSets:")
    for root, elements in ds.get_sets().items():
        print(f"  {root}: {elements}")

    print("\n=== Count Islands ===")
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    for row in grid:
        print(f"  {row}")

    print(f"Number of islands: {count_islands(grid)}")

    print("\n=== Minimum Spanning Tree (Kruskal) ===")
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (1, 2, 2),
        (1, 3, 1),
        (2, 3, 5),
    ]

    print(f"Edges: {edges}")
    mst = min_spanning_tree_kruskal(edges, 4)
    print(f"MST edges: {mst}")
    total_weight = sum(e[2] for e in mst)
    print(f"Total weight: {total_weight}")
