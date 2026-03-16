"""
Activity Selection Problem

Given n activities with start and finish times, select the maximum number of non-overlapping activities.

GREEDY APPROACH:
    Sort by finish time, always pick the activity with earliest finish.

WHY GREEDY WORKS:
    Optimal substructure property: choosing earliest finish leaves maximum room for remaining activities.

Time Complexity: O(n log n) for sorting
Space Complexity: O(n)
"""

from typing import List, Tuple


def activity_selection(activities: List[Tuple[int, int]]) -> int:
    """
    Select maximum non-overlapping activities.

    GREEDY ALGORITHM:
    1. Sort activities by finish time
    2. Select first activity
    3. Skip activities that overlap with selected
    4. Repeat until no more activities

    Args:
        activities: List of (start_time, finish_time) tuples

    Returns:
        Maximum number of non-overlapping activities

    Example:
        >>> activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
        >>> activity_selection(activities)
        4
    """
    if not activities:
        return 0

    # Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])

    count = 0
    last_finish = float('-inf')
    selected_indices = []

    for i, (start, finish) in enumerate(sorted_activities):
        if start >= last_finish:
            count += 1
            last_finish = finish
            selected_indices.append(i)

    return count


def activity_selection_with_indices(activities: List[Tuple[int, int]]) -> List[int]:
    """
    Return indices of selected activities.
    """
    if not activities:
        return []

    sorted_with_idx = sorted(enumerate(activities), key=lambda x: x[1][1])

    count = 0
    last_finish = float('-inf')
    selected = []

    for idx, (start, finish) in sorted_with_idx:
        if start >= last_finish:
            count += 1
            last_finish = finish
            selected.append(idx)

    return selected


def activity_selection_with_names(activities: List[Tuple[str, int, int]]) -> List[str]:
    """
    Select activities with names.

    Args:
        activities: List of (name, start, finish) tuples

    Returns:
        List of selected activity names
    """
    if not activities:
        return []

    # Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[2])

    selected = []
    last_finish = float('-inf')

    for name, start, finish in sorted_activities:
        if start >= last_finish:
            selected.append(name)
            last_finish = finish

    return selected


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("ACTIVITY SELECTION DEMONSTRATION")
    print("=" * 60)

    # Basic example
    print("\n1. Basic Example")
    activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(f"   Activities (start, finish): {activities}")
    print(f"   Maximum activities: {activity_selection(activities)}")

    # With names
    print("\n2. With Activity Names")
    named_activities = [
        ("A", 1, 2), ("B", 3, 4), ("C", 0, 6),
        ("D", 5, 7), ("E", 8, 9), ("F", 5, 9)
    ]
    selected = activity_selection_with_names(named_activities)
    print(f"   All activities: {[a[0] for a in named_activities]}")
    print(f"   Selected: {selected}")

    # Visual representation
    print("\n3. Timeline Visualization")
    timeline = [(0, 2, 'A'), (3, 4, 'B'), (0, 6, 'C'), (5, 7, 'D'), (8, 9, 'E')]
    print("   Time: 0 1 2 3 4 5 6 7 8 9")
    print("   A:   ████░")
    print("   B:       ████→")
    print("   C:   ████████→")
    print("   D:             ████→")
    print("   E:                 ██→")

    print("\n" + "=" * 60)
    print("All tests completed!")
