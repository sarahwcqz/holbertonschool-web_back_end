#!/usr/bin/env python3
"""This module provides simple examples of using Python type annotations."""


from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a tuple with the string k and the square of v as a float.

        Args:
            k: A string representing the key.
            v: An integer or float representing the value.

        Returns:
            A tuple where the first element is the key and the second is the square of v as a float.
        """
    return (k, float(v ** 2))
