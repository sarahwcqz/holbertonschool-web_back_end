#!/usr/bin/env python3
"""Tools to keep personal data out of the logs: a field obfuscator, a
redacting formatter, and a database connection built from the environment."""

import re
from typing import List
import logging
import mysql.connector
import os


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
    """Return the "user_data" logger, which keeps personal information out
    of every record it emits.

    Returns:
        A logger reporting INFO and above through a redacting formatter,
        and never propagating to its ancestors.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connection to the database holding the users table.
    """
    host_name = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(host=host_name,
                                         database=db_name,
                                         user=username,
                                         password=db_password)
    return connection


def main() -> None:
    """Log every row of the users table with its personal fields hidden."""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    columns = cursor.column_names
    for row in cursor:
        message = "".join(f"{column}={value}; "
                          for column, value in zip(columns, row))
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()