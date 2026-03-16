"""
Control Flow: Conditionals in Python.

This module demonstrates conditional statements including if/elif/else,
ternary expressions, and pattern matching (Python 3.10+).

Time Complexity: O(1) for conditionals (unless condition evaluation is expensive)
Space Complexity: O(1)
"""

from __future__ import annotations


# ============================================================================
# BASIC IF/ELIF/ELSE
# ============================================================================

def demonstrate_basic_conditionals() -> None:
    """Demonstrate basic if, elif, else statements."""
    temperature: int = 25

    # Simple if statement
    if temperature > 30:
        print("It's hot!")

    # if-else statement
    age: int = 18
    if age >= 18:
        status: str = "adult"
    else:
        status = "minor"
    print(f"Age {age}: {status}")

    # if-elif-else chain
    score: int = 85
    if score >= 90:
        grade: str = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score {score}: Grade {grade}")


def conditional_with_logical_operators() -> None:
    """Demonstrate conditionals with and, or, not."""
    age: int = 25
    has_license: bool = True
    has_insurance: bool = True

    # Using 'and' - all conditions must be True
    if age >= 18 and has_license and has_insurance:
        print("You can rent a car")

    # Using 'or' - at least one condition must be True
    is_member: bool = False
    has_coupon: bool = True

    if is_member or has_coupon:
        print("You get a discount!")

    # Using 'not'
    is_banned: bool = False
    if not is_banned:
        print("Access granted")

    # Combining operators (use parentheses for clarity)
    is_weekend: bool = True
    is_holiday: bool = False
    is_working_hours: bool = False

    if (is_weekend or is_holiday) and not is_working_hours:
        print("Office is closed")


# ============================================================================
# NESTED CONDITIONALS
# ============================================================================

def demonstrate_nested_conditionals() -> None:
    """Demonstrate nested if statements (and why to avoid deep nesting)."""
    user_type: str = "premium"
    purchase_amount: float = 150.0

    # Deeply nested (harder to read)
    if user_type == "premium":
        if purchase_amount > 100:
            if purchase_amount > 200:
                discount: float = 0.25
            else:
                discount = 0.15
        else:
            discount = 0.10
    elif user_type == "regular":
        if purchase_amount > 100:
            discount = 0.10
        else:
            discount = 0.05
    else:
        discount = 0.0

    print(f"Discount: {discount * 100}%")


def flattened_conditionals() -> None:
    """Demonstrate flattened conditionals (preferred style)."""
    user_type: str = "premium"
    purchase_amount: float = 150.0
    discount: float = 0.0

    # Early returns / guard clauses pattern
    if user_type == "premium" and purchase_amount > 200:
        discount = 0.25
    elif user_type == "premium" and purchase_amount > 100:
        discount = 0.15
    elif user_type == "premium":
        discount = 0.10
    elif user_type == "regular" and purchase_amount > 100:
        discount = 0.10
    elif user_type == "regular":
        discount = 0.05

    print(f"Discount: {discount * 100}%")


# ============================================================================
# TERNARY EXPRESSION (CONDITIONAL EXPRESSION)
# ============================================================================

def demonstrate_ternary() -> None:
    """
    Demonstrate ternary conditional expressions.

    Syntax: value_if_true if condition else value_if_false

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Basic ternary
    age: int = 20
    status: str = "adult" if age >= 18 else "minor"
    print(f"Status: {status}")

    # Ternary with function calls
    def get_greeting(is_formal: bool) -> str:
        return "Good day, sir" if is_formal else "Hey there!"

    print(get_greeting(True))
    print(get_greeting(False))

    # Nested ternary (use sparingly - can be hard to read)
    score: int = 85
    result: str = (
        "Excellent" if score >= 90
        else "Good" if score >= 80
        else "Average" if score >= 70
        else "Needs Improvement"
    )
    print(f"Score {score}: {result}")

    # Ternary for default values
    user_input: str | None = None
    name: str = user_input if user_input is not None else "Guest"
    print(f"Hello, {name}!")


# ============================================================================
# MATCH-CASE (PYTHON 3.10+)
# ============================================================================

def demonstrate_match_basic() -> None:
    """
    Demonstrate basic pattern matching with match-case.

    Python 3.10+ structural pattern matching.
    """
    status_code: int = 404

    # Simple value matching
    match status_code:
        case 200:
            message: str = "OK"
        case 201:
            message = "Created"
        case 400:
            message = "Bad Request"
        case 404:
            message = "Not Found"
        case 500:
            message = "Internal Server Error"
        case _:  # Wildcard (default case)
            message = "Unknown status"

    print(f"Status {status_code}: {message}")


def demonstrate_match_with_or() -> None:
    """Demonstrate match with multiple patterns (OR pattern)."""
    command: str = "quit"

    match command:
        case "start" | "begin" | "run":
            action: str = "Starting..."
        case "stop" | "end" | "halt":
            action = "Stopping..."
        case "quit" | "exit" | "q":
            action = "Goodbye!"
        case _:
            action = "Unknown command"

    print(f"Command '{command}': {action}")


def demonstrate_match_with_guards() -> None:
    """Demonstrate match with guard conditions (if clauses)."""
    point: tuple[int, int] = (3, 4)

    match point:
        case (0, 0):
            description: str = "Origin"
        case (x, 0):
            description = f"On x-axis at {x}"
        case (0, y):
            description = f"On y-axis at {y}"
        case (x, y) if x == y:
            description = f"On diagonal at ({x}, {y})"
        case (x, y) if x > 0 and y > 0:
            description = f"First quadrant at ({x}, {y})"
        case (x, y) if x < 0 and y > 0:
            description = f"Second quadrant at ({x}, {y})"
        case (x, y) if x < 0 and y < 0:
            description = f"Third quadrant at ({x}, {y})"
        case (x, y):
            description = f"Fourth quadrant at ({x}, {y})"

    print(f"Point {point}: {description}")


def demonstrate_match_sequences() -> None:
    """Demonstrate pattern matching with sequences."""
    # List pattern matching
    items: list[str] = ["apple", "banana", "cherry"]

    match items:
        case []:
            result: str = "Empty list"
        case [single]:
            result = f"Single item: {single}"
        case [first, second]:
            result = f"Two items: {first} and {second}"
        case [first, second, third]:
            result = f"Three items: {first}, {second}, {third}"
        case [first, *rest]:
            result = f"First: {first}, Rest: {rest}"

    print(f"List match: {result}")

    # Tuple unpacking in match
    coordinates: tuple[int, int, int] = (1, 2, 3)

    match coordinates:
        case (0, 0, 0):
            desc: str = "Origin (3D)"
        case (x, 0, 0):
            desc = f"On x-axis at {x}"
        case (x, y, 0):
            desc = f"On xy-plane at ({x}, {y})"
        case (x, y, z):
            desc = f"3D point at ({x}, {y}, {z})"

    print(f"Tuple match: {desc}")


def demonstrate_match_dicts() -> None:
    """Demonstrate pattern matching with dictionaries."""
    user_data: dict[str, str | int] = {
        "name": "Alice",
        "role": "admin",
        "active": True
    }

    match user_data:
        case {"role": "admin", "name": name}:
            result: str = f"Admin user: {name}"
        case {"role": "user", "name": name}:
            result = f"Regular user: {name}"
        case {"name": name}:
            result = f"Unknown role user: {name}"
        case _:
            result = "Anonymous user"

    print(f"Dict match: {result}")


def demonstrate_match_classes() -> None:
    """Demonstrate pattern matching with class instances."""

    class Point:
        """A 2D point class."""

        def __init__(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

    class Circle:
        """A circle with center and radius."""

        def __init__(self, center: Point, radius: int) -> None:
            self.center = center
            self.radius = radius

    class Rectangle:
        """A rectangle with top-left corner and dimensions."""

        def __init__(self, x: int, y: int, width: int, height: int) -> None:
            self.x = x
            self.y = y
            self.width = width
            self.height = height

    shape: Circle | Rectangle = Circle(Point(0, 0), 5)

    match shape:
        case Circle(center=Point(x=cx, y=cy), radius=r):
            result: str = f"Circle at ({cx}, {cy}) with radius {r}"
        case Rectangle(x=x, y=y, width=w, height=h):
            result = f"Rectangle at ({x}, {y}) with size {w}x{h}"

    print(f"Class match: {result}")


# ============================================================================
# COMMON PATTERNS
# ============================================================================

def guard_clause_pattern() -> None:
    """
    Demonstrate guard clause pattern (early returns).

    This pattern reduces nesting and improves readability.
    """
    def process_user(
        user: dict[str, str | int | bool] | None,
        is_authenticated: bool
    ) -> str:
        # Guard clauses - check for invalid states first
        if user is None:
            return "Error: No user provided"

        if not is_authenticated:
            return "Error: User not authenticated"

        if not user.get("active", False):
            return "Error: User account is inactive"

        # Main logic (only reached if all guards pass)
        name = user.get("name", "Unknown")
        return f"Welcome, {name}!"

    # Test cases
    print(process_user(None, True))
    print(process_user({"name": "Alice", "active": True}, False))
    print(process_user({"name": "Alice", "active": True}, True))


def dictionary_dispatch() -> None:
    """
    Demonstrate dictionary dispatch pattern.

    An alternative to long if-elif chains for simple value mapping.
    """
    def calculate(operation: str, a: float, b: float) -> float | None:
        operations: dict[str, float] = {
            "add": a + b,
            "subtract": a - b,
            "multiply": a * b,
            "divide": a / b if b != 0 else float('nan'),
        }
        return operations.get(operation)

    print(f"add 5 + 3 = {calculate('add', 5, 3)}")
    print(f"multiply 4 * 2 = {calculate('multiply', 4, 2)}")


def truthiness_in_conditionals() -> None:
    """Demonstrate truthy/falsy values in conditionals."""
    # Falsy values: False, None, 0, 0.0, '', [], {}, set()

    values: list[tuple[object, str]] = [
        (0, "zero"),
        ("", "empty string"),
        ([], "empty list"),
        ({}, "empty dict"),
        (None, "None"),
        (False, "False"),
        ("hello", "non-empty string"),
        ([1], "non-empty list"),
    ]

    for value, description in values:
        if value:
            print(f"{description}: TRUTHY")
        else:
            print(f"{description}: FALSY")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Run all demonstrations."""
    print("=" * 60)
    print("BASIC CONDITIONALS")
    print("=" * 60)
    demonstrate_basic_conditionals()

    print("\n" + "=" * 60)
    print("CONDITIONALS WITH LOGICAL OPERATORS")
    print("=" * 60)
    conditional_with_logical_operators()

    print("\n" + "=" * 60)
    print("NESTED vs FLATTENED CONDITIONALS")
    print("=" * 60)
    demonstrate_nested_conditionals()
    flattened_conditionals()

    print("\n" + "=" * 60)
    print("TERNARY EXPRESSIONS")
    print("=" * 60)
    demonstrate_ternary()

    print("\n" + "=" * 60)
    print("MATCH-CASE (Python 3.10+)")
    print("=" * 60)
    demonstrate_match_basic()
    demonstrate_match_with_or()
    demonstrate_match_with_guards()
    demonstrate_match_sequences()
    demonstrate_match_dicts()
    demonstrate_match_classes()

    print("\n" + "=" * 60)
    print("COMMON PATTERNS")
    print("=" * 60)
    guard_clause_pattern()
    dictionary_dispatch()
    truthiness_in_conditionals()


if __name__ == "__main__":
    main()
