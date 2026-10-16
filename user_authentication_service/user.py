#!/usr/bin/env python3
"""SQLAlchemy model for the users table."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """A registered user, as stored in the users table.

    Attributes:
        id: the primary key, assigned by the database.
        email: the address identifying the user.
        hashed_password: the bcrypt hash, never the password itself.
        session_id: the current session, or None when logged out.
        reset_token: the token of a pending password reset, if any.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
