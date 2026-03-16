"""
Breadth-First Search (BFS) Algorithm

BFS explores a graph level by level, visiting all neighbors of a node
before moving to the next level. It uses a queue to maintain the
frontier of nodes to visit.

KEY PROPERTIES:
    - Finds shortest path in unweighted graphs
    - Explores nodes in order of distance from source
    - Uses queue (FIFO) for frontier

Time Complexity: O(V + E) where V = vertices, E = edges
Space Complexity: O(V) for visited set and queue

COMMON USES:
    - Shortest path in unweighted graphs
    - Level-order traversal
    - Finding connected components
    - Checking bipartiteness
"""

from collections import deque
from typing import Dict, List, Set, Optional, Callable, Any


def bfs_adj_list(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    BFS on adjacency list representation.

    ALGORITHM:
    1. Initialize queue with start node, mark as visited
    2. While queue not empty:
       a. Dequeue node
       b. Add to result
       c. For each unvisited neighbor, enqueue and mark visited

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Args:
        graph: Dict mapping node to list of neighbors
        start: Starting node

    Returns:
        List of nodes in BFS order

    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: []}
        >>> bfs_adj_list(graph, 0)
        [0, 1, 2, 3]
    """
    if start not in graph:
        return []

    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_adj_matrix(matrix: List[List[int]], start: int) -> List[int]:
    """
    BFS on adjacency matrix representation.

    ADJACENCY MATRIX:
    matrix[i][j] = 1 if edge exists from i to j, 0 otherwise

    Time Complexity: O(V²)
    Space Complexity: O(V)
    """
    n = len(matrix)
    if start < 0 or start >= n:
        return []

    visited = [False] * n
    result = []
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


def bfs_shortest_path(graph: Dict[Any, List[Any]], start: Any, end: Any) -> Optional[List[Any]]:
    """
    Find shortest path using BFS.

    WHY BFS FINDS SHORTEST PATH:
    BFS explores nodes in order of distance from start.
    First time we reach end, we have shortest path.

    TRACKING PATH:
    Store parent of each node, then reconstruct path.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start == end:
        return [start]

    if start not in graph:
        return None

    visited = {start}
    parent = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

                if neighbor == end:
                    path = []
                    current = end
                    while current is not None:
                        path.append(current)
                        current = parent[current]
                    return path[::-1]

    return None


def bfs_distance(graph: Dict[Any, List[Any]], start: Any) -> Dict[Any, int]:
    """
    Compute distance from start to all reachable nodes.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start not in graph:
        return {}

    distances = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        current_dist = distances[node]

        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)

    return distances


def bfs_level_order(graph: Dict[Any, List[Any]], start: Any) -> List[List[Any]]:
    """
    BFS returning nodes grouped by level/distance.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start not in graph:
        return []

    visited = {start}
    queue = deque([start])
    levels = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        levels.append(level)

    return levels


def bfs_connected_components(graph: Dict[Any, List[Any]]) -> List[Set[Any]]:
    """
    Find all connected components using BFS.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = set()
            queue = deque([node])
            visited.add(node)

            while queue:
                current = queue.popleft()
                component.add(current)

                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components


def bfs_bipartite(graph: Dict[Any, List[Any]]) -> bool:
    """
    Check if graph is bipartite using BFS.

    BIPARTITE GRAPH:
    Can color vertices with 2 colors such that no adjacent
    vertices have same color.

    APPROACH:
    BFS and alternate colors level by level.
    If conflict found, graph is not bipartite.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    color = {}

    for start in graph:
        if start in color:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in graph.get(node, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

    return True


def bfs_grid(grid: List[List[str]], start: tuple[int, int],
             is_valid: Callable[[int, int], bool]) -> Set[tuple[int, int]]:
    """
    BFS on 2D grid.

    Args:
        grid: 2D grid
        start: Starting position (row, col)
        is_valid: Function to check if cell is traversable

    Returns:
        Set of reachable positions
    """
    if not grid:
        return set()

    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and is_valid(nr, nc)):
                visited.add((nr, nc))
                queue.append((nr, nc))

    return visited


def bfs_with_callback(graph: Dict[Any, List[Any]], start: Any,
                      callback: Callable[[Any], None]) -> None:
    """
    BFS with callback for each visited node.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start not in graph:
        return

    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        callback(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BREADTH-FIRST SEARCH DEMONSTRATION")
    print("=" * 60)

    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3],
        3: [4],
        4: []
    }

    # Basic BFS
    print("\n1. Basic BFS Traversal")
    print(f"   Graph: {graph}")
    print(f"   BFS from 0: {bfs_adj_list(graph, 0)}")

    # Shortest path
    print("\n2. Shortest Path (Unweighted)")
    print(f"   Path from 0 to 4: {bfs_shortest_path(graph, 0, 4)}")

    # Distances
    print("\n3. Distances from Source")
    print(f"   Distances from 0: {bfs_distance(graph, 0)}")

    # Level order
    print("\n4. Level Order")
    levels = bfs_level_order(graph, 0)
    for i, level in enumerate(levels):
        print(f"   Level {i}: {level}")

    # Bipartite check
    print("\n5. Bipartite Check")
    bipartite_graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    non_bipartite = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print(f"   Bipartite graph: {bfs_bipartite(bipartite_graph)}")
    print(f"   Non-bipartite (triangle): {bfs_bipartite(non_bipartite)}")

    # Connected components
    print("\n6. Connected Components")
    disconnected = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
    components = bfs_connected_components(disconnected)
    print(f"   Graph: {disconnected}")
    print(f"   Components: {components}")

    print("\n" + "=" * 60)
    print("All tests completed!")
