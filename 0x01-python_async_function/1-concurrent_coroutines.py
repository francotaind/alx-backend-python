#!/usr/bin/env python3
"""concurrent_coroutines.py: Demonstrate concurrent coroutines using asyncio"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times concurrently"""

    wait_times = await asyncio.gather(*tuple(map(lambda _:
        wait_random(max_delay), range(n))))
    return sorted(wait_times)
