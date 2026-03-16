# String Algorithms

Pattern matching and text processing algorithms.

## Algorithms

| Algorithm | Preprocessing | Search | Space |
|-----------|---------------|-------|-------|
| KMP | O(m) | O(n+m) | O(m) |
| Rabin-Karp | None | O(n+m) avg | O(1) |

## Files

- `kmp.py` - Knuth-Morris-Pratt with LPS array
- `rabin_karp.py` - Rolling hash string matching
- `README.md` - This guide

## When to Use

- **KMP**: Good for multiple searches of same pattern
- **Rabin-Karp**: Good for multiple patterns,- **Built-in**: Simple single search

## Key Takeaways

1. KMP uses LPS array to skip redundant comparisons
2. Rabin-Karp uses hashing for O(1) comparisons
3. Both achieve O(n+m) average complexity
