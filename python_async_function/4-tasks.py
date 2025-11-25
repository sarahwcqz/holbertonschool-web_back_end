#!/usr/bin/env python3
"""Module to learn about the asynchronous programming"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a task for wait_random."""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all the delays when you spawn n times wait_random with
    the specified max_delay"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
