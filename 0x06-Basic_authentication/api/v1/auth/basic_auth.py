#!/usr/bin/env python3
'''
Class inherits from auth.
'''

from api.v1.auth.auth import Auth
from base64 import b64decode
import binascii


class BasicAuth(Auth):
    '''
    Inherits from auth class.
    '''

    def extract_base64_authorization_header(self,
                                            authorization_header: str)\
            -> str:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        '''
        Returns the decode value of a Base64 string.
        '''
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decode_str = b64decode(base64_authorization_header)
        except binascii.Error:
            return None

        return decode_str.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)\
            -> tuple(str, str):
        '''
        Returns the email and password from base64 decoded value.
        '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email_pass_str = decoded_base64_authorization_header.split(':')

        return(email_pass_str[0], email_pass_str[1])
