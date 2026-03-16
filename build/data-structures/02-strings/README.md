# Strings

## Overview

Strings in Python are immutable sequences of Unicode characters. They support rich operations for manipulation, searching, and formatting.

## Time Complexity Table

| Operation | Time | Notes |
|-----------|------|-------|
| **Index Access** | O(1) | s[i] |
| **Length** | O(1) | len(s) |
| **Concatenation (+)** | O(n+m) | Creates new string |
| **Repetition (*)** | O(n*k) | Creates new string |
| **Membership (in)** | O(n) | Linear search |
| **Find/Index** | O(n*m) | Substring search |
| **Split** | O(n) | Returns list |
| **Join** | O(n) | From iterable |
| **Replace** | O(n) | All occurrences |
| **Lower/Upper** | O(n) | Case conversion |
| **Strip** | O(n) | Remove characters |
| **Format** | O(n) | String formatting |
| **Regex Compile** | O(m) | Pattern length m |
| **Regex Search** | O(n*m) | Worst case |
| **Regex Match (compiled)** | O(n) | Average case |

## Space Complexity

| Operation | Space | Notes |
|-----------|-------|-------|
| **Creation** | O(n) | n = string length |
| **Concatenation** | O(n+m) | New string required |
| **Slice** | O(k) | k = slice length |
| **Split** | O(n) | List of substrings |
| **Join** | O(n) | Single string |

## Immutability

Strings are immutable - all operations return new strings:

```python
s = "hello"
s_upper = s.upper()  # New string "HELLO"
# s is still "hello"
```

This has implications:
- String concatenation in loops is inefficient (use join)
- Strings can be safely shared between functions
- Strings are hashable (can be dict keys)

## String vs List

| Feature | String | List |
|---------|--------|------|
| Mutable | No | Yes |
| Elements | Characters | Any type |
| Methods | Text-specific | Generic |
| Concatenation | O(n+m) | O(1) amortized (append) |
| Join efficiency | N/A | O(n) to string |

## Common Operations

### Searching

| Method | Returns | Raises Error |
|--------|---------|--------------|
| `find()` | Index or -1 | No |
| `rfind()` | Index from right or -1 | No |
| `index()` | Index | Yes (ValueError) |
| `rindex()` | Index from right | Yes (ValueError) |
| `count()` | Count | No |

### Splitting

| Method | Behavior |
|--------|----------|
| `split()` | Split on whitespace |
| `split(sep)` | Split on separator |
| `split(sep, n)` | Max n splits |
| `rsplit()` | From right |
| `splitlines()` | On line breaks |
| `partition()` | 3-tuple (before, sep, after) |

### Formatting

| Method | Example | Use Case |
|--------|---------|----------|
| f-string | `f"{x}"` | Python 3.6+, readable |
| `.format()` | `"{}".format(x)` | Complex formatting |
| `%` | `"%s" % x` | Legacy code |

## Regex Metacharacters

### Character Classes

| Pattern | Matches |
|---------|---------|
| `.` | Any character except newline |
| `\d` | Digit [0-9] |
| `\D` | Non-digit |
| `\w` | Word character [a-zA-Z0-9_] |
| `\W` | Non-word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `[abc]` | a, b, or c |
| `[^abc]` | Not a, b, or c |
| `[a-z]` | Range a to z |

### Quantifiers

| Pattern | Matches |
|---------|---------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 |
| `{n}` | Exactly n |
| `{n,}` | n or more |
| `{n,m}` | n to m |
| `*?` | Non-greedy 0+ |
| `+?` | Non-greedy 1+ |

### Anchors

| Pattern | Matches |
|---------|---------|
| `^` | Start of string |
| `$` | End of string |
| `\b` | Word boundary |
| `\B` | Not word boundary |
| `\A` | Start of string |
| `\Z` | End of string |

### Groups

| Pattern | Purpose |
|---------|---------|
| `(...)` | Capturing group |
| `(?:...)` | Non-capturing group |
| `(?P<name>...)` | Named group |
| `(?=...)` | Lookahead |
| `(?!...)` | Negative lookahead |
| `(?<=...)` | Lookbehind |
| `(?<!...)` | Negative lookbehind |

## Pattern Matching Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| Naive | O(n*m) | O(1) | Simple cases |
| KMP | O(n+m) | O(m) | Repeated searches |
| Rabin-Karp | O(n+m) avg | O(1) | Multiple patterns |
| Boyer-Moore | O(n/m) best | O(k) | Long patterns |

## Best Practices

1. **Use join() for concatenation in loops**
   ```python
   # Bad - O(n²)
   result = ""
   for s in strings:
       result += s

   # Good - O(n)
   result = "".join(strings)
   ```

2. **Use f-strings for formatting (Python 3.6+)**
   ```python
   # Readable and fast
   message = f"Hello, {name}!"
   ```

3. **Compile regex for repeated use**
   ```python
   pattern = re.compile(r"\d+")
   for text in texts:
       matches = pattern.findall(text)
   ```

4. **Use raw strings for regex patterns**
   ```python
   # Good - backslashes preserved
   pattern = r"\d+\.\d+"
   ```

5. **Prefer specific methods over regex when possible**
   ```python
   # Simple check - use string method
   if text.startswith("Hello"):
       pass

   # Complex pattern - use regex
   if re.match(r"\d{3}-\d{4}", text):
       pass
   ```

## Memory Considerations

- Strings stored as contiguous Unicode code points
- Interning: Python may reuse identical string literals
- Empty strings and single characters are often interned
- Large strings: consider memory when concatenating

## Unicode Support

```python
# Unicode characters
emoji = "😀"
chinese = "中文"
mixed = "Hello 世界 🌍"

# Character properties
"a".isalpha()      # True
"3".isdigit()      # True
"①".isnumeric()    # True (not digit)
"①".isdigit()      # False
```
