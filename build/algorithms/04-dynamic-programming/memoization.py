"""
Memoization (Top-Down Dynamic Programming)

Memoization is a technique where we cache the results of expensive function
calls and return the cached result when the same inputs occur again.

KEY IDEA:
    Store results of subproblems to avoid redundant computation.

TOP-DOWN APPROACH:
    Start with the original problem and recursively break it down.
    Cache results as we compute them.

WHY USE MEMOIZATION:
    - Natural recursive thinking
    - Only compute needed subproblems
    - Easy to implement with Python's @lru_cache

TIME/SPACE TRADE-OFF:
    Time: Usually reduces from exponential to polynomial
    Space: O(n) for cache + O(depth) for call stack
"""

from functools import lru_cache


# =============================================================================
# FIBONACCI WITH MEMOIZATION
# =============================================================================

def fibonacci_naive(n: int) -> int:
    """
    Naive recursive Fibonacci - exponential time.

    TIME ANALYSIS:
    T(n) = T(n-1) + T(n-2) + O(1)
    This gives O(2^n) time complexity!

    WHY SLOW:
    Same subproblems computed repeatedly:
    F(5) = F(4) + F(3)
         = (F(3) + F(2)) + (F(2) + F(1))
         = ((F(2) + F(1)) + F(2)) + (F(2) + F(1))
    F(2) computed 3 times!
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# Manual memoization with dictionary
def fibonacci_memo_manual(n: int, memo: dict | None = None) -> int:
    """
    Fibonacci with manual memoization.

    APPROACH:
    1. Check if result is in cache
    2. If yes, return cached result
    3. If no, compute and cache before returning

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    result = fibonacci_memo_manual(n - 1, memo) + fibonacci_memo_manual(n - 2, memo)
    memo[n] = result
    return result


# Using Python's built-in decorator
@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """
    Fibonacci with lru_cache decorator.

    @lru_cache:
    - Automatically caches function results
    - maxsize=None means unlimited cache
    - Thread-safe
    - Can clear cache with fibonacci_memo.cache_clear()

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


# =============================================================================
# CLIMBING STAIRS
# =============================================================================

@lru_cache(maxsize=None)
def climb_stairs(n: int) -> int:
    """
    Count ways to climb n stairs taking 1 or 2 steps at a time.

    RECURRENCE:
    ways(n) = ways(n-1) + ways(n-2)

    WHY:
    - From step n-1, take 1 step
    - From step n-2, take 2 steps

    Same as Fibonacci with different base cases!

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs_k_steps(n: int, k: int) -> int:
    """
    Count ways to climb n stairs taking 1 to k steps.

    RECURRENCE:
    ways(n) = sum(ways(n-i)) for i in 1..k

    Time Complexity: O(n*k)
    Space Complexity: O(n)
    """
    @lru_cache(maxsize=None)
    def dp(remaining: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0

        total = 0
        for step in range(1, k + 1):
            total += dp(remaining - step)
        return total

    return dp(n)


# =============================================================================
# GRID PATHS
# =============================================================================

@lru_cache(maxsize=None)
def unique_paths(m: int, n: int) -> int:
    """
    Count unique paths from top-left to bottom-right in m×n grid.

    CONSTRAINT: Can only move right or down.

    RECURRENCE:
    paths(r, c) = paths(r-1, c) + paths(r, c-1)
    paths(1, c) = 1  (only one way along top row)
    paths(r, 1) = 1  (only one way along left column)

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    if m == 1 or n == 1:
        return 1
    return unique_paths(m - 1, n) + unique_paths(m, n - 1)


def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    """
    Count paths with obstacles in grid.

    grid[i][j] = 1 means obstacle (can't pass)
    grid[i][j] = 0 means empty cell
    """
    m, n = len(grid), len(grid[0])

    @lru_cache(maxsize=None)
    def dp(r: int, c: int) -> int:
        if r >= m or c >= n or grid[r][c] == 1:
            return 0
        if r == m - 1 and c == n - 1:
            return 1
        return dp(r + 1, c) + dp(r, c + 1)

    return dp(0, 0)


# =============================================================================
# KNAPSACK PROBLEM (0/1)
# =============================================================================

def knapsack_memo(weights: list[int], values: list[int], capacity: int) -> int:
    """
    0/1 Knapsack - maximize value with weight constraint.

    PROBLEM:
    Given items with weights and values, select items to maximize
    total value without exceeding capacity.

    RECURRENCE:
    dp(i, w) = max(
        dp(i-1, w),                    # Don't take item i
        dp(i-1, w - weights[i]) + values[i]  # Take item i
    )

    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    """
    n = len(weights)

    @lru_cache(maxsize=None)
    def dp(i: int, remaining: int) -> int:
        if i == n or remaining == 0:
            return 0

        # Don't take item i
        result = dp(i + 1, remaining)

        # Take item i (if possible)
        if weights[i] <= remaining:
            result = max(result, values[i] + dp(i + 1, remaining - weights[i]))

        return result

    return dp(0, capacity)


# =============================================================================
# COIN CHANGE
# =============================================================================

def coin_change_memo(coins: list[int], amount: int) -> int:
    """
    Minimum coins to make amount.

    PROBLEM:
    Given coin denominations, find minimum coins to make amount.

    RECURRENCE:
    dp(amount) = 1 + min(dp(amount - coin)) for all valid coins

    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    @lru_cache(maxsize=None)
    def dp(remaining: int) -> int:
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            result = dp(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, 1 + result)

        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1


def coin_change_ways(coins: list[int], amount: int) -> int:
    """
    Count number of ways to make amount.

    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    @lru_cache(maxsize=None)
    def dp(i: int, remaining: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0 or i == len(coins):
            return 0

        # Use coin i or skip it
        return dp(i, remaining - coins[i]) + dp(i + 1, remaining)

    return dp(0, amount)


# =============================================================================
# LONGEST COMMON SUBSEQUENCE
# =============================================================================

def lcs_memo(text1: str, text2: str) -> int:
    """
    Length of longest common subsequence.

    PROBLEM:
    Find longest sequence that appears in both strings (not necessarily contiguous).

    RECURRENCE:
    If text1[i] == text2[j]:
        dp(i, j) = 1 + dp(i+1, j+1)
    Else:
        dp(i, j) = max(dp(i+1, j), dp(i, j+1))

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + dp(i + 1, j + 1)
        else:
            return max(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)


# =============================================================================
# EDIT DISTANCE
# =============================================================================

def edit_distance(word1: str, word2: str) -> int:
    """
    Minimum operations to convert word1 to word2.

    OPERATIONS: insert, delete, replace

    RECURRENCE:
    If word1[i] == word2[j]:
        dp(i, j) = dp(i+1, j+1)  # No operation needed
    Else:
        dp(i, j) = 1 + min(
            dp(i+1, j),     # Delete from word1
            dp(i, j+1),     # Insert into word1
            dp(i+1, j+1)    # Replace
        )

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if i == len(word1):
            return len(word2) - j  # Insert remaining chars
        if j == len(word2):
            return len(word1) - i  # Delete remaining chars

        if word1[i] == word2[j]:
            return dp(i + 1, j + 1)

        return 1 + min(
            dp(i + 1, j),      # Delete
            dp(i, j + 1),      # Insert
            dp(i + 1, j + 1)   # Replace
        )

    return dp(0, 0)


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("MEMOIZATION (TOP-DOWN DP) DEMONSTRATION")
    print("=" * 60)

    # Fibonacci comparison
    print("\n1. Fibonacci")
    print(f"   F(35) naive: {fibonacci_naive(35)} (slow - O(2^n))")
    fibonacci_memo.cache_clear()
    print(f"   F(35) memo:  {fibonacci_memo(35)} (fast - O(n))")
    print(f"   F(100) memo: {fibonacci_memo(100)} (would timeout naive)")

    # Climbing stairs
    print("\n2. Climbing Stairs")
    print(f"   Ways to climb 10 stairs (1-2 steps): {climb_stairs(10)}")
    print(f"   Ways to climb 5 stairs (1-3 steps): {climb_stairs_k_steps(5, 3)}")

    # Grid paths
    print("\n3. Grid Paths")
    print(f"   Unique paths in 3×7 grid: {unique_paths(3, 7)}")

    # Knapsack
    print("\n4. 0/1 Knapsack")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print(f"   Weights: {weights}, Values: {values}, Capacity: {capacity}")
    print(f"   Maximum value: {knapsack_memo(weights, values, capacity)}")

    # Coin change
    print("\n5. Coin Change")
    coins = [1, 2, 5]
    amount = 11
    print(f"   Coins: {coins}, Amount: {amount}")
    print(f"   Minimum coins: {coin_change_memo(coins, amount)}")
    print(f"   Number of ways: {coin_change_ways(coins, amount)}")

    # LCS
    print("\n6. Longest Common Subsequence")
    print(f"   LCS('abcde', 'ace'): {lcs_memo('abcde', 'ace')}")

    # Edit distance
    print("\n7. Edit Distance")
    print(f"   Edit distance('horse', 'ros'): {edit_distance('horse', 'ros')}")

    print("\n" + "=" * 60)
    print("All tests completed!")
