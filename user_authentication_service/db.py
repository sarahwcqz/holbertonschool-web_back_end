#!/usr/bin/env python3
"""DB module."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """Data access layer for the users table.

    This class is the only one allowed to talk to the database; the rest
    of the application goes through Auth, which goes through DB.
    """

    def __init__(self) -> None:
        """Create the engine and reset the users table."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Return the session, creating it on first access."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save a new user and return it.

        Args:
            email: the address identifying the user.
            hashed_password: the bcrypt hash of the user's password.

        Returns:
            The User that has just been written to the database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user
