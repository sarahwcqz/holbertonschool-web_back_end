#!/usr/bin/env python3
"""This module provides a function to return a list of tuples with elements and their lengths.

The function element_length takes an iterable of sequences (e.g., strings, lists, tuples)
and returns a list of tuples, each containing an element and its length.
"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing an element and its length."""
    return [(i, len(i)) for i in lst]
