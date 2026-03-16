"""
Variables and Type Hints in Python 3.12+

This module covers the fundamentals of variables, type annotations,
and how Python handles data storage and type checking.

Time Complexity: Variable assignment is O(1)
Space Complexity: Variables store references, not copies (unless immutable)
"""

from __future__ import annotations


def basic_variables() -> None:
    """
    Demonstrate basic variable assignment and naming conventions.

    Variables in Python are references to objects in memory.
    Python uses snake_case for variable names by convention.

    Time Complexity: O(1) for assignment
    Space Complexity: O(1) for the reference
    """
    # Basic variable assignments
    user_name: str = "Alice"
    user_age: int = 28
    account_balance: float = 1250.75
    is_active: bool = True

    print(f"User: {user_name}, Age: {user_age}")
    print(f"Balance: ${account_balance:.2f}, Active: {is_active}")

    # Python allows type inference (type hints are optional but recommended)
    inferred_string = "Type inferred as str"
    inferred_number = 42  # Type inferred as int

    # Multiple assignment (tuple unpacking)
    x, y, z = 1, 2, 3
    print(f"Coordinates: ({x}, {y}, {z})")

    # Swap variables (Pythonic way)
    x, y = y, x
    print(f"After swap: x={x}, y={y}")


def type_annotations_basics() -> None:
    """
    Demonstrate Python 3.12+ type annotation syntax.

    Type hints help with:
    - Code documentation
    - IDE autocomplete
    - Static type checking (mypy, pyright)

    Note: Type hints are NOT enforced at runtime by default.
    """
    # Built-in generic types (Python 3.9+)
    # No need to import List, Dict from typing
    numbers: list[int] = [1, 2, 3, 4, 5]
    user_scores: dict[str, int] = {"Alice": 95, "Bob": 87}
    unique_ids: set[int] = {101, 102, 103}

    # Tuple with fixed types
    coordinates: tuple[float, float, float] = (1.5, 2.3, 3.7)

    # Optional type (can be None)
    middle_name: str | None = None

    print(f"Numbers: {numbers}")
    print(f"Scores: {user_scores}")
    print(f"IDs: {unique_ids}")
    print(f"Coords: {coordinates}")
    print(f"Middle name: {middle_name}")


def variable_scopes() -> None:
    """
    Demonstrate variable scope rules (LEGB: Local, Enclosing, Global, Built-in).

    Understanding scope is crucial for avoiding bugs and writing clean code.
    """
    global_var: str = "I'm global"

    def outer_function() -> None:
        enclosing_var: str = "I'm enclosing"

        def inner_function() -> None:
            local_var: str = "I'm local"
            # Access order: local -> enclosing -> global -> built-in
            print(f"Inside inner: {local_var}")
            print(f"Can access enclosing: {enclosing_var}")
            print(f"Can access global: {global_var}")

        inner_function()
        # print(local_var)  # Would raise NameError

    outer_function()

    # Using global keyword (use sparingly - prefer passing parameters)
    counter: list[int] = [0]  # Using list to demonstrate mutable state

    def increment() -> None:
        counter[0] += 1  # Modifying mutable object

    increment()
    increment()
    print(f"Counter: {counter[0]}")


def constants_and_naming() -> None:
    """
    Demonstrate naming conventions for constants and variables.

    Python conventions:
    - CONSTANTS_USE_ALL_CAPS
    - variables_use_snake_case
    - _private_variables_start_with_underscore
    - __dunder_methods__ have double underscores
    """
    # Constants (by convention - not enforced)
    MAX_CONNECTIONS: int = 100
    DEFAULT_TIMEOUT: float = 30.0
    API_BASE_URL: str = "https://api.example.com"

    # "Private" variables (convention only - name mangling with __)
    _internal_state: int = 42
    __really_private: str = "This triggers name mangling"

    print(f"Max connections: {MAX_CONNECTIONS}")
    print(f"Timeout: {DEFAULT_TIMEOUT}s")
    print(f"API URL: {API_BASE_URL}")


def type_aliases() -> None:
    """
    Demonstrate type aliases for cleaner code (Python 3.12+).

    Type aliases make complex types more readable and reusable.
    """
    # Simple type alias
    type Vector = tuple[float, float, float]
    type UserID = int
    type UserDatabase = dict[UserID, str]

    # Using the type aliases
    position: Vector = (1.0, 2.0, 3.0)
    user_id: UserID = 12345
    users: UserDatabase = {1: "Alice", 2: "Bob"}

    print(f"Position: {position}")
    print(f"User ID: {user_id}")
    print(f"Users: {users}")


def variable_destruction() -> None:
    """
    Demonstrate memory management and variable deletion.

    Python uses reference counting and garbage collection.
    """
    # Create a variable
    data: list[int] = [1, 2, 3, 4, 5]
    print(f"Before deletion: {data}")

    # Delete variable (removes reference, may trigger garbage collection)
    del data
    # print(data)  # Would raise NameError

    # Partial deletion (delete specific indices)
    numbers: list[int] = [1, 2, 3, 4, 5]
    del numbers[2]  # Remove element at index 2
    print(f"After del numbers[2]: {numbers}")

    # Slice deletion
    more_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]
    del more_numbers[1:4]  # Remove elements at indices 1, 2, 3
    print(f"After del more_numbers[1:4]: {more_numbers}")


def demonstrate_variable_reassignment() -> None:
    """
    Demonstrate dynamic typing and variable reassignment.

    Python variables can reference different types over their lifetime.
    This is called dynamic typing, but type hints help catch errors.
    """
    # Variable can change types (but type checkers will warn)
    value: int | str | float = 42
    print(f"Initial value (int): {value}")

    value = "Now I'm a string"
    print(f"Reassigned (str): {value}")

    value = 3.14159
    print(f"Reassigned (float): {value}")

    # Better approach: use union types when type varies intentionally
    flexible_value: int | str = 100
    print(f"Flexible value: {flexible_value}")


if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON VARIABLES AND TYPE HINTS DEMONSTRATION")
    print("=" * 60)

    print("\n--- Basic Variables ---")
    basic_variables()

    print("\n--- Type Annotations ---")
    type_annotations_basics()

    print("\n--- Variable Scopes ---")
    variable_scopes()

    print("\n--- Constants and Naming ---")
    constants_and_naming()

    print("\n--- Type Aliases (Python 3.12+) ---")
    type_aliases()

    print("\n--- Variable Destruction ---")
    variable_destruction()

    print("\n--- Variable Reassignment ---")
    demonstrate_variable_reassignment()

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("1. Python 3.12+ uses built-in generics (list[int], dict[str, int])")
    print("2. Type hints improve code documentation and IDE support")
    print("3. Variables are references, not the objects themselves")
    print("4. Use snake_case for variables, ALL_CAPS for constants")
    print("5. Understand LEGB scope rules for clean code")
    print("=" * 60)
