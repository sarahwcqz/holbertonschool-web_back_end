#!/usr/bin/env python3
"""Session Auth module
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Auth system class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Open a new session for the given user and return its id.

        Args:
            user_id: the id of the user the session belongs to.

        Returns:
            The generated Session ID, or None when user_id is
            missing or is not a string.
        """
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return the id of the user the given session belongs to.

        Args:
            session_id: the Session ID carried by the request.

        Returns:
            The matching user id, or None when session_id is missing, is
            not a string, or is unknown to the store.
        """
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return the instance of User based on a cookie value"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Close the session the given request belongs to.

        Args:
            request: the Flask request carrying the Session ID cookie.

        Returns:
            True once the session has been forgotten, False when the
            request carries no cookie or an unknown one.
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if self.user_id_for_session_id(session_id) is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
