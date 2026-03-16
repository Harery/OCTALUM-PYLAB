# Functions

Create reusable blocks of code with Python functions.

## Basic Functions

```python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)  # Hello, Alice!
```

## Parameters

### Default Parameters

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
```

### *args and **kwargs

```python
def sum_all(*args: int) -> int:
    """Sum all arguments."""
    return sum(args)

sum_all(1, 2, 3, 4, 5)  # 15

def print_info(**kwargs: str) -> None:
    """Print keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", city="NYC")
```

### Keyword-Only Arguments

```python
def create_user(name: str, *, age: int, email: str) -> dict:
    """Age and email must be keyword arguments."""
    return {"name": name, "age": age, "email": email}

# Must use keywords
user = create_user("Alice", age=30, email="alice@example.com")
```

## Return Values

### Multiple Returns

```python
def get_min_max(numbers: list[int]) -> tuple[int, int]:
    """Return min and max values."""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
```

### Early Returns

```python
def find_item(items: list[str], target: str) -> int | None:
    """Return index of target or None."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return None
```

## Lambda Functions

```python
# Anonymous function
square = lambda x: x ** 2
square(5)  # 25

# Common with sorted
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted(pairs, key=lambda x: x[0])
# [(1, 'one'), (2, 'two'), (3, 'three')]

# With filter
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]

# With map
squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25, 36]
```

## Decorators

```python
def timer(func):
    """Measure function execution time."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"
```

## Generators

```python
def countdown(n: int):
    """Generate countdown sequence."""
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

## Error Handling

```python
def safe_divide(a: int, b: int) -> float | None:
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    finally:
        print("Division attempt completed.")

safe_divide(10, 2)   # 5.0
safe_divide(10, 0)   # None, with error message
```

## Type Hints

```python
from typing import TypeVar, Generic, Sequence

T = TypeVar('T')

def first_item(items: Sequence[T]) -> T | None:
    """Return first item or None."""
    return items[0] if items else None

# Generic class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T | None:
        return self._items.pop() if self._items else None
```

## Practice Files

- `build/foundations/03-functions/basics.py`
- `build/foundations/03-functions/decorators.py`
- `build/foundations/03-functions/generators.py`

## Next Phase

Ready for [Data Structures](../data-structures/index.md)!
