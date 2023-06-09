#!/usr/bin/env python3
"""Module that run wait_random n times"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    "Wait for n random delays, and return a list of the delays."

    The function is asynchronous, so it returns a coroutine object

    :param n: the number of coroutines to run
    :type n: int
    :param max_delay: The maximum delay in seconds
    :type max_delay: int
    :return: A list of coroutines.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    return [await coroutine for coroutine in asyncio.as_completed(coroutines)]
