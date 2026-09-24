#!/usr/bin/env python3
"""Basic Auth module
"""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the UTF-8 text carried by the given Base64 string.

        Args:
            base64_authorization_header: the Base64 part of the header.

        Returns:
            The decoded text, or None if the value is missing, is not a
            string, or is not valid Base64.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            octets = base64.b64decode(base64_authorization_header)
            return octets.decode('utf-8')
        except Exception:
            return None
