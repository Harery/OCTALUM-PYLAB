"""
Stack Module
============
Stack implementations using both list and linked list.

LIFO (Last In, First Out) data structure.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Is Empty: O(1)

Space Complexity: O(n)
"""

from __future__ import annotations


class StackList:
    """
    Stack implementation using Python list.

    Simple and efficient for most use cases.
    """

    def __init__(self) -> None:
        self._data: list[int] = []

    def __repr__(self) -> str:
        return f"StackList({self._data})"

    def __str__(self) -> str:
        if not self._data:
            return "Stack: []"
        items = " <- ".join(str(x) for x in self._data)
        return f"Stack: [BOTTOM] {items} [TOP]"

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return bool(self._data)

    def push(self, value: int) -> None:
        self._data.append(value)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self) -> int:
        if not self._data:
            raise IndexError("Peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def clear(self) -> None:
        self._data.clear()

    def to_list(self) -> list[int]:
        return self._data.copy()


class StackNode:
    """Node for linked list stack."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: StackNode | None = None

    def __repr__(self) -> str:
        return f"StackNode({self.value})"


class StackLinkedList:
    """
    Stack implementation using singly linked list.

    Push and pop at head for O(1) operations.
    """

    def __init__(self) -> None:
        self._head: StackNode | None = None
        self._size: int = 0

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"StackLinkedList([{', '.join(reversed(values))}])"

    def __str__(self) -> str:
        if not self._head:
            return "Stack: []"
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        items = " <- ".join(reversed(values))
        return f"Stack: [BOTTOM] {items} [TOP]"

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._head is not None

    def push(self, value: int) -> None:
        new_node = StackNode(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self) -> int:
        if not self._head:
            raise IndexError("Pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def peek(self) -> int:
        if not self._head:
            raise IndexError("Peek from empty stack")
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        return self._size

    def clear(self) -> None:
        self._head = None
        self._size = 0

    def to_list(self) -> list[int]:
        result: list[int] = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return list(reversed(result))


class MinStack:
    """
    Stack that supports O(1) minimum value retrieval.

    Uses auxiliary stack to track minimums.
    """

    def __init__(self) -> None:
        self._data: list[int] = []
        self._mins: list[int] = []

    def __repr__(self) -> str:
        return f"MinStack({self._data}, min={self.get_min() if self._data else None})"

    def __str__(self) -> str:
        if not self._data:
            return "MinStack: []"
        return f"MinStack: {self._data}, min={self.get_min()}"

    def __len__(self) -> int:
        return len(self._data)

    def push(self, value: int) -> None:
        self._data.append(value)
        if not self._mins or value <= self._mins[-1]:
            self._mins.append(value)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("Pop from empty stack")
        value = self._data.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def peek(self) -> int:
        if not self._data:
            raise IndexError("Peek from empty stack")
        return self._data[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("Get min from empty stack")
        return self._mins[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0


def is_valid_parentheses(s: str) -> bool:
    """
    Check if parentheses string is valid using stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def evaluate_postfix(expression: str) -> int:
    """
    Evaluate postfix (Reverse Polish Notation) expression.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack: list[int] = []
    operators = {"+", "-", "*", "/"}

    tokens = expression.split()

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack.pop()


def infix_to_postfix(expression: str) -> str:
    """
    Convert infix expression to postfix notation.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output: list[str] = []
    stack: list[str] = []

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != "(" and
                   stack[-1] in precedence and
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


def next_greater_element(nums: list[int]) -> list[int]:
    """
    Find next greater element for each element.

    Returns -1 if no greater element exists.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    result = [-1] * n
    stack: list[int] = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])

    return result


def reverse_string(s: str) -> str:
    """
    Reverse a string using stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack: list[str] = list(s)
    result: list[str] = []
    while stack:
        result.append(stack.pop())
    return "".join(result)


def sort_stack(stack: list[int]) -> list[int]:
    """
    Sort a stack using only stack operations.

    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    def insert_sorted(s: list[int], item: int) -> None:
        if not s or s[-1] <= item:
            s.append(item)
            return
        temp = s.pop()
        insert_sorted(s, item)
        s.append(temp)

    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)

    return stack


if __name__ == "__main__":
    print("=== StackList ===")
    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    print(f"Size: {len(stack)}")

    print("\n=== StackLinkedList ===")
    ll_stack = StackLinkedList()
    ll_stack.push(10)
    ll_stack.push(20)
    ll_stack.push(30)
    print(f"Stack: {ll_stack}")
    print(f"Pop: {ll_stack.pop()}")

    print("\n=== MinStack ===")
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(3)
    min_stack.push(7)
    print(f"Stack: {min_stack}")
    print(f"Min: {min_stack.get_min()}")
    min_stack.pop()
    print(f"After pop, Min: {min_stack.get_min()}")

    print("\n=== Valid Parentheses ===")
    print(f"'()' -> {is_valid_parentheses('()')}")
    print(f"'()[]{{}}' -> {is_valid_parentheses('()[]{}')}")
    print(f"'([)]' -> {is_valid_parentheses('([)]')}")

    print("\n=== Postfix Evaluation ===")
    print(f"'2 3 + 4 *' = {evaluate_postfix('2 3 + 4 *')}")

    print("\n=== Next Greater Element ===")
    print(f"[4, 5, 2, 25] -> {next_greater_element([4, 5, 2, 25])}")
