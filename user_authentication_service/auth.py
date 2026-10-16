#!/usr/bin/env python3
"""Authentication logic, sitting between the Flask app and the database."""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the given password.

    Args:
        password: the clear text password to protect.

    Returns:
        The hash, salt included, as a byte string.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Open the data access layer this instance will work through."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Create an account for the given email and password.

        Args:
            email: the address the account is identified by.
            password: the clear text password, hashed before storage.

        Returns:
            The newly created User.

        Raises:
            ValueError: when an account already uses that email.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Tell whether the given credentials match a stored account.

        Args:
            email: the address the caller claims to own.
            password: the clear text password to check.

        Returns:
            True when the account exists and the password matches,
            False in every other case.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("utf-8"),
                              user.hashed_password)
