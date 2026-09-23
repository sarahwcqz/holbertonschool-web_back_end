#!/usr/bin/env python3
"""Basic Auth module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication system class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return the Base64 part of a Basic Authorization header.

        Args:
            authorization_header: the raw value of the Authorization header.

        Returns:
            What follows "Basic ", or None if the header is missing, is not
            a string, or does not announce a Basic authentication.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.removeprefix("Basic ")
