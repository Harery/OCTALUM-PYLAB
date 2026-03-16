# Control Flow Module

This module covers Python's control flow mechanisms for directing program execution.

## Overview

| File | Description | Key Topics |
|------|-------------|------------|
| `conditionals.py` | Conditional statements | if/elif/else, ternary, match-case (3.10+) |
| `loops.py` | Loop constructs | for, while, break, continue, else clauses |
| `comprehensions.py` | Comprehensions | list, dict, set, generator comprehensions |

## Learning Objectives

After completing this module, you will be able to:

1. **Conditionals**
   - Use if/elif/else for branching logic
   - Apply ternary expressions for concise conditionals
   - Leverage match-case pattern matching (Python 3.10+)
   - Implement guard clauses for cleaner code

2. **Loops**
   - Iterate with for and while loops
   - Use enumerate, zip, and range effectively
   - Control loop flow with break and continue
   - Understand the loop else clause

3. **Comprehensions**
   - Create lists, dicts, and sets with comprehensions
   - Filter and transform data in a single expression
   - Use generator expressions for memory efficiency
   - Apply nested comprehensions for complex transformations

## Quick Reference

### Conditionals

```python
# Basic if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"

# Ternary expression
status = "adult" if age >= 18 else "minor"

# Chained comparison
if 10 < x < 20:
    print("x is between 10 and 20")

# Match-case (Python 3.10+)
match command:
    case "start" | "begin":
        start()
    case "stop" | "end":
        stop()
    case _:
        unknown()
```

### Loops

```python
# For loop with range
for i in range(5):
    print(i)

# For loop with enumerate
for index, value in enumerate(items):
    print(f"{index}: {value}")

# For loop with zip
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# While loop
while count < 10:
    count += 1

# Loop else (executes if no break)
for item in items:
    if item == target:
        break
else:
    print("Not found")
```

### Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Dict comprehension
name_lengths = {name: len(name) for name in names}

# Set comprehension
unique_lengths = {len(word) for word in words}

# Generator expression (memory efficient)
sum_of_squares = sum(x**2 for x in range(1000000))
```

## Running the Examples

```bash
# Run individual files
python build/foundations/02-control-flow/conditionals.py
python build/foundations/02-control-flow/loops.py
python build/foundations/02-control-flow/comprehensions.py
```

## Common Pitfalls

1. **Mutable default in loops**: Creating lists inside loops can be slow
2. **Infinite loops**: Always ensure while loops have a termination condition
3. **Off-by-one errors**: Remember range(n) goes from 0 to n-1
4. **Modifying while iterating**: Don't modify a list while iterating over it
5. **Nested complexity**: Deep nesting hurts readability - use guard clauses

## Performance Tips

| Approach | Time | Space | Use Case |
|----------|------|-------|----------|
| List comprehension | O(n) | O(n) | Need all results |
| Generator expression | O(n) | O(1) | Streaming/one-pass |
| dict comprehension | O(n) | O(n) | Key-value mapping |
| set comprehension | O(n) | O(n) | Unique values |

## Next Steps

After mastering control flow, continue to:
- **03-functions**: Function definitions, decorators, and generators
