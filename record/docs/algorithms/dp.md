# Dynamic Programming

Optimize problems with overlapping subproblems.

## Core Concepts

1. **Overlapping Subproblems** - Same subproblems solved multiple times
2. **Optimal Substructure** - Optimal solution contains optimal solutions to subproblems
3. **Memoization** - Cache results (top-down)
4. **Tabulation** - Build table (bottom-up)

## Fibonacci Example

### Naive Recursion (O(2ⁿ))

```python
def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
```

### Memoization (O(n))

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)
```

### Tabulation (O(n))

```python
def fib_tab(n: int) -> int:
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### Space Optimized (O(1) space)

```python
def fib_optimized(n: int) -> int:
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

## Common DP Problems

### Climbing Stairs

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

### Coin Change

```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

### Longest Common Subsequence

```python
def lcs(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

### 0/1 Knapsack

```python
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
```

## DP Patterns

| Pattern | Example Problems |
|---------|------------------|
| Linear | Fibonacci, Climbing Stairs |
| Grid | Unique Paths, Min Path Sum |
| String | LCS, Edit Distance |
| Subset | Knapsack, Partition |
| Interval | Matrix Chain, Burst Balloons |

## When to Use DP

- Counting problems
- Optimization problems
- Yes/no decision problems
- Problems with overlapping subproblems

## Practice Files

- `build/algorithms/04-dynamic-programming/fibonacci.py`
- `build/algorithms/04-dynamic-programming/coin_change.py`
- `build/algorithms/04-dynamic-programming/knapsack.py`

## Next Topic

Continue to [Graph Algorithms](graphs.md).
