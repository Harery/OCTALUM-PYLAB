# Functions Module

This module covers Python functions, decorators, and generators.

## Overview

| File | Description | Key Topics |
|------|-------------|------------|
| `basics.py` | Function fundamentals | Parameters, return types, *args, **kwargs |
| `decorators.py` | Decorator patterns | @property, @staticmethod, @classmethod, custom |
| `generators.py` | Generator functions | yield, generator expressions, itertools |

## Learning Objectives

After completing this module, you will be able to:

1. **Function Basics**
   - Define functions with proper type annotations
   - Use positional-only, keyword-only, and variable arguments
   - Return multiple values and different types
   - Apply functions as first-class objects

2. **Decorators**
   - Create and use custom decorators
   - Apply @property for getter/setter patterns
   - Use @staticmethod and @classmethod appropriately
   - Chain multiple decorators

3. **Generators**
   - Create generator functions with yield
   - Use generator expressions for memory efficiency
   - Apply itertools for common patterns
   - Build lazy evaluation pipelines

## Quick Reference

### Function Basics

```python
# Basic function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Default parameters
def power(base: int, exp: int = 2) -> int:
    return base ** exp

# Positional-only (Python 3.8+)
def pos_only(a: int, b: int, /) -> int:
    return a + b

# Keyword-only
def kw_only(*, a: int, b: int) -> int:
    return a + b

# Variable arguments
def var_args(*args: int, **kwargs: str) -> None:
    print(f"Args: {args}, Kwargs: {kwargs}")

# Multiple return values
def divide(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b
```

### Decorators

```python
# Custom decorator
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# @property for computed attributes
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.14159 * self._radius ** 2

# @classmethod for factory methods
class Person:
    @classmethod
    def from_string(cls, data: str):
        name, age = data.split(',')
        return cls(name, int(age))

# @staticmethod for utility methods
class Math:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
```

### Generators

```python
# Basic generator
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

# Generator expression
squares = (x**2 for x in range(10))

# yield from
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# itertools common patterns
from itertools import count, cycle, chain, islice

# Infinite counter
for i in islice(count(10, 2), 5):
    print(i)  # 10, 12, 14, 16, 18

# Chain iterables
chained = list(chain([1, 2], [3, 4]))
```

## Running the Examples

```bash
# Run individual files
python build/foundations/03-functions/basics.py
python build/foundations/03-functions/decorators.py
python build/foundations/03-functions/generators.py
```

## Common Pitfalls

1. **Mutable defaults**: Never use mutable objects as default arguments
   ```python
   # Wrong
   def add_item(item, items=[]):
       items.append(item)
       return items

   # Correct
   def add_item(item, items=None):
       if items is None:
           items = []
       items.append(item)
       return items
   ```

2. **Late binding closures**: Capture values in default arguments
   ```python
   # Wrong - all lambdas capture final i value
   funcs = [lambda: i for i in range(3)]

   # Correct - capture current value
   funcs = [lambda i=i: i for i in range(3)]
   ```

3. **Generator exhaustion**: Generators can only be iterated once
   ```python
   gen = (x for x in range(3))
   list(gen)  # [0, 1, 2]
   list(gen)  # [] (exhausted!)
   ```

## Performance Comparison

| Approach | Memory | Use Case |
|----------|--------|----------|
| List | O(n) | Need random access, multiple iterations |
| Generator | O(1) | Large datasets, single pass |
| Iterator class | O(1) | Complex state management |

## Next Steps

After mastering functions, continue to:
- **Data Structures**: Arrays, linked lists, trees, graphs
- **Algorithms**: Searching, sorting, dynamic programming
