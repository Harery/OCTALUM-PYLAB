#!/usr/bin/env python3
"""
System Design: Rate Limiter

Implement a rate limiter to control the rate of requests to an API.

Common Algorithms:
1. Token Bucket
2. Leaky Bucket
3. Fixed Window Counter
4. Sliding Window Log
5. Sliding Window Counter

Time Complexity: O(1) for all operations
Space Complexity: O(n) where n = number of unique clients
"""

from __future__ import annotations

import time
from collections import defaultdict
from threading import Lock


class TokenBucket:
    """
    Token Bucket Rate Limiter.

    - Tokens are added at a fixed rate
    - Each request consumes one token
    - If no tokens available, request is denied
    """

    def __init__(self, rate: float, capacity: int) -> None:
        """
        Initialize token bucket.

        Args:
            rate: Tokens added per second
            capacity: Maximum tokens in bucket
        """
        self._rate = rate
        self._capacity = capacity
        self._tokens: dict[str, float] = defaultdict(lambda: capacity)
        self._last_update: dict[str, float] = defaultdict(time.time)
        self._lock = Lock()

    def allow_request(self, client_id: str) -> bool:
        """
        Check if request should be allowed.

        Args:
            client_id: Unique identifier for client

        Returns:
            True if request allowed, False if rate limited
        """
        with self._lock:
            now = time.time()
            elapsed = now - self._last_update[client_id]

            # Add tokens based on elapsed time
            self._tokens[client_id] = min(
                self._capacity, self._tokens[client_id] + elapsed * self._rate
            )
            self._last_update[client_id] = now

            if self._tokens[client_id] >= 1:
                self._tokens[client_id] -= 1
                return True

            return False


class SlidingWindowLog:
    """
    Sliding Window Log Rate Limiter.

    - Maintains timestamps of all requests
    - Counts requests within the time window
    - More accurate but higher memory usage
    """

    def __init__(self, max_requests: int, window_seconds: float) -> None:
        """
        Initialize sliding window.

        Args:
            max_requests: Maximum requests allowed in window
            window_seconds: Time window in seconds
        """
        self._max_requests = max_requests
        self._window = window_seconds
        self._requests: dict[str, list[float]] = defaultdict(list)
        self._lock = Lock()

    def allow_request(self, client_id: str) -> bool:
        """Check if request should be allowed."""
        with self._lock:
            now = time.time()
            cutoff = now - self._window

            # Remove old requests outside window
            self._requests[client_id] = [
                ts for ts in self._requests[client_id] if ts > cutoff
            ]

            if len(self._requests[client_id]) < self._max_requests:
                self._requests[client_id].append(now)
                return True

            return False

    def get_remaining(self, client_id: str) -> int:
        """Get remaining requests for client."""
        with self._lock:
            now = time.time()
            cutoff = now - self._window
            self._requests[client_id] = [
                ts for ts in self._requests[client_id] if ts > cutoff
            ]
            return max(0, self._max_requests - len(self._requests[client_id]))


class LeakyBucket:
    """
    Leaky Bucket Rate Limiter.

    - Requests go into a queue (bucket)
    - Queue drains at a constant rate
    - If queue full, request is denied
    """

    def __init__(self, rate: float, capacity: int) -> None:
        """
        Initialize leaky bucket.

        Args:
            rate: Requests processed per second
            capacity: Maximum queue size
        """
        self._rate = rate
        self._capacity = capacity
        self._water: dict[str, int] = defaultdict(int)
        self._last_leak: dict[str, float] = defaultdict(time.time)
        self._lock = Lock()

    def allow_request(self, client_id: str) -> bool:
        """Check if request should be allowed."""
        with self._lock:
            now = time.time()
            elapsed = now - self._last_leak[client_id]

            # Leak water (process requests)
            leaked = int(elapsed * self._rate)
            self._water[client_id] = max(0, self._water[client_id] - leaked)
            self._last_leak[client_id] = now

            if self._water[client_id] < self._capacity:
                self._water[client_id] += 1
                return True

            return False


def test() -> None:
    """Test cases for rate limiters."""
    # Test Token Bucket
    tb = TokenBucket(rate=10, capacity=10)
    assert tb.allow_request("user1") is True
    # Exhaust tokens
    for _ in range(9):
        tb.allow_request("user1")
    assert tb.allow_request("user1") is False

    # Test Sliding Window
    sw = SlidingWindowLog(max_requests=3, window_seconds=1.0)
    assert sw.allow_request("user1") is True
    assert sw.allow_request("user1") is True
    assert sw.allow_request("user1") is True
    assert sw.allow_request("user1") is False
    assert sw.get_remaining("user1") == 0

    print("All rate limiter tests passed!")


if __name__ == "__main__":
    test()
