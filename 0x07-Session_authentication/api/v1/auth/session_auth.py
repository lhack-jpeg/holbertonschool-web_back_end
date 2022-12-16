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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Returns the User ID based on the session ID.
        '''
        if not isinstance(session_id, str) or session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)
