#!/usr/bin/env python3
"""Define a Cache class to store data in Redis."""

import uuid
import redis
from typing import Union, Any, Callable, Optional


class Cache:
    """Class to connect to Redis and store data under random keys."""

    def __init__(self) -> None:
        """Instantiate the connection to Redis and flush the db."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis and return its random uuid key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Get a value from Redis and convert it with fn if one is given."""
        val = self._redis.get(key)
        if val is None or fn is None:
            return val
        return fn(val)

    def get_str(self, key: str) -> Optional[str]:
        """Get a value from Redis and decode its bytes to a str."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key/ int) -> Optional[int]:
        """Get a value from Redis and decode its bytes to an int."""
        return self.get(key, fn=int)
    