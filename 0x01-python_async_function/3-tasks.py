#!/usr/bin/env python3
"""Moudule that returns the asyncio tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    "Return a asyncio task."

    The function is asynchronous, so it returns a coroutine object

    :param max_delay: The maximum delay in seconds
    :type max_delay: int
    :return: A asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
