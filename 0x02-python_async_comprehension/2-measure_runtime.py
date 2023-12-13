#!/usr/bin/env python3

"""
write a measure_runtime coroutine that will execute async_comprehension four
times in parallel using asyncio.gather. measure_runtime should measure the
total runtime and return it.
"""
import time
import asyncio
from typing import Coroutine
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that measures the total runtime and returns it
    """
    start_time = time.time()
    tasks = [async_comprehension()for _ in range(4)]

    results = await asyncio.gather(*tasks)
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
