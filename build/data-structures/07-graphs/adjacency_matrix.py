"""
Adjacency Matrix Graph Module
=============================
Graph implementation using adjacency matrix representation.

Time Complexity:
- Add vertex: O(V²)
- Add edge: O(1)
- Remove vertex: O(V²)
- Remove edge: O(1)
- Check edge: O(1)
- Get neighbors: O(V)

Space Complexity: O(V²)
"""

from __future__ import annotations


class GraphAdjacencyMatrix:
    """
    Undirected graph using adjacency matrix.
    """

    def __init__(self, num_vertices: int = 0) -> None:
        self.num_vertices: int = num_vertices
        self.matrix: list[list[int]] = [[0] * num_vertices for _ in range(num_vertices)]
        self._edge_count: int = 0

    def __repr__(self) -> str:
        return f"GraphMatrix(vertices={self.num_vertices}, edges={self._edge_count})"

    def __str__(self) -> str:
        lines = [f"Adjacency Matrix ({self.num_vertices} vertices):"]
        if self.num_vertices == 0:
            return "\n".join(lines)

        header = "   " + " ".join(f"{i:2}" for i in range(self.num_vertices))
        lines.append(header)

        for i, row in enumerate(self.matrix):
            row_str = " ".join(f"{val:2}" for val in row)
            lines.append(f"{i:2}: {row_str}")

        return "\n".join(lines)

    def add_vertex(self) -> int:
        self.num_vertices += 1

        for row in self.matrix:
            row.append(0)

        self.matrix.append([0] * self.num_vertices)

        return self.num_vertices - 1

    def add_edge(self, v1: int, v2: int) -> None:
        if v1 < 0 or v1 >= self.num_vertices or v2 < 0 or v2 >= self.num_vertices:
            raise IndexError("Vertex index out of range")

        if self.matrix[v1][v2] == 0:
            self.matrix[v1][v2] = 1
            self.matrix[v2][v1] = 1
            self._edge_count += 1

    def remove_edge(self, v1: int, v2: int) -> None:
        if v1 < 0 or v1 >= self.num_vertices or v2 < 0 or v2 >= self.num_vertices:
            return

        if self.matrix[v1][v2] == 1:
            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0
            self._edge_count -= 1

    def has_edge(self, v1: int, v2: int) -> bool:
        if v1 < 0 or v1 >= self.num_vertices or v2 < 0 or v2 >= self.num_vertices:
            return False
        return self.matrix[v1][v2] == 1

    def get_neighbors(self, vertex: int) -> list[int]:
        if vertex < 0 or vertex >= self.num_vertices:
            return []

        neighbors: list[int] = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] == 1:
                neighbors.append(i)

        return neighbors

    def degree(self, vertex: int) -> int:
        return len(self.get_neighbors(vertex))

    def vertex_count(self) -> int:
        return self.num_vertices

    def edge_count(self) -> int:
        return self._edge_count

    def bfs(self, start: int) -> list[int]:
        if start < 0 or start >= self.num_vertices:
            return []

        visited: set[int] = set()
        result: list[int] = []
        queue: list[int] = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start: int) -> list[int]:
        if start < 0 or start >= self.num_vertices:
            return []

        visited: set[int] = set()
        result: list[int] = []

        def dfs_recursive(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def connected_components(self) -> list[list[int]]:
        visited: set[int] = set()
        components: list[list[int]] = []

        for vertex in range(self.num_vertices):
            if vertex not in visited:
                component = self.bfs(vertex)
                components.append(component)
                visited.update(component)

        return components

    def is_connected(self) -> bool:
        if self.num_vertices == 0:
            return True
        return len(self.bfs(0)) == self.num_vertices

    def has_cycle(self) -> bool:
        visited: set[int] = set()

        def dfs_cycle(vertex: int, parent: int | None) -> bool:
            visited.add(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    if dfs_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True

            return False

        for vertex in range(self.num_vertices):
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True

        return False


class WeightedGraphMatrix:
    """
    Weighted graph using adjacency matrix.

    0 indicates no edge, positive values indicate edge weight.
    """

    NO_EDGE = 0

    def __init__(self, num_vertices: int = 0) -> None:
        self.num_vertices: int = num_vertices
        self.matrix: list[list[int | float]] = [
            [self.NO_EDGE] * num_vertices for _ in range(num_vertices)
        ]
        self._edge_count: int = 0

    def __repr__(self) -> str:
        return f"WeightedGraphMatrix(vertices={self.num_vertices}, edges={self._edge_count})"

    def __str__(self) -> str:
        lines = [f"Weighted Adjacency Matrix ({self.num_vertices} vertices):"]
        if self.num_vertices == 0:
            return "\n".join(lines)

        header = "   " + " ".join(f"{i:5}" for i in range(self.num_vertices))
        lines.append(header)

        for i, row in enumerate(self.matrix):
            row_str = " ".join(f"{val:5}" if val != self.NO_EDGE else "    ∞" for val in row)
            lines.append(f"{i:2}: {row_str}")

        return "\n".join(lines)

    def add_vertex(self) -> int:
        self.num_vertices += 1

        for row in self.matrix:
            row.append(self.NO_EDGE)

        self.matrix.append([self.NO_EDGE] * self.num_vertices)

        return self.num_vertices - 1

    def add_edge(self, v1: int, v2: int, weight: int | float) -> None:
        if v1 < 0 or v1 >= self.num_vertices or v2 < 0 or v2 >= self.num_vertices:
            raise IndexError("Vertex index out of range")

        if self.matrix[v1][v2] == self.NO_EDGE:
            self._edge_count += 1

        self.matrix[v1][v2] = weight
        self.matrix[v2][v1] = weight

    def remove_edge(self, v1: int, v2: int) -> None:
        if v1 < 0 or v1 >= self.num_vertices or v2 < 0 or v2 >= self.num_vertices:
            return

        if self.matrix[v1][v2] != self.NO_EDGE:
            self.matrix[v1][v2] = self.NO_EDGE
            self.matrix[v2][v1] = self.NO_EDGE
            self._edge_count -= 1

    def get_weight(self, v1: int, v2: int) -> int | float | None:
        if v1 < 0 or v1 >= self.num_vertices or v2 < 0 or v2 >= self.num_vertices:
            return None

        weight = self.matrix[v1][v2]
        return weight if weight != self.NO_EDGE else None

    def get_neighbors(self, vertex: int) -> list[tuple[int, int | float]]:
        if vertex < 0 or vertex >= self.num_vertices:
            return []

        neighbors: list[tuple[int, int | float]] = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] != self.NO_EDGE:
                neighbors.append((i, self.matrix[vertex][i]))

        return neighbors

    def floyd_warshall(self) -> list[list[int | float]]:
        """
        Compute shortest paths between all pairs of vertices.

        Time Complexity: O(V³)
        Space Complexity: O(V²)
        """
        INF = float("inf")
        dist: list[list[int | float]] = [[INF] * self.num_vertices for _ in range(self.num_vertices)]

        for i in range(self.num_vertices):
            dist[i][i] = 0

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matrix[i][j] != self.NO_EDGE:
                    dist[i][j] = self.matrix[i][j]

        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist


if __name__ == "__main__":
    print("=== Adjacency Matrix Graph ===")
    g = GraphAdjacencyMatrix(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print(g)
    print(f"\nBFS from 0: {g.bfs(0)}")
    print(f"DFS from 0: {g.dfs(0)}")
    print(f"Neighbors of 2: {g.get_neighbors(2)}")
    print(f"Has edge 1-2: {g.has_edge(1, 2)}")
    print(f"Is connected: {g.is_connected()}")

    print("\n=== Weighted Graph Matrix ===")
    wg = WeightedGraphMatrix(4)
    wg.add_edge(0, 1, 5)
    wg.add_edge(0, 2, 3)
    wg.add_edge(1, 2, 2)
    wg.add_edge(1, 3, 6)
    wg.add_edge(2, 3, 7)

    print(wg)

    print("\nFloyd-Warshall all-pairs shortest paths:")
    dist = wg.floyd_warshall()
    for i, row in enumerate(dist):
        print(f"  From {i}: {[f'{d:.0f}' if d != float('inf') else '∞' for d in row]}")
