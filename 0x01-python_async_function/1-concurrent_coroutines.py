#!/usr/bin/env python3
"""concurrent_coroutines.py: Demonstrate concurrent coroutines using asyncio"""

import asyncio
from typing import List

from asyncio.events import socket
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay.
    Args:
        n: number of times to call wait_random
        max_delay: maximum delay for each call
    Returns:
        list of floats 

    """

    async def add_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)
        return delay

    await asyncio.gather(*(add_delay() for _ in range(n)))

    return sorted(delays)
