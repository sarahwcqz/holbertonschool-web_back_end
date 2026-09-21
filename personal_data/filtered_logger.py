#!/usr/bin/env python3
"""This module provides a helper to obfuscate the values of sensitive
fields inside a log line before it gets written anywhere."""

import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """Logging formatter that hides the values of sensitive fields in the
    lines it produces."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Set up the formatter with the fields whose values must be hidden.

        Args:
            fields: names of the fields to obfuscate in every record.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Return the record rendered with FORMAT, with the value of every
        field listed in fields replaced by REDACTION.

        Args:
            record: the log record to render.

        Returns:
            The formatted log line with its sensitive values obfuscated.
        """
        log_msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_msg,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Return the "user_data" logger, ready to record events without
    exposing personal information.

    The logger reports events from INFO upwards on a stream handler whose
    formatter obfuscates the values of the PII_FIELDS fields, and it keeps
    its records to itself so that no ancestor logger can emit them
    unredacted.

    Returns:
        The configured "user_data" logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
