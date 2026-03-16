"""
Python Operators - Complete Reference.

This module covers all Python operators with practical examples
using Python 3.12+ syntax.

Time Complexity: O(1) for all operator operations unless noted
Space Complexity: O(1)
"""

from __future__ import annotations


# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================

def demonstrate_arithmetic_operators() -> None:
    """
    Demonstrate all arithmetic operators.

    Operators: +, -, *, /, //, %, **

    Time Complexity: O(1) for basic types, O(log n) for large integers
    Space Complexity: O(1)
    """
    a: int = 17
    b: int = 5

    # Addition
    sum_result: int = a + b
    print(f"{a} + {b} = {sum_result}")

    # Subtraction
    diff: int = a - b
    print(f"{a} - {b} = {diff}")

    # Multiplication
    product: int = a * b
    print(f"{a} * {b} = {product}")

    # Division (always returns float)
    quotient: float = a / b
    print(f"{a} / {b} = {quotient}")

    # Floor division (rounds down to nearest integer)
    floor_div: int = a // b
    print(f"{a} // {b} = {floor_div}")

    # Important: floor division with negative numbers
    neg_floor: int = -17 // 5
    print(f"-17 // 5 = {neg_floor}")  # -4 (rounds toward negative infinity)

    # Modulo (remainder)
    remainder: int = a % b
    print(f"{a} % {b} = {remainder}")

    # Exponentiation
    power: int = a ** 2
    print(f"{a} ** 2 = {power}")

    # Unary operators
    positive: int = +a
    negative: int = -a
    print(f"Unary +{a} = {positive}, Unary -{a} = {negative}")

    # With floats
    x: float = 17.5
    y: float = 5.0
    print(f"\nWith floats:")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} // {y} = {x // y}")
    print(f"{x} % {y} = {x % y}")


# ============================================================================
# COMPARISON OPERATORS
# ============================================================================

def demonstrate_comparison_operators() -> None:
    """
    Demonstrate all comparison operators.

    Operators: ==, !=, <, >, <=, >=
    All return bool values.

    Time Complexity: O(1) for simple types, O(n) for sequences
    Space Complexity: O(1)
    """
    x: int = 10
    y: int = 20

    # Equality
    print(f"{x} == {y}: {x == y}")
    print(f"{x} == 10: {x == 10}")

    # Inequality
    print(f"{x} != {y}: {x != y}")

    # Less than
    print(f"{x} < {y}: {x < y}")

    # Greater than
    print(f"{x} > {y}: {x > y}")

    # Less than or equal
    print(f"{x} <= {y}: {x <= y}")
    print(f"{x} <= 10: {x <= 10}")

    # Greater than or equal
    print(f"{x} >= {y}: {x >= y}")

    # Chained comparisons (Python feature)
    a_val: int = 5
    print(f"\nChained: 1 < {a_val} < 10: {1 < a_val < 10}")
    print(f"Equivalent to: (1 < {a_val}) and ({a_val} < 10)")

    # Comparing different types
    print(f"\n'10' == 10: {'10' == 10}")  # False (different types)

    # Comparing sequences (lexicographic)
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [1, 2, 4]
    print(f"\n[1, 2, 3] < [1, 2, 4]: {list1 < list2}")  # True

    # String comparison (lexicographic)
    print(f"'apple' < 'banana': {'apple' < 'banana'}")  # True
    print(f"'Apple' < 'apple': {'Apple' < 'apple'}")  # True (uppercase < lowercase in ASCII)


# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

def demonstrate_logical_operators() -> None:
    """
    Demonstrate logical operators.

    Operators: and, or, not

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    a_bool: bool = True
    b_bool: bool = False

    # AND (both must be True)
    print(f"{a_bool} and {b_bool}: {a_bool and b_bool}")  # False
    print(f"{a_bool} and {a_bool}: {a_bool and a_bool}")  # True

    # OR (at least one must be True)
    print(f"{a_bool} or {b_bool}: {a_bool or b_bool}")  # True
    print(f"{b_bool} or {b_bool}: {b_bool or b_bool}")  # False

    # NOT (inverts)
    print(f"not {a_bool}: {not a_bool}")  # False
    print(f"not {b_bool}: {not b_bool}")  # True

    # Short-circuit evaluation
    print("\nShort-circuit evaluation:")

    def returns_true() -> bool:
        print("  returns_true() called")
        return True

    def returns_false() -> bool:
        print("  returns_false() called")
        return False

    # AND short-circuits on first False
    print("False and returns_true():")
    result: bool = False and returns_true()  # returns_true() not called
    print(f"  Result: {result}")

    # OR short-circuits on first True
    print("\nTrue or returns_false():")
    result = True or returns_false()  # returns_false() not called
    print(f"  Result: {result}")

    # With non-boolean values (truthy/falsy)
    print("\nWith truthy/falsy values:")

    # Returns last evaluated value (not necessarily bool!)
    and_result: int = 5 and 3  # Returns 3 (both truthy, returns last)
    print(f"5 and 3 = {and_result}")

    and_result = 0 and 3  # Returns 0 (first is falsy, short-circuit)
    print(f"0 and 3 = {and_result}")

    or_result: int = 5 or 3  # Returns 5 (first is truthy, short-circuit)
    print(f"5 or 3 = {or_result}")

    or_result = 0 or 3  # Returns 3 (first is falsy)
    print(f"0 or 3 = {or_result}")


# ============================================================================
# BITWISE OPERATORS
# ============================================================================

def demonstrate_bitwise_operators() -> None:
    """
    Demonstrate bitwise operators.

    Operators: &, |, ^, ~, <<, >>
    Work on integers at the bit level.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    a_bits: int = 12  # Binary: 1100
    b_bits: int = 10  # Binary: 1010

    print(f"a = {a_bits} (binary: {bin(a_bits)})")
    print(f"b = {b_bits} (binary: {bin(b_bits)})")

    # Bitwise AND
    and_bits: int = a_bits & b_bits  # 1000 (8)
    print(f"\na & b = {and_bits} (binary: {bin(and_bits)})")

    # Bitwise OR
    or_bits: int = a_bits | b_bits  # 1110 (14)
    print(f"a | b = {or_bits} (binary: {bin(or_bits)})")

    # Bitwise XOR (exclusive or)
    xor_bits: int = a_bits ^ b_bits  # 0110 (6)
    print(f"a ^ b = {xor_bits} (binary: {bin(xor_bits)})")

    # Bitwise NOT (one's complement)
    not_bits: int = ~a_bits  # -(a + 1) = -13
    print(f"~a = {not_bits} (binary: {bin(not_bits)})")

    # Left shift (multiply by 2^n)
    left_shift: int = a_bits << 2  # 110000 (48)
    print(f"\na << 2 = {left_shift} (binary: {bin(left_shift)})")
    print(f"Equivalent to a * 2^2 = {a_bits * 4}")

    # Right shift (divide by 2^n)
    right_shift: int = a_bits >> 2  # 0011 (3)
    print(f"a >> 2 = {right_shift} (binary: {bin(right_shift)})")
    print(f"Equivalent to a // 2^2 = {a_bits // 4}")

    # Practical uses
    print("\n--- Practical Uses ---")

    # Check if number is even/odd
    num: int = 7
    is_odd: bool = bool(num & 1)
    print(f"{num} is odd: {is_odd}")

    # Swap without temp variable
    x_swap: int = 5
    y_swap: int = 10
    print(f"\nBefore swap: x={x_swap}, y={y_swap}")
    x_swap ^= y_swap
    y_swap ^= x_swap
    x_swap ^= y_swap
    print(f"After swap: x={x_swap}, y={y_swap}")

    # Check if power of 2
    def is_power_of_two(n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

    print(f"\n8 is power of 2: {is_power_of_two(8)}")
    print(f"6 is power of 2: {is_power_of_two(6)}")


# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================

def demonstrate_assignment_operators() -> None:
    """
    Demonstrate assignment operators.

    Operators: =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Simple assignment
    x: int = 10
    print(f"x = {x}")

    # Augmented assignment (modifies in place)
    x += 5  # Same as: x = x + 5
    print(f"x += 5: {x}")

    x -= 3  # Same as: x = x - 3
    print(f"x -= 3: {x}")

    x *= 2  # Same as: x = x * 2
    print(f"x *= 2: {x}")

    x //= 4  # Same as: x = x // 4
    print(f"x //= 4: {x}")

    # Important: lists and += behavior
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = list_a
    list_a += [4]  # Modifies list_a in place! list_b also affected
    print(f"\nlist_a after +=: {list_a}")
    print(f"list_b (same reference): {list_b}")

    # vs.
    list_c: list[int] = [1, 2, 3]
    list_d: list[int] = list_c
    list_c = list_c + [4]  # Creates new list! list_d unchanged
    print(f"\nlist_c after = ... +: {list_c}")
    print(f"list_d (different reference): {list_d}")

    # Walrus operator (Python 3.8+) - assignment expression
    print("\n--- Walrus Operator (:=) ---")

    # Without walrus
    numbers: list[int] = [1, 2, 3, 4, 5]
    n: int = len(numbers)
    if n > 3:
        print(f"List has {n} elements")

    # With walrus (assigns and uses in one expression)
    if (n := len(numbers)) > 3:
        print(f"List has {n} elements (using walrus)")

    # Useful in while loops
    data: list[str] = ["a", "b", "c"]
    index: int = 0
    while (item := data[index] if index < len(data) else None):
        print(f"  Processing: {item}")
        index += 1


# ============================================================================
# IDENTITY OPERATORS
# ============================================================================

def demonstrate_identity_operators() -> None:
    """
    Demonstrate identity operators.

    Operators: is, is not
    Compare object identity (memory location), not value.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Integers (small integers are cached)
    a_int: int = 256
    b_int: int = 256
    print(f"a = {a_int}, b = {b_int}")
    print(f"a == b: {a_int == b_int}")  # Value equality
    print(f"a is b: {a_int is b_int}")  # Identity (True for small ints)

    # Large integers (not cached)
    c_int: int = 257
    d_int: int = 257
    print(f"\nc = {c_int}, d = {d_int}")
    print(f"c == d: {c_int == d_int}")  # True (same value)
    print(f"c is d: {c_int is d_int}")  # False (different objects)

    # Strings (interned)
    s1: str = "hello"
    s2: str = "hello"
    print(f"\ns1 = 'hello', s2 = 'hello'")
    print(f"s1 is s2: {s1 is s2}")  # True (string interning)

    # Dynamically created strings (may not be interned)
    s3: str = "hello!"
    s4: str = "hel" + "lo!"
    print(f"\ns3 = 'hello!', s4 = 'hel' + 'lo!'")
    print(f"s3 == s4: {s3 == s4}")  # True
    print(f"s3 is s4: {s3 is s4}")  # May be False

    # Lists (always different objects)
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [1, 2, 3]
    print(f"\nlist1 = [1, 2, 3], list2 = [1, 2, 3]")
    print(f"list1 == list2: {list1 == list2}")  # True
    print(f"list1 is list2: {list1 is list2}")  # False

    # None comparison (always use 'is')
    value: str | None = None
    print(f"\nvalue = None")
    print(f"value is None: {value is None}")  # Correct
    print(f"value == None: {value == None}")  # Works but not recommended

    # is not
    print(f"\nvalue is not None: {value is not None}")


# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================

def demonstrate_membership_operators() -> None:
    """
    Demonstrate membership operators.

    Operators: in, not in
    Check if value exists in a container.

    Time Complexity:
    - O(1) for sets, dicts
    - O(n) for lists, tuples, strings

    Space Complexity: O(1)
    """
    # Lists
    fruits: list[str] = ["apple", "banana", "cherry"]
    print(f"'apple' in {fruits}: {'apple' in fruits}")
    print(f"'grape' in {fruits}: {'grape' in fruits}")

    # Strings
    sentence: str = "Hello, World!"
    print(f"\n'World' in '{sentence}': {'World' in sentence}")
    print(f"'world' in '{sentence}': {'world' in sentence}")  # Case-sensitive

    # Dictionaries (checks keys, not values)
    scores: dict[str, int] = {"Alice": 95, "Bob": 87}
    print(f"\n'Alice' in scores: {'Alice' in scores}")  # True (key exists)
    print(f"95 in scores: {95 in scores}")  # False (not a key)
    print(f"95 in scores.values(): {95 in scores.values()}")  # True

    # Sets (very fast)
    unique_nums: set[int] = {1, 2, 3, 4, 5}
    print(f"\n3 in {unique_nums}: {3 in unique_nums}")  # O(1)

    # not in
    print(f"\n'grape' not in {fruits}: {'grape' not in fruits}")

    # Nested membership
    nested: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
    print(f"\n[1, 2] in {nested}: {[1, 2] in nested}")
    print(f"1 in nested: {1 in nested}")  # False (1 is not an element)


# ============================================================================
# OPERATOR PRECEDENCE
# ============================================================================

def demonstrate_operator_precedence() -> None:
    """
    Demonstrate operator precedence (highest to lowest).

    1. Parentheses ()
    2. Exponentiation **
    3. Unary +, -, ~
    4. *, /, //, %
    5. +, -
    6. <<, >>
    7. &
    8. ^
    9. |
    10. Comparison (==, !=, <, >, <=, >=)
    11. Identity (is, is not)
    12. Membership (in, not in)
    13. Logical not
    14. Logical and
    15. Logical or
    """
    print("Operator Precedence Examples:")

    # Exponentiation is right-associative
    result: int = 2 ** 3 ** 2  # 2 ** (3 ** 2) = 2 ** 9 = 512
    print(f"2 ** 3 ** 2 = {result} (right-associative)")

    # vs.
    result = (2 ** 3) ** 2  # 8 ** 2 = 64
    print(f"(2 ** 3) ** 2 = {result}")

    # Arithmetic precedence
    result = 2 + 3 * 4  # 2 + 12 = 14
    print(f"\n2 + 3 * 4 = {result}")

    # vs.
    result = (2 + 3) * 4  # 5 * 4 = 20
    print(f"(2 + 3) * 4 = {result}")

    # Mixed operators
    x_val: int = 5
    y_val: int = 10
    z_val: int = 15

    # Complex expression
    expr: bool = x_val < y_val and y_val < z_val or z_val == 15
    print(f"\n{x_val} < {y_val} and {y_val} < {z_val} or {z_val} == 15 = {expr}")

    # Use parentheses for clarity
    expr_clear: bool = (x_val < y_val and y_val < z_val) or (z_val == 15)
    print(f"With parentheses: {expr_clear}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Run all demonstrations."""
    print("=" * 60)
    print("ARITHMETIC OPERATORS")
    print("=" * 60)
    demonstrate_arithmetic_operators()

    print("\n" + "=" * 60)
    print("COMPARISON OPERATORS")
    print("=" * 60)
    demonstrate_comparison_operators()

    print("\n" + "=" * 60)
    print("LOGICAL OPERATORS")
    print("=" * 60)
    demonstrate_logical_operators()

    print("\n" + "=" * 60)
    print("BITWISE OPERATORS")
    print("=" * 60)
    demonstrate_bitwise_operators()

    print("\n" + "=" * 60)
    print("ASSIGNMENT OPERATORS")
    print("=" * 60)
    demonstrate_assignment_operators()

    print("\n" + "=" * 60)
    print("IDENTITY OPERATORS")
    print("=" * 60)
    demonstrate_identity_operators()

    print("\n" + "=" * 60)
    print("MEMBERSHIP OPERATORS")
    print("=" * 60)
    demonstrate_membership_operators()

    print("\n" + "=" * 60)
    print("OPERATOR PRECEDENCE")
    print("=" * 60)
    demonstrate_operator_precedence()

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("1. Use // for integer division, / for float division")
    print("2. Use 'is' for None comparison, '==' for value comparison")
    print("3. 'in' is O(1) for sets/dicts, O(n) for lists")
    print("4. Use parentheses for clarity in complex expressions")
    print("5. Walrus operator (:=) assigns and returns in one expression")
    print("=" * 60)


if __name__ == "__main__":
    main()
