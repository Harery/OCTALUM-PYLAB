#!/usr/bin/env python3
"""
System Design: URL Shortener (like bit.ly)

Design a URL shortening service that converts long URLs into short aliases.

Requirements:
- Generate unique short URLs
- Redirect short URLs to original URLs
- Handle high traffic (millions of requests/day)
- URLs should be predictable length (6-8 characters)

Key Components:
1. Hashing function (base62 encoding)
2. Key-value store for URL mapping
3. Rate limiting
4. Caching layer

Time Complexity: O(1) for encode/decode
Space Complexity: O(n) where n = number of URLs
"""

from __future__ import annotations

import hashlib
import string
from collections import OrderedDict
from threading import Lock


class URLShortener:
    """
    URL Shortener using base62 encoding with LRU cache.

    Uses a deterministic hash function to generate short URLs.
    Includes thread-safe operations and size-limited cache.
    """

    BASE62_CHARS = string.ascii_letters + string.digits  # a-zA-Z0-9
    BASE = 62

    def __init__(self, cache_size: int = 10000, short_length: int = 7) -> None:
        """
        Initialize URL shortener.

        Args:
            cache_size: Maximum URLs to store in memory (LRU eviction)
            short_length: Length of short URL codes (7 chars = 3.5 trillion combinations)
        """
        self._cache_size = cache_size
        self._short_length = short_length
        self._url_to_code: OrderedDict[str, str] = OrderedDict()
        self._code_to_url: dict[str, str] = {}
        self._counter = 0
        self._lock = Lock()

    def _hash_url(self, url: str) -> str:
        """Generate short code using MD5 hash + base62 encoding."""
        # Get MD5 hash of URL
        hash_bytes = hashlib.md5(url.encode()).digest()

        # Convert first N bytes to integer
        num = int.from_bytes(hash_bytes[: self._short_length], byteorder="big")

        # Convert to base62
        chars = []
        for _ in range(self._short_length):
            chars.append(self.BASE62_CHARS[num % self.BASE])
            num //= self.BASE

        return "".join(reversed(chars))

    def encode(self, long_url: str) -> str:
        """
        Encode a long URL to a short URL code.

        Args:
            long_url: The original URL to shorten

        Returns:
            Short URL code (e.g., "abc123X")
        """
        with self._lock:
            # Check if already encoded
            if long_url in self._url_to_code:
                # Move to end (most recently used)
                self._url_to_code.move_to_end(long_url)
                return self._url_to_code[long_url]

            # Generate short code
            short_code = self._hash_url(long_url)

            # Handle collision (unlikely but possible)
            while short_code in self._code_to_url:
                # Append counter and rehash
                short_code = self._hash_url(long_url + str(self._counter))
                self._counter += 1

            # Evict oldest if at capacity
            if len(self._url_to_code) >= self._cache_size:
                oldest_url, oldest_code = self._url_to_code.popitem(last=False)
                del self._code_to_url[oldest_code]

            # Store mapping
            self._url_to_code[long_url] = short_code
            self._code_to_url[short_code] = long_url

            return short_code

    def decode(self, short_code: str) -> str | None:
        """
        Decode a short URL code to the original URL.

        Args:
            short_code: The short URL code

        Returns:
            Original URL or None if not found
        """
        with self._lock:
            url = self._code_to_url.get(short_code)
            if url:
                # Update LRU
                self._url_to_code.move_to_end(url)
            return url

    def get_stats(self) -> dict[str, int]:
        """Get current statistics."""
        with self._lock:
            return {
                "total_urls": len(self._url_to_code),
                "cache_size": self._cache_size,
                "collision_counter": self._counter,
            }


def test() -> None:
    """Test cases for URL shortener."""
    shortener = URLShortener(cache_size=100, short_length=7)

    # Test basic encode/decode
    url1 = "https://www.example.com/very/long/url/that/needs/shortening"
    code1 = shortener.encode(url1)
    assert len(code1) == 7
    assert shortener.decode(code1) == url1

    # Test same URL returns same code
    code1_again = shortener.encode(url1)
    assert code1 == code1_again

    # Test different URLs
    url2 = "https://www.google.com"
    code2 = shortener.encode(url2)
    assert code2 != code1
    assert shortener.decode(code2) == url2

    # Test unknown code
    assert shortener.decode("unknown") is None

    # Test stats
    stats = shortener.get_stats()
    assert stats["total_urls"] == 2

    print("All URL shortener tests passed!")


if __name__ == "__main__":
    test()
