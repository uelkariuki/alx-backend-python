#!/usr/bin/env python3

"""
Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay and
returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) ->asyncio.Task:
    """
    task_wait_random that takes an integer max_delay and returns
    a asyncio.Task
    """
    async def async_task():
        await asyncio.sleep(max_delay)
        return max_delay

    task = asyncio.create_task(async_task())
    return task
