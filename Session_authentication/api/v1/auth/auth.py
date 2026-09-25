#!/usr/bin/env python3
"""Auth module
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """Authentication system class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Tell whether the given path has to be authenticated."""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith("/"):
            path = path + "/"
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header carried by the request."""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the user the request is authenticated as."""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from the request"""
        if request is None:
            return None
        cookie_name = getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)
