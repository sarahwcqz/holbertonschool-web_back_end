#!/usr/bin/env python3
"""This module provides a helper to obfuscate the values of sensitive
fields inside a log line before it gets written anywhere."""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return a copy of the given log line in which the value of every
    field listed in fields has been replaced by the redaction string.

    Args:
        fields: names of the fields whose values must be obfuscated.
        redaction: string used in place of each sensitive value.
        message: the log line to process.
        separator: character delimiting the fields inside message.

    Returns:
        The log line with every listed field value obfuscated.
    """
    pattern = rf"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, rf"\1={redaction}", message)
