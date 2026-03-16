"""
Sliding Window Pattern

Use when: Finding subarrays/substrings with specific properties
Time: Usually O(n) - each element visited at most twice
Space: O(k) for window contents or O(1) for counts
"""

from typing import List, Dict
from collections import defaultdict, Counter

# ============================================================
# TEMPLATE 1: Fixed Size Window
# ============================================================

def max_sum_subarray_fixed(nums: List[int], k: int) -> int:
    """
    Maximum sum of any contiguous subarray of size k.
    Time: O(n), Space: O(1)
    """
    if len(nums) < k:
        return -1

    # Initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # Add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum


def find_averages(nums: List[int], k: int) -> List[float]:
    """
    Find average of each contiguous subarray of size k.
    Time: O(n), Space: O(n/k) for result
    """
    result = []
    window_sum = sum(nums[:k])
    result.append(window_sum / k)

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        result.append(window_sum / k)

    return result


def contains_duplicate_in_range(nums: List[int], k: int) -> bool:
    """
    Check if there are duplicate elements within k distance.
    Time: O(n), Space: O(k)
    """
    window = set()

    for i, num in enumerate(nums):
        if num in window:
            return True

        window.add(num)

        # Maintain window of size k
        if i >= k:
            window.remove(nums[i - k])

    return False


# ============================================================
# TEMPLATE 2: Variable Size Window - Shrinkable
# ============================================================

def min_size_subarray_sum(nums: List[int], target: int) -> int:
    """
    Minimum length subarray with sum >= target.
    Time: O(n), Space: O(1)
    """
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        # Shrink from left while condition is met
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0


def longest_substring_without_repeating(s: str) -> int:
    """
    Length of longest substring without repeating characters.
    Time: O(n), Space: O(min(m, n)) where m = charset size
    """
    char_index = {}  # Most recent index of each character
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If char seen and is in current window, move left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def length_of_longest_substring_two_distinct(s: str) -> int:
    """
    Longest substring with at most 2 distinct characters.
    Time: O(n), Space: O(1) - max 3 chars in map
    """
    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_count[char] += 1

        # Shrink while more than 2 distinct chars
        while len(char_count) > 2:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================================
# TEMPLATE 3: Variable Size Window - Expandable
# ============================================================

def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    Longest substring with same char after at most k replacements.
    Time: O(n), Space: O(1)
    """
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    max_count = 0  # Count of most frequent char in window

    for right, char in enumerate(s):
        char_count[char] += 1
        max_count = max(max_count, char_count[char])

        # Window is valid if (window_size - max_count) <= k
        # i.e., we can replace the non-majority chars
        while (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================================
# TEMPLATE 4: Permutation/Anagram Matching
# ============================================================

def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s.
    Time: O(n), Space: O(1) - 26 letters max
    """
    if len(p) > len(s):
        return []

    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p)])

    if window_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Remove old character
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result


def check_inclusion(s1: str, s2: str) -> bool:
    """Check if s1's permutation is in s2. Time: O(n), Space: O(1)"""
    return len(find_anagrams(s2, s1)) > 0


# ============================================================
# TEMPLATE 5: Substring with All Characters
# ============================================================

def min_window_substring(s: str, t: str) -> str:
    """
    Minimum window in s that contains all chars of t.
    Time: O(n), Space: O(k) where k = unique chars in t
    """
    if not s or not t:
        return ""

    need = Counter(t)
    have = defaultdict(int)

    left = 0
    min_len = float('inf')
    min_start = 0
    formed = 0  # Count of chars that meet requirement
    required = len(need)  # Unique chars needed

    for right, char in enumerate(s):
        have[char] += 1

        if char in need and have[char] == need[char]:
            formed += 1

        # Try to shrink while window is valid
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            # Remove left char
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return s[min_start:min_start + min_len] if min_len != float('inf') else ""


# ============================================================
# TEMPLATE 6: At Most K Type Problems
# ============================================================

def subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    """
    Count subarrays with exactly k distinct elements.
    Use: exactly(k) = atMost(k) - atMost(k-1)
    Time: O(n), Space: O(k)
    """
    def at_most_k(k: int) -> int:
        count = defaultdict(int)
        left = 0
        result = 0

        for right, num in enumerate(nums):
            count[num] += 1

            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            # All subarrays ending at right with at most k distinct
            result += right - left + 1

        return result

    return at_most_k(k) - at_most_k(k - 1)


# ============================================================
# Quick Test
# ============================================================
if __name__ == "__main__":
    # Fixed Window
    print("Max sum k=3:", max_sum_subarray_fixed([2, 1, 5, 1, 3, 2], 3))

    # Variable - Minimum Size
    print("Min size sum>=7:", min_size_subarray_sum([2, 3, 1, 2, 4, 3], 7))

    # Longest without repeating
    print("Longest unique:", longest_substring_without_repeating("abcabcbb"))

    # Character replacement
    print("Char replacement:", longest_repeating_character_replacement("AABABBA", 1))

    # Find anagrams
    print("Anagrams of 'ab' in 'abab':", find_anagrams("abab", "ab"))

    # Min window
    print("Min window:", min_window_substring("ADOBECODEBANC", "ABC"))
