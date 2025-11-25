#!/usr/bin/env python3
"""This module provides simple examples of using Python type annotations."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of float"""
    return sum(input_list)
