"""
Subsets / Backtracking Pattern

Use when: Generate all combinations, permutations, subsets
Time: O(2^n) for subsets, O(n!) for permutations
Space: O(n) for recursion stack
"""

from typing import List

# ============================================================
# TEMPLATE 1: Subsets (Power Set)
# ============================================================

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets.
    Time: O(n × 2^n), Space: O(n) recursion
    """
    result = []

    def backtrack(start: int, path: List[int]) -> None:
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def subsets_iterative(nums: List[int]) -> List[List[int]]:
    """Iterative approach. Time: O(n × 2^n)"""
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result


# ============================================================
# TEMPLATE 2: Subsets with Duplicates
# ============================================================

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """
    Subsets with duplicates in input (no duplicate subsets).
    Time: O(n × 2^n), Space: O(n)
    """
    nums.sort()
    result = []

    def backtrack(start: int, path: List[int]) -> None:
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# ============================================================
# TEMPLATE 3: Permutations
# ============================================================

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations.
    Time: O(n × n!), Space: O(n)
    """
    result = []

    def backtrack(path: List[int], used: List[bool]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


def permute_swap(nums: List[int]) -> List[List[int]]:
    """Permutations using swap. Time: O(n × n!)"""
    result = []

    def backtrack(first: int) -> None:
        if first == len(nums):
            result.append(nums[:])
            return

        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack(0)
    return result


# ============================================================
# TEMPLATE 4: Permutations with Duplicates
# ============================================================

def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Permutations with duplicates (no duplicate permutations).
    Time: O(n × n!), Space: O(n)
    """
    from collections import Counter
    result = []
    count = Counter(nums)

    def backtrack(path: List[int]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in count:
            if count[num] > 0:
                count[num] -= 1
                path.append(num)
                backtrack(path)
                path.pop()
                count[num] += 1

    backtrack([])
    return result


# ============================================================
# TEMPLATE 5: Combinations
# ============================================================

def combine(n: int, k: int) -> List[List[int]]:
    """
    All combinations of k numbers from 1 to n.
    Time: O(C(n,k) × k), Space: O(k)
    """
    result = []

    def backtrack(start: int, path: List[int]) -> None:
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


# ============================================================
# TEMPLATE 6: Combination Sum
# ============================================================

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    All combinations summing to target (can reuse elements).
    Time: O(n^(target/min)), Space: O(target/min)
    """
    result = []

    def backtrack(start: int, path: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i not i+1 (reuse)
            path.pop()

    backtrack(0, [], target)
    return result


def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Combinations summing to target (no reuse, unique combinations).
    Time: O(2^n), Space: O(n)
    """
    candidates.sort()
    result = []

    def backtrack(start: int, path: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


# ============================================================
# TEMPLATE 7: Letter Combinations of Phone Number
# ============================================================

def letter_combinations(digits: str) -> List[str]:
    """
    Generate all letter combinations for phone digits.
    Time: O(4^n), Space: O(n)
    """
    if not digits:
        return []

    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index: int, path: List[str]) -> None:
        if index == len(digits):
            result.append(''.join(path))
            return

        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# ============================================================
# TEMPLATE 8: Generate Parentheses
# ============================================================

def generate_parenthesis(n: int) -> List[str]:
    """
    Generate all valid parentheses with n pairs.
    Time: O(4^n / sqrt(n)), Space: O(n)
    """
    result = []

    def backtrack(path: List[str], open_count: int, close_count: int) -> None:
        if len(path) == 2 * n:
            result.append(''.join(path))
            return

        if open_count < n:
            path.append('(')
            backtrack(path, open_count + 1, close_count)
            path.pop()

        if close_count < open_count:
            path.append(')')
            backtrack(path, open_count, close_count + 1)
            path.pop()

    backtrack([], 0, 0)
    return result


# ============================================================
# TEMPLATE 9: Palindrome Partitioning
# ============================================================

def partition_palindrome(s: str) -> List[List[str]]:
    """
    All palindrome partitions of string.
    Time: O(n × 2^n), Space: O(n)
    """
    result = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int, path: List[str]) -> None:
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


# ============================================================
# TEMPLATE 10: N-Queens
# ============================================================

def solve_n_queens(n: int) -> List[List[str]]:
    """
    N-Queens problem.
    Time: O(n!), Space: O(n²)
    """
    result = []
    board = [['.'] * n for _ in range(n)]

    def is_safe(row: int, col: int) -> bool:
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True

    def backtrack(row: int) -> None:
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return result


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    print("Subsets of [1,2,3]:", subsets([1, 2, 3]))
    print("Permute [1,2,3]:", permute([1, 2, 3]))
    print("Combine n=4, k=2:", combine(4, 2))
    print("Combination sum [2,3,6,7], target=7:", combination_sum([2, 3, 6, 7], 7))
    print("Letter combinations '23':", letter_combinations("23"))
    print("Generate parenthesis n=3:", generate_parenthesis(3))
    print("Palindrome partition 'aab':", partition_palindrome("aab"))
    print("N-Queens n=4:", len(solve_n_queens(4)), "solutions")
