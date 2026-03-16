"""
Island/Matrix Traversal Pattern (DFS & BFS)

Use when: 2D grid problems, connected components, flood fill
Time: O(m × n) visiting each cell once
Space: O(m × n) for visited, O(min(m,n)) to O(m×n) for recursion stack
"""

from typing import List, Tuple, Deque
from collections import deque

# Direction vectors for 4-directional movement
DIRS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Direction vectors for 8-directional movement
DIRS_8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


# ============================================================
# TEMPLATE 1: DFS - Recursive
# ============================================================

def num_islands_dfs(grid: List[List[str]]) -> int:
    """
    Count number of islands (connected '1's).
    Time: O(m × n), Space: O(m × n) worst case recursion
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = '#'  # Mark visited

        for dr, dc in DIRS_4:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Find maximum island area.
    Time: O(m × n), Space: O(m × n)
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0

        grid[r][c] = 0
        area = 1

        for dr, dc in DIRS_4:
            area += dfs(r + dr, c + dc)

        return area

    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area


# ============================================================
# TEMPLATE 2: BFS - Iterative with Queue
# ============================================================

def num_islands_bfs(grid: List[List[str]]) -> int:
    """
    Count islands using BFS.
    Time: O(m × n), Space: O(min(m, n)) queue size
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                grid[r][c] = '#'
                queue = deque([(r, c)])

                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in DIRS_4:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '#'
                            queue.append((nr, nc))

    return count


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    Find shortest path from top-left to bottom-right.
    Time: O(m × n), Space: O(m × n)
    """
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark visited

    while queue:
        r, c, dist = queue.popleft()

        if r == n - 1 and c == n - 1:
            return dist

        for dr, dc in DIRS_8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))

    return -1


# ============================================================
# TEMPLATE 3: Flood Fill
# ============================================================

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    Flood fill starting from (sr, sc).
    Time: O(m × n), Space: O(m × n)
    """
    if not image or image[sr][sc] == color:
        return image

    rows, cols = len(image), len(image[0])
    start_color = image[sr][sc]

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
            return

        image[r][c] = color
        for dr, dc in DIRS_4:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return image


# ============================================================
# TEMPLATE 4: Surrounded Regions
# ============================================================

def solve_surrounded_regions(board: List[List[str]]) -> None:
    """
    Capture surrounded 'O' regions (flip to 'X').
    Keep 'O's connected to border unchanged.
    Time: O(m × n), Space: O(m × n)
    """
    if not board:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # Temporarily mark as safe
        for dr, dc in DIRS_4:
            dfs(r + dr, c + dc)

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'


# ============================================================
# TEMPLATE 5: Pacific Atlantic Water Flow
# ============================================================

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Find cells that can flow to both oceans.
    Water flows from cell to equal or lower height neighbors.
    Time: O(m × n), Space: O(m × n)
    """
    if not heights:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r: int, c: int, visited: set, prev_height: int) -> None:
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if heights[r][c] < prev_height:
            return

        visited.add((r, c))
        for dr, dc in DIRS_4:
            dfs(r + dr, c + dc, visited, heights[r][c])

    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    return list(map(list, pacific & atlantic))


# ============================================================
# TEMPLATE 6: Number of Enclaves
# ============================================================

def num_enclaves(grid: List[List[int]]) -> int:
    """
    Count 1s that cannot reach boundary.
    Time: O(m × n), Space: O(m × n)
    """
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        count = 1
        for dr, dc in DIRS_4:
            count += dfs(r + dr, c + dc)
        return count

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    return sum(sum(row) for row in grid)


# ============================================================
# TEMPLATE 7: Walls and Gates
# ============================================================

def walls_and_gates(rooms: List[List[int]]) -> None:
    """
    Fill each room with distance to nearest gate.
    INF = empty room, -1 = wall, 0 = gate.
    Time: O(m × n), Space: O(m × n)
    """
    if not rooms:
        return

    rows, cols = len(rooms), len(rooms[0])
    INF = 2**31 - 1
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRS_4:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))


# ============================================================
# TEMPLATE 8: Rotting Oranges
# ============================================================

def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Return minutes until no fresh oranges, or -1 if impossible.
    Time: O(m × n), Space: O(m × n)
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in DIRS_4:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

    return minutes if fresh == 0 else -1


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("Num islands:", num_islands_dfs([row[:] for row in grid1]))

    grid2 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    print("Max island area:", max_area_of_island([row[:] for row in grid2]))

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print("Flood fill:", flood_fill([row[:] for row in image], 1, 1, 2))

    oranges = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print("Oranges rotting:", oranges_rotting(oranges))
