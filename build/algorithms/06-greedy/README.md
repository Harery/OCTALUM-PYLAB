# Greedy Algorithms

Algorithms that make locally optimal choices at each step.

## Key Concept

Greedy algorithms make the choice that looks best at the moment, hoping it leads to globally optimal solution.

## Files

- `activity_selection.py` - Maximum non-overlapping activities
- `huffman.py` - Variable-length prefix codes for compression
- `README.md` - This guide

## When Greedy Works

Greedy produces optimal solution when problem has:

1. **Greedy Choice Property**: Local optimal leads to global optimal
2. **Optimal Substructure**: Optimal solution contains optimal subsolutions

## Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|---------------------|
| Choice | Make one choice, never reconsider | Consider all choices |
| Time | Usually O(n log n) | Usually O(n²) or O(n*m) |
| Memory | O(1) or O(n) | O(n) or O(n*m) |
| Correctness | Doesn't always work | Always works |

## Classic Greedy Problems

- **Activity Selection**: Sort by finish time, pick non-overlapping
- **Huffman Coding**: Build tree from least frequent chars
- **Kruskal's MST**: Add edges in order of weight
- **Prim's MST**: Add minimum edge to growing tree
- **Dijkstra**: Process minimum distance first

## Key Takeaways

1. Greedy is fast but doesn't always give optimal answer
2. Prove greedy choice property before using
3. When greedy fails, consider DP or backtracking
