"""
Rabin-Karp String Matching Algorithm

Rabin-Karp uses hashing to find pattern occurrences in text.
Instead of comparing characters one by one, compare hash values.

KEY INSIGHT:
    Compare hash values first (O(1)).
    Only do full string comparison when hashes match.

Time Complexity:
    - Average: O(n + m)
    - Worst: O(nm) when many hash collisions

Space Complexity: O(1)
"""

from typing import List


def rabin_karp(text: str, pattern: str, prime: int = 101) -> List[int]:
    """
    Find all occurrences of pattern in text using rolling hash.

    ROLLING HASH:
    Instead of computing hash from scratch, update hash by:
    1. Remove contribution of leftmost character
    2. Add contribution of new rightmost character

    HASH FORMULA:
    hash = (hash - old_char * base^(m-1)) * base + new_char

    Args:
        text: String to search in
        pattern: String to search for
        prime: Prime number for modulo operation

    Returns:
        List of starting indices where pattern occurs
    """
    n, m = len(text), len(pattern)

    if m == 0 or m > n:
        return []

    if m == 1:
        return [i for i, c in enumerate(text) if c == pattern]

    base = 256
    result = []

    h = pow(base, m - 1, prime)

    p_hash = 0
    t_hash = 0

    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        t_hash = (base * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            if t_hash < 0:
                t_hash += prime

    return result


def rabin_karp_count(text: str, pattern: str) -> int:
    """Count occurrences of pattern in text."""
    return len(rabin_karp(text, pattern))


def rabin_karp_multiple_patterns(text: str, patterns: List[str]) -> dict[str, List[int]]:
    """
    Find multiple patterns efficiently.

    Group patterns by length to reuse hash computations.
    """
    result = {p: [] for p in patterns}

    by_length = {}
    for p in patterns:
        by_length.setdefault(len(p), []).append(p)

    for length, pats in by_length.items():
        for p in pats:
            matches = rabin_karp(text, p)
            result[p] = matches

    return result


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("RABIN-KARP DEMONSTRATION")
    print("=" * 60)

    # Basic search
    print("\n1. Basic Pattern Search")
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    matches = rabin_karp(text, pattern)
    print(f"   Text: {text}")
    print(f"   Pattern: {pattern}")
    print(f"   Matches at: {matches}")

    # Count
    print("\n2. Count Occurrences")
    print(f"   '{pattern}' appears {rabin_karp_count(text, pattern)} times")

    # Multiple patterns
    print("\n3. Multiple Patterns")
    patterns = ["ABAB", "DAB"]
    results = rabin_karp_multiple_patterns(text, patterns)
    for p, indices in results.items():
        print(f"   '{p}': {indices}")

    print("\n" + "=" * 60)
    print("All tests completed!")
