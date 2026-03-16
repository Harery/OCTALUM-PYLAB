# Graph Algorithms

Solve network and connectivity problems.

## Graph Representations

```python
# Adjacency List
graph: dict[int, list[int]] = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
```

## Traversal Algorithms

### BFS (Breadth-First Search)

```python
from collections import deque

def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    visited: set[int] = set()
    queue: deque[int] = deque([start])
    result: list[int] = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result
```

### DFS (Depth-First Search)

```python
def dfs(graph: dict[int, list[int]], start: int, visited: set[int] | None = None) -> list[int]:
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result
```

## Shortest Path

### Dijkstra's Algorithm

```python
import heapq

def dijkstra(graph: dict[int, dict[int, int]], start: int) -> dict[int, int]:
    distances: dict[int, int] = {start: 0}
    pq: list[tuple[int, int]] = [(0, start)]

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

### Bellman-Ford

```python
def bellman_ford(edges: list[tuple[int, int, int]], n: int, start: int) -> dict[int, int]:
    distances: dict[int, int] = {i: float('inf') for i in range(n)}
    distances[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances
```

## Minimum Spanning Tree

### Kruskal's Algorithm

```python
def kruskal(edges: list[tuple[int, int, int]], n: int) -> list[tuple[int, int, int]]:
    parent = list(range(n))

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> None:
        parent[find(x)] = find(y)

    edges.sort(key=lambda e: e[2])
    mst: list[tuple[int, int, int]] = []

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    return mst
```

## Topological Sort

```python
def topological_sort(graph: dict[int, list[int]], n: int) -> list[int]:
    in_degree = [0] * n
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result: list[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []
```

## Cycle Detection

```python
def has_cycle(graph: dict[int, list[int]], n: int) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node: int) -> bool:
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    return any(dfs(i) for i in range(n) if color[i] == WHITE)
```

## Algorithm Complexity

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V) |
| Bellman-Ford | O(V * E) | O(V) |
| Kruskal | O(E log E) | O(V) |
| Topological Sort | O(V + E) | O(V) |

## Practice Files

- `build/algorithms/05-graph-algorithms/bfs_dfs.py`
- `build/algorithms/05-graph-algorithms/shortest_path.py`
- `build/algorithms/05-graph-algorithms/mst.py`

## Next Phase

Continue to [Patterns](../patterns/index.md).
