#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a float multiplier as"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier."""
    def inner(n: float) -> float:
        """Return a function that multiplies a float by multiplier."""
        return n * multiplier
    return inner
