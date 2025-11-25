#!/usr/bin/env python3
"""This module provides a function to convert a key and a value to a
key-value tuple.

The function to_kv takes a string key and a numeric value (int or float),
and returns a tuple with the key and the square of the value as a float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v as a float."""
    return (k, float(v ** 2))
