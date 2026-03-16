"""
Classic Dynamic Programming Problems

This module contains comprehensive implementations of classic DP problems
with detailed explanations of the recurrence relations.
"""

from typing import List
from functools import lru_cache


# =============================================================================
# FIBONACCI VARIATIONS
# =============================================================================

def fibonacci_matrix(n: int) -> int:
    """
    Fibonacci using matrix exponentiation.

    MATRIX METHOD:
    [F(n+1)]   [1 1]^n   [F(1)]
    [F(n)  ] = [1 0]   × [F(0)]

    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    def matrix_mult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def matrix_pow(M: List[List[int]], n: int) -> List[List[int]]:
        result = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                result = matrix_mult(result, M)
            M = matrix_mult(M, M)
            n //= 2
        return result

    if n <= 1:
        return n

    M = [[1, 1], [1, 0]]
    result = matrix_pow(M, n)
    return result[0][1]


# =============================================================================
# KNAPSACK VARIATIONS
# =============================================================================

def unbounded_knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Unbounded knapsack - can use each item unlimited times.

    DIFFERENCE FROM 0/1:
    dp[w] uses dp[w - weight[i]] (same item) instead of dp[w - weight[i]] from previous row.

    Time Complexity: O(n * capacity)
    Space Complexity: O(capacity)
    """
    dp = [0] * (capacity + 1)

    for w in range(capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    """
    Fractional knapsack - can take fractions of items.

    GREEDY SOLUTION:
    Sort by value/weight ratio, take highest ratio first.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    items = sorted(
        zip(weights, values),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    total_value = 0.0
    remaining = capacity

    for weight, value in items:
        if remaining >= weight:
            total_value += value
            remaining -= weight
        else:
            fraction = remaining / weight
            total_value += value * fraction
            break

    return total_value


# =============================================================================
# SUBSET SUM
# =============================================================================

def subset_sum_exists(nums: List[int], target: int) -> bool:
    """
    Check if any subset sums to target.

    Time Complexity: O(n * target)
    Space Complexity: O(target)
    """
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]

    return dp[target]


def partition_equal_subset(nums: List[int]) -> bool:
    """
    Check if array can be partitioned into two equal-sum subsets.

    Time Complexity: O(n * sum)
    Space Complexity: O(sum)
    """
    total = sum(nums)
    if total % 2 != 0:
        return False

    return subset_sum_exists(nums, total // 2)


# =============================================================================
# ROD CUTTING
# =============================================================================

def rod_cutting(prices: List[int], n: int) -> int:
    """
    Maximize revenue from cutting rod of length n.

    prices[i] = price for piece of length i+1

    RECURRENCE:
    dp[i] = max(prices[j] + dp[i-j-1]) for j in 0..i-1

    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j <= len(prices):
                dp[i] = max(dp[i], prices[j - 1] + dp[i - j])

    return dp[n]


# =============================================================================
# PAINT HOUSE / FENCE
# =============================================================================

def paint_house(costs: List[List[int]]) -> int:
    """
    Minimum cost to paint n houses with 3 colors.
    No two adjacent houses can have same color.

    costs[i][j] = cost to paint house i with color j

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not costs:
        return 0

    n = len(costs)
    prev_r = prev_g = prev_b = 0

    for i in range(n):
        curr_r = costs[i][0] + min(prev_g, prev_b)
        curr_g = costs[i][1] + min(prev_r, prev_b)
        curr_b = costs[i][2] + min(prev_r, prev_g)
        prev_r, prev_g, prev_b = curr_r, curr_g, curr_b

    return min(prev_r, prev_g, prev_b)


# =============================================================================
# DECODE WAYS
# =============================================================================

def num_decodings(s: str) -> int:
    """
    Number of ways to decode a string of digits.

    MAPPING: 1->A, 2->B, ..., 26->Z

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not s or s[0] == '0':
        return 0

    prev2 = 1
    prev1 = 1

    for i in range(1, len(s)):
        current = 0

        if s[i] != '0':
            current += prev1

        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            current += prev2

        prev2 = prev1
        prev1 = current

    return prev1


# =============================================================================
# MAXIMUM SUBARRAY (KADANE'S ALGORITHM)
# =============================================================================

def max_subarray(nums: List[int]) -> int:
    """
    Maximum sum contiguous subarray.

    KADANE'S ALGORITHM:
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    Answer is max of all dp[i]

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_ending_here = max_so_far = nums[0]

    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_subarray_with_indices(nums: List[int]) -> tuple[int, int, int]:
    """Returns (max_sum, start_idx, end_idx)."""
    max_ending_here = max_so_far = nums[0]
    start = end = temp_start = 0

    for i, num in enumerate(nums[1:], 1):
        if num > max_ending_here + num:
            max_ending_here = num
            temp_start = i
        else:
            max_ending_here += num

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i

    return max_so_far, start, end


# =============================================================================
# HOUSE ROBBER
# =============================================================================

def house_robber(nums: List[int]) -> int:
    """
    Maximum sum without robbing adjacent houses.

    RECURRENCE:
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current

    return prev1


def house_robber_circular(nums: List[int]) -> int:
    """
    Houses in a circle - first and last are adjacent.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) <= 2:
        return max(nums) if nums else 0

    return max(
        house_robber(nums[:-1]),
        house_robber(nums[1:])
    )


# =============================================================================
# JUMP GAME
# =============================================================================

def can_jump(nums: List[int]) -> bool:
    """
    Can reach the last index?

    GREEDY APPROACH:
    Track furthest reachable position.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    furthest = 0

    for i, jump in enumerate(nums):
        if i > furthest:
            return False
        furthest = max(furthest, i + jump)

    return furthest >= len(nums) - 1


def min_jumps(nums: List[int]) -> int:
    """
    Minimum jumps to reach last index.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    furthest = 0

    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = furthest

            if current_end >= len(nums) - 1:
                break

    return jumps


# =============================================================================
# PALINDROME
# =============================================================================

def longest_palindromic_substring(s: str) -> str:
    """
    Find longest palindromic substring.

    EXPAND AROUND CENTER:
    For each position, expand outward checking palindrome.

    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if not s:
        return ""

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = s[0]

    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)

        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even

    return longest


def longest_palindromic_subsequence(s: str) -> int:
    """
    Length of longest palindromic subsequence.

    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CLASSIC DP PROBLEMS DEMONSTRATION")
    print("=" * 60)

    # Fibonacci matrix
    print("\n1. Fibonacci (Matrix Exponentiation)")
    print(f"   F(50): {fibonacci_matrix(50)}")

    # Knapsack variations
    print("\n2. Knapsack Variations")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print(f"   0/1 Knapsack: {7} (see tabulation.py)")
    print(f"   Unbounded: {unbounded_knapsack(weights, values, capacity)}")
    print(f"   Fractional: {fractional_knapsack(weights, values, capacity):.2f}")

    # Subset sum
    print("\n3. Subset Sum")
    nums = [1, 5, 11, 5]
    print(f"   Can partition {nums} equally: {partition_equal_subset(nums)}")

    # Rod cutting
    print("\n4. Rod Cutting")
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print(f"   Max revenue for rod length 8: {rod_cutting(prices, 8)}")

    # Decode ways
    print("\n5. Decode Ways")
    print(f"   '226' has {num_decodings('226')} decodings (BZ, VF, BBF)")

    # Max subarray
    print("\n6. Maximum Subarray (Kadane's)")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = max_subarray_with_indices(nums)
    print(f"   Array: {nums}")
    print(f"   Max sum: {max_sum}, subarray: {nums[start:end+1]}")

    # House robber
    print("\n7. House Robber")
    houses = [2, 7, 9, 3, 1]
    print(f"   Linear: {house_robber(houses)}")
    print(f"   Circular: {house_robber_circular(houses)}")

    # Jump game
    print("\n8. Jump Game")
    nums = [2, 3, 1, 1, 4]
    print(f"   Can jump {nums}: {can_jump(nums)}")
    print(f"   Min jumps: {min_jumps(nums)}")

    # Palindrome
    print("\n9. Palindrome Problems")
    print(f"   Longest palindrome in 'babad': '{longest_palindromic_substring('babad')}'")
    print(f"   LPS length of 'bbbab': {longest_palindromic_subsequence('bbbab')}")

    print("\n" + "=" * 60)
    print("All tests completed!")
