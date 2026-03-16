"""
Adjacency List Graph Module
===========================
Graph implementation using adjacency list representation.

Time Complexity:
- Add vertex: O(1)
- Add edge: O(1)
- Remove vertex: O(V + E)
- Remove edge: O(E)
- Check edge: O(degree(v))
- Get neighbors: O(degree(v))

Space Complexity: O(V + E)
"""

from __future__ import annotations


class GraphAdjacencyList:
    """
    Undirected graph using adjacency list.
    """

    def __init__(self) -> None:
        self.adjacency_list: dict[int, list[int]] = {}
        self._edge_count: int = 0

    def __repr__(self) -> str:
        return f"Graph(vertices={len(self.adjacency_list)}, edges={self._edge_count})"

    def __str__(self) -> str:
        lines = [f"Graph with {len(self.adjacency_list)} vertices:"]
        for vertex in sorted(self.adjacency_list.keys()):
            neighbors = sorted(self.adjacency_list[vertex])
            lines.append(f"  {vertex}: {neighbors}")
        return "\n".join(lines)

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1: int, v2: int) -> None:
        self.add_vertex(v1)
        self.add_vertex(v2)

        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            self._edge_count += 1

    def remove_vertex(self, vertex: int) -> None:
        if vertex not in self.adjacency_list:
            return

        for neighbor in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor].remove(vertex)
            self._edge_count -= 1

        del self.adjacency_list[vertex]

    def remove_edge(self, v1: int, v2: int) -> None:
        if v1 in self.adjacency_list and v2 in self.adjacency_list[v1]:
            self.adjacency_list[v1].remove(v2)
            self.adjacency_list[v2].remove(v1)
            self._edge_count -= 1

    def has_vertex(self, vertex: int) -> bool:
        return vertex in self.adjacency_list

    def has_edge(self, v1: int, v2: int) -> bool:
        return (v1 in self.adjacency_list and
                v2 in self.adjacency_list[v1])

    def get_neighbors(self, vertex: int) -> list[int]:
        return self.adjacency_list.get(vertex, []).copy()

    def get_vertices(self) -> list[int]:
        return list(self.adjacency_list.keys())

    def vertex_count(self) -> int:
        return len(self.adjacency_list)

    def edge_count(self) -> int:
        return self._edge_count

    def degree(self, vertex: int) -> int:
        return len(self.adjacency_list.get(vertex, []))

    def bfs(self, start: int) -> list[int]:
        if start not in self.adjacency_list:
            return []

        visited: set[int] = set()
        result: list[int] = []
        queue: list[int] = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start: int) -> list[int]:
        if start not in self.adjacency_list:
            return []

        visited: set[int] = set()
        result: list[int] = []

        def dfs_recursive(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)

            for neighbor in sorted(self.adjacency_list[vertex]):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def dfs_iterative(self, start: int) -> list[int]:
        if start not in self.adjacency_list:
            return []

        visited: set[int] = set()
        result: list[int] = []
        stack: list[int] = [start]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor in sorted(self.adjacency_list[vertex], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    def connected_components(self) -> list[list[int]]:
        visited: set[int] = set()
        components: list[list[int]] = []

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = self.bfs(vertex)
                components.append(component)
                visited.update(component)

        return components

    def is_connected(self) -> bool:
        if not self.adjacency_list:
            return True
        return len(self.bfs(next(iter(self.adjacency_list)))) == len(self.adjacency_list)

    def shortest_path(self, start: int, end: int) -> list[int] | None:
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return None

        if start == end:
            return [start]

        visited: set[int] = {start}
        parent: dict[int, int] = {}
        queue: list[int] = [start]

        while queue:
            vertex = queue.pop(0)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = vertex
                    queue.append(neighbor)

                    if neighbor == end:
                        path = [end]
                        current = end
                        while current in parent:
                            current = parent[current]
                            path.append(current)
                        return list(reversed(path))

        return None

    def has_cycle(self) -> bool:
        visited: set[int] = set()

        def dfs_cycle(vertex: int, parent: int | None) -> bool:
            visited.add(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True

            return False

        for vertex in self.adjacency_list:
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True

        return False

    def is_bipartite(self) -> bool:
        if not self.adjacency_list:
            return True

        color: dict[int, int] = {}

        for start in self.adjacency_list:
            if start in color:
                continue

            queue: list[int] = [start]
            color[start] = 0

            while queue:
                vertex = queue.pop(0)

                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[vertex]
                        queue.append(neighbor)
                    elif color[neighbor] == color[vertex]:
                        return False

        return True


class DirectedGraph:
    """
    Directed graph using adjacency list.
    """

    def __init__(self) -> None:
        self.adjacency_list: dict[int, list[int]] = {}
        self._edge_count: int = 0

    def __repr__(self) -> str:
        return f"DirectedGraph(vertices={len(self.adjacency_list)}, edges={self._edge_count})"

    def __str__(self) -> str:
        lines = [f"Directed Graph with {len(self.adjacency_list)} vertices:"]
        for vertex in sorted(self.adjacency_list.keys()):
            neighbors = sorted(self.adjacency_list[vertex])
            lines.append(f"  {vertex} -> {neighbors}")
        return "\n".join(lines)

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        if to_vertex not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(to_vertex)
            self._edge_count += 1

    def remove_edge(self, from_vertex: int, to_vertex: int) -> None:
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].remove(to_vertex)
            self._edge_count -= 1

    def has_edge(self, from_vertex: int, to_vertex: int) -> bool:
        return (from_vertex in self.adjacency_list and
                to_vertex in self.adjacency_list[from_vertex])

    def in_degree(self, vertex: int) -> int:
        count = 0
        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                count += 1
        return count

    def out_degree(self, vertex: int) -> int:
        return len(self.adjacency_list.get(vertex, []))

    def topological_sort(self) -> list[int] | None:
        in_degree: dict[int, int] = {v: 0 for v in self.adjacency_list}

        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                in_degree[neighbor] += 1

        queue: list[int] = [v for v, d in in_degree.items() if d == 0]
        result: list[int] = []

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbor in self.adjacency_list[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(self.adjacency_list):
            return None

        return result

    def has_cycle(self) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        color: dict[int, int] = {v: WHITE for v in self.adjacency_list}

        def dfs(vertex: int) -> bool:
            color[vertex] = GRAY

            for neighbor in self.adjacency_list[vertex]:
                if color[neighbor] == GRAY:
                    return True
                if color[neighbor] == WHITE and dfs(neighbor):
                    return True

            color[vertex] = BLACK
            return False

        for vertex in self.adjacency_list:
            if color[vertex] == WHITE:
                if dfs(vertex):
                    return True

        return False


if __name__ == "__main__":
    print("=== Undirected Graph ===")
    g = GraphAdjacencyList()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(g)

    print(f"\nBFS from 0: {g.bfs(0)}")
    print(f"DFS from 0: {g.dfs(0)}")
    print(f"Shortest path 0->3: {g.shortest_path(0, 3)}")
    print(f"Has cycle: {g.has_cycle()}")
    print(f"Is bipartite: {g.is_bipartite()}")

    print("\n=== Directed Graph ===")
    dg = DirectedGraph()
    dg.add_edge(5, 2)
    dg.add_edge(5, 0)
    dg.add_edge(4, 0)
    dg.add_edge(4, 1)
    dg.add_edge(2, 3)
    dg.add_edge(3, 1)
    print(dg)

    print(f"\nTopological sort: {dg.topological_sort()}")
    print(f"Has cycle: {dg.has_cycle()}")
