# Python Basics

Master the fundamentals of Python programming.

## Variables and Data Types

```python
# Numbers
age: int = 25
price: float = 19.99

# Strings
name: str = "Alice"
message: str = 'Hello, World!'

# Booleans
is_active: bool = True

# None
result: None = None
```

## Collections

### Lists

```python
# Create a list
numbers: list[int] = [1, 2, 3, 4, 5]

# Common operations
numbers.append(6)      # Add to end
numbers.insert(0, 0)   # Insert at index
numbers.pop()          # Remove last
numbers.remove(3)      # Remove by value

# Slicing
first_three = numbers[:3]
last_two = numbers[-2:]
reversed_list = numbers[::-1]
```

### Tuples (Immutable)

```python
coordinates: tuple[int, int] = (10, 20)
x, y = coordinates  # Unpacking
```

### Sets (Unique values)

```python
unique_numbers: set[int] = {1, 2, 3, 3, 2}
# Result: {1, 2, 3}

# Operations
a = {1, 2, 3}
b = {3, 4, 5}
a | b  # Union: {1, 2, 3, 4, 5}
a & b  # Intersection: {3}
a - b  # Difference: {1, 2}
```

### Dictionaries

```python
# Key-value pairs
person: dict[str, str | int] = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

# Access
name = person["name"]
age = person.get("age", 0)

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")
```

## String Operations

```python
text = "Hello, Python!"

# Common operations
text.lower()          # "hello, python!"
text.upper()          # "HELLO, PYTHON!"
text.replace("Python", "World")
text.split(", ")      # ["Hello", "Python!"]
", ".join(["a", "b"]) # "a, b"

# F-strings (formatted strings)
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```

## Operators

```python
# Arithmetic
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division (float)
//  # Floor division
%   # Modulo
**  # Power

# Comparison
==  # Equal
!=  # Not equal
>   # Greater than
<   # Less than
>=  # Greater or equal
<=  # Less or equal

# Logical
and  # Both true
or   # At least one true
not  # Negation
```

## Practice Files

Explore the implementation files:

- `build/foundations/01-python-basics/hello.py` - Hello World
- `build/foundations/01-python-basics/variables.py` - Variables demo
- `build/foundations/01-python-basics/collections.py` - Collections demo

## Next Topic

Continue to [Control Flow](control-flow.md).
