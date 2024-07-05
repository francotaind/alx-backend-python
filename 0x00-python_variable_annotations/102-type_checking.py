#!/usr/bin/env python3
"""Type Checking"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Type Checking"""
    zoomed_in: List[int] = []
    for item in lst:
        for _ in range(factor):
            zoomed_in.append(item)
    return zoomed_in
