"""
Python Data Types - Complete Reference.

This module covers all Python built-in data types with practical examples
using Python 3.12+ syntax.

Time Complexity: Varies by type and operation (documented per type)
Space Complexity: Varies by type (documented per type)
"""

from __future__ import annotations
from decimal import Decimal
from fractions import Fraction
from datetime import datetime, date, time, timedelta
from pathlib import Path


# ============================================================================
# NUMERIC TYPES
# ============================================================================

def demonstrate_integers() -> None:
    """
    Demonstrate integer type features.

    Integers in Python have unlimited precision (arbitrary precision).

    Time Complexity: O(1) for basic ops, O(n) for very large numbers
    Space Complexity: O(log n) where n is the value
    """
    # Basic integers
    positive: int = 42
    negative: int = -17
    zero: int = 0

    # Large integers (unlimited precision)
    huge_number: int = 10**100  # Googol
    print(f"Googol has {len(str(huge_number))} digits")

    # Different bases
    binary: int = 0b1010  # 10 in binary
    octal: int = 0o12     # 10 in octal
    hexadecimal: int = 0xA  # 10 in hexadecimal

    print(f"Binary 0b1010 = {binary}")
    print(f"Octal 0o12 = {octal}")
    print(f"Hex 0xA = {hexadecimal}")

    # Underscores for readability (Python 3.6+)
    million: int = 1_000_000
    credit_card: int = 1234_5678_9012_3456

    print(f"Million: {million:,}")
    print(f"Credit card: {credit_card}")


def demonstrate_floats() -> None:
    """
    Demonstrate floating-point numbers.

    Floats are IEEE 754 double-precision (64-bit).
    Be aware of precision limitations!

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Basic floats
    pi: float = 3.14159
    scientific: float = 1.5e10  # 1.5 × 10^10
    negative_exp: float = 2.5e-3  # 0.0025

    print(f"Pi: {pi}")
    print(f"Scientific notation: {scientific}")
    print(f"Negative exponent: {negative_exp}")

    # Precision warning!
    result: float = 0.1 + 0.2
    print(f"0.1 + 0.2 = {result}")  # Not exactly 0.3!
    print(f"Is it 0.3? {result == 0.3}")  # False!

    # Special float values
    infinity: float = float('inf')
    neg_infinity: float = float('-inf')
    not_a_number: float = float('nan')

    print(f"Infinity: {infinity}")
    print(f"Negative infinity: {neg_infinity}")
    print(f"NaN: {not_a_number}")

    # NaN comparison gotcha
    print(f"NaN == NaN? {not_a_number == not_a_number}")  # False!
    print(f"Use math.isnan() instead")


def demonstrate_complex_numbers() -> None:
    """
    Demonstrate complex number type.

    Complex numbers have real and imaginary parts.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Complex number literals
    z1: complex = 3 + 4j
    z2: complex = complex(2, 5)  # 2 + 5j

    print(f"z1 = {z1}")
    print(f"z2 = {z2}")

    # Accessing parts
    print(f"Real part of z1: {z1.real}")
    print(f"Imaginary part of z1: {z1.imag}")

    # Operations
    sum_complex: complex = z1 + z2
    product: complex = z1 * z2
    magnitude: float = abs(z1)  # sqrt(3^2 + 4^2) = 5

    print(f"Sum: {sum_complex}")
    print(f"Product: {product}")
    print(f"Magnitude of z1: {magnitude}")


def demonstrate_decimal_and_fraction() -> None:
    """
    Demonstrate Decimal and Fraction for precise arithmetic.

    Use Decimal for financial calculations.
    Use Fraction for exact rational numbers.
    """
    # Decimal for precision
    a: Decimal = Decimal('0.1')
    b: Decimal = Decimal('0.2')
    precise_sum: Decimal = a + b

    print(f"Decimal: 0.1 + 0.2 = {precise_sum}")  # Exactly 0.3!

    # Fraction for exact arithmetic
    frac1: Fraction = Fraction(1, 3)  # 1/3
    frac2: Fraction = Fraction(2, 3)  # 2/3
    frac_sum: Fraction = frac1 + frac2

    print(f"Fraction: 1/3 + 2/3 = {frac_sum}")  # Exactly 1!


# ============================================================================
# BOOLEAN TYPE
# ============================================================================

def demonstrate_booleans() -> None:
    """
    Demonstrate boolean type and truthiness.

    Bool is a subclass of int (True=1, False=0).

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Boolean literals
    is_true: bool = True
    is_false: bool = False

    print(f"True: {is_true}, False: {is_false}")

    # Bool as int
    print(f"True + True = {True + True}")  # 2
    print(f"True * 5 = {True * 5}")  # 5

    # Truthy and Falsy values
    falsy_values: list[object] = [
        False, None, 0, 0.0, 0j, '', (), [], {}, set(), range(0)
    ]

    print("\nFalsy values:")
    for val in falsy_values:
        print(f"  {repr(val)}: {bool(val)}")

    # Everything else is truthy
    truthy_values: list[object] = [
        True, 1, -1, 0.1, 'hello', [0], (0,), {'a': 1}, {1}
    ]

    print("\nTruthy values:")
    for val in truthy_values:
        print(f"  {repr(val)}: {bool(val)}")


# ============================================================================
# SEQUENCE TYPES
# ============================================================================

def demonstrate_strings() -> None:
    """
    Demonstrate string type features.

    Strings are immutable sequences of Unicode characters.

    Time Complexity: O(n) for most operations where n is length
    Space Complexity: O(n)
    """
    # String literals
    single: str = 'Hello'
    double: str = "World"
    triple: str = '''Multi-line
    string'''

    # Escape sequences
    escaped: str = "Line1\nLine2\tTabbed"

    # Raw strings (no escape processing)
    raw: str = r"C:\Users\name\folder"

    # f-strings (formatted string literals)
    name: str = "Alice"
    age: int = 30
    formatted: str = f"{name} is {age} years old"
    print(formatted)

    # String methods
    text: str = "  Hello, Python World!  "
    print(f"Original: '{text}'")
    print(f"Strip: '{text.strip()}'")
    print(f"Lower: '{text.lower()}'")
    print(f"Upper: '{text.upper()}'")
    print(f"Replace: '{text.replace('Python', 'Amazing')}'")
    print(f"Split: {text.split()}")

    # String slicing
    word: str = "Python"
    print(f"word[0]: {word[0]}")  # P
    print(f"word[-1]: {word[-1]}")  # n
    print(f"word[0:3]: {word[0:3]}")  # Pyt
    print(f"word[::2]: {word[::2]}")  # Pto (every 2nd char)
    print(f"word[::-1]: {word[::-1]}")  # nohtyP (reversed)


def demonstrate_lists() -> None:
    """
    Demonstrate list type features.

    Lists are mutable, ordered sequences.

    Time Complexity:
    - Indexing: O(1)
    - Append: O(1) amortized
    - Insert at beginning: O(n)
    - Search: O(n)

    Space Complexity: O(n)
    """
    # List creation
    empty: list[int] = []
    numbers: list[int] = [1, 2, 3, 4, 5]
    mixed: list[int | str | float] = [1, "hello", 3.14]

    # List comprehension
    squares: list[int] = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")

    # Common operations
    fruits: list[str] = ["apple", "banana", "cherry"]

    # Append (add to end)
    fruits.append("date")
    print(f"After append: {fruits}")

    # Insert at position
    fruits.insert(1, "apricot")
    print(f"After insert: {fruits}")

    # Remove by value
    fruits.remove("banana")
    print(f"After remove: {fruits}")

    # Pop (remove and return)
    last: str = fruits.pop()
    print(f"Popped: {last}, Remaining: {fruits}")

    # Index and count
    idx: int = fruits.index("cherry")
    count: int = fruits.count("apple")

    # Sort and reverse
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    numbers.sort()
    print(f"Sorted: {numbers}")
    numbers.reverse()
    print(f"Reversed: {numbers}")

    # Slicing creates new list
    original: list[int] = [1, 2, 3, 4, 5]
    copy: list[int] = original[:]
    copy[0] = 99
    print(f"Original: {original}, Copy: {copy}")


def demonstrate_tuples() -> None:
    """
    Demonstrate tuple type features.

    Tuples are immutable, ordered sequences.
    Use for fixed collections, dictionary keys, function returns.

    Time Complexity: O(1) for indexing
    Space Complexity: O(n)
    """
    # Tuple creation
    empty: tuple[()] = ()
    single: tuple[int] = (1,)  # Note the comma!
    multiple: tuple[int, str, float] = (1, "hello", 3.14)

    # Without parentheses (tuple packing)
    packed: tuple[int, int, int] = 1, 2, 3

    # Unpacking
    a, b, c = packed
    print(f"Unpacked: a={a}, b={b}, c={c}")

    # Extended unpacking
    first, *middle, last = (1, 2, 3, 4, 5)
    print(f"First: {first}, Middle: {middle}, Last: {last}")

    # Named tuples (for readable code)
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p: Point = Point(3, 4)
    print(f"Point: x={p.x}, y={p.y}")

    # Tuples as dictionary keys (lists can't be used)
    locations: dict[tuple[int, int], str] = {
        (0, 0): "Origin",
        (1, 0): "Unit X",
        (0, 1): "Unit Y"
    }
    print(f"Location (0,0): {locations[(0, 0)]}")

    # Immutability
    coords: tuple[int, int] = (10, 20)
    # coords[0] = 15  # TypeError!


# ============================================================================
# SET TYPES
# ============================================================================

def demonstrate_sets() -> None:
    """
    Demonstrate set type features.

    Sets are mutable, unordered collections of unique elements.

    Time Complexity:
    - Add, remove, contains: O(1) average
    - Union, intersection: O(len(s) + len(t))

    Space Complexity: O(n)
    """
    # Set creation
    empty: set[int] = set()  # NOT {} (that's an empty dict)
    numbers: set[int] = {1, 2, 3, 4, 5}
    from_list: set[int] = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

    print(f"From list with duplicates: {from_list}")

    # Set operations
    a: set[int] = {1, 2, 3, 4}
    b: set[int] = {3, 4, 5, 6}

    print(f"A: {a}")
    print(f"B: {b}")
    print(f"Union (A | B): {a | b}")
    print(f"Intersection (A & B): {a & b}")
    print(f"Difference (A - B): {a - b}")
    print(f"Symmetric diff (A ^ B): {a ^ b}")

    # Membership test (very fast)
    print(f"Is 3 in A? {3 in a}")

    # Add and remove
    numbers.add(6)
    numbers.discard(10)  # No error if not found
    # numbers.remove(10)  # Would raise KeyError


def demonstrate_frozenset() -> None:
    """
    Demonstrate frozenset type.

    Frozensets are immutable sets - can be dict keys or set elements.

    Time Complexity: Same as set
    Space Complexity: Same as set
    """
    # Creation
    fs: frozenset[int] = frozenset([1, 2, 3])

    # Can be used as dictionary keys
    set_as_key: dict[frozenset[int], str] = {
        frozenset([1, 2]): "first",
        frozenset([3, 4]): "second"
    }
    print(f"Dict with frozenset keys: {set_as_key}")

    # Can be elements of another set
    set_of_sets: set[frozenset[int]] = {
        frozenset([1, 2]),
        frozenset([3, 4])
    }
    print(f"Set of frozensets: {set_of_sets}")


# ============================================================================
# MAPPING TYPE
# ============================================================================

def demonstrate_dictionaries() -> None:
    """
    Demonstrate dictionary type features.

    Dicts are mutable, unordered mappings of key-value pairs.
    Keys must be hashable (immutable).

    Time Complexity:
    - Get, set, delete: O(1) average
    - Iteration: O(n)

    Space Complexity: O(n)
    """
    # Dictionary creation
    empty: dict[str, int] = {}
    scores: dict[str, int] = {"Alice": 95, "Bob": 87}

    # Using dict() constructor
    from_pairs: dict[str, int] = dict([("a", 1), ("b", 2)])

    # Dict comprehension
    squares_dict: dict[int, int] = {x: x**2 for x in range(1, 6)}
    print(f"Squares dict: {squares_dict}")

    # Accessing values
    print(f"Alice's score: {scores['Alice']}")
    print(f"Charlie's score (with default): {scores.get('Charlie', 0)}")

    # Modifying
    scores["Alice"] = 98  # Update
    scores["Charlie"] = 92  # Add
    print(f"Updated scores: {scores}")

    # Deleting
    del scores["Bob"]
    removed: int | None = scores.pop("Charlie", None)
    print(f"Removed Charlie's score: {removed}")

    # Common operations
    print(f"Keys: {list(scores.keys())}")
    print(f"Values: {list(scores.values())}")
    print(f"Items: {list(scores.items())}")

    # Merging dicts (Python 3.9+)
    dict_a: dict[str, int] = {"a": 1, "b": 2}
    dict_b: dict[str, int] = {"b": 3, "c": 4}
    merged: dict[str, int] = dict_a | dict_b  # b is 3 (dict_b wins)
    print(f"Merged: {merged}")


# ============================================================================
# BINARY SEQUENCE TYPES
# ============================================================================

def demonstrate_bytes_and_bytearray() -> None:
    """
    Demonstrate bytes and bytearray types.

    bytes: Immutable sequence of bytes
    bytearray: Mutable sequence of bytes

    Time Complexity: O(1) for indexing
    Space Complexity: O(n)
    """
    # bytes creation
    b1: bytes = b"hello"
    b2: bytes = bytes([72, 101, 108, 108, 111])  # "Hello"
    b3: bytes = "Hello".encode('utf-8')

    print(f"bytes from literal: {b1}")
    print(f"bytes from list: {b2}")
    print(f"bytes from encode: {b3}")

    # bytearray creation (mutable)
    ba: bytearray = bytearray(b"hello")
    ba[0] = 72  # Change 'h' to 'H'
    print(f"Modified bytearray: {ba}")

    # Hex representation
    data: bytes = b"\x48\x65\x6c\x6c\x6f"
    print(f"Hex: {data.hex()}")


# ============================================================================
# SPECIAL TYPES
# ============================================================================

def demonstrate_none() -> None:
    """
    Demonstrate None type.

    None represents the absence of a value.
    Commonly used for default arguments and representing "no result".
    """
    # None is a singleton
    a: None = None
    b: None = None
    print(f"None is None: {a is b}")  # True (same object)

    # Default return value
    def no_return() -> None:
        pass

    result: None = no_return()
    print(f"Function with no return: {result}")

    # Common pattern: default argument
    def process(items: list[int] | None = None) -> list[int]:
        if items is None:
            items = []
        items.append(1)
        return items


def demonstrate_range() -> None:
    """
    Demonstrate range type.

    Range is an immutable sequence of numbers.
    Memory-efficient (doesn't store all values).

    Time Complexity: O(1) for creation
    Space Complexity: O(1) (stores only start, stop, step)
    """
    # Basic ranges
    r1: range = range(5)  # 0, 1, 2, 3, 4
    r2: range = range(2, 6)  # 2, 3, 4, 5
    r3: range = range(0, 10, 2)  # 0, 2, 4, 6, 8

    print(f"range(5): {list(r1)}")
    print(f"range(2, 6): {list(r2)}")
    print(f"range(0, 10, 2): {list(r3)}")

    # Memory efficiency
    huge: range = range(1_000_000)  # Uses constant memory
    print(f"Huge range created (1M elements, constant memory)")

    # Membership test (efficient)
    print(f"Is 500 in range(0, 1000, 2)? {500 in range(0, 1000, 2)}")  # False
    print(f"Is 500 in range(0, 1001, 2)? {500 in range(0, 1001, 2)}")  # True


def demonstrate_datetime_types() -> None:
    """
    Demonstrate datetime module types.

    datetime provides date, time, datetime, and timedelta types.
    """
    # Current datetime
    now: datetime = datetime.now()
    today: date = date.today()

    print(f"Now: {now}")
    print(f"Today: {today}")

    # Creating specific dates/times
    birthday: date = date(1990, 5, 15)
    meeting: datetime = datetime(2024, 12, 25, 14, 30)

    print(f"Birthday: {birthday}")
    print(f"Meeting: {meeting}")

    # Timedelta (duration)
    one_week: timedelta = timedelta(days=7)
    next_week: date = today + one_week
    print(f"Next week: {next_week}")

    # Formatting
    formatted: str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted: {formatted}")


def demonstrate_path() -> None:
    """
    Demonstrate pathlib.Path type.

    Path provides an object-oriented interface for filesystem paths.
    """
    # Creating paths
    home: Path = Path.home()
    current: Path = Path.cwd()

    print(f"Home: {home}")
    print(f"Current: {current}")

    # Path operations
    file_path: Path = Path("build") / "foundations" / "data_types.py"
    print(f"File path: {file_path}")

    # Path components
    print(f"Parent: {file_path.parent}")
    print(f"Name: {file_path.name}")
    print(f"Stem: {file_path.stem}")
    print(f"Suffix: {file_path.suffix}")


# ============================================================================
# TYPE CHECKING UTILITIES
# ============================================================================

def demonstrate_type_checking() -> None:
    """
    Demonstrate type checking functions.
    """
    value: int | str = 42

    # isinstance() - recommended for type checking
    print(f"isinstance(42, int): {isinstance(value, int)}")
    print(f"isinstance(42, (int, str)): {isinstance(value, (int, str))}")

    # type() - returns the type object
    print(f"type(42): {type(value)}")
    print(f"type(42) == int: {type(value) == int}")

    # type() vs isinstance() for inheritance
    class Animal: pass
    class Dog(Animal): pass

    dog: Dog = Dog()
    print(f"type(dog) == Animal: {type(dog) == Animal}")  # False
    print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")  # True


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Run all demonstrations."""
    print("=" * 60)
    print("NUMERIC TYPES")
    print("=" * 60)
    demonstrate_integers()
    print()
    demonstrate_floats()
    print()
    demonstrate_complex_numbers()
    print()
    demonstrate_decimal_and_fraction()

    print("\n" + "=" * 60)
    print("BOOLEAN TYPE")
    print("=" * 60)
    demonstrate_booleans()

    print("\n" + "=" * 60)
    print("SEQUENCE TYPES")
    print("=" * 60)
    demonstrate_strings()
    print()
    demonstrate_lists()
    print()
    demonstrate_tuples()

    print("\n" + "=" * 60)
    print("SET TYPES")
    print("=" * 60)
    demonstrate_sets()
    print()
    demonstrate_frozenset()

    print("\n" + "=" * 60)
    print("MAPPING TYPE")
    print("=" * 60)
    demonstrate_dictionaries()

    print("\n" + "=" * 60)
    print("BINARY TYPES")
    print("=" * 60)
    demonstrate_bytes_and_bytearray()

    print("\n" + "=" * 60)
    print("SPECIAL TYPES")
    print("=" * 60)
    demonstrate_none()
    print()
    demonstrate_range()
    print()
    demonstrate_datetime_types()
    print()
    demonstrate_path()

    print("\n" + "=" * 60)
    print("TYPE CHECKING")
    print("=" * 60)
    demonstrate_type_checking()


if __name__ == "__main__":
    main()
