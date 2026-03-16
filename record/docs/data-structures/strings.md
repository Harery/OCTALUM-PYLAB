# Strings

Master string manipulation and pattern matching techniques.

## Overview

Strings are immutable sequences of characters in Python.

```python
# Creation
s1 = "Hello"
s2 = 'World'
s3 = """Multi-line
string"""

# Escape characters
escaped = "Line 1\nLine 2\tTabbed"

# Raw strings
raw = r"C:\Users\name"  # Backslashes preserved
```

## Common Operations

```python
s = "Hello, World!"

# Case
s.lower()           # "hello, world!"
s.upper()           # "HELLO, WORLD!"
s.title()           # "Hello, World!"
s.capitalize()      # "Hello, world!"

# Search
s.find("World")     # 7 (index) or -1
s.index("World")    # 7 or ValueError
s.count("l")        # 3

# Modify
s.replace("World", "Python")
s.strip()           # Remove whitespace
s.split(", ")       # ["Hello", "World!"]
", ".join(["a", "b"])  # "a, b"

# Check
s.startswith("Hello")  # True
s.endswith("!")        # True
"World" in s           # True
s.isalpha()            # False (has punctuation)
s.isdigit()            # False
```

## String Slicing

```python
s = "Hello, World!"

s[0]        # "H"
s[-1]       # "!"
s[0:5]      # "Hello"
s[:5]       # "Hello"
s[7:]       # "World!"
s[::-1]     # "!dlroW ,olleH" (reversed)
s[::2]      # "Hlo ol!" (every 2nd char)
```

## String Building

```python
# Bad: String concatenation in loop
result = ""
for i in range(1000):
    result += str(i)  # O(n²) due to immutability

# Good: Use join
result = "".join(str(i) for i in range(1000))  # O(n)

# Good: Use f-strings
name = "Alice"
age = 30
message = f"{name} is {age} years old"
```

## Pattern Matching

```python
import re

text = "Contact: email@example.com"

# Search
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())  # email@example.com

# Find all
emails = re.findall(r'[\w.]+@[\w.]+', text)

# Split
parts = re.split(r'\s+', "Hello   World  Python")

# Replace
cleaned = re.sub(r'\s+', ' ', "Hello   World")
```

## Common Algorithms

### Reverse String

```python
def reverse_string(s: str) -> str:
    return s[::-1]
```

### Palindrome Check

```python
def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```

### Anagram Check

```python
from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1.lower()) == Counter(s2.lower())
```

## Time Complexity

| Operation | Time |
|-----------|------|
| Access | O(1) |
| Search | O(n) |
| Concatenate | O(n + m) |
| Slice | O(k) |
| Split | O(n) |

## Practice Files

- `build/data-structures/02-strings/string_basics.py`
- `build/data-structures/02-strings/pattern_matching.py`
- `build/challenges/leetcode-easy/0344_reverse_string.py`

## Next Topic

Continue to [Hash Tables](hash-tables.md).
