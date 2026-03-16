"""
Fast & Slow Pointers (Floyd's Cycle Detection)

Use when: Linked lists, cycle detection, finding middle element
Time: O(n), Space: O(1)
"""

from typing import Optional, List

# ============================================================
# Linked List Node
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# TEMPLATE 1: Cycle Detection
# ============================================================

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if linked list has a cycle.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the node where cycle begins.
    Time: O(n), Space: O(1)

    Math: After slow and fast meet, reset one pointer to head.
    Move both at same speed - they meet at cycle start.
    """
    if not head or not head.next:
        return None

    slow = fast = head

    # Phase 1: Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def cycle_length(head: Optional[ListNode]) -> int:
    """
    Find length of cycle if exists.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return 0

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Count cycle length
            length = 1
            current = slow.next
            while current != slow:
                current = current.next
                length += 1
            return length

    return 0


# ============================================================
# TEMPLATE 2: Find Middle Element
# ============================================================

def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node. If even length, return second middle.
    Time: O(n), Space: O(1)
    """
    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def find_middle_first(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find middle node. If even length, return first middle.
    Time: O(n), Space: O(1)
    """
    if not head:
        return None

    slow = fast = head
    fast = fast.next  # Start fast one step ahead

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# ============================================================
# TEMPLATE 3: Happy Number (Cycle in sequence)
# ============================================================

def is_happy(n: int) -> bool:
    """
    Check if number is happy (eventually reaches 1).
    Non-happy numbers cycle. Time: O(log n), Space: O(1)
    """
    def sum_squares(num: int) -> int:
        total = 0
        while num:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    slow = n
    fast = sum_squares(n)

    while fast != 1 and slow != fast:
        slow = sum_squares(slow)
        fast = sum_squares(sum_squares(fast))

    return fast == 1


# ============================================================
# TEMPLATE 4: Palindrome Linked List
# ============================================================

def is_palindrome_linked_list(head: Optional[ListNode]) -> bool:
    """
    Check if linked list is palindrome.
    Time: O(n), Space: O(1) - modifies list temporarily
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse_list(slow.next)

    # Compare both halves
    first, second = head, second_half
    result = True
    while second:
        if first.val != second.val:
            result = False
            break
        first = first.next
        second = second.next

    # Restore list (optional)
    slow.next = reverse_list(second_half)

    return result


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse linked list. Time: O(n), Space: O(1)"""
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev


# ============================================================
# TEMPLATE 5: Find Kth from End
# ============================================================

def find_kth_from_end(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Find kth node from end (1-indexed).
    Time: O(n), Space: O(1)
    """
    fast = head

    # Move fast k steps ahead
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    slow = head
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end.
    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0, head)
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


# ============================================================
# TEMPLATE 6: Reorder List
# ============================================================

def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorder: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return

    # Find middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = reverse_list(slow.next)
    slow.next = None

    # Merge two halves
    first = head
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


# ============================================================
# Quick Test
# ============================================================
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # Cycle detection
    head = create_linked_list([3, 2, 0, -4])
    head.next.next.next.next = head.next  # Create cycle
    print("Has cycle:", has_cycle(head))

    # Middle element
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Middle:", find_middle(head).val)

    # Happy number
    print("19 is happy:", is_happy(19))
    print("2 is happy:", is_happy(2))

    # Palindrome
    head = create_linked_list([1, 2, 2, 1])
    print("Is palindrome:", is_palindrome_linked_list(head))

    # Kth from end
    head = create_linked_list([1, 2, 3, 4, 5])
    print("2nd from end:", find_kth_from_end(head, 2).val)
