#!/usr/bin/env python3
"""Basic Auth module
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Split a decoded Basic credential into its email and password.

        Args:
            decoded_base64_authorization_header: the decoded credential,
                expected to read "email:password".

        Returns:
            The email and the password, or None and None when the value is
            missing, is not a string, or carries no colon.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        mail, password = decoded_base64_authorization_header.split(':', 1)
        return mail, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return the user matching the given email and password.

        Args:
            user_email: the email the caller claims to own.
            user_pwd: the clear text password to check against the record.

        Returns:
            The stored User, or None when either value is missing or not a
            string, when no account carries that email, or when the
            password does not match.
        """
        if user_email is None:
            return None
        if not isinstance(user_email, str):
            return None
        if user_pwd is None:
            return None
        if not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if users == []:
                return None
            if not users[0].is_valid_password(user_pwd):
                return None
            return users[0]
        except Exception:
            return None
