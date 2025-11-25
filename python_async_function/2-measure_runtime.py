#!/usr/bin/env python3
"""Module to learn about the asynchronous programming"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    start = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start
    return total_time / n
