# Island/Matrix Traversal Pattern

## When to Use
- **2D grid/matrix problems** - games, maps, images
- **Connected components** - islands, regions
- **Flood fill** - paint bucket, area coloring
- **Shortest path in grid** - BFS when all edges same weight
- **Boundary-connected** - regions touching edge

## Key Signals
| Signal | Example |
|--------|---------|
| "Number of islands" | Count connected components |
| "Surrounded regions" | Mark from boundary |
| "Shortest path in grid" | BFS from source |
| "Flood fill" | DFS from starting point |
| "Rotting/spreading" | Multi-source BFS |

## Template Variants

### 1. DFS Recursive
```python
def dfs(r, c):
    if out_of_bounds or visited or invalid:
        return
    visited.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)
```

### 2. BFS Iterative
```python
queue = deque([(start_r, start_c)])
while queue:
    r, c = queue.popleft()
    for dr, dc in directions:
        if valid(nr, nc):
            queue.append((nr, nc))
```

### 3. Multi-source BFS
```python
queue = deque()
for source in all_sources:
    queue.append(source)
while queue:
    # Process level by level for distance tracking
```

## Direction Vectors
```python
DIRS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
DIRS_8 = [all 8 directions]  # Including diagonals
```

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| DFS traversal | O(m × n) | O(m × n) worst |
| BFS traversal | O(m × n) | O(min(m, n)) queue |
| Multi-source BFS | O(m × n) | O(m × n) |

## LeetCode Problems

| # | Problem | Difficulty | Pattern |
|---|---------|------------|---------|
| [200](https://leetcode.com/problems/number-of-islands/) | Number of Islands | Medium | DFS/BFS |
| [695](https://leetcode.com/problems/max-area-of-island/) | Max Area of Island | Medium | DFS |
| [733](https://leetcode.com/problems/flood-fill/) | Flood Fill | Easy | DFS |
| [130](https://leetcode.com/problems/surrounded-regions/) | Surrounded Regions | Medium | Boundary DFS |
| [417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Pacific Atlantic | Medium | Reverse DFS |
| [1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Shortest Path Binary | Medium | BFS |
| [994](https://leetcode.com/problems/rotting-oranges/) | Rotting Oranges | Medium | Multi-source BFS |
| [286](https://leetcode.com/problems/walls-and-gates/) | Walls and Gates | Medium | Multi-source BFS |
| [1020](https://leetcode.com/problems/number-of-enclaves/) | Number of Enclaves | Medium | Boundary DFS |
| [547](https://leetcode.com/problems/number-of-provinces/) | Number of Provinces | Medium | Connected components |

## Common Mistakes
1. **Modifying input** - Ask if allowed, or copy grid
2. **Wrong visited check** - Mark BEFORE recursing/queueing
3. **Direction errors** - Use consistent direction vectors
4. **Stack overflow** - Use BFS for large grids

## Quick Reference
```python
# Standard island count
def num_islands(grid):
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # Marks all connected as visited
    return count

# BFS shortest path
def shortest_path(grid, start, end):
    queue = deque([(*start, 0)])
    visited = {start}
    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == end:
            return dist
        for nr, nc in neighbors(r, c):
            if valid and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1
```

## DFS vs BFS Decision
| Use DFS | Use BFS |
|---------|---------|
| Count/area problems | Shortest path |
| Connected components | Level-order needed |
| Stack is fine | Memory constrained |
| Simpler code | Distance tracking |
