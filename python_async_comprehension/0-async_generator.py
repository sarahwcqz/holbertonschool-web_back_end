#!/usr/bin/env python3
"""Module to learn the async comprehension"""


import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator that yields a random number
    between 0 and 10 every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        res = random.uniform(0, 10)
        yield res
