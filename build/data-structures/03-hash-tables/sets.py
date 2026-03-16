"""
Set Operations Module
=====================
Comprehensive demonstration of Python set operations and set theory concepts.

Sets are unordered collections of unique elements with O(1) membership testing.
"""

from __future__ import annotations


class SimpleSet:
    """
    A simple set implementation using a hash table.
    """

    def __init__(self) -> None:
        self._data: dict[int, None] = {}

    def __repr__(self) -> str:
        items = ", ".join(str(k) for k in self._data)
        return "{" + items + "}"

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return len(self._data)

    def add(self, item: int) -> None:
        self._data[item] = None

    def remove(self, item: int) -> bool:
        if item in self._data:
            del self._data[item]
            return True
        return False

    def contains(self, item: int) -> bool:
        return item in self._data


def create_sets() -> dict[str, set[int] | frozenset[int]]:
    """
    Demonstrate various ways to create sets.

    Time Complexity: O(n) for creation
    Space Complexity: O(n)
    """
    return {
        "empty": set(),
        "literal": {1, 2, 3, 4, 5},
        "from_list": set([1, 2, 2, 3, 3, 3]),
        "from_string": set("hello"),
        "from_range": set(range(5)),
        "comprehension": {x**2 for x in range(5)},
        "frozen": frozenset([1, 2, 3]),
    }


def basic_operations() -> dict[str, int | bool]:
    """
    Demonstrate basic set operations.

    Time Complexity: O(1) for add/remove/contains
    """
    s: set[int] = set()

    s.add(1)
    s.add(2)
    s.add(3)
    added_twice = s.add(2)

    return {
        "len": len(s),
        "contains_2": 2 in s,
        "contains_4": 4 in s,
        "add_returns_none": added_twice is None,
    }


def modification_operations() -> dict[str, set[int]]:
    """
    Demonstrate set modification operations.
    """
    results: dict[str, set[int]] = {}

    s = {1, 2, 3}
    s.add(4)
    results["after_add"] = s.copy()

    s.remove(1)
    results["after_remove"] = s.copy()

    s.discard(99)
    results["after_discard_missing"] = s.copy()

    popped = s.pop()
    results["after_pop"] = s.copy()

    s.update([5, 6, 7])
    results["after_update"] = s.copy()

    s.clear()
    results["after_clear"] = s.copy()

    return results


def remove_vs_discard() -> dict[str, str]:
    """
    Demonstrate difference between remove() and discard().
    """
    s1 = {1, 2, 3}
    s2 = {1, 2, 3}

    s1.discard(99)

    try:
        s2.remove(99)
        result = "No error"
    except KeyError:
        result = "KeyError raised"

    return {
        "discard_missing": "Silently does nothing",
        "remove_missing": result,
    }


def union_operations() -> dict[str, set[int]]:
    """
    Demonstrate set union operations.

    Union: A ∪ B = all elements in A or B (or both)
    Time Complexity: O(len(A) + len(B))
    """
    a = {1, 2, 3}
    b = {3, 4, 5}

    return {
        "union_method": a.union(b),
        "union_operator": a | b,
        "union_multiple": a.union(b, {6, 7}),
        "union_update": a.copy().__ior__(b),
        "original_a": a,
    }


def intersection_operations() -> dict[str, set[int]]:
    """
    Demonstrate set intersection operations.

    Intersection: A ∩ B = elements in both A and B
    Time Complexity: O(min(len(A), len(B)))
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    return {
        "intersection_method": a.intersection(b),
        "intersection_operator": a & b,
        "intersection_multiple": a.intersection(b, {3, 4, 7}),
        "original_a": a,
    }


def difference_operations() -> dict[str, set[int]]:
    """
    Demonstrate set difference operations.

    Difference: A - B = elements in A but not in B
    Time Complexity: O(len(A))
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    return {
        "a_minus_b": a.difference(b),
        "a_minus_b_operator": a - b,
        "b_minus_a": b.difference(a),
        "b_minus_a_operator": b - a,
        "original_a": a,
    }


def symmetric_difference_operations() -> dict[str, set[int]]:
    """
    Demonstrate symmetric difference operations.

    Symmetric Difference: A △ B = elements in A or B but not in both
    Time Complexity: O(len(A) + len(B))
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    return {
        "symmetric_difference_method": a.symmetric_difference(b),
        "symmetric_difference_operator": a ^ b,
        "original_a": a,
    }


def subset_operations() -> dict[str, bool]:
    """
    Demonstrate subset operations.

    Subset: A ⊆ B (all elements of A are in B)
    Proper Subset: A ⊂ B (A ⊆ B and A ≠ B)
    Time Complexity: O(len(A))
    """
    a = {1, 2}
    b = {1, 2, 3}
    c = {1, 2, 3}
    d = {4, 5}

    return {
        "a_issubset_b": a.issubset(b),
        "a_subseteq_b": a <= b,
        "a_proper_subset_b": a < b,
        "c_issubset_b": c.issubset(b),
        "c_subseteq_b": c <= b,
        "c_proper_subset_b": c < b,
        "d_disjoint_a": d.isdisjoint(a),
    }


def superset_operations() -> dict[str, bool]:
    """
    Demonstrate superset operations.

    Superset: B ⊇ A (B contains all elements of A)
    Proper Superset: B ⊃ A (B ⊇ A and B ≠ A)
    """
    a = {1, 2}
    b = {1, 2, 3}
    c = {1, 2, 3}

    return {
        "b_issuperset_a": b.issuperset(a),
        "b_superseteq_a": b >= a,
        "b_proper_superset_a": b > a,
        "c_superseteq_a": c >= a,
        "c_proper_superset_a": c > a,
        "b_issuperset_c": b.issuperset(c),
    }


def membership_operations() -> dict[str, bool]:
    """
    Demonstrate membership testing.

    Time Complexity: O(1) average for sets vs O(n) for lists
    """
    s = {1, 2, 3, 4, 5}
    l = [1, 2, 3, 4, 5]

    return {
        "in_set_3": 3 in s,
        "in_set_6": 6 in s,
        "not_in_set_3": 3 not in s,
    }


def venn_diagram_operations() -> dict[str, set[int] | int]:
    """
    Demonstrate all Venn diagram regions.
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    return {
        "only_a": a - b,
        "only_b": b - a,
        "intersection": a & b,
        "union": a | b,
        "symmetric_difference": a ^ b,
        "union_minus_intersection": (a | b) - (a & b),
    }


def set_comprehensions() -> dict[str, set[int] | set[str]]:
    """
    Demonstrate set comprehensions.
    """
    return {
        "squares": {x**2 for x in range(-5, 6)},
        "even_squares": {x**2 for x in range(10) if x % 2 == 0},
        "unique_chars": {c for c in "hello world"},
        "from_nested": {x for row in [[1, 2], [2, 3], [3, 4]] for x in row},
        "conditional": {x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]},
    }


def frozen_sets() -> dict[str, str | bool]:
    """
    Demonstrate frozenset usage.

    Frozensets are immutable and hashable (can be dict keys or set elements).
    """
    fs = frozenset([1, 2, 3])

    d: dict[frozenset[int], str] = {fs: "immutable set"}

    s: set[frozenset[int]] = set()
    s.add(fs)

    return {
        "type": type(fs).__name__,
        "can_be_dict_key": fs in d,
        "can_be_set_element": fs in s,
        "immutable": "Cannot add/remove elements",
    }


def performance_comparison() -> dict[str, str]:
    """
    Compare set vs list for membership testing.
    """
    return {
        "set_lookup": "O(1) average - hash table",
        "list_lookup": "O(n) - linear search",
        "set_memory": "Higher overhead due to hash table",
        "list_memory": "Lower overhead - contiguous storage",
        "set_use_case": "When you need fast lookups and uniqueness",
        "list_use_case": "When you need ordering or allow duplicates",
    }


def common_patterns() -> dict[str, set[int] | list[int]]:
    """
    Common set usage patterns.
    """
    list1 = [1, 2, 2, 3, 3, 3]
    list2 = [3, 4, 4, 5, 5, 5]

    unique: set[int] = set(list1)

    common = set(list1) & set(list2)

    all_unique = set(list1) | set(list2)

    only_first = set(list1) - set(list2)

    return {
        "remove_duplicates": unique,
        "find_common": common,
        "find_all_unique": all_unique,
        "find_only_in_first": only_first,
    }


def mathematical_operations() -> dict[str, str]:
    """
    Set theory mathematical notation reference.
    """
    return {
        "union": "A ∪ B = {x : x ∈ A or x ∈ B}",
        "intersection": "A ∩ B = {x : x ∈ A and x ∈ B}",
        "difference": "A \\ B = {x : x ∈ A and x ∉ B}",
        "symmetric_diff": "A △ B = (A \\ B) ∪ (B \\ A)",
        "complement": "A^c = U \\ A (where U is universe)",
        "cartesian_product": "A × B = {(a, b) : a ∈ A, b ∈ B}",
        "power_set": "P(A) = {X : X ⊆ A}",
    }


def set_algebra_laws() -> dict[str, str]:
    """
    Set algebra laws reference.
    """
    return {
        "commutative_union": "A ∪ B = B ∪ A",
        "commutative_intersection": "A ∩ B = B ∩ A",
        "associative_union": "(A ∪ B) ∪ C = A ∪ (B ∪ C)",
        "associative_intersection": "(A ∩ B) ∩ C = A ∩ (B ∩ C)",
        "distributive": "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
        "de_morgan_1": "(A ∪ B)^c = A^c ∩ B^c",
        "de_morgan_2": "(A ∩ B)^c = A^c ∪ B^c",
        "identity_union": "A ∪ ∅ = A",
        "identity_intersection": "A ∩ U = A",
        "complement_law": "A ∪ A^c = U",
    }


class MultiSet:
    """
    Simple multiset (bag) implementation - allows duplicates.
    """

    def __init__(self) -> None:
        self._counts: dict[int, int] = {}

    def __repr__(self) -> str:
        items = []
        for item, count in self._counts.items():
            items.extend([str(item)] * count)
        return "MultiSet({" + ", ".join(items) + "})"

    def __str__(self) -> str:
        return self.__repr__()

    def add(self, item: int, count: int = 1) -> None:
        self._counts[item] = self._counts.get(item, 0) + count

    def remove(self, item: int) -> bool:
        if item in self._counts:
            self._counts[item] -= 1
            if self._counts[item] <= 0:
                del self._counts[item]
            return True
        return False

    def count(self, item: int) -> int:
        return self._counts.get(item, 0)


if __name__ == "__main__":
    print("=== Set Creation ===")
    for name, s in create_sets().items():
        print(f"  {name}: {s}")

    print("\n=== Union Operations ===")
    for name, s in union_operations().items():
        print(f"  {name}: {s}")

    print("\n=== Venn Diagram ===")
    for name, s in venn_diagram_operations().items():
        print(f"  {name}: {s}")

    print("\n=== Subset/Superset ===")
    for name, result in subset_operations().items():
        print(f"  {name}: {result}")

    print("\n=== Common Patterns ===")
    for name, s in common_patterns().items():
        print(f"  {name}: {s}")
