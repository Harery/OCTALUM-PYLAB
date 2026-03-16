"""
Functions: Decorators in Python.

This module demonstrates decorator patterns, @property, @staticmethod,
@classmethod, and creating custom decorators using Python 3.12+ syntax.

Time Complexity: O(1) for decorator application
Space Complexity: O(1) per decorated function
"""

from __future__ import annotations
from functools import wraps
from typing import Callable, TypeVar, ParamSpec
from dataclasses import dataclass
import time

P = ParamSpec('P')
R = TypeVar('R')


def basic_decorator(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Before {func.__name__}")
        result: R = func(*args, **kwargs)
        print(f"After {func.__name__}")
        return result
    return wrapper


@basic_decorator
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


def decorator_with_args(prefix: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            print(f"{prefix}: Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@decorator_with_args("LOG")
def calculate(x: int, y: int) -> int:
    return x + y


def timer_decorator(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start: float = time.perf_counter()
        result: R = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


@timer_decorator
def slow_function(n: int) -> int:
    total: int = 0
    for i in range(n):
        total += i
    return total


def retry_decorator(max_attempts: int = 3) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_error: Exception | None = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise last_error if last_error else RuntimeError("All attempts failed")
        return wrapper
    return decorator


@retry_decorator(max_attempts=3)
def unreliable_function(should_fail: bool) -> str:
    if should_fail:
        raise ValueError("Simulated failure")
    return "Success!"


def validate_types(**expected_types: type) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for param_name, expected_type in expected_types.items():
                if param_name in kwargs:
                    actual_value = kwargs[param_name]
                    if not isinstance(actual_value, expected_type):
                        raise TypeError(
                            f"{param_name} must be {expected_type.__name__}, "
                            f"got {type(actual_value).__name__}"
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_types(name=str, age=int)
def greet_person(name: str, age: int) -> str:
    return f"{name} is {age} years old"


def memoize_decorator(func: Callable[P, R]) -> Callable[P, R]:
    cache: dict[tuple, R] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        key: tuple = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


@memoize_decorator
def expensive_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return expensive_fibonacci(n - 1) + expensive_fibonacci(n - 2)


def count_calls(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        wrapper.call_count += 1
        print(f"{func.__name__} called {wrapper.call_count} times")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


@count_calls
def increment_counter(x: int) -> int:
    return x + 1


class BankAccount:
    def __init__(self, initial_balance: float) -> None:
        self._balance: float = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @balance.deleter
    def balance(self) -> None:
        print("Deleting balance")
        self._balance = 0.0


class Circle:
    def __init__(self, radius: float) -> None:
        self._radius: float = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self) -> float:
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * 3.14159 * self._radius


class MathOperations:
    PI: float = 3.14159

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @classmethod
    def create_with_pi(cls) -> "MathOperations":
        instance = cls.__new__(cls)
        instance.value = cls.PI
        return instance


class Counter:
    _instance_count: int = 0

    def __init__(self) -> None:
        Counter._instance_count += 1
        self._id: int = Counter._instance_count

    @classmethod
    def get_instance_count(cls) -> int:
        return cls._instance_count

    @classmethod
    def from_value(cls, value: int) -> "Counter":
        instance = cls()
        instance._id = value
        return instance

    @staticmethod
    def is_valid_id(id_value: int) -> bool:
        return id_value > 0


@dataclass
class Person:
    name: str
    age: int

    @property
    def is_adult(self) -> bool:
        return self.age >= 18

    @classmethod
    def from_string(cls, data: str) -> "Person":
        name, age_str = data.split(",")
        return cls(name=name.strip(), age=int(age_str.strip()))

    @staticmethod
    def validate_age(age: int) -> bool:
        return 0 <= age <= 150


def register_plugin(name: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        func._plugin_name = name
        return func
    return decorator


@register_plugin("data_processor")
def process_data(data: list[int]) -> list[int]:
    return [x * 2 for x in data]


class Singleton:
    _instance: "Singleton | None" = None

    def __new__(cls) -> "Singleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized: bool = True
            self.value: int = 0


def main() -> None:
    print("=" * 60)
    print("BASIC DECORATORS")
    print("=" * 60)
    result: str = say_hello("World")
    print(f"Result: {result}")

    print("\n" + "=" * 60)
    print("DECORATOR WITH ARGUMENTS")
    print("=" * 60)
    print(f"calculate(5, 3): {calculate(5, 3)}")

    print("\n" + "=" * 60)
    print("TIMER DECORATOR")
    print("=" * 60)
    slow_function(100000)

    print("\n" + "=" * 60)
    print("RETRY DECORATOR")
    print("=" * 60)
    print(f"unreliable_function(False): {unreliable_function(False)}")

    print("\n" + "=" * 60)
    print("TYPE VALIDATION DECORATOR")
    print("=" * 60)
    print(greet_person(name="Alice", age=30))

    print("\n" + "=" * 60)
    print("MEMOIZATION DECORATOR")
    print("=" * 60)
    print(f"expensive_fibonacci(30): {expensive_fibonacci(30)}")

    print("\n" + "=" * 60)
    print("CALL COUNTING DECORATOR")
    print("=" * 60)
    increment_counter(5)
    increment_counter(10)
    increment_counter(15)

    print("\n" + "=" * 60)
    print("@PROPERTY DECORATOR")
    print("=" * 60)
    account: BankAccount = BankAccount(100.0)
    print(f"Initial balance: {account.balance}")
    account.balance = 200.0
    print(f"After deposit: {account.balance}")

    circle: Circle = Circle(5.0)
    print(f"Circle radius: {circle.radius}")
    print(f"Circle area: {circle.area:.2f}")
    print(f"Circle circumference: {circle.circumference:.2f}")

    print("\n" + "=" * 60)
    print("@STATICMETHOD AND @CLASSMETHOD")
    print("=" * 60)
    print(f"MathOperations.add(5, 3): {MathOperations.add(5, 3)}")
    print(f"Counter.get_instance_count(): {Counter.get_instance_count()}")
    c1: Counter = Counter()
    c2: Counter = Counter()
    print(f"After 2 instances: {Counter.get_instance_count()}")
    print(f"Counter.is_valid_id(5): {Counter.is_valid_id(5)}")

    print("\n" + "=" * 60)
    print("DATACLASS WITH DECORATORS")
    print("=" * 60)
    person: Person = Person("Alice", 25)
    print(f"Person: {person.name}, is_adult: {person.is_adult}")
    person2: Person = Person.from_string("Bob, 30")
    print(f"From string: {person2.name}, age: {person2.age}")

    print("\n" + "=" * 60)
    print("SINGLETON PATTERN")
    print("=" * 60)
    s1: Singleton = Singleton()
    s2: Singleton = Singleton()
    print(f"Same instance? {s1 is s2}")


if __name__ == "__main__":
    main()
