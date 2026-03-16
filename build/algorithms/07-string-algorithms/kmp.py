"""
Knuth-Morris-Pratt (KMP) Pattern Matching

KMP efficiently finds all occurrences of a pattern in a text by avoiding
recomparisons using the failure function (also called LPS array).

KEY INSIGHT:
    When a mismatch occurs, we know part of the text from previous comparisons.
    Use this information to skip ahead instead of starting over.

Time Complexity: O(n + m) where n = text length, m = pattern length
Space Complexity: O(m) for LPS array
"""

from typing import List


def compute_lps(pattern: str) -> List[int]:
    """
    Compute Longest Proper Prefix which is also Suffix array.

    LPS[i] = length of longest proper prefix of pattern[0:i+1]
             that is also a suffix.

    WHY IT HELPS:
    On mismatch at position i, we know pattern[0:lps[i-1]] matches.
    We can skip lps[i-1] characters instead of starting from 0.
    """
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Find all occurrences of pattern in text.

    ALGORITHM:
    1. Compute LPS array for pattern
    2. Compare text and pattern character by character
    3. On mismatch, use LPS to skip ahead
    4. Report match when j reaches pattern length

    Args:
        text: String to search in
        pattern: String to search for

    Returns:
        List of starting indices where pattern occurs

    Example:
        >>> kmp_search("ABABDABACDABABCABAB", "ABABCABAB")
        [10]
    """
    if not pattern:
        return list(range(len(text) + 1))

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    result = []
    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


def kmp_count(text: str, pattern: str) -> int:
    """Count occurrences of pattern in text."""
    return len(kmp_search(text, pattern))


def kmp_first(text: str, pattern: str) -> int:
    """Find first occurrence, or -1 if not found."""
    matches = kmp_search(text, pattern)
    return matches[0] if matches else -1


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("KMP PATTERN MATCHING DEMONSTRATION")
    print("=" * 60)

    # LPS computation
    print("\n1. LPS Array Computation")
    pattern = "ABABCABAB"
    lps = compute_lps(pattern)
    print(f"   Pattern: {pattern}")
    print(f"   LPS:     {lps}")

    # Search example
    print("\n2. Pattern Search")
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print(f"   Text: {text}")
    print(f"   Pattern: {pattern}")
    print(f"   Matches at indices: {matches}")

    # Multiple matches
    print("\n3. Multiple Matches")
    text = "AAAAA"
    pattern = "AA"
    print(f"   Text: '{text}', Pattern: '{pattern}'")
    print(f"   Matches: {kmp_search(text, pattern)}")
    print(f"   Count: {kmp_count(text, pattern)}")

    print("\n" + "=" * 60)
    print("All tests completed!")
