# Search Algorithms

A comprehensive guide to searching algorithms with implementations, complexity analysis, and practical guidance.

## Overview

| Algorithm | Best | Average | Worst | Space | Prerequisite |
|-----------|------|---------|-------|-------|--------------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | None |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted |
| Interpolation Search | O(1) | O(log log n) | O(n) | O(1) | Sorted + Uniform |

## Files

- `linear_search.py` - Basic, all-occurrences, last, sentinel, ordered variations
- `binary_search.py` - Iterative, recursive, first/last occurrence, rotated array
- `interpolation_search.py` - Uniform distribution optimization
- `README.py` - Comparison guide with decision flowchart

## Decision Guide

```
Is array sorted?
    ├── NO → Linear Search O(n)
    └── YES → Is data uniformly distributed?
                    ├── YES → Interpolation Search O(log log n)
                    └── NO → Binary Search O(log n)
```

## Quick Examples

```python
from linear_search import linear_search, linear_search_all
from binary_search import binary_search_iterative, binary_search_first
from interpolation_search import interpolation_search

# Linear search - works on any data
linear_search([4, 2, 7, 1], 7)  # Returns 2

# Binary search - requires sorted data
binary_search_iterative([1, 2, 3, 4, 5], 3)  # Returns 2

# Interpolation search - best for uniform distribution
interpolation_search([10, 20, 30, 40, 50], 30)  # Returns 2
```

## Key Takeaways

1. **Sort once, search many** - O(n log n) sort + O(log n) searches beats repeated O(n) searches
2. **Know your distribution** - Uniform → Interpolation, Unknown → Binary
3. **Space matters** - Iterative binary search uses O(1), recursive uses O(log n) stack
