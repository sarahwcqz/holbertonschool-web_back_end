#!/usr/bin/env python3
"""Authentication logic, sitting between the Flask app and the database."""
import uuid

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


def _generate_uuid() -> str:
    """Return a brand new UUID, as a string.

    Returns:
        A random identifier, used for session ids and reset tokens.
    """
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """Open a session for the user owning the given email.

        Args:
            email: the address identifying the account.

        Returns:
            The new session id, or None when no account uses that email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Return the user the given session belongs to.

        Args:
            session_id: the value carried by the session cookie.

        Returns:
            The matching User, or None when session_id is None or no
            account carries it.
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Start a password reset for the user owning the given email.

        Args:
            email: the address the account is identified by.

        Returns:
            The token proving the reset was requested for that account.

        Raises:
            ValueError: when no account uses that email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("No user found for {}".format(email))
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def destroy_session(self, user_id: int) -> None:
        """Close the session of the user with the given id.

        Args:
            user_id: the primary key of the user to log out.
        """
        self._db.update_user(user_id, session_id=None)
