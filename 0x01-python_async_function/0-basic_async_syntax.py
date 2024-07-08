#!/usr/bin/env python3
"""Task 0. Basic async syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay between 0 and
    `max_delay` seconds and then returns it.
    Args:
    max_delay (int): The maximum number of seconds to wait.
    Returns:
    float: The number of seconds waited.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
