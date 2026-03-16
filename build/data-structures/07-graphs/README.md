# Graphs

## Overview

Graphs are non-linear data structures consisting of vertices (nodes) and edges that connect pairs of vertices. They are used to represent relationships and connections.

## Graph Representations

### Adjacency List
```
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
```

### Adjacency Matrix
```
    0  1  2  3
0 [ 0  1  1  0 ]
1 [ 1  0  1  0 ]
2 [ 1  1  0  1 ]
3 [ 0  0  1  0 ]
```

## Time Complexity Comparison

| Operation | Adjacency List | Adjacency Matrix |
|-----------|----------------|------------------|
| **Add Vertex** | O(1) | O(V²) |
| **Add Edge** | O(1) | O(1) |
| **Remove Vertex** | O(V + E) | O(V²) |
| **Remove Edge** | O(E) | O(1) |
| **Check Edge** | O(V) | O(1) |
| **Get Neighbors** | O(V) | O(V) |
| **Space** | O(V + E) | O(V²) |

## Space Complexity

| Representation | Sparse Graph | Dense Graph |
|----------------|--------------|-------------|
| **Adjacency List** | O(V + E) | O(V + E) |
| **Adjacency Matrix** | O(V²) | O(V²) |

## Graph Types

| Type | Property | Example |
|------|----------|---------|
| **Undirected** | Edges have no direction | Social network |
| **Directed** | Edges have direction | Web links |
| **Weighted** | Edges have weights | Road map |
| **Unweighted** | All edges equal | Connection exists |
| **Cyclic** | Contains cycles | Dependencies |
| **Acyclic** | No cycles | DAG |
| **Connected** | Path between any two vertices | Network |
| **Bipartite** | Two-colorable | Matching |

## Graph Traversals

### BFS (Breadth-First Search)
```
Level-by-level exploration using queue.

    0
   / \
  1   2
 / \   \
3   4   5

BFS: [0, 1, 2, 3, 4, 5]
```

Time: O(V + E), Space: O(V)

### DFS (Depth-First Search)
```
Go deep before going wide using stack/recursion.

DFS: [0, 1, 3, 4, 2, 5]
```

Time: O(V + E), Space: O(V)

## Common Graph Algorithms

### Shortest Path (Unweighted - BFS)
```python
def shortest_path(graph, start, end):
    visited = {start}
    parent = {start: None}
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            break
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)

    # Reconstruct path
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return list(reversed(path))
```

### Topological Sort (Kahn's Algorithm)
```python
def topological_sort(graph):
    in_degree = {v: 0 for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    queue = [v for v, d in in_degree.items() if d == 0]
    result = []

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else None
```

### Cycle Detection
```python
def has_cycle_undirected(graph, vertex, visited, parent):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if has_cycle_undirected(graph, neighbor, visited, vertex):
                return True
        elif neighbor != parent:
            return True
    return False
```

### Connected Components
```python
def connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = bfs(graph, vertex)
            components.append(component)
            visited.update(component)

    return components
```

## Graph Algorithm Complexities

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **BFS** | O(V + E) | O(V) | Shortest path (unweighted) |
| **DFS** | O(V + E) | O(V) | Cycle detection, connectivity |
| **Dijkstra** | O((V + E) log V) | O(V) | Shortest path (weighted) |
| **Bellman-Ford** | O(V * E) | O(V) | Shortest path with negatives |
| **Floyd-Warshall** | O(V³) | O(V²) | All-pairs shortest |
| **Topological Sort** | O(V + E) | O(V) | DAG ordering |
| **Kruskal's MST** | O(E log E) | O(V) | Minimum spanning tree |
| **Prim's MST** | O(E log V) | O(V) | Minimum spanning tree |

## When to Use Which Representation

### Adjacency List
- Sparse graphs (E << V²)
- Need to iterate over neighbors
- Memory is limited
- Frequent vertex additions

### Adjacency Matrix
- Dense graphs (E ≈ V²)
- Need O(1) edge lookup
- Fixed number of vertices
- Matrix operations needed

## Graph Applications

| Application | Graph Type | Algorithm |
|-------------|------------|-----------|
| Social networks | Undirected | BFS, communities |
| Web crawling | Directed | BFS, DFS |
| GPS navigation | Weighted | Dijkstra |
| Network flow | Weighted directed | Max flow |
| Task scheduling | DAG | Topological sort |
| Circuit design | Undirected | MST |
| Compiler | DAG | Topological sort |

## Best Practices

1. **Use adjacency list** for sparse graphs (most real-world graphs)

2. **Use BFS** for shortest path in unweighted graphs
   ```python
   queue = deque([start])
   visited = {start}
   ```

3. **Use DFS** for cycle detection and connectivity
   ```python
   visited.add(vertex)
   for neighbor in graph[vertex]:
       if neighbor not in visited:
           dfs(neighbor)
   ```

4. **Track visited** to avoid infinite loops

5. **Consider iterative** DFS for deep graphs (avoid stack overflow)

## Common Graph Problems

| Problem | Technique | Time |
|---------|-----------|------|
| Number of islands | DFS/BFS | O(V + E) |
| Clone graph | DFS + HashMap | O(V + E) |
| Course schedule | Topological sort | O(V + E) |
| Word ladder | BFS | O(V + E) |
| Bipartite check | BFS coloring | O(V + E) |
| Detect cycle | DFS/Union-Find | O(V + E) |
