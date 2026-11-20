#!/usr/bin/env python3
"""Define a Cache class to store data in Redis."""

import uuid
import redis
from typing import Union, Any, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times the decorated method is called, in Redis."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Increment the method's counter, then call the original method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the inputs and outputs of the decorated method in Redis lists."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Log the call's arguments, run the method, then log its result."""
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper


class Cache:
    """Class to connect to Redis and store data under random keys."""

    def __init__(self) -> None:
        """Instantiate the connection to Redis and flush the db."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_int(self, key: str) -> Optional[int]:
        """Get a value from Redis and decode its bytes to an int."""
        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """Display how many times a method was called, with each call's history."""
    name = method.__qualname__
    client = method.__self__._redis
    count = int(client.get(name) or 0)
    print("{} was called {} times:".format(name, count))
    inputs = client.lrange(name + ":inputs", 0, -1)
    outputs = client.lrange(name + ":outputs", 0, -1)
    for call_input, call_output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, call_input.decode("utf-8"),
                                     call_output.decode("utf-8")))
