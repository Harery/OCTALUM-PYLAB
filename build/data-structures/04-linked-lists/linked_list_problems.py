"""
Linked List Problems Module
===========================
Common algorithmic problems and solutions for linked lists.

Problems included:
- detect_cycle: Floyd's cycle detection algorithm
- find_middle: Find middle node using fast/slow pointers
- merge_two_sorted: Merge two sorted linked lists
- reverse_list: Reverse a linked list in-place
- remove_nth_from_end: Remove nth node from end

Time Complexity: Varies by problem (documented per function)
Space Complexity: O(1) for most solutions (in-place)
"""

from __future__ import annotations


class ListNode:
    """Node for linked list problems."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: ListNode | None = None

    def __repr__(self) -> str:
        return f"ListNode({self.value})"

    def __str__(self) -> str:
        return str(self.value)


def detect_cycle(head: ListNode | None) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's algorithm.

    Uses two pointers moving at different speeds. If there's a cycle,
    the fast pointer will eventually catch up to the slow pointer.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        head: Head node of the linked list

    Returns:
        True if cycle exists, False otherwise
    """
    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def find_middle(head: ListNode | None) -> ListNode | None:
    """
    Find the middle node of a linked list using fast/slow pointers.

    When fast reaches the end, slow will be at the middle.
    For even-length lists, returns the second middle node.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        head: Head node of the linked list

    Returns:
        Middle node, or None if list is empty
    """
    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_two_sorted(head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
    """
    Merge two sorted linked lists into one sorted list.

    Uses a dummy node to simplify edge cases and iteratively
    builds the merged list by comparing node values.

    Time Complexity: O(n + m) where n, m are lengths of input lists
    Space Complexity: O(1) - rearranges existing nodes

    Args:
        head1: Head of first sorted list
        head2: Head of second sorted list

    Returns:
        Head of merged sorted list
    """
    dummy = ListNode(0)
    current = dummy

    while head1 is not None and head2 is not None:
        if head1.value <= head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1 is not None:
        current.next = head1
    else:
        current.next = head2

    return dummy.next


def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    Reverse a linked list in-place.

    Iteratively reverses by changing next pointers to point
    to the previous node instead of the next node.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        head: Head node of the linked list

    Returns:
        New head of the reversed list
    """
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    """
    Remove the nth node from the end of a linked list.

    Uses two pointers separated by n nodes. When the front pointer
    reaches the end, the back pointer is at the node to remove.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        head: Head node of the linked list
        n: Position from end (1-indexed)

    Returns:
        Head of modified list

    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    dummy = ListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n):
        if fast.next is None:
            raise ValueError(f"List has fewer than {n} nodes")
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


def create_cycle_list(values: list[int], cycle_pos: int) -> ListNode | None:
    """
    Create a linked list with a cycle for testing.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        values: Values to create nodes from
        cycle_pos: Index of node to connect tail to (creates cycle)

    Returns:
        Head of the cyclic list
    """
    if not values:
        return None

    nodes: list[ListNode] = []
    for val in values:
        nodes.append(ListNode(val))

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if 0 <= cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


def list_to_array(head: ListNode | None) -> list[int]:
    """
    Convert linked list to array for easy comparison.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        head: Head node of the linked list

    Returns:
        List of values in order
    """
    result: list[int] = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def array_to_list(values: list[int]) -> ListNode | None:
    """
    Convert array to linked list for testing.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        values: Values to create nodes from

    Returns:
        Head of the linked list
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


if __name__ == "__main__":
    print("=== Linked List Problems Demo ===\n")

    # Test find_middle
    print("1. Find Middle:")
    head1 = array_to_list([1, 2, 3, 4, 5])
    print(f"   List: {list_to_array(head1)}")
    middle = find_middle(head1)
    print(f"   Middle value: {middle.value if middle else None}")

    head2 = array_to_list([1, 2, 3, 4])
    print(f"   List (even): {list_to_array(head2)}")
    middle2 = find_middle(head2)
    print(f"   Middle value: {middle2.value if middle2 else None}")

    # Test reverse_list
    print("\n2. Reverse List:")
    head3 = array_to_list([1, 2, 3, 4, 5])
    print(f"   Original: {list_to_array(head3)}")
    reversed_head = reverse_list(head3)
    print(f"   Reversed: {list_to_array(reversed_head)}")

    # Test merge_two_sorted
    print("\n3. Merge Two Sorted Lists:")
    list1 = array_to_list([1, 3, 5])
    list2 = array_to_list([2, 4, 6])

    print(f"   List 1: {list_to_array(list1)}")
    print(f"   List 2: {list_to_array(list2)}")
    merged = merge_two_sorted(list1, list2)
    print(f"   Merged: {list_to_array(merged)}")

    # Test remove_nth_from_end
    print("\n4. Remove Nth From End:")
    head4 = array_to_list([1, 2, 3, 4, 5])
    print(f"   Original: {list_to_array(head4)}")
    new_head = remove_nth_from_end(head4, 2)
    print(f"   After removing 2nd from end: {list_to_array(new_head)}")

    new_head = remove_nth_from_end(new_head, 4)
    print(f"   After removing 4th from end: {list_to_array(new_head)}")

    # Test detect_cycle
    print("\n5. Detect Cycle:")
    head5 = array_to_list([1, 2, 3, 4, 5])
    print(f"   List without cycle: {list_to_array(head5)}")
    print(f"   Has cycle: {detect_cycle(head5)}")

    cycle_head = create_cycle_list([1, 2, 3, 4, 5], 2)
    print(f"   List with cycle at position 2")
    print(f"   Has cycle: {detect_cycle(cycle_head)}")
