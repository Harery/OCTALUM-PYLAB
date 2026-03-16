# Graphs

Network structures with nodes (vertices) and edges.

## Overview

```
    A --- B
    |     |
    C --- D
```

## Graph Representations

### Adjacency List

```python
# Dictionary of sets
graph: dict[str, set[str]] = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}
```

### Adjacency Matrix

```python
# 2D array
#   A  B  C  D
# A[0, 1, 1, 0]
# B[1, 0, 0, 1]
# C[1, 0, 0, 1]
# D[0, 1, 1, 0]
```

## Graph Traversals

### BFS (Breadth-First Search)

```python
from collections import deque

def bfs(graph: dict[str, set[str]], start: str) -> list[str]:
    visited: set[str] = set()
    queue: deque[str] = deque([start])
    result: list[str] = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, set()) - visited)

    return result
```

### DFS (Depth-First Search)

```python
def dfs(graph: dict[str, set[str]], start: str, visited: set[str] | None = None) -> list[str]:
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, set()):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result
```

## Common Algorithms

### Shortest Path (Dijkstra)

```python
import heapq

def dijkstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, int]:
    distances: dict[str, int] = {start: 0}
    pq: list[tuple[int, str]] = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances.get(node, float('inf')):
            continue
        for neighbor, weight in graph.get(node, {}).items():
            new_dist = dist + weight
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances
```

### Detect Cycle

```python
def has_cycle(graph: dict[str, set[str]]) -> bool:
    visited: set[str] = set()
    rec_stack: set[str] = set()

    def dfs(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    return any(dfs(node) for node in graph if node not in visited)
```

### Topological Sort

```python
def topological_sort(graph: dict[str, set[str]]) -> list[str]:
    visited: set[str] = set()
    stack: list[str] = []

    def dfs(node: str) -> None:
        visited.add(node)
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]
```

## Time Complexity

| Operation | Adjacency List | Adjacency Matrix |
|-----------|----------------|------------------|
| Add Vertex | O(1) | O(V²) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V + E) | O(V²) |
| Remove Edge | O(E) | O(1) |
| Query | O(V) | O(1) |

## When to Use

- Social networks
- Maps and navigation
- Dependency resolution
- Network analysis

## Practice Files

- `build/data-structures/07-graphs/graph_basics.py`
- `build/data-structures/07-graphs/bfs_dfs.py`
- `build/data-structures/07-graphs/shortest_path.py`

## Next Phase

Continue to [Algorithms](../algorithms/index.md).
