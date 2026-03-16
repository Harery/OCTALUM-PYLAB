"""
Recursion Fundamentals Module

Recursion is a programming technique where a function calls itself to solve
smaller instances of the same problem. Understanding recursion is essential
for tree traversals, divide-and-conquer algorithms, and dynamic programming.

KEY CONCEPTS:
    1. Base Case: The condition that stops recursion
    2. Recursive Case: The function calling itself with smaller input
    3. Call Stack: Memory where function calls are stored

TIME/SPACE ANALYSIS:
    - Time: Usually related to number of recursive calls
    - Space: O(depth) for call stack

COMMON PITFALLS:
    - Missing base case → infinite recursion → stack overflow
    - Wrong base case → incorrect results
    - Too deep recursion → stack overflow
"""

from typing import TypeVar

T = TypeVar('T')


# =============================================================================
# BASIC RECURSIVE EXAMPLES
# =============================================================================

def factorial(n: int) -> int:
    """
    Calculate factorial using recursion.

    MATHEMATICAL DEFINITION:
    n! = n × (n-1) × (n-2) × ... × 1
    n! = n × (n-1)!  (recursive definition)
    0! = 1            (base case)

    CALL STACK VISUALIZATION for factorial(4):
    factorial(4)
    └── 4 × factorial(3)
        └── 3 × factorial(2)
            └── 2 × factorial(1)
                └── 1 × factorial(0)
                    └── return 1 (base case)
                ← returns 1
            ← returns 2 × 1 = 2
        ← returns 3 × 2 = 6
    ← returns 4 × 6 = 24

    Time Complexity: O(n)
    Space Complexity: O(n) for call stack

    Args:
        n: Non-negative integer

    Returns:
        n!
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")

    # Base case: 0! = 1
    if n <= 1:
        return 1

    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calculate nth Fibonacci number (naive recursion).

    FIBONACCI SEQUENCE: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1

    WHY THIS IS INEFFICIENT:
    Same subproblems are solved repeatedly.
    fibonacci(5) calls:
    - fibonacci(4) calls fibonacci(3) and fibonacci(2)
    - fibonacci(3) calls fibonacci(2) and fibonacci(1)
    Notice fibonacci(2) is computed multiple times!

    Time Complexity: O(2^n) - exponential!
    Space Complexity: O(n)

    BETTER APPROACH: Use memoization (see dynamic programming)
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")

    # Base cases
    if n <= 1:
        return n

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Fibonacci using iteration (avoids recursion overhead).

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


def sum_array(arr: list[int], n: int | None = None) -> int:
    """
    Sum array elements using recursion.

    RECURSIVE APPROACH:
    sum(arr, n) = arr[n-1] + sum(arr, n-1)
    sum(arr, 0) = 0  (base case)

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n is None:
        n = len(arr)

    if n <= 0:
        return 0

    return arr[n - 1] + sum_array(arr, n - 1)


def power(base: int, exp: int) -> int:
    """
    Calculate base^exp using recursion.

    NAIVE APPROACH:
    base^exp = base × base^(exp-1)

    Time Complexity: O(exp)
    Space Complexity: O(exp)
    """
    if exp < 0:
        raise ValueError("This implementation doesn't handle negative exponents")

    if exp == 0:
        return 1

    return base * power(base, exp - 1)


def power_optimized(base: int, exp: int) -> int:
    """
    Calculate base^exp using binary exponentiation.

    OPTIMIZED APPROACH (Exponentiation by Squaring):
    base^exp = (base^2)^(exp/2)     if exp is even
    base^exp = base × base^(exp-1)  if exp is odd

    WHY FASTER:
    exp is halved each step instead of reduced by 1.

    Time Complexity: O(log exp)
    Space Complexity: O(log exp)
    """
    if exp < 0:
        raise ValueError("This implementation doesn't handle negative exponents")

    if exp == 0:
        return 1

    if exp % 2 == 0:
        # Even: (base^2)^(exp/2)
        half = power_optimized(base, exp // 2)
        return half * half
    else:
        # Odd: base × base^(exp-1)
        return base * power_optimized(base, exp - 1)


def gcd(a: int, b: int) -> int:
    """
    Calculate GCD using Euclidean algorithm.

    EUCLIDEAN ALGORITHM:
    gcd(a, b) = gcd(b, a mod b)
    gcd(a, 0) = a  (base case)

    WHY IT WORKS:
    If a = bq + r, then gcd(a,b) = gcd(b,r)
    Eventually r becomes 0, and we have the GCD.

    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(log(min(a, b)))
    """
    if b == 0:
        return abs(a)

    return gcd(b, a % b)


# =============================================================================
# RECURSION PATTERNS
# =============================================================================

def print_numbers_desc(n: int) -> None:
    """
    Print numbers from n to 1 (tail recursion).

    TAIL RECURSION:
    Recursive call is the last operation.
    Can be optimized to iteration by compilers.
    """
    if n < 1:
        return

    print(n, end=' ')
    print_numbers_desc(n - 1)


def print_numbers_asc(n: int) -> None:
    """
    Print numbers from 1 to n (head recursion).

    HEAD RECURSION:
    Recursive call comes before the processing.
    Print happens after returning from recursive calls.
    """
    if n < 1:
        return

    print_numbers_asc(n - 1)
    print(n, end=' ')


def reverse_string(s: str) -> str:
    """
    Reverse a string using recursion.

    APPROACH:
    reverse(s) = reverse(s[1:]) + s[0]
    reverse("") = ""  (base case)

    Time Complexity: O(n²) due to string concatenation
    Space Complexity: O(n)
    """
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome using recursion.

    APPROACH:
    - Compare first and last characters
    - Recursively check middle portion

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


def sum_digits(n: int) -> int:
    """
    Sum of digits using recursion.

    APPROACH:
    sum_digits(n) = (n % 10) + sum_digits(n // 10)
    sum_digits(0) = 0  (base case)

    Time Complexity: O(log n) - number of digits
    Space Complexity: O(log n)
    """
    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


def count_digits(n: int) -> int:
    """
    Count number of digits using recursion.

    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    if n == 0:
        return 0 if n == 0 else 1

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


# =============================================================================
# TAIL RECURSION OPTIMIZATION
# =============================================================================

def factorial_tail(n: int, accumulator: int = 1) -> int:
    """
    Factorial with tail recursion.

    TAIL RECURSION:
    The recursive call is the very last operation.
    Accumulator carries the result forward.

    Python doesn't optimize tail recursion, but this
    pattern is useful in languages that do (Scheme, Scala).

    Time Complexity: O(n)
    Space Complexity: O(n) in Python (no TCO)
    """
    if n <= 1:
        return accumulator

    return factorial_tail(n - 1, n * accumulator)


# =============================================================================
# TREE RECURSION (Multiple Recursive Calls)
# =============================================================================

def towers_of_hanoi(n: int, source: str, auxiliary: str, target: str) -> list[str]:
    """
    Solve Towers of Hanoi puzzle.

    PROBLEM:
    Move n disks from source to target using auxiliary,
    never placing larger disk on smaller disk.

    RECURSIVE SOLUTION:
    1. Move n-1 disks from source to auxiliary
    2. Move largest disk from source to target
    3. Move n-1 disks from auxiliary to target

    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    moves = []

    def hanoi(n: int, src: str, aux: str, tgt: str) -> None:
        if n == 1:
            moves.append(f"{src} → {tgt}")
            return

        hanoi(n - 1, src, tgt, aux)
        moves.append(f"{src} → {tgt}")
        hanoi(n - 1, aux, src, tgt)

    hanoi(n, source, auxiliary, target)
    return moves


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("RECURSION FUNDAMENTALS DEMONSTRATION")
    print("=" * 60)

    # Basic recursion
    print("\n1. Factorial")
    print(f"   5! = {factorial(5)}")
    print(f"   0! = {factorial(0)}")

    # Fibonacci comparison
    print("\n2. Fibonacci")
    print(f"   F(10) recursive: {fibonacci(10)}")
    print(f"   F(10) iterative: {fibonacci_iterative(10)}")
    print("   (Recursive is O(2^n), iterative is O(n))")

    # Power
    print("\n3. Power")
    print(f"   2^10 naive: {power(2, 10)}")
    print(f"   2^10 optimized: {power_optimized(2, 10)}")
    print("   (Optimized is O(log n) vs O(n))")

    # GCD
    print("\n4. GCD (Euclidean Algorithm)")
    print(f"   gcd(48, 18) = {gcd(48, 18)}")

    # String recursion
    print("\n5. String Operations")
    print(f"   reverse('hello'): {reverse_string('hello')}")
    print(f"   is_palindrome('racecar'): {is_palindrome('racecar')}")
    print(f"   is_palindrome('hello'): {is_palindrome('hello')}")

    # Digit operations
    print("\n6. Digit Operations")
    print(f"   sum_digits(12345): {sum_digits(12345)}")
    print(f"   count_digits(12345): {count_digits(12345)}")

    # Towers of Hanoi
    print("\n7. Towers of Hanoi (3 disks)")
    moves = towers_of_hanoi(3, 'A', 'B', 'C')
    print(f"   Moves: {moves}")
    print(f"   Total moves: {len(moves)} (2^n - 1 = {2**3 - 1})")

    # Print patterns
    print("\n8. Recursion Patterns")
    print("   Descending: ", end='')
    print_numbers_desc(5)
    print("\n   Ascending:  ", end='')
    print_numbers_asc(5)
    print()

    print("\n" + "=" * 60)
    print("All tests completed!")
