#!/usr/bin/env python3
""" Basic auth for authorization
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """"Extract base64 authorization header"""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode header in base64"""
        if base64_authorization_header is None or not isinstance(
            base64_authorization_header, str
        ):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')
            ).decode('utf-8')
        except Exception:
            return None
