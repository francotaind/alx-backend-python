#!/usr/bin/env python3
"""concurrent_coroutines.py: Demonstrate concurrent coroutines using asyncio"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times concurrently
    Args:
        n: number of times to call wait_random
        max_delay: maximum wait time in seconds
    Returns:
        list of float numbers
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
