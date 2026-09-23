#!/usr/bin/env python3
"""Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication system class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Tell whether the given path has to be authenticated."""
        return False

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header carried by the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the user the request is authenticated as."""
        return None
