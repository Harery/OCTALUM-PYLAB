"""
Dijkstra's Shortest Path Algorithm

Dijkstra's algorithm finds the shortest paths from a source vertex to all
other vertices in a weighted graph with non-negative edge weights.

KEY INSIGHT:
    Always process the vertex with minimum distance next.
    This ensures we never need to update a processed vertex.

Time Complexity: O((V + E) log V) with min-heap
Space Complexity: O(V + E)

CONSTRAINT: Edge weights must be non-negative!

WHEN TO USE:
    - Shortest path with non-negative weights
    - GPS navigation
    - Network routing

WHEN NOT TO USE:
    - Negative weights (use Bellman-Ford)
    - Unweighted graphs (use BFS)
"""

import heapq
from typing import Dict, List, Tuple, Optional, Any


def dijkstra(graph: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Dict[Any, int]:
    """
    Dijkstra's algorithm returning shortest distances.

    ALGORITHM:
    1. Initialize distances: start = 0, others = infinity
    2. Use min-heap with (distance, node) pairs
    3. Extract minimum, update neighbors if shorter path found
    4. Repeat until heap empty

    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)

    Args:
        graph: Dict mapping node to list of (neighbor, weight) tuples
        start: Source vertex

    Returns:
        Dict mapping node to shortest distance from start

    Example:
        >>> graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        >>> dijkstra(graph, 0)
        {0: 0, 1: 3, 2: 1, 3: 4}
    """
    distances = {start: 0}
    heap = [(0, start)]
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor in visited:
                continue

            new_dist = dist + weight

            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


def dijkstra_with_path(graph: Dict[Any, List[Tuple[Any, int]]],
                       start: Any, end: Any) -> Tuple[int, List[Any]]:
    """
    Dijkstra returning shortest path and distance.

    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)

    Returns:
        Tuple of (distance, path list)

    Raises:
        ValueError: If no path exists
    """
    distances = {start: 0}
    previous = {start: None}
    heap = [(0, start)]
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)

        if node in visited:
            continue
        visited.add(node)

        if node == end:
            break

        for neighbor, weight in graph.get(node, []):
            if neighbor in visited:
                continue

            new_dist = dist + weight

            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    if end not in distances:
        raise ValueError(f"No path from {start} to {end}")

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]

    return distances[end], path[::-1]


def dijkstra_all_paths(graph: Dict[Any, List[Tuple[Any, int]]],
                       start: Any) -> Tuple[Dict[Any, int], Dict[Any, Any]]:
    """
    Dijkstra returning distances and previous nodes for path reconstruction.

    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """
    distances = {start: 0}
    previous: Dict[Any, Any] = {start: None}
    heap = [(0, start)]
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor in visited:
                continue

            new_dist = dist + weight

            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    return distances, previous


def reconstruct_path(previous: Dict[Any, Any], start: Any, end: Any) -> Optional[List[Any]]:
    """
    Reconstruct path from previous node mapping.
    """
    if end not in previous:
        return None

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous.get(current)

    return path[::-1]


def dijkstra_adj_matrix(matrix: List[List[int]], start: int) -> List[int]:
    """
    Dijkstra on adjacency matrix.

    Time Complexity: O(V²) - better for dense graphs
    Space Complexity: O(V)
    """
    n = len(matrix)
    INF = float('inf')

    distances = [INF] * n
    distances[start] = 0
    visited = [False] * n

    for _ in range(n):
        min_dist = INF
        u = -1

        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if not visited[v] and matrix[u][v] > 0:
                new_dist = distances[u] + matrix[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist

    return distances


def dijkstra_grid(grid: List[List[int]], start: Tuple[int, int],
                  end: Tuple[int, int]) -> int:
    """
    Dijkstra on 2D grid with costs.

    grid[i][j] = cost to enter cell (i, j)
    Find minimum cost path from start to end.

    Time Complexity: O(V log V) where V = rows * cols
    Space Complexity: O(V)
    """
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    distances = {start: grid[start[0]][start[1]]}
    heap = [(grid[start[0]][start[1]], start)]
    visited = set()

    while heap:
        dist, (r, c) = heapq.heappop(heap)

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == end:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                new_dist = dist + grid[nr][nc]

                if (nr, nc) not in distances or new_dist < distances[(nr, nc)]:
                    distances[(nr, nc)] = new_dist
                    heapq.heappush(heap, (new_dist, (nr, nc)))

    return -1


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DIJKSTRA'S ALGORITHM DEMONSTRATION")
    print("=" * 60)

    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

    # Basic Dijkstra
    print("\n1. Basic Dijkstra (Shortest Distances)")
    print(f"   Graph: {graph}")
    print(f"   Distances from 0: {dijkstra(graph, 0)}")

    # Path reconstruction
    print("\n2. Shortest Path")
    dist, path = dijkstra_with_path(graph, 0, 3)
    print(f"   Distance 0→3: {dist}")
    print(f"   Path: {path}")

    # All paths
    print("\n3. All Shortest Paths from Source")
    distances, previous = dijkstra_all_paths(graph, 0)
    print(f"   Distances: {distances}")
    print(f"   Previous: {previous}")
    for node in [1, 2, 3]:
        p = reconstruct_path(previous, 0, node)
        print(f"   Path to {node}: {p}")

    # Adjacency matrix
    print("\n4. Dijkstra on Adjacency Matrix")
    matrix = [
        [0, 4, 1, 0],
        [4, 0, 2, 1],
        [1, 2, 0, 5],
        [0, 1, 5, 0]
    ]
    print(f"   Distances from 0: {dijkstra_adj_matrix(matrix, 0)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
