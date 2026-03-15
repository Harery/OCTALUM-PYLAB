# Interview Preparation Checklist

Complete guide to preparing for technical interviews.

## Pre-Interview Checklist

### Week Before

- [ ] Review all 12 coding patterns
- [ ] Solve 5 problems per day (mixed difficulty)
- [ ] Practice explaining solutions out loud
- [ ] Do at least 2 mock interviews
- [ ] Review your strongest projects
- [ ] Prepare 5 stories (2 wins, 2 challenges, 1 failure)

### Day Before

- [ ] Light review only - no cramming
- [ ] Prepare interview environment (if remote)
- [ ] Test audio/video equipment
- [ ] Get adequate sleep
- [ ] Prepare water and notepad

### Day Of

- [ ] Arrive 10-15 minutes early (or log in early)
- [ ] Have resume and notes ready
- [ ] Prepare questions for interviewer
- [ ] Relax and breathe

---

## Topics to Master

### Must Know (High Priority)

| Topic | Questions | Status |
|-------|-----------|--------|
| Arrays & Strings | 20+ | ⬜ |
| Hash Tables | 15+ | ⬜ |
| Two Pointers | 10+ | ⬜ |
| Sliding Window | 10+ | ⬜ |
| Binary Search | 10+ | ⬜ |
| Trees (BST, Traversals) | 15+ | ⬜ |
| BFS/DFS | 10+ | ⬜ |
| Linked Lists | 10+ | ⬜ |
| Stacks & Queues | 10+ | ⬜ |
| Heaps | 8+ | ⬜ |

### Should Know (Medium Priority)

| Topic | Questions | Status |
|-------|-----------|--------|
| Dynamic Programming | 15+ | ⬜ |
| Graph Algorithms | 10+ | ⬜ |
| Backtracking | 10+ | ⬜ |
| Greedy | 8+ | ⬜ |
| Tries | 5+ | ⬜ |
| Design (LRU Cache) | 5+ | ⬜ |

### Nice to Know (Lower Priority)

| Topic | Questions | Status |
|-------|-----------|--------|
| Segment Trees | 3+ | ⬜ |
| Union-Find | 5+ | ⬜ |
| Bit Manipulation | 5+ | ⬜ |
| Math/Geometry | 5+ | ⬜ |

---

## Problem-Solving Framework

### UMPIRE Method

1. **U**nderstand
   - Read the problem twice
   - Clarify assumptions
   - Ask about edge cases

2. **M**atch
   - What pattern fits?
   - Similar problems solved?
   - What data structure?

3. **P**lan
   - Write pseudocode
   - Identify complexity
   - Consider tradeoffs

4. **I**mplement
   - Write clean code
   - Use meaningful names
   - Handle edge cases

5. **R**eview
   - Test with examples
   - Check edge cases
   - Optimize if needed

6. **E**valuate
   - Time complexity
   - Space complexity
   - Alternative approaches

---

## Common Pitfalls

### Coding Mistakes

| Pitfall | How to Avoid |
|---------|--------------|
| Off-by-one errors | Test boundary indices |
| Integer overflow | Use Python or check bounds |
| Empty input | Handle null/empty early |
| Infinite loops | Clear exit conditions |
| Index out of bounds | Check array length |

### Logic Errors

| Pitfall | How to Avoid |
|---------|--------------|
| Wrong base case | Test smallest input |
| Missing edge case | List all edge cases |
| Incorrect complexity | Analyze properly |
| State not reset | Track variables carefully |

### Communication Errors

| Pitfall | How to Avoid |
|---------|--------------|
| Silent coding | Narrate your thought |
| Not asking questions | Clarify before coding |
| Giving up too early | Try brute force first |
| Defending bad code | Acknowledge issues |

---

## Question Categories

### Array/String Questions

- [ ] Two Sum
- [ ] Contains Duplicate
- [ ] Product of Array Except Self
- [ ] Maximum Subarray
- [ ] Merge Intervals
- [ ] Longest Substring Without Repeating

### Linked List Questions

- [ ] Reverse Linked List
- [ ] Detect Cycle
- [ ] Merge Two Sorted Lists
- [ ] Remove Nth From End
- [ ] Reorder List

### Tree Questions

- [ ] Maximum Depth
- [ ] Validate BST
- [ ] Level Order Traversal
- [ ] Lowest Common Ancestor
- [ ] Serialize/Deserialize

### Graph Questions

- [ ] Number of Islands
- [ ] Clone Graph
- [ ] Course Schedule
- [ ] Pacific Atlantic Flow
- [ ] Word Ladder

### Dynamic Programming

- [ ] Coin Change
- [ ] Longest Increasing Subsequence
- [ ] Edit Distance
- [ ] Maximum Product Subarray
- [ ] Decode Ways

---

## Behavioral Questions

### STAR Method

**S**ituation → **T**ask → **A**ction → **R**esult

### Prepare 5 Stories

1. **Technical Challenge**
   - Problem: Complex bug or architecture decision
   - Action: Debugging process or design choices
   - Result: Solution and lessons learned

2. **Collaboration**
   - Problem: Team conflict or coordination issue
   - Action: How you facilitated resolution
   - Result: Improved team dynamics

3. **Leadership**
   - Problem: Project ownership or initiative
   - Action: Steps you took to lead
   - Result: Impact on team/project

4. **Failure**
   - Problem: Something that didn't work
   - Action: How you handled it
   - Result: What you learned

5. **Success**
   - Problem: Significant achievement
   - Action: Your contribution
   - Result: Measurable impact

---

## Questions to Ask Interviewer

### About the Role

- What does a typical day look like?
- How is success measured in this role?
- What's the biggest challenge the team is facing?

### About the Team

- How is the team structured?
- How does the team collaborate?
- What's the code review process?

### About the Company

- What excites you about the company's future?
- How would you describe the engineering culture?
- What opportunities for growth exist?

---

## Time Management During Interview

| Phase | Time (45 min) | Time (60 min) |
|-------|---------------|---------------|
| Understanding | 5 min | 7 min |
| Planning | 5 min | 8 min |
| Coding | 25 min | 30 min |
| Testing | 5 min | 8 min |
| Optimization | 5 min | 7 min |

---

## Mock Interview Checklist

### Self-Assessment

- [ ] Did I understand the problem before coding?
- [ ] Did I clarify edge cases?
- [ ] Did I explain my approach?
- [ ] Did I handle all edge cases?
- [ ] Did I test my solution?
- [ ] Did I analyze complexity?
- [ ] Was my code clean and readable?

### Feedback to Seek

- [ ] Communication clarity
- [ ] Problem-solving approach
- [ ] Code quality
- [ ] Time management
- [ ] Areas for improvement

---

## Quick Reference

### Python One-Liners

```python
# Reverse string
s[::-1]

# Check palindrome
s == s[::-1]

# Frequency count
from collections import Counter; Counter(arr)

# Unique elements
list(set(arr))

# Flatten 2D list
[item for sublist in matrix for item in sublist]

# Sort by key
sorted(arr, key=lambda x: x[1])

# Group by
from itertools import groupby

# Binary search
import bisect; bisect.bisect_left(arr, target)
```

### Common Complexities

| Input Size | Acceptable Complexity |
|------------|----------------------|
| n ≤ 10 | O(n!) |
| n ≤ 20 | O(2^n) |
| n ≤ 500 | O(n³) |
| n ≤ 5000 | O(n²) |
| n ≤ 10^6 | O(n log n) |
| n ≤ 10^8 | O(n) |

---

*Good luck! You've got this! 🍀*
