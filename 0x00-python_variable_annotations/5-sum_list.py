#!/usr/bin/env python3
"""Sum of a list of integers."""

from typing import List, float


def sum_list(input_list: List[float]) -> float:
    """Sum of a list of integers."""
    total_sum = 0.0
    for num in input_list:
        total_sum += num
    return total_sum
