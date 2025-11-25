#!/usr/bin/env python3
"""This module provides simple examples of using Python type annotations."""


from typing import Tuple, Sequence, Any, List


def element_length(lst: Sequence[Any]) -> List[Tuple[Any, int]]:
    """Return a list of tuples, each containing an element and its length."""
    return [(i, len(i)) for i in lst]
