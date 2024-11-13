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
        if path is None:
            return True
        
        if not excluded_paths:
            return True
        
        path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if path == excluded_path.rstrip('/'):
                return False
        
        return True

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
