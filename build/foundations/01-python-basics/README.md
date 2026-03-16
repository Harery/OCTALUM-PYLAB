# Python Basics Module

This module covers the fundamental building blocks of Python programming.

## Overview

| File | Description | Key Topics |
|------|-------------|------------|
| `variables.py` | Variables and type hints | Assignment, scoping, type annotations, constants |
| `data_types.py` | All Python data types | Numeric, sequence, set, mapping, binary types |
| `operators.py` | Python operators | Arithmetic, comparison, logical, bitwise operators |

## Learning Objectives

After completing this module, you will be able to:

1. **Variables**
   - Declare and use variables with proper type hints
   - Understand Python's dynamic typing
   - Apply naming conventions (snake_case, ALL_CAPS)
   - Use type aliases for cleaner code (Python 3.12+)
   - Understand LEGB scope rules

2. **Data Types**
   - Work with all built-in Python types
   - Choose appropriate types for different use cases
   - Understand immutability vs mutability
   - Use specialized types (Decimal, Fraction, Path)
   - Convert between types

3. **Operators**
   - Use all arithmetic operators (including // and **)
   - Apply comparison operators and chaining
   - Understand short-circuit evaluation in logical operators
   - Use bitwise operators for low-level operations
   - Apply the walrus operator (:=)

## Quick Reference

### Variables (Python 3.12+)

```python
# Basic type hints
name: str = "Alice"
age: int = 30
scores: list[int] = [95, 87, 92]
mapping: dict[str, int] = {"a": 1}

# Union types
value: str | int | None = "hello"

# Type aliases
type Vector = tuple[float, float, float]
type UserID = int
```

### Data Types

```python
# Numeric
integer: int = 42
floating: float = 3.14
complex_num: complex = 3 + 4j

# Sequences (ordered)
string: str = "hello"
my_list: list[int] = [1, 2, 3]      # Mutable
my_tuple: tuple[int, int] = (1, 2)   # Immutable

# Sets (unordered, unique)
my_set: set[int] = {1, 2, 3}         # Mutable
my_frozenset: frozenset[int] = frozenset([1, 2])  # Immutable

# Mappings
my_dict: dict[str, int] = {"a": 1, "b": 2}

# Special
nothing: None = None
my_range: range = range(10)
```

### Operators

```python
# Arithmetic
+, -, *, /, //, %, **

# Comparison (chaining supported)
==, !=, <, >, <=, >=
1 < x < 10  # Chained comparison

# Logical (short-circuit)
and, or, not

# Bitwise
&, |, ^, ~, <<, >>

# Assignment
=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=

# Identity (use 'is' for None comparison)
is, is not

# Membership
in, not in

# Walrus (Python 3.8+)
if (n := len(data)) > 10:
    print(f"Large dataset: {n} items")
```

## Running the Examples

```bash
# Run individual files
python build/foundations/01-python-basics/variables.py
python build/foundations/01-python-basics/data_types.py
python build/foundations/01-python-basics/operators.py
```

## Common Pitfalls

1. **Float Precision**: `0.1 + 0.2 != 0.3` — use `Decimal` for financial calculations
2. **Identity vs Equality**: Use `is` for `None`, `==` for value comparison
3. **Mutable Defaults**: Never use mutable objects as default arguments
4. **Integer Division**: `5 / 2 = 2.5` (float), `5 // 2 = 2` (int)
5. **Small Integer Caching**: `256 is 256` is True, `257 is 257` may be False

## Next Steps

After mastering the basics, continue to:
- **02-control-flow**: Conditionals, loops, and comprehensions
- **03-functions**: Function definitions, decorators, and generators

## Resources

- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP 695 - Type Parameter Syntax (Python 3.12)](https://peps.python.org/pep-0695/)
