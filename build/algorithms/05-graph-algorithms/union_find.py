"""
Union-Find (Disjoint Set Union) Data Structure

Union-Find efficiently tracks connected components and supports two operations:
- find(v): Find which set contains v
- union(u, v): Unite sets containing u and v

Time Complexity:
    - Construction: O(V)
    - Find: O(α(V)) - α is number of disjoint sets
    - Union: O(α(V)) - α depends on union order
    Space Complexity: O(V)

APPLICATIONS:
    - Kruskal's algorithm for MST
    - Connected components in undirected graphs
    - Network connectivity
    - Image processing (connected regions)
"""

from typing import List, Tuple, Set, Dict, Optional, Any


class UnionFind:
    """
    Union-Find data structure for efficient set operations.
    """

    def __init__(self, elements: List[Any]):
        self.elements = elements
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x: Any) -> Any:
        """
        Find root of element with path compression.

        PATH COMPRESSION:
        On find, update parent pointers to point directly to root.
        This flattens the tree, making future finds O(1).

        Time Complexity: O(α(n)) amortized over operations
        Space Complexity: O(1) for recursion
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: Any, y: Any) -> bool:
        """
        Unite two sets by rank.

        UNION BY RANK:
        - Attach shorter tree to root of taller tree
        - If ranks equal, arbitrarily choose one as root

        Time Complexity: O(α(n)) for find operations
        Space Complexity: O(1)
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x: Any, y: Any) -> bool:
        """Check if two elements are in same set."""
        return self.find(x) == self.find(y)

    def count(self) -> int:
        """Count number of disjoint sets."""
        roots = set()
        for x in self.elements:
            roots.add(self.find(x))
        return len(roots)

    def get_set(self, x: Any) -> Set[Any]:
        """Get all elements in the same set as x."""
        root = self.find(x)
        return {elem for elem in self.elements if self.find(elem) == root}


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("UNION-FIND DEMONSTRATION")
    print("=" * 60)

    # Basic operations
    uf = UnionFind([1, 2, 3, 4, 5])
    print(f"   Elements: {uf.elements}")

    print(f"   Find(3): {uf.find(3)}")
    print(f"   Find(1): {uf.find(1)}")

    # Union operation
    print("\n2. Union Operation")
    print(f"   Union(1, 2): {uf.union(1, 2)}")
    print(f"   Find(1) after union: {uf.find(1)}")
    print(f"   Find(2) after union: {uf.find(2)}")
    print(f"   Sets count: {uf.count()}")

    print("\n" + "=" * 60)
    print("All tests completed!")
