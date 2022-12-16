#!/usr/bin/env python3
'''
Class inherits from auth.
'''

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    Inherits from auth class.
    '''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''
        Checks the authorisation header for Basic string to encode in Base64.
        '''
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]
