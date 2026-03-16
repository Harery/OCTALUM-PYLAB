# Fast & Slow Pointers Pattern

## When to Use
- **Linked list problems** - especially with cycle detection
- **Finding middle element** - in single pass
- **Problems involving cycles** - not just linked lists
- **Reversing portions of linked list** - combine with other ops

## Key Signals
| Signal | Example |
|--------|---------|
| "Detect cycle/loop" | Linked list, sequence |
| "Find middle" | Single pass requirement |
| "Happy number" | Cycle in transformation |
| "Palindrome linked list" | O(1) space requirement |
| "Kth from end" | Single traversal |

## Template Variants

### 1. Basic Cycle Detection
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle exists
return False
```

### 2. Find Cycle Start
```python
# After detecting cycle at meeting point
slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next
return slow  # Cycle start
```

### 3. Find Middle
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow  # Middle node
```

### 4. Kth from End
```python
fast = head
for _ in range(k):
    fast = fast.next
slow = head
while fast:
    slow = slow.next
    fast = fast.next
return slow
```

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Cycle detection | O(n) | O(1) |
| Find middle | O(n) | O(1) |
| Happy number | O(log n) | O(1) |
| Palindrome check | O(n) | O(1) |

## LeetCode Problems

### Cycle Detection
| # | Problem | Difficulty |
|---|---------|------------|
| [141](https://leetcode.com/problems/linked-list-cycle/) | Linked List Cycle | Easy |
| [142](https://leetcode.com/problems/linked-list-cycle-ii/) | Linked List Cycle II | Medium |

### Middle Element
| # | Problem | Difficulty |
|---|---------|------------|
| [876](https://leetcode.com/problems/middle-of-the-linked-list/) | Middle of Linked List | Easy |

### Other Applications
| # | Problem | Difficulty |
|---|---------|------------|
| [202](https://leetcode.com/problems/happy-number/) | Happy Number | Easy |
| [234](https://leetcode.com/problems/palindrome-linked-list/) | Palindrome Linked List | Easy |
| [19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Remove Nth From End | Medium |
| [143](https://leetcode.com/problems/reorder-list/) | Reorder List | Medium |
| [457](https://leetcode.com/problems/circular-array-loop/) | Circular Array Loop | Medium |

## Common Mistakes
1. **Not checking fast.next** - Causes null pointer in odd-length lists
2. **Wrong cycle start logic** - Reset slow to head, not keep it
3. **Infinite loop on happy number** - Check `slow == fast` before `fast == 1`
4. **Off-by-one in kth from end** - Use dummy node for remove

## Quick Reference
```python
# Fast-slow for cycle
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:  # Cycle detected
        # Phase 2: find start
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow

# Fast-slow for middle
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
return slow
```

## Math Behind Cycle Start
- Distance from head to cycle start: `a`
- Distance from cycle start to meeting point: `b`
- Cycle length: `c`
- When they meet: `slow` traveled `a + b`, `fast` traveled `a + b + nc`
- Since fast is 2x speed: `2(a + b) = a + b + nc` → `a + b = nc`
- So: `a = nc - b` = distance from meeting point to cycle start
