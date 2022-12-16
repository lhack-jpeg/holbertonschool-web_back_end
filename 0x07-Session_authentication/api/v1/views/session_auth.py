#!/usr/bin/env python3
""" Module of session_auth views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login',
                 methods=['POST'],
                 strict_slashes=False)
def session_auth_form():
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        abort(400, jsonify({"error": "email missing"}))
    if password is None:
        abort(400, jsonify({"error": "password missing"}))

    users = User.search({'email': email})
    print(users)
    return jsonify({}), 200
