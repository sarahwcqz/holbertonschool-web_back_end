#!/usr/bin/env python3
"""This module provides simple examples of using Python type annotations."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its input by the given multiplier."""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
