#!/usr/bin/env python3
'''
Class inherits from auth.
'''

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''
    Inherits from auth class.
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        Creates a sessionID for a UserID.
        '''
        if not isinstance(user_id, str) or user_id is None:
            return None
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id.update({session_id: user_id})
        return session_id
