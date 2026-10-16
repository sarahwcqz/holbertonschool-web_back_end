#!/usr/bin/env python3
"""Authentication logic, sitting between the Flask app and the database."""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the given password.

    Args:
        password: the clear text password to protect.

    Returns:
        The hash, salt included, as a byte string.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
