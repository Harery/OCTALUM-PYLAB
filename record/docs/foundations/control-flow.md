# Control Flow

Learn to control the flow of your Python programs.

## Conditionals

### if/elif/else

```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

### Ternary Operator

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

### Match Statement (Python 3.10+)

```python
def get_day_type(day: str) -> str:
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Invalid day"
```

## Loops

### for Loop

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Dictionary iteration
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")
```

### while Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control

```python
# break - exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4

# else after loop (executes if no break)
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

### List Comprehensions

```python
# Basic
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Nested
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

### Dictionary Comprehensions

```python
# Create dict from lists
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
# {"Alice": 5, "Bob": 3, "Charlie": 7}

# With condition
long_names = {k: v for k, v in name_lengths.items() if v > 4}
# {"Alice": 5, "Charlie": 7}
```

## Practice Files

- `build/foundations/02-control-flow/conditionals.py`
- `build/foundations/02-control-flow/loops.py`
- `build/foundations/02-control-flow/comprehensions.py`

## Next Topic

Continue to [Functions](functions.md).
