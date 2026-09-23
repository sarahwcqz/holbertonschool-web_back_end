#!/usr/bin/env python3
"""Basic Auth module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication system class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.removeprefix("Basic ")
