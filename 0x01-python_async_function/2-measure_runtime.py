#!/usr/bin/env python3
"""Module that run measure the runtime"""
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    "Measure the runtime of wait_n."

    The function is asynchronous, so it returns a coroutine object

    :param n: the number of coroutines to run
    :type n: int
    :param max_delay: The maximum delay in seconds
    :type max_delay: int
    :return: The total time of execution.
    """
    start = perf_counter()
    await wait_n(n, max_delay)
    end = perf_counter()
    return (end - start) / n
