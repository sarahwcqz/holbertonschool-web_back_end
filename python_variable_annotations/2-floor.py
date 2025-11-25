#!/usr/bin/env python3
"""This module provides simple examples of using Python type annotations."""


from math import floor as math_floor


def floor(n: float) -> int:
    """Returns the floor of a float"""
    return math_floor(n)
