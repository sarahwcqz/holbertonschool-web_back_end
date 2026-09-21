#!/usr/bin/env python3
"""Hash user passwords with bcrypt so that none of them is ever stored
in plain text."""

import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted hash of the given password.

    Args:
        password: the clear text password to protect.

    Returns:
        The bcrypt hash, salt included, as a byte string.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Tell whether the given password is the one behind the stored hash.

    Args:
        hashed_password: the bcrypt hash kept in the database.
        password: the clear text password to check against it.

    Returns:
        True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
