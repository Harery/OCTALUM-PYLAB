# Merge Intervals Pattern

## When to Use
- **Problems with ranges/intervals** - meetings, schedules, time slots
- **Finding overlaps** - between ranges
- **Merging contiguous regions** - combining adjacent intervals
- **Resource allocation** - meeting rooms, CPU scheduling

## Key Signals
| Signal | Example |
|--------|---------|
| "Merge overlapping" | Combine intersecting intervals |
| "Meeting rooms/schedule" | Time slot management |
| "Insert interval" | Add and merge in sorted list |
| "Minimum rooms/resources" | Count concurrent intervals |
| "Non-overlapping" | Remove/modify conflicting ranges |

## Template Variants

### 1. Merge Overlapping
```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]

for current in intervals[1:]:
    if current[0] <= merged[-1][1]:  # Overlap
        merged[-1][1] = max(merged[-1][1], current[1])
    else:
        merged.append(current)
```

### 2. Meeting Rooms (Count Concurrent)
```python
starts = sorted(i[0] for i in intervals)
ends = sorted(i[1] for i in intervals)
rooms = end_ptr = 0

for start in starts:
    if start >= ends[end_ptr]:
        end_ptr += 1
    else:
        rooms += 1
```

### 3. Insert Interval
```python
result = []
# Add intervals before new
# Merge overlapping with new
# Add remaining intervals
```

## Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Merge intervals | O(n log n) | O(n) |
| Insert interval | O(n) | O(n) |
| Min meeting rooms | O(n log n) | O(n) |
| Interval intersection | O(n + m) | O(n + m) |

## LeetCode Problems

| # | Problem | Difficulty | Key Insight |
|---|---------|------------|-------------|
| [56](https://leetcode.com/problems/merge-intervals/) | Merge Intervals | Medium | Sort + merge |
| [57](https://leetcode.com/problems/insert-interval/) | Insert Interval | Medium | Three phases |
| [252](https://leetcode.com/problems/meeting-rooms/) | Meeting Rooms | Easy | Check overlap |
| [253](https://leetcode.com/problems/meeting-rooms-ii/) | Meeting Rooms II | Medium | Two pointers |
| [435](https://leetcode.com/problems/non-overlapping-intervals/) | Non-overlapping Intervals | Medium | Greedy by end |
| [452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Min Arrows | Medium | Same as non-overlap |
| [986](https://leetcode.com/problems/interval-list-intersections/) | Interval Intersection | Medium | Two pointers |
| [759](https://leetcode.com/problems/employee-free-time/) | Employee Free Time | Hard | Merge all + gaps |

## Common Mistakes
1. **Not sorting first** - Always sort by start time
2. **Wrong overlap condition** - `a.start <= b.end` AND `b.start <= a.end`
3. **Modifying while iterating** - Create new list for merged
4. **Using exclusive vs inclusive** - Clarify if endpoints overlap

## Quick Reference
```python
# Overlap check
def overlaps(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

# Merge two overlapping
def merge(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

# Standard merge pattern
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for curr in intervals[1:]:
    if curr[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], curr[1])
    else:
        merged.append(curr)
```

## Greedy Insight
For "minimum removals" problems, sort by **end time** and greedily keep intervals that end earliest. This leaves maximum room for remaining intervals.
