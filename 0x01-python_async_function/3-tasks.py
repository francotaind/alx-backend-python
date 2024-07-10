#!/usr/bin/env python3
"""create an asyncio task that was called wait_n"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        n: number of times to call wait_random
        max_delay: maximum wait time in seconds
    Returns:
        asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
