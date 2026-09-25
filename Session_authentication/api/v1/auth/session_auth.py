#!/usr/bin/env python3
"""Session Auth module
"""

from api.v1.auth.auth import Auth
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
