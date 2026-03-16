"""
Trie (Prefix Tree) Module
=========================
Implementation of a trie for efficient prefix-based string operations.

Time Complexity:
- Insert: O(m) where m is length of word
- Search: O(m)
- Delete: O(m)
- StartsWith: O(m)

Space Complexity: O(n * m) worst case, where n is number of words
"""

from __future__ import annotations


class TrieNode:
    """Node in a trie."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

    def __repr__(self) -> str:
        return f"TrieNode(end={self.is_end_of_word}, children={len(self.children)})"

    def __str__(self) -> str:
        return f"{'*' if self.is_end_of_word else ''}{list(self.children.keys())}"


class Trie:
    """
    Trie (Prefix Tree) for string storage and retrieval.
    """

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()
        self._word_count: int = 0

    def __repr__(self) -> str:
        return f"Trie(words={self._word_count})"

    def __str__(self) -> str:
        words = self.get_all_words()
        return f"Trie: {words}"

    def __len__(self) -> int:
        return self._word_count

    def __contains__(self, word: str) -> bool:
        return self.search(word)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        if not node.is_end_of_word:
            self._word_count += 1
        node.is_end_of_word = True

    def insert_many(self, words: list[str]) -> None:
        for word in words:
            self.insert(word)

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode | None:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def delete(self, word: str) -> bool:
        if not word:
            return False

        nodes: list[TrieNode] = [self.root]
        for char in word:
            if char not in nodes[-1].children:
                return False
            nodes.append(nodes[-1].children[char])

        if not nodes[-1].is_end_of_word:
            return False

        nodes[-1].is_end_of_word = False
        self._word_count -= 1

        for i in range(len(word), 0, -1):
            node = nodes[i]
            if node.is_end_of_word or node.children:
                break
            parent = nodes[i - 1]
            del parent.children[word[i - 1]]

        return True

    def get_words_with_prefix(self, prefix: str) -> list[str]:
        start_node = self._find_node(prefix)
        if not start_node:
            return []

        words: list[str] = []
        self._collect_words(start_node, prefix, words)
        return words

    def _collect_words(self, node: TrieNode, prefix: str, words: list[str]) -> None:
        if node.is_end_of_word:
            words.append(prefix)

        for char, child in sorted(node.children.items()):
            self._collect_words(child, prefix + char, words)

    def get_all_words(self) -> list[str]:
        words: list[str] = []
        self._collect_words(self.root, "", words)
        return words

    def count_words_with_prefix(self, prefix: str) -> int:
        start_node = self._find_node(prefix)
        if not start_node:
            return 0
        return self._count_words(start_node)

    def _count_words(self, node: TrieNode) -> int:
        count = 1 if node.is_end_of_word else 0
        for child in node.children.values():
            count += self._count_words(child)
        return count

    def longest_common_prefix(self) -> str:
        if not self.root.children:
            return ""

        prefix = []
        node = self.root

        while len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children))
            prefix.append(char)
            node = node.children[char]

        return "".join(prefix)

    def longest_word_with_prefix(self, prefix: str) -> str | None:
        words = self.get_words_with_prefix(prefix)
        if not words:
            return None
        return max(words, key=len)

    def autocomplete(self, prefix: str, limit: int = 10) -> list[str]:
        words = self.get_words_with_prefix(prefix)
        return words[:limit]

    def pattern_match(self, pattern: str) -> list[str]:
        words: list[str] = []
        self._pattern_match(self.root, "", pattern, words)
        return words

    def _pattern_match(self, node: TrieNode, current: str, pattern: str, words: list[str]) -> None:
        if not pattern:
            if node.is_end_of_word:
                words.append(current)
            return

        char = pattern[0]
        if char == ".":
            for c, child in node.children.items():
                self._pattern_match(child, current + c, pattern[1:], words)
        elif char in node.children:
            self._pattern_match(node.children[char], current + char, pattern[1:], words)

    def clear(self) -> None:
        self.root = TrieNode()
        self._word_count = 0

    def is_empty(self) -> bool:
        return self._word_count == 0


class CompressedTrie:
    """
    Compressed trie (Radix tree) that merges single-child chains.
    """

    def __init__(self) -> None:
        self.root: CompressedTrieNode = CompressedTrieNode()
        self._word_count: int = 0

    def __repr__(self) -> str:
        return f"CompressedTrie(words={self._word_count})"

    def __len__(self) -> int:
        return self._word_count

    def insert(self, word: str) -> None:
        if not word:
            return

        node = self.root
        i = 0

        while i < len(word):
            char = word[i]
            if char not in node.children:
                node.children[char] = CompressedTrieNode(word[i:])
                node.children[char].is_end_of_word = True
                self._word_count += 1
                return

            child = node.children[char]
            j = 0
            while j < len(child.label) and i < len(word) and child.label[j] == word[i]:
                i += 1
                j += 1

            if j < len(child.label):
                new_node = CompressedTrieNode(child.label[:j])
                new_node.children[child.label[j]] = CompressedTrieNode(child.label[j:])
                new_node.children[child.label[j]].children = child.children
                new_node.children[child.label[j]].is_end_of_word = child.is_end_of_word

                node.children[char] = new_node
                child = new_node

                if i < len(word):
                    child.is_end_of_word = False

            if i == len(word):
                if not child.is_end_of_word:
                    self._word_count += 1
                child.is_end_of_word = True
                return

            node = child

    def search(self, word: str) -> bool:
        node = self.root
        i = 0

        while i < len(word):
            char = word[i]
            if char not in node.children:
                return False

            child = node.children[char]
            if not word[i:].startswith(child.label):
                return False

            i += len(child.label)
            node = child

        return node.is_end_of_word


class CompressedTrieNode:
    """Node for compressed trie."""

    def __init__(self, label: str = "") -> None:
        self.label: str = label
        self.children: dict[str, CompressedTrieNode] = {}
        self.is_end_of_word: bool = False


if __name__ == "__main__":
    print("=== Trie ===")
    trie = Trie()
    words = ["apple", "app", "application", "apply", "apt", "bat", "batch"]
    trie.insert_many(words)

    print(f"Inserted: {words}")
    print(f"All words: {trie.get_all_words()}")

    print(f"\nSearch 'apple': {trie.search('apple')}")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Search 'appl': {trie.search('appl')}")

    print(f"\nStartsWith 'app': {trie.starts_with('app')}")
    print(f"Words with prefix 'app': {trie.get_words_with_prefix('app')}")

    print(f"\nLongest common prefix: {trie.longest_common_prefix()}")

    print(f"\nAutocomplete 'ap': {trie.autocomplete('ap', 3)}")

    print(f"\nPattern match 'a..': {trie.pattern_match('a..')}")

    print(f"\nDelete 'app': {trie.delete('app')}")
    print(f"Search 'app' after delete: {trie.search('app')}")
    print(f"Search 'apple' after delete: {trie.search('apple')}")

    print("\n=== Compressed Trie ===")
    ct = CompressedTrie()
    for w in ["apple", "app", "application"]:
        ct.insert(w)
    print(f"Search 'apple': {ct.search('apple')}")
    print(f"Search 'app': {ct.search('app')}")
