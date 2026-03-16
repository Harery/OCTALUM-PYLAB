# Sorting Algorithms

Comprehensive implementations of classic sorting algorithms with complexity analysis and optimizations.

## Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | Type |
|-----------|------|---------|-------|-------|--------|------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Comparison |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Comparison |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Comparison |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Comparison |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Comparison |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Comparison |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | Non-comparison |
| Radix Sort | O(d·n) | O(d·n) | O(d·n) | O(n) | Yes | Non-comparison |

## Files

- `bubble_sort.py` - Basic, optimized, cocktail shaker variations
- `selection_sort.py` - Basic, stable, bidirectional variations
- `insertion_sort.py` - Basic, binary, shell sort variations
- `merge_sort.py` - Top-down, bottom-up, k-way merge
- `quick_sort.py` - Lomuto, Hoare, randomized, 3-way partition
- `heap_sort.py` - Max-heap, min-heap, priority queue operations
- `counting_sort.py` - Basic, stable, object sorting
- `radix_sort.py` - LSD, MSD, string sorting

## Quick Selection Guide

```
Array Size Small (< 50)?
    └── YES → Insertion Sort (simple, fast for small n)
    └── NO → Range limited (k << n)?
                ├── YES → Counting/Radix Sort O(n)
                └── NO → Stability needed?
                            ├── YES → Merge Sort
                            └── NO → Quick Sort (average fast)
                                    or Heap Sort (guaranteed O(n log n))
```

## Key Takeaways

1. **No universal best sort** - Choose based on data characteristics
2. **Quick sort** - Fastest average case, but worst case O(n²)
3. **Merge sort** - Guaranteed O(n log n), stable, uses extra memory
4. **Heap sort** - O(n log n) in-place, but slower in practice
5. **Non-comparison sorts** - O(n) possible for integer keys with limited range
