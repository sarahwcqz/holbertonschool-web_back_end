#!/usr/bin/env python3
"""Define a Cache class to store data in Redis."""

import uuid
import redis
from typing import Union


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
