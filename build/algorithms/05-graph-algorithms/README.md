# Graph Algorithms

Comprehensive implementations of fundamental graph algorithms.

## Algorithm Overview

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| BFS | O(V+E) | O(V) | Shortest path (unweighted) |
| DFS | O(V+E) | O(V) | Path finding, cycles |
| Dijkstra | O((V+E)log V) | O(V) | Shortest path (weighted) |
| Topological Sort | O(V+E) | O(V) | DAG ordering |
| Union-Find | O(α(V)) | O(V) | Connected components |

## Files

- `bfs.py` - Breadth-first search, shortest path, bipartite check
- `dfs.py` - Depth-first search, cycle detection, topological sort
- `dijkstra.py` - Shortest path with non-negative weights
- `topological_sort.py` - Kahn's and DFS-based implementations
- `union_find.py` - Disjoint set union with path compression

## Quick Selection

```
Need shortest path?
├── Unweighted graph → BFS
└── Weighted graph
    ├── Non-negative weights → Dijkstra
    └── Negative weights → Bellman-Ford (not implemented)

Need to detect cycles?
├── Directed → DFS with 3-color marking
└── Undirected → DFS with parent tracking

Need to process dependencies?
└── Topological Sort (Kahn's or DFS)

Need connected components?
└── Union-Find (dynamic) or DFS/BFS (static)
```

## Key Takeaways

1. **BFS finds shortest path** in unweighted graphs
2. **DFS explores deeply** - good for backtracking
3. **Dijkstra requires non-negative weights**
4. **Union-Find is optimal** for dynamic connectivity
