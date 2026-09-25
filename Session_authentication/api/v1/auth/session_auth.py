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
            The freshly generated Session ID, or None when user_id is
            missing or is not a string.
        """
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
