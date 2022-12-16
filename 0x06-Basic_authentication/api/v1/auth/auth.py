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
        if path is None return True.
        if excluded paths is None or empty return True.
        Return false if path in excluded_paths. Needs to be slash tolerant.
        '''
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return True

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
