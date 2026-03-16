# Recursion

Solve problems by breaking them into smaller subproblems.

## Anatomy of Recursion

Every recursive function needs:

1. **Base case** - Stops recursion
2. **Recursive case** - Calls itself with smaller input

```python
def factorial(n: int) -> int:
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)
```

## Classic Examples

### Fibonacci

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# With memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
```

### Sum of Array

```python
def array_sum(arr: list[int]) -> int:
    if not arr:
        return 0
    return arr[0] + array_sum(arr[1:])
```

### Reverse String

```python
def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
```

### Power

```python
def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Optimized (O(log n))
def power_fast(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return power_fast(base * base, exp // 2)
    return base * power_fast(base, exp - 1)
```

## Tree Recursion

### Tree Traversal

```python
def inorder(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

## Backtracking

### Generate Permutations

```python
def permute(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(path: list[int], remaining: list[int]) -> None:
        if not remaining:
            result.append(path)
            return
        for i, num in enumerate(remaining):
            backtrack(path + [num], remaining[:i] + remaining[i + 1:])

    backtrack([], nums)
    return result
```

### N-Queens

```python
def solve_n_queens(n: int) -> list[list[str]]:
    result: list[list[str]] = []

    def is_valid(board: list[str], row: int, col: int) -> bool:
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def solve(board: list[str], row: int) -> None:
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = '.' * col + 'Q' + '.' * (n - col - 1)
                solve(board, row + 1)
                board[row] = '.' * n

    solve(['.' * n] * n, 0)
    return result
```

## Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Readability | Often cleaner | Can be verbose |
| Memory | Stack overhead | Usually less |
| Performance | Function call cost | Generally faster |
| Use case | Trees, divide & conquer | Simple loops |

## Tail Recursion

```python
# Not tail recursive
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Operation after call

# Tail recursive (Python doesn't optimize)
def factorial_tail(n: int, acc: int = 1) -> int:
    if n <= 1:
        return acc
    return factorial_tail(n - 1, n * acc)
```

## Practice Files

- `build/algorithms/03-recursion/fibonacci.py`
- `build/algorithms/03-recursion/permutations.py`
- `build/algorithms/03-recursion/backtracking.py`

## Next Topic

Continue to [Dynamic Programming](dp.md).
