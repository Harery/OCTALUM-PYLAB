# Recursion Algorithms

Understanding recursion - the foundation of divide-and-conquer and dynamic programming.

## Core Concepts

| Concept | Description |
|---------|-------------|
| Base Case | Stops recursion |
| Recursive Case | Calls itself with smaller input |
| Call Stack | Stores pending function calls |
| Stack Depth | Maximum recursion depth |

## Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Readability | Often clearer | Can be verbose |
| Memory | O(depth) stack | O(1) typically |
| Performance | Function call overhead | Usually faster |
| Use Case | Trees, divide-conquer | Simple loops |

## Files

- `basics.py` - Factorial, Fibonacci, GCD, string operations
- `backtracking.py` - Permutations, N-Queens, subset sum, maze solving

## When to Use Recursion

1. **Tree traversals** - Natural recursive structure
2. **Divide and conquer** - Merge sort, quick sort
3. **Backtracking** - Exploring all possibilities
4. **Dynamic programming** - Memoized recursion

## When to Avoid Recursion

1. **Deep recursion** - Risk of stack overflow
2. **Simple iteration** - Loops are more efficient
3. **Performance critical** - Function call overhead

## Key Pattern: Backtracking Template

```python
def backtrack(candidate, state):
    if is_complete(candidate):
        record_solution(candidate)
        return

    for choice in get_valid_choices(state):
        make_choice(choice)
        backtrack(candidate, state)
        undo_choice(choice)  # Backtrack!
```

## Common Pitfalls

- Missing base case → infinite recursion
- Wrong base case → incorrect results
- Not backtracking → incomplete solutions
- Too deep → stack overflow
