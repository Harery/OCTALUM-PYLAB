#!/usr/bin/env python3
"""
LeetCode Hard #212: Word Search II

Given an m x n board of characters and a list of words, return all words
that exist on the board. Words must be constructed from adjacent cells
(horizontally or vertically neighboring).

Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
                    ["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Time Complexity: O(m * n * 4^L) where L is max word length
Space Complexity: O(total characters in all words) for Trie
"""

from __future__ import annotations


class TrieNode:
    """Trie node for word search."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: str | None = None  # Store complete word at end node


def build_trie(words: list[str]) -> TrieNode:
    """Build trie from list of words."""
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    return root


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Find all words from the list that exist on the board.

    Uses Trie + DFS backtracking for efficient prefix matching.

    Args:
        board: 2D grid of characters
        words: List of words to search for

    Returns:
        List of found words
    """
    if not board or not board[0] or not words:
        return []

    rows, cols = len(board), len(board[0])
    root = build_trie(words)
    found: list[str] = []

    def dfs(r: int, c: int, node: TrieNode) -> None:
        """DFS with backtracking."""
        char = board[r][c]

        if char not in node.children:
            return

        curr = node.children[char]

        # Found a word
        if curr.word:
            found.append(curr.word)
            curr.word = None  # Avoid duplicates

        # Mark as visited
        board[r][c] = "#"

        # Explore 4 directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, curr)

        # Backtrack
        board[r][c] = char

        # Optimization: remove leaf nodes
        if not curr.children:
            del node.children[char]

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return found


def test() -> None:
    """Test cases for word search II."""
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    result1 = find_words(board1, words1)
    assert sorted(result1) == sorted(["eat", "oath"]), f"Got: {result1}"

    board2 = [["a", "b"], ["c", "d"]]
    words2 = ["abcb"]
    result2 = find_words(board2, words2)
    assert result2 == [], f"Expected empty, got: {result2}"

    print("All tests passed!")


if __name__ == "__main__":
    test()
