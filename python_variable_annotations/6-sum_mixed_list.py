#!/usr/bin/env python3
"""This module provides simple examples of using Python type annotations."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of int + float"""
    return float(sum(mxd_lst))
