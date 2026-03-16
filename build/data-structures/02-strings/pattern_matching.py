"""
Pattern Matching Module
=======================
Introduction to pattern matching and regular expressions in Python.

Covers: basic patterns, regex syntax, common use cases.
"""

from __future__ import annotations

import re


class PatternMatcher:
    """
    A wrapper class for common pattern matching operations.
    """

    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
        self._compiled: re.Pattern[str] | None = None

    @property
    def compiled(self) -> re.Pattern[str]:
        if self._compiled is None:
            self._compiled = re.compile(self.pattern)
        return self._compiled

    def __repr__(self) -> str:
        return f"PatternMatcher('{self.pattern}')"

    def __str__(self) -> str:
        return self.pattern


def basic_matching() -> dict[str, bool | str | None]:
    """
    Demonstrate basic string matching without regex.

    Time Complexity: O(n*m) for substring search
    """
    text = "Hello, World!"

    return {
        "contains": "World" in text,
        "startswith": text.startswith("Hello"),
        "endswith": text.endswith("!"),
        "find_index": text.find("World"),
        "count_o": text.count("o"),
    }


def regex_basic_patterns() -> dict[str, str]:
    """
    Demonstrate basic regex metacharacters.

    Metacharacters: . ^ $ * + ? { } [ ] \ | ( )
    """
    return {
        "dot": ". matches any character except newline",
        "caret": "^ matches start of string",
        "dollar": "$ matches end of string",
        "star": "* matches 0 or more of preceding",
        "plus": "+ matches 1 or more of preceding",
        "question": "? matches 0 or 1 of preceding",
        "escape": "\\ escapes metacharacters",
        "pipe": "| alternation (OR)",
        "group": "(...) creates capturing group",
    }


def regex_character_classes() -> dict[str, list[str]]:
    """
    Demonstrate character class patterns.
    """
    text = "Hello123 World456"

    return {
        "digits": re.findall(r"\d", text),
        "non_digits": re.findall(r"\D", text[:5]),
        "word_chars": re.findall(r"\w", text[:5]),
        "non_word": re.findall(r"\W", text),
        "whitespace": re.findall(r"\s", text),
        "non_whitespace": re.findall(r"\S", text),
        "custom_class": re.findall(r"[aeiou]", text.lower()),
        "range": re.findall(r"[a-z]", text),
        "negated": re.findall(r"[^aeiou\s]", text.lower()),
    }


def regex_quantifiers() -> dict[str, list[str]]:
    """
    Demonstrate quantifier patterns.
    """
    text = "aaa b aaaa bbbbb"

    return {
        "zero_or_more": re.findall(r"ab*", text),
        "one_or_more": re.findall(r"a+", text),
        "zero_or_one": re.findall(r"ab?", text),
        "exactly_n": re.findall(r"a{3}", text),
        "n_or_more": re.findall(r"a{2,}", text),
        "n_to_m": re.findall(r"a{2,3}", text),
        "greedy": re.findall(r"a.*b", "aabab"),
        "non_greedy": re.findall(r"a.*?b", "aabab"),
    }


def regex_anchors() -> dict[str, bool]:
    """
    Demonstrate anchor patterns.
    """
    text = "Hello World"

    return {
        "start_match": bool(re.match(r"^Hello", text)),
        "end_match": bool(re.search(r"World$", text)),
        "word_boundary": bool(re.search(r"\bWorld\b", text)),
        "not_word_boundary": bool(re.search(r"\Bo\B", text)),  # 'o' inside word
        "start_string": bool(re.search(r"\AHello", text)),
        "end_string": bool(re.search(r"World\Z", text + "\n")),
    }


def regex_groups() -> dict[str, tuple[str, ...] | str | None]:
    """
    Demonstrate grouping and capturing.
    """
    text = "John: 25, Jane: 30"

    return {
        "capture_group": re.search(r"(\w+): (\d+)", text).groups() if re.search(r"(\w+): (\d+)", text) else (),
        "named_group": re.search(r"(?P<name>\w+): (?P<age>\d+)", text).group("name") if re.search(r"(?P<name>\w+): (?P<age>\d+)", text) else None,
        "non_capturing": re.findall(r"(?:\w+): (\d+)", text),
        "lookahead": re.findall(r"\w+(?=:)", text),
        "negative_lookahead": re.findall(r"\d+(?!0)", text),
        "lookbehind": re.findall(r"(?<=: )\d+", text),
        "negative_lookbehind": re.findall(r"(?<!, )\d+", text),
    }


def regex_functions() -> dict[str, str | list[str] | int]:
    """
    Demonstrate main regex functions.
    """
    text = "The quick brown fox jumps over the lazy dog"
    pattern = r"\b\w{4}\b"

    return {
        "search": re.search(pattern, text).group() if re.search(pattern, text) else "",
        "findall": re.findall(pattern, text),
        "finditer_count": len(list(re.finditer(pattern, text))),
        "sub": re.sub(r"fox", "cat", text),
        "sub_count": re.subn(r"o", "0", text)[1],
        "split": re.split(r"\s+", text)[:3],
    }


def compiled_regex() -> dict[str, str | list[str]]:
    """
    Demonstrate compiled regex for better performance.

    Compiling is useful when using the same pattern multiple times.
    """
    pattern = re.compile(r"\b\w+@\w+\.\w+\b", re.IGNORECASE)
    text = "Contact: john@example.com or JANE@EXAMPLE.COM"

    return {
        "findall": pattern.findall(text),
        "search": pattern.search(text).group() if pattern.search(text) else "",
        "flags": "re.IGNORECASE compiled into pattern",
    }


def regex_flags() -> dict[str, list[str]]:
    """
    Demonstrate regex flags.
    """
    text = "Hello\nWorld"

    return {
        "ignorecase": re.findall(r"hello", text, re.IGNORECASE),
        "multiline": re.findall(r"^\w+", text, re.MULTILINE),
        "dotall": re.findall(r"Hello.World", text, re.DOTALL),
        "verbose": re.findall(
            r"""
            \b      # word boundary
            \w+     # one or more word chars
            \b      # word boundary
            """,
            text,
            re.VERBOSE
        ),
        "ascii": re.findall(r"\w+", "hello世界", re.ASCII),
    }


def common_patterns() -> dict[str, str | bool]:
    """
    Common regex patterns for practical use.
    """
    patterns: dict[str, str] = {
        "email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "phone_us": r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$",
        "url": r"^https?://[\w\-.]+(:\d+)?(/[\w\-./?%&=]*)?$",
        "ip_v4": r"^(\d{1,3}\.){3}\d{1,3}$",
        "date_iso": r"^\d{4}-\d{2}-\d{2}$",
        "time_24h": r"^([01]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?$",
        "hex_color": r"^#[0-9A-Fa-f]{6}$",
        "username": r"^[a-zA-Z][a-zA-Z0-9_]{2,15}$",
        "password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
        "credit_card": r"^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$",
    }

    tests: dict[str, str | bool] = {}

    email = "user@example.com"
    tests["email_valid"] = bool(re.match(patterns["email"], email))
    tests["email_invalid"] = bool(re.match(patterns["email"], "not-an-email"))

    phone = "555-123-4567"
    tests["phone_valid"] = bool(re.match(patterns["phone_us"], phone))

    url = "https://example.com:8080/path"
    tests["url_valid"] = bool(re.match(patterns["url"], url))

    return tests


def string_algorithms() -> dict[str, int | list[int]]:
    """
    Classic string pattern matching algorithms.
    """
    def naive_search(text: str, pattern: str) -> list[int]:
        """Naive pattern matching - O(n*m)"""
        n, m = len(text), len(pattern)
        matches: list[int] = []
        for i in range(n - m + 1):
            if text[i:i+m] == pattern:
                matches.append(i)
        return matches

    def kmp_search(text: str, pattern: str) -> list[int]:
        """Knuth-Morris-Pratt algorithm - O(n+m)"""
        def build_lps(p: str) -> list[int]:
            lps = [0] * len(p)
            length = 0
            i = 1
            while i < len(p):
                if p[i] == p[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
            return lps

        if not pattern:
            return []

        lps = build_lps(pattern)
        matches: list[int] = []
        i = j = 0

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    matches.append(i - j)
                    j = lps[j - 1]
            elif j:
                j = lps[j - 1]
            else:
                i += 1

        return matches

    def rabin_karp(text: str, pattern: str) -> list[int]:
        """Rabin-Karp algorithm - O(n+m) average"""
        if not pattern:
            return []

        n, m = len(text), len(pattern)
        base = 256
        mod = 101

        pattern_hash = 0
        text_hash = 0
        h = 1

        for _ in range(m - 1):
            h = (h * base) % mod

        for i in range(m):
            pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
            text_hash = (base * text_hash + ord(text[i])) % mod

        matches: list[int] = []

        for i in range(n - m + 1):
            if pattern_hash == text_hash:
                if text[i:i+m] == pattern:
                    matches.append(i)

            if i < n - m:
                text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
                if text_hash < 0:
                    text_hash += mod

        return matches

    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    return {
        "naive": naive_search(text, pattern),
        "kmp": kmp_search(text, pattern),
        "rabin_karp": rabin_karp(text, pattern),
    }


def string_utilities() -> dict[str, str]:
    """
    Utility functions for string manipulation.
    """
    def reverse_words(s: str) -> str:
        words = s.split()
        return " ".join(reversed(words))

    def remove_duplicates(s: str) -> str:
        seen: set[str] = set()
        result: list[str] = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return "".join(result)

    def is_palindrome(s: str) -> str:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        return str(cleaned == cleaned[::-1])

    def longest_common_prefix(strings: list[str]) -> str:
        if not strings:
            return ""
        prefix = strings[0]
        for s in strings[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    return {
        "reverse_words": reverse_words("Hello World"),
        "remove_duplicates": remove_duplicates("aabbcc"),
        "is_palindrome": is_palindrome("A man, a plan, a canal: Panama"),
        "longest_common_prefix": longest_common_prefix(["flower", "flow", "flight"]),
    }


if __name__ == "__main__":
    print("=== Basic Matching ===")
    for name, result in basic_matching().items():
        print(f"  {name}: {result}")

    print("\n=== Character Classes ===")
    for name, result in regex_character_classes().items():
        print(f"  {name}: {result}")

    print("\n=== Quantifiers ===")
    for name, result in regex_quantifiers().items():
        print(f"  {name}: {result}")

    print("\n=== Common Patterns ===")
    for name, result in common_patterns().items():
        print(f"  {name}: {result}")

    print("\n=== String Algorithms ===")
    for name, result in string_algorithms().items():
        print(f"  {name}: {result}")

    print("\n=== String Utilities ===")
    for name, result in string_utilities().items():
        print(f"  {name}: {result}")
