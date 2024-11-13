#!/usr/bin/env python3
""" Class for authorization
"""

from typing import List, TypeVar
from flask import request


class Auth():
    """Handle user authentication and
    authorization
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return false- path and
        excluded path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ returns None - request will be the
          Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None - request will be the
          Flask request object
        """
        return None