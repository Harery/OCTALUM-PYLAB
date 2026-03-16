"""
Depth-First Search (DFS) Algorithm

DFS explores a graph by going as deep as possible before backtracking.
It uses a stack (or recursion) to maintain the frontier.

KEY PROPERTIES:
    - Explores deeply before backtracking
    - Uses stack (LIFO) or recursion
    - Good for path finding, cycle detection, topological sort

Time Complexity: O(V + E) where V = vertices, E = edges
Space Complexity: O(V) for visited set and recursion/stack

COMMON USES:
    - Finding paths (not necessarily shortest)
    - Cycle detection
    - Topological sorting
    - Finding strongly connected components
    - Solving mazes
"""

from typing import Dict, List, Set, Optional, Any, Callable


def dfs_recursive(graph: Dict[Any, List[Any]], start: Any,
                  visited: Set[Any] | None = None) -> List[Any]:
    """
    DFS using recursion.

    ALGORITHM:
    1. Mark current node as visited
    2. Add to result
    3. For each unvisited neighbor, recursively call DFS

    Time Complexity: O(V + E)
    Space Complexity: O(V) for recursion stack

    Args:
        graph: Dict mapping node to list of neighbors
        start: Starting node
        visited: Set of visited nodes (for recursive calls)

    Returns:
        List of nodes in DFS order
    """
    if visited is None:
        visited = set()

    if start in visited:
        return []

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


def dfs_iterative(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    DFS using explicit stack (no recursion).

    WHY ITERATIVE:
    - Avoids recursion depth limit
    - Better for very deep graphs

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start not in graph:
        return []

    visited = set()
    result = []
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        result.append(node)

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return result


def dfs_path(graph: Dict[Any, List[Any]], start: Any, end: Any,
             visited: Set[Any] | None = None) -> Optional[List[Any]]:
    """
    Find any path from start to end using DFS.

    NOTE: Not necessarily shortest path!
    Use BFS for shortest path in unweighted graphs.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if visited is None:
        visited = set()

    if start == end:
        return [start]

    if start in visited:
        return None

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_path(graph, neighbor, end, visited)
            if path:
                return [start] + path

    return None


def dfs_all_paths(graph: Dict[Any, List[Any]], start: Any, end: Any) -> List[List[Any]]:
    """
    Find all paths from start to end.

    Time Complexity: O(V + E) in best case, exponential in worst case
    Space Complexity: O(V) for current path
    """
    def backtrack(node: Any, path: List[Any], visited: Set[Any]) -> None:
        if node == end:
            all_paths.append(path[:])
            return

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                backtrack(neighbor, path, visited)
                path.pop()
                visited.remove(neighbor)

    all_paths: List[List[Any]] = []
    backtrack(start, [start], {start})
    return all_paths


def dfs_cycle_detection(graph: Dict[Any, List[Any]]) -> bool:
    """
    Detect cycle in directed graph using DFS.

    APPROACH:
    Use three states: unvisited, visiting (in current path), visited.
    If we encounter a node that's "visiting", we found a cycle.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    state = {node: UNVISITED for node in graph}

    def has_cycle(node: Any) -> bool:
        if state[node] == VISITING:
            return True
        if state[node] == VISITED:
            return False

        state[node] = VISITING

        for neighbor in graph.get(node, []):
            if neighbor in state and has_cycle(neighbor):
                return True

        state[node] = VISITED
        return False

    for node in graph:
        if state[node] == UNVISITED:
            if has_cycle(node):
                return True

    return False


def dfs_cycle_undirected(graph: Dict[Any, List[Any]]) -> bool:
    """
    Detect cycle in undirected graph.

    APPROACH:
    Track parent to avoid false positive from back edge to parent.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()

    def has_cycle(node: Any, parent: Any) -> bool:
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if has_cycle(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if has_cycle(node, None):
                return True

    return False


def dfs_topological_sort(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    Topological sort using DFS.

    PREREQUISITE: Graph must be a DAG (Directed Acyclic Graph)

    APPROACH:
    Reverse postorder of DFS gives topological order.
    Nodes with no outgoing edges finish first, so they come last
    in reverse order, meaning they're processed first in topo sort.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    result = []

    def dfs(node: Any) -> None:
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]


def dfs_connected_components(graph: Dict[Any, List[Any]]) -> List[Set[Any]]:
    """
    Find connected components in undirected graph.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    components = []

    def dfs(node: Any, component: Set[Any]) -> None:
        visited.add(node)
        component.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component: Set[Any] = set()
            dfs(node, component)
            components.append(component)

    return components


def dfs_articulation_points(graph: Dict[Any, List[Any]]) -> Set[Any]:
    """
    Find articulation points (cut vertices) using DFS.

    ARTICULATION POINT:
    A vertex whose removal disconnects the graph.

    APPROACH:
    Use discovery time and lowest reachable ancestor.
    A node is articulation point if:
    1. It's root with 2+ children
    2. It's not root and has child with low >= disc[node]

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    disc = {}
    low = {}
    parent = {}
    articulation_points = set()
    time = [0]

    def dfs(node: Any) -> None:
        children = 0
        visited.add(node)
        disc[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                children += 1
                parent[neighbor] = node
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])

                if parent.get(node) is None and children > 1:
                    articulation_points.add(node)
                elif parent.get(node) is not None and low[neighbor] >= disc[node]:
                    articulation_points.add(node)
            elif neighbor != parent.get(node):
                low[node] = min(low[node], disc[neighbor])

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)

    return articulation_points


def dfs_bridges(graph: Dict[Any, List[Any]]) -> List[tuple[Any, Any]]:
    """
    Find bridges (cut edges) using DFS.

    BRIDGE:
    An edge whose removal disconnects the graph.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    disc = {}
    low = {}
    parent = {}
    bridges = []
    time = [0]

    def dfs(node: Any) -> None:
        visited.add(node)
        disc[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                parent[neighbor] = node
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])

                if low[neighbor] > disc[node]:
                    bridges.append((node, neighbor))
            elif neighbor != parent.get(node):
                low[node] = min(low[node], disc[neighbor])

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)

    return bridges


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DEPTH-FIRST SEARCH DEMONSTRATION")
    print("=" * 60)

    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3],
        3: [4],
        4: []
    }

    # Basic DFS
    print("\n1. Basic DFS Traversal")
    print(f"   Graph: {graph}")
    print(f"   DFS recursive: {dfs_recursive(graph, 0)}")
    print(f"   DFS iterative: {dfs_iterative(graph, 0)}")

    # Path finding
    print("\n2. Path Finding")
    print(f"   Path from 0 to 4: {dfs_path(graph, 0, 4)}")

    # All paths
    print("\n3. All Paths")
    multi_path = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(f"   Graph: {multi_path}")
    print(f"   All paths 0->3: {dfs_all_paths(multi_path, 0, 3)}")

    # Cycle detection
    print("\n4. Cycle Detection")
    cyclic = {0: [1], 1: [2], 2: [0]}
    print(f"   Cyclic graph {cyclic}: {dfs_cycle_detection(cyclic)}")
    print(f"   Acyclic graph {graph}: {dfs_cycle_detection(graph)}")

    # Topological sort
    print("\n5. Topological Sort")
    dag = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(f"   Graph: {dag}")
    print(f"   Topological order: {dfs_topological_sort(dag)}")

    # Articulation points
    print("\n6. Articulation Points")
    ap_graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1, 4], 4: [3]}
    print(f"   Graph: {ap_graph}")
    print(f"   Articulation points: {dfs_articulation_points(ap_graph)}")

    # Bridges
    print("\n7. Bridges")
    print(f"   Graph: {ap_graph}")
    print(f"   Bridges: {dfs_bridges(ap_graph)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
