#!/usr/bin/env python3
"""Module that wait for random sec"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    "Wait for a random amount of time, and return the amount of time waited."

    The function is asynchronous, so it returns a coroutine

    :param max_delay: The maximum delay in seconds, defaults to 10
    :type max_delay: int (optional)
    :return: A coroutine object.
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
