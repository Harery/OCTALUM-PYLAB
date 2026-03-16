# Advanced Data Structures

## Overview

Advanced data structures provide specialized capabilities for specific use cases. They trade off simplicity for improved performance or unique functionality.

## Bloom Filter

A probabilistic data structure for set membership testing.

### Properties
- **Space-efficient**: Uses bit array
- **Fast**: O(k) lookup where k = number of hash functions
- **One-sided errors**: Can have false positives, never false negatives

### Time Complexity

| Operation | Time |
|-----------|------|
| **Add** | O(k) |
| **Contains** | O(k) |

### Space Complexity

O(m) bits where m = filter size

### False Positive Rate

```
P(fp) ≈ (1 - e^(-kn/m))^n
```

Where:
- n = number of elements
- m = filter size
- k = number of hash functions

### When to Use
- Web crawlers (URL deduplication)
- Spell checkers
- Database query optimization
- Cache filtering

## Disjoint Set (Union-Find)

Data structure for tracking connected components efficiently.

### Operations

| Operation | Time (amortized) |
|-----------|------------------|
| **Make-Set** | O(1) |
| **Union** | O(α(n)) ≈ O(1) |
| **Find** | O(α(n)) ≈ O(1) |

### Space Complexity

O(n)

### Optimizations
1. **Path Compression**: Flatten tree during find
2. **Union by Rank**: Attach smaller tree to larger tree root
3. **Union by Size**: Track component sizes

### When to Use
- Kruskal's MST algorithm
- Image processing (connected components)
- Social networks (friend groups)
- Grid percolation

## Algorithm Applications

### Kruskal's Minimum Spanning Tree
```
1. Sort edges by weight
2. For each edge (u, v):
   if find(u) ≠ find(v):
     union(u, v)
     add edge to MST
3. Return MST
```

Time: O(E log E) or O(E α(V))

### Number of Islands
```
1. Create DisjointSet with n*m elements
2. For each land cell:
   - Union with adjacent land cells
3. Count unique roots among land cells
```

Time: O(n*m * α(n*m))

## Comparison Table

| Feature | Bloom Filter | Hash Set | Disjoint Set |
|---------|--------------|----------|--------------|
| **Membership Test** | O(k) | O(1) | N/A |
| **Space** | O(m) bits | O(n) | O(n) |
| **False Positives** | Yes | No | N/A |
| **False Negatives** | No | No | N/A |
| **Union Operations** | N/A | N/A | O(α(n)) |
| **Dynamic** | Yes | Yes | Yes |

## Best Practices

### Bloom Filter
1. Choose appropriate size based on expected elements and error rate
2. Use multiple independent hash functions
3. Consider Counting Bloom Filter for frequency estimation
4. Use Scalable Bloom Filter for growing datasets

### Disjoint Set
1. Always use path compression
2. Use union by rank or size
3. Consider using it for MST algorithms
4. Good for connectivity problems

## Implementation Variants

### Bloom Filter Variants
- **Counting Bloom Filter**: Estimates element frequency
- **Scalable Bloom Filter**: Grows as needed
- **Compressed Bloom Filter**: Reduced space with compression
- **Cuckoo Filter**: Supports deletion

### Disjoint Set Variants
- **Quick Find**: Without path compression
- **Weighted Union**: Union by component size
- **Rem's Algorithm**: Worst case O(log n) guaranteed

