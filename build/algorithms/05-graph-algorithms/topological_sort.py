"""
Topological Sort Algorithm

Topological sorting orders vertices of a DAG (Directed Acyclic Graph) such that
for every directed edge (u, v), vertex u comes before v in the ordering.

KEY INSIGHT:
    Only works on DAGs (Directed Acyclic Graphs).
    If graph has cycle, topological sort is impossible.

Time Complexity: O(V + E)
Space Complexity: O(V)

APPLICATIONS:
    - Task scheduling (prerequisites)
    - Build systems (dependencies)
    - Course prerequisites
    - Symbol resolution in linker
"""

from collections import deque
from typing import Dict, List, Set, Any, Optional


def kahn_topological_sort(graph: Dict[Any, List[Any]]) -> Optional[List[Any]]:
    """
    Kahn's algorithm (BFS-based topological sort).

    ALGORITHM:
    1. Compute in-degree of all vertices
    2. Add all vertices with 0 in-degree to queue
    3. While queue not empty:
       a. Remove vertex, add to result
       b. Decrease in-degree of neighbors
       c. If neighbor's in-degree becomes 0, add to queue
    4. If result contains all vertices, return it
       Otherwise, graph has cycle

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Args:
        graph: Dict mapping node to list of neighbors

    Returns:
        Topological order, or None if cycle exists
    """
    in_degree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(in_degree):
        return None

    return result


def dfs_topological_sort(graph: Dict[Any, List[Any]]) -> Optional[List[Any]]:
    """
    DFS-based topological sort.

    ALGORITHM:
    1. For each unvisited node, do DFS
    2. After visiting all neighbors, add node to result
    3. Reverse result at end

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    state = {node: UNVISITED for node in graph}
    result = []
    has_cycle = [False]

    def dfs(node: Any) -> None:
        if state[node] == VISITING:
            has_cycle[0] = True
            return
        if state[node] == VISITED:
            return

        state[node] = VISITING

        for neighbor in graph.get(node, []):
            if neighbor not in state:
                state[neighbor] = UNVISITED
            dfs(neighbor)

        state[node] = VISITED
        result.append(node)

    for node in graph:
        if state[node] == UNVISITED:
            dfs(node)

    if has_cycle[0]:
        return None

    return result[::-1]


def topological_sort_all(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Generate all possible topological orderings.

    Time Complexity: O(V! * V) worst case
    Space Complexity: O(V)
    """
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    result = []

    def backtrack(current: List[int], in_deg: Dict[int, int], visited: Set[int]) -> None:
        if len(current) == len(graph):
            result.append(current[:])
            return

        for node in graph:
            if node not in visited and in_deg.get(node, 0) == 0:
                visited.add(node)
                current.append(node)

                new_deg = in_deg.copy()
                for neighbor in graph.get(node, []):
                    new_deg[neighbor] = new_deg.get(neighbor, 0) - 1

                backtrack(current, new_deg, visited)

                current.pop()
                visited.remove(node)

    backtrack([], in_degree.copy(), set())
    return result


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TOPOLOGICAL SORT DEMONSTRATION")
    print("=" * 60)

    dag = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }

    print("\n1. Kahn's Algorithm (BFS-based)")
    print(f"   Graph: {dag}")
    print(f"   Order: {kahn_topological_sort(dag)}")

    print("\n2. DFS-based")
    print(f"   Order: {dfs_topological_sort(dag)}")

    print("\n3. Cycle Detection")
    cyclic = {0: [1], 1: [2], 2: [0]}
    print(f"   Cyclic graph: {cyclic}")
    print(f"   Kahn result: {kahn_topological_sort(cyclic)}")
    print(f"   DFS result: {dfs_topological_sort(cyclic)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
