#!/usr/bin/env python3
"""Measure the runtime of the wait_n coroutine"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return average time per call
    Args:
        n: number of calls
        max_delay: maximum delay

    Returns:
        float: average time per call in seconds
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    return total_time / n
