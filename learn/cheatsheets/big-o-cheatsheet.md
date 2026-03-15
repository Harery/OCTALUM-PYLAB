# Big-O Complexity Cheatsheet

Quick reference for algorithm and data structure complexity.

## Data Structure Operations

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Sorted Array** | O(1) | O(log n) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Doubly Linked** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Stack (array)** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue (array)** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | N/A | O(1)† | O(1)† | O(1)† | O(n) |
| **BST** | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap** | O(1)§ | O(n) | O(log n) | O(log n) | O(n) |
| **Trie** | O(m) | O(m) | O(m) | O(m) | O(n×m) |
| **Graph (adj list)** | O(1) | O(V+E) | O(1) | O(E) | O(V+E) |
| **Graph (adj matrix)** | O(1) | O(V) | O(1) | O(1) | O(V²) |

*At head/tail only
†Average case, O(n) worst case
‡Average case, O(n) worst case for unbalanced
§Root only (min/max)

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

k = range of values, n = number of elements

---

## Search Algorithms

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) |
| **Interpolation Search** | O(1) | O(log log n) | O(n) | O(1) |
| **Exponential Search** | O(1) | O(log n) | O(log n) | O(1) |
| **Jump Search** | O(1) | O(√n) | O(√n) | O(1) |

---

## Graph Algorithms

| Algorithm | Time | Space |
|-----------|------|-------|
| **BFS** | O(V + E) | O(V) |
| **DFS** | O(V + E) | O(V) |
| **Dijkstra** | O((V + E) log V) | O(V) |
| **Bellman-Ford** | O(V × E) | O(V) |
| **Floyd-Warshall** | O(V³) | O(V²) |
| **Topological Sort** | O(V + E) | O(V) |
| **Union-Find** | O(α(n))* | O(n) |
| **Kruskal's MST** | O(E log E) | O(V) |
| **Prim's MST** | O(E log V) | O(V) |

*α(n) ≈ O(1) for all practical purposes

---

## Dynamic Programming Patterns

| Pattern | Time | Space | Problems |
|---------|------|-------|----------|
| **1D DP** | O(n) | O(n) / O(1)* | Fibonacci, Climbing Stairs |
| **2D DP** | O(n×m) | O(n×m) | LCS, Edit Distance |
| **Knapsack** | O(n×W) | O(n×W) | Subset Sum, Partition |
| **Interval DP** | O(n³) | O(n²) | Matrix Chain, Burst Balloons |
| **Bitmask DP** | O(2^n × n) | O(2^n) | TSP, Assignment |

*Can often be optimized to O(1) space

---

## Heap Operations

| Operation | Binary Heap | Binomial Heap | Fibonacci Heap |
|-----------|-------------|---------------|----------------|
| **Find Min** | O(1) | O(log n) | O(1) |
| **Insert** | O(log n) | O(log n) | O(1)* |
| **Delete Min** | O(log n) | O(log n) | O(log n)* |
| **Decrease Key** | O(log n) | O(log n) | O(1)* |
| **Merge** | O(n) | O(log n) | O(1) |

*Amortized

---

## String Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **Naive Search** | O(n×m) | O(1) | Simple cases |
| **KMP** | O(n+m) | O(m) | Pattern matching |
| **Rabin-Karp** | O(n+m)* | O(1) | Multiple patterns |
| **Boyer-Moore** | O(n/m) to O(n×m) | O(k) | Large patterns |
| **Z-Algorithm** | O(n+m) | O(n+m) | Pattern matching |
| **Suffix Array** | O(n log n) | O(n) | Substring queries |

*Average case, O(n×m) worst case

---

## Python-Specific Complexity

| Operation | List | Set/Dict | Deque |
|-----------|------|----------|-------|
| **Append** | O(1)* | O(1) | O(1) |
| **Pop Last** | O(1) | O(1) | O(1) |
| **Pop First** | O(n) | O(1) | O(1) |
| **Insert Middle** | O(n) | N/A | O(n) |
| **Contains** | O(n) | O(1) | O(n) |
| **Index** | O(n) | N/A | O(n) |
| **Sort** | O(n log n) | N/A | N/A |

*Amortized (occasional O(n) for resize)

---

## Amortized Analysis

| Structure | Why Amortized? |
|-----------|---------------|
| **Dynamic Array** | Resize doubles capacity, happens rarely |
| **Hash Table** | Rehashing spreads across many operations |
| **Fibonacci Heap** | Lazy consolidation spreads costs |

---

## Quick Rules of Thumb

### When to Use O(1) Space
- Two pointers (opposite directions)
- In-place swaps
- Using output array

### When to Use O(n) Space
- Hash map/set for lookup
- Memoization
- Sliding window with state

### When O(n log n) is Optimal
- Comparison-based sorting (lower bound)
- Divide and conquer

### When O(n²) is Acceptable
- n < 10,000
- Simple implementation matters
- Matrix problems

---

## Common Complexity Classes

```
O(1)         < O(log n)    < O(n)        < O(n log n)
Constant       Logarithmic    Linear        Linearithmic

< O(n²)       < O(n³)       < O(2^n)     < O(n!)
Quadratic       Cubic         Exponential   Factorial
```

### Practical Limits (1 second)

| Complexity | n ≈ |
|------------|-----|
| O(n) | 100,000,000 |
| O(n log n) | 5,000,000 |
| O(n²) | 10,000 |
| O(n³) | 500 |
| O(2^n) | 20 |
| O(n!) | 11 |

---

*Reference: CP Algorithms, Wikipedia, CLRS*
