#!/usr/bin/env python3
'''
Class inherits from auth.
'''

from api.v1.auth.auth import Auth
from base64 import b64decode
import binascii
from models.user import User
from typing import TypeVar


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
            -> (str, str):
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

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''
        Returns the user based of on the email and password.
        '''
        if not isinstance(user_email, str) or user_email is None:
            return None

        if not isinstance(user_pwd, str) or user_pwd is None:
            return None

        try:
            existing_user = User.search({'email': user_email})
        except Exception:
            return None

        for user in existing_user:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Overloads the Auth and returns the User intance for a request.
        '''
        header = self.authorization_header(request)

        if header is None:
            return None

        auth_64 = self.extract_base64_authorization_header(header)
        if auth_64 is None:
            return None

        decode_auth = self.decode_base64_authorization_header(auth_64)

        if decode_auth is None:
            return None

        user_credentials = self.extract_user_credentials(decode_auth)

        if user_credentials[0] is None or user_credentials[1] is None:
            return None

        return self.user_object_from_credentials(user_credentials[0], user_credentials[1])
