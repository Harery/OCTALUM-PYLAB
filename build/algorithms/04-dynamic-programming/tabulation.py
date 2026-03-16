"""
Tabulation (Bottom-Up Dynamic Programming)

Tabulation builds the solution iteratively from the smallest subproblems,
storing results in a table and avoiding recursion entirely.

KEY IDEA:
    Solve all subproblems from smallest to largest, store in table.

BOTTOM-UP APPROACH:
    Start with base cases, iteratively build up to the solution.

ADVANTAGES OVER MEMOIZATION:
    - No recursion stack overhead
    - Better cache locality
    - Can often optimize space

DISADVANTAGES:
    - Must solve all subproblems (even unnecessary ones)
    - Sometimes less intuitive than recursive approach
"""

from typing import List


# =============================================================================
# FIBONACCI WITH TABULATION
# =============================================================================

def fibonacci_tab(n: int) -> int:
    """
    Fibonacci using bottom-up tabulation.

    APPROACH:
    1. Create table dp[0..n]
    2. Fill base cases: dp[0] = 0, dp[1] = 1
    3. Fill table: dp[i] = dp[i-1] + dp[i-2]

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Fibonacci with space optimization.

    OBSERVATION:
    Only need previous 2 values, not entire table.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# =============================================================================
# CLIMBING STAIRS
# =============================================================================

def climb_stairs_tab(n: int) -> int:
    """
    Climbing stairs with tabulation.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# =============================================================================
# UNIQUE PATHS
# =============================================================================

def unique_paths_tab(m: int, n: int) -> int:
    """
    Unique paths in grid with tabulation.

    APPROACH:
    Fill 2D table where dp[i][j] = paths to reach (i,j)

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def unique_paths_optimized(m: int, n: int) -> int:
    """
    Unique paths with 1D array optimization.

    OBSERVATION:
    Only need previous row to compute current row.

    Time Complexity: O(m*n)
    Space Complexity: O(n)
    """
    dp = [1] * n

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[n - 1]


# =============================================================================
# KNAPSACK (0/1)
# =============================================================================

def knapsack_tab(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack with tabulation.

    TABLE: dp[i][w] = max value using first i items with capacity w

    RECURRENCE:
    dp[i][w] = max(
        dp[i-1][w],                          # Don't take item
        dp[i-1][w-weights[i-1]] + values[i-1] # Take item
    )

    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]

            # Take item i if possible
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )

    return dp[n][capacity]


def knapsack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Knapsack with 1D array optimization.

    KEY INSIGHT:
    Process items in outer loop, capacity in reverse for inner loop.
    Reverse order ensures each item is used at most once.

    Time Complexity: O(n * capacity)
    Space Complexity: O(capacity)
    """
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # Process capacity in reverse to avoid using item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


# =============================================================================
# COIN CHANGE
# =============================================================================

def coin_change_tab(coins: List[int], amount: int) -> int:
    """
    Minimum coins to make amount.

    TABLE: dp[a] = min coins to make amount a

    RECURRENCE:
    dp[a] = 1 + min(dp[a - coin]) for all coins <= a

    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways_tab(coins: List[int], amount: int) -> int:
    """
    Number of ways to make amount.

    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


# =============================================================================
# LONGEST COMMON SUBSEQUENCE
# =============================================================================

def lcs_tab(text1: str, text2: str) -> int:
    """
    LCS with tabulation.

    TABLE: dp[i][j] = LCS of text1[0:i] and text2[0:j]

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_with_sequence(text1: str, text2: str) -> tuple[int, str]:
    """
    LCS returning the actual subsequence.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the sequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs))


# =============================================================================
# LONGEST INCREASING SUBSEQUENCE
# =============================================================================

def lis_tab(nums: List[int]) -> int:
    """
    Length of longest increasing subsequence.

    TABLE: dp[i] = length of LIS ending at index i

    RECURRENCE:
    dp[i] = 1 + max(dp[j]) for all j < i where nums[j] < nums[i]

    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(nums: List[int]) -> int:
    """
    LIS with binary search optimization.

    APPROACH:
    Maintain array of smallest tail elements for each length.
    Use binary search to update efficiently.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0

    import bisect

    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


# =============================================================================
# MINIMUM PATH SUM
# =============================================================================

def min_path_sum(grid: List[List[int]]) -> int:
    """
    Minimum sum path from top-left to bottom-right.

    RECURRENCE:
    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # First column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Rest of grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TABULATION (BOTTOM-UP DP) DEMONSTRATION")
    print("=" * 60)

    # Fibonacci
    print("\n1. Fibonacci")
    print(f"   F(10) tabulation: {fibonacci_tab(10)}")
    print(f"   F(10) optimized:  {fibonacci_optimized(10)}")

    # Unique paths
    print("\n2. Unique Paths (3×7 grid)")
    print(f"   2D table: {unique_paths_tab(3, 7)}")
    print(f"   1D optimized: {unique_paths_optimized(3, 7)}")

    # Knapsack
    print("\n3. 0/1 Knapsack")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print(f"   Weights: {weights}, Values: {values}, Capacity: {capacity}")
    print(f"   2D table: {knapsack_tab(weights, values, capacity)}")
    print(f"   1D optimized: {knapsack_optimized(weights, values, capacity)}")

    # Coin change
    print("\n4. Coin Change")
    coins = [1, 2, 5]
    amount = 11
    print(f"   Coins: {coins}, Amount: {amount}")
    print(f"   Minimum coins: {coin_change_tab(coins, amount)}")
    print(f"   Number of ways: {coin_change_ways_tab(coins, amount)}")

    # LCS
    print("\n5. Longest Common Subsequence")
    text1, text2 = "abcde", "ace"
    length, seq = lcs_with_sequence(text1, text2)
    print(f"   '{text1}' vs '{text2}'")
    print(f"   Length: {length}, Sequence: '{seq}'")

    # LIS
    print("\n6. Longest Increasing Subsequence")
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"   Array: {nums}")
    print(f"   LIS length O(n²): {lis_tab(nums)}")
    print(f"   LIS length O(n log n): {lis_binary_search(nums)}")

    # Min path sum
    print("\n7. Minimum Path Sum")
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(f"   Grid: {grid}")
    print(f"   Min path sum: {min_path_sum(grid)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
