#!/usr/bin/env python3
'''
Module for the authorisation manager in the API.
'''

from flask import request
from typing import List, TypeVar


class Auth():
    '''
    This class managers the authorisation of the User.
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Returns which routes don't need authentication.
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        Handles the request object header from flask.
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Checks to see the current user from the request object.
        '''
        return None
