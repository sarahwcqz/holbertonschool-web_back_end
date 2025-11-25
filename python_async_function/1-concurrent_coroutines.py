#!/usr/bin/env python3
"""Module to learn about the asynchronous programming"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all the delays when you spawn n times wait_random with
    the specified max_delay"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
