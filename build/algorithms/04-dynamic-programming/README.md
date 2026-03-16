# Dynamic Programming

Optimization technique using memoization (top-down) or tabulation (bottom-up).

## Core Concepts

| Concept | Description |
|---------|-------------|
| Overlapping Subproblems | Same subproblems solved repeatedly |
| Optimal Substructure | Optimal solution contains optimal subsolutions |
| State | Variables that define a subproblem |
| Recurrence | Mathematical formula relating states |

## Memoization vs Tabulation

| Aspect | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|--------|------------------------|------------------------|
| Approach | Recursive | Iterative |
| Space | O(depth) + cache | O(table size) |
| Subproblems | Only needed ones | All subproblems |
| Stack overflow | Possible | No |
| Intuitiveness | Often more natural | Sometimes harder |

## Files

- `memoization.py` - @lru_cache, manual memoization patterns
- `tabulation.py` - 1D/2D table, space optimization
- `classic_problems.py` - Fibonacci, Knapsack, LCS, LIS, etc.

## Common Patterns

### 1. Linear Sequence
```
dp[i] = f(dp[i-1], dp[i-2], ...)
```
Examples: Fibonacci, climbing stairs, house robber

### 2. Grid/Matrix
```
dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...)
```
Examples: unique paths, min path sum, LCS

### 3. Subset/Knapsack
```
dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi] + vi)
```
Examples: 0/1 knapsack, subset sum, coin change

## Key Takeaways

1. **Identify the state** - What defines each subproblem?
2. **Find the recurrence** - How do states relate?
3. **Define base cases** - Smallest subproblems
4. **Choose direction** - Top-down or bottom-up
5. **Optimize space** - Often can reduce dimension
