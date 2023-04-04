#!/usr/bin/env python3
"""Module that async generator"""
import asyncio
import random


async def async_generator():
    """Function that async generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
