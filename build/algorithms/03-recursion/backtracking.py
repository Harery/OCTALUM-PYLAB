"""
Backtracking Algorithm Module

Backtracking is a systematic way to explore all possible solutions by
building candidates incrementally and abandoning candidates that cannot
possibly lead to a valid solution.

KEY CONCEPT:
    "Backtrack" = undo the last choice and try another option

TEMPLATE PATTERN:
    def backtrack(candidate, state):
        if is_complete(candidate):
            add_to_solutions(candidate)
            return

        for choice in get_choices(state):
            if is_valid(choice, state):
                make_choice(choice, candidate, state)
                backtrack(candidate, state)
                undo_choice(choice, candidate, state)  # BACKTRACK

TIME COMPLEXITY:
    Usually exponential, but pruning makes it faster in practice
    Worst case: explore entire state space

COMMON APPLICATIONS:
    - N-Queens problem
    - Sudoku solver
    - Permutations/Combinations
    - Subset sum
    - Maze solving
"""

from typing import Generator


# =============================================================================
# PERMUTATIONS AND COMBINATIONS
# =============================================================================

def permutations(elements: list[str]) -> list[list[str]]:
    """
    Generate all permutations of elements.

    BACKTRACKING APPROACH:
    1. Choose each element as first
    2. Recursively permute remaining elements
    3. Backtrack by unchoosing

    VISUALIZATION for [1, 2, 3]:
    Start: []
    ├── Choose 1 → [1]
    │   ├── Choose 2 → [1, 2]
    │   │   └── Choose 3 → [1, 2, 3] ✓
    │   └── Choose 3 → [1, 3]
    │       └── Choose 2 → [1, 3, 2] ✓
    ├── Choose 2 → [2]
    │   └── ... (similar)
    └── Choose 3 → [3]
        └── ... (similar)

    Time Complexity: O(n!)
    Space Complexity: O(n) for recursion
    """
    result = []
    n = len(elements)
    used = [False] * n

    def backtrack(current: list[str]) -> None:
        if len(current) == n:
            result.append(current[:])
            return

        for i in range(n):
            if used[i]:
                continue

            # Choose
            used[i] = True
            current.append(elements[i])

            # Explore
            backtrack(current)

            # Unchoose (backtrack)
            current.pop()
            used[i] = False

    backtrack([])
    return result


def permutations_generator(elements: list[str]) -> Generator[list[str], None, None]:
    """
    Generate permutations as generator (memory efficient).

    Yields each permutation instead of storing all.
    Useful when you only need to process each once.
    """
    n = len(elements)
    used = [False] * n

    def backtrack(current: list[str]) -> Generator[list[str], None, None]:
        if len(current) == n:
            yield current[:]
            return

        for i in range(n):
            if used[i]:
                continue

            used[i] = True
            current.append(elements[i])

            yield from backtrack(current)

            current.pop()
            used[i] = False

    yield from backtrack([])


def combinations(elements: list[str], k: int) -> list[list[str]]:
    """
    Generate all k-combinations of elements.

    COMBINATION vs PERMUTATION:
    - Permutation: order matters (ABC ≠ BAC)
    - Combination: order doesn't matter (ABC = BAC)

    BACKTRACKING APPROACH:
    Choose elements in order to avoid duplicates.
    Only consider elements after current position.

    Time Complexity: O(C(n,k) * k)
    Space Complexity: O(k)
    """
    result = []

    def backtrack(start: int, current: list[str]) -> None:
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, len(elements)):
            # Choose
            current.append(elements[i])

            # Explore (start from i+1 to avoid duplicates)
            backtrack(i + 1, current)

            # Unchoose
            current.pop()

    backtrack(0, [])
    return result


def subsets(elements: list[str]) -> list[list[str]]:
    """
    Generate all subsets (power set).

    APPROACH:
    Each element can be either included or excluded.
    Total subsets = 2^n

    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    """
    result = []

    def backtrack(start: int, current: list[str]) -> None:
        result.append(current[:])

        for i in range(start, len(elements)):
            current.append(elements[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


# =============================================================================
# N-QUEENS PROBLEM
# =============================================================================

def n_queens(n: int) -> list[list[tuple[int, int]]]:
    """
    Solve N-Queens problem using backtracking.

    PROBLEM:
    Place n queens on n×n board such that no two queens
    attack each other (same row, column, or diagonal).

    BACKTRACKING APPROACH:
    1. Place queen row by row
    2. Check if position is safe (no conflicts)
    3. If safe, place and move to next row
    4. If no valid position in row, backtrack

    Time Complexity: O(n!) worst case
    Space Complexity: O(n)
    """
    solutions = []

    def is_safe(queens: list[tuple[int, int]], row: int, col: int) -> bool:
        for q_row, q_col in queens:
            # Same column
            if q_col == col:
                return False
            # Same diagonal (|row diff| == |col diff|)
            if abs(q_row - row) == abs(q_col - col):
                return False
        return True

    def backtrack(row: int, queens: list[tuple[int, int]]) -> None:
        if row == n:
            solutions.append(queens[:])
            return

        for col in range(n):
            if is_safe(queens, row, col):
                queens.append((row, col))
                backtrack(row + 1, queens)
                queens.pop()

    backtrack(0, [])
    return solutions


def print_chessboard(queens: list[tuple[int, int]], n: int) -> None:
    """Print chessboard with queens."""
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in queens:
        board[row][col] = 'Q'

    for row in board:
        print(' '.join(row))


# =============================================================================
# SUBSET SUM
# =============================================================================

def subset_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Find all subsets that sum to target.

    BACKTRACKING APPROACH:
    Try including or excluding each element.
    Prune paths where sum exceeds target.

    Time Complexity: O(2^n) worst case
    Space Complexity: O(n)
    """
    result = []

    def backtrack(start: int, current: list[int], current_sum: int) -> None:
        if current_sum == target:
            result.append(current[:])
            return

        if current_sum > target:
            return  # Prune - sum exceeded

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current, current_sum + nums[i])
            current.pop()

    backtrack(0, [], 0)
    return result


def subset_sum_exists(nums: list[int], target: int) -> bool:
    """
    Check if any subset sums to target.

    OPTIMIZATION:
    Returns True on first found solution.
    """
    def backtrack(index: int, current_sum: int) -> bool:
        if current_sum == target:
            return True

        if current_sum > target or index >= len(nums):
            return False

        # Try including or excluding current element
        return (backtrack(index + 1, current_sum + nums[index]) or
                backtrack(index + 1, current_sum))

    return backtrack(0, 0)


# =============================================================================
# GENERATE PARENTHESES
# =============================================================================

def generate_parentheses(n: int) -> list[str]:
    """
    Generate all valid parentheses combinations.

    CONSTRAINTS:
    - n opening and n closing parentheses
    - At any point: open count >= close count

    BACKTRACKING APPROACH:
    - Add '(' if open < n
    - Add ')' if close < open

    Time Complexity: O(4^n / sqrt(n)) - Catalan number
    Space Complexity: O(n)
    """
    result = []

    def backtrack(current: str, open_count: int, close_count: int) -> None:
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add opening parenthesis
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Add closing parenthesis
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result


# =============================================================================
# LETTER COMBINATIONS OF PHONE NUMBER
# =============================================================================

def letter_combinations(digits: str) -> list[str]:
    """
    Generate letter combinations from phone digits.

    MAPPING:
    2 → abc, 3 → def, 4 → ghi, 5 → jkl, 6 → mno,
    7 → pqrs, 8 → tuv, 9 → wxyz

    Time Complexity: O(4^n) where n = len(digits)
    Space Complexity: O(n)
    """
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index: int, current: str) -> None:
        if index == len(digits):
            result.append(current)
            return

        for letter in mapping[digits[index]]:
            backtrack(index + 1, current + letter)

    backtrack(0, '')
    return result


# =============================================================================
# PATH FINDING (MAZE)
# =============================================================================

def find_path_maze(maze: list[list[int]], start: tuple[int, int],
                   end: tuple[int, int]) -> list[tuple[int, int]] | None:
    """
    Find path through maze using backtracking.

    MAZE FORMAT:
    0 = open path, 1 = wall

    MOVEMENT: Up, down, left, right (no diagonals)

    Time Complexity: O(4^(m*n)) worst case
    Space Complexity: O(m*n)
    """
    if not maze or not maze[0]:
        return None

    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []

    def is_valid(row: int, col: int) -> bool:
        return (0 <= row < rows and 0 <= col < cols and
                maze[row][col] == 0 and not visited[row][col])

    def backtrack(row: int, col: int) -> bool:
        if (row, col) == end:
            path.append((row, col))
            return True

        if not is_valid(row, col):
            return False

        visited[row][col] = True
        path.append((row, col))

        # Try all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if backtrack(row + dr, col + dc):
                return True

        # Backtrack
        path.pop()
        visited[row][col] = False
        return False

    if backtrack(start[0], start[1]):
        return path
    return None


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BACKTRACKING DEMONSTRATION")
    print("=" * 60)

    # Permutations
    print("\n1. Permutations of [1, 2, 3]")
    perms = permutations(['1', '2', '3'])
    print(f"   Count: {len(perms)} (3! = 6)")
    print(f"   Permutations: {perms}")

    # Combinations
    print("\n2. 2-Combinations of [1, 2, 3, 4]")
    combs = combinations(['1', '2', '3', '4'], 2)
    print(f"   Count: {len(combs)} (C(4,2) = 6)")
    print(f"   Combinations: {combs}")

    # Subsets
    print("\n3. Subsets of [1, 2]")
    subs = subsets(['1', '2'])
    print(f"   Count: {len(subs)} (2^2 = 4)")
    print(f"   Subsets: {subs}")

    # N-Queens
    print("\n4. 4-Queens Solutions")
    solutions = n_queens(4)
    print(f"   Found {len(solutions)} solutions")
    if solutions:
        print("   First solution:")
        print_chessboard(solutions[0], 4)

    # Subset Sum
    print("\n5. Subset Sum (target = 7)")
    nums = [3, 1, 4, 2, 5]
    subsets_found = subset_sum(nums, 7)
    print(f"   Array: {nums}")
    print(f"   Subsets summing to 7: {subsets_found}")

    # Generate Parentheses
    print("\n6. Generate Parentheses (n=3)")
    parens = generate_parentheses(3)
    print(f"   Count: {len(parens)} (Catalan(3) = 5)")
    print(f"   Parentheses: {parens}")

    # Letter Combinations
    print("\n7. Letter Combinations of '23'")
    combos = letter_combinations('23')
    print(f"   Count: {len(combos)}")
    print(f"   Combinations: {combos}")

    # Maze
    print("\n8. Maze Path Finding")
    maze = [
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    path = find_path_maze(maze, start, end)
    print(f"   Start: {start}, End: {end}")
    print(f"   Path found: {path}")

    print("\n" + "=" * 60)
    print("All tests completed!")
