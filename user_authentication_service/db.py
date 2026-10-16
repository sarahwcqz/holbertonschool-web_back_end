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

    def find_user_by(self, **kwargs) -> User:
        """Return the first user matching the given attributes.

        Args:
            **kwargs: column names and the values they must equal.

        Returns:
            The first matching User.

        Raises:
            NoResultFound: when no user matches.
            InvalidRequestError: when a key is not a column of users.
        """
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Change some attributes of the user with the given id.

        Args:
            user_id: the primary key of the user to update.
            **kwargs: column names and the values to store in them.

        Raises:
            ValueError: when a key is not an attribute of User, in which
                case nothing is changed at all.
        """
        user = self.find_user_by(id=user_id)
        for key in kwargs:
            if not hasattr(user, key):
                raise ValueError("{} is not an attribute of User".format(key))
        for key, value in kwargs.items():
            setattr(user, key, value)
        self._session.commit()
