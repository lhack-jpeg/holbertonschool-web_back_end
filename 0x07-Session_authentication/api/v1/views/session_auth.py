#!/usr/bin/env python3
""" Module of session_auth views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User


@app_views.route('/auth_session/login',
                 methods=['POST'],
                 strict_slashes=False)
def session_auth_form():
    print(request.form)
    email = request.form.get('email')
    print(email)
    password = request.form.get('password')

    if email is None:
        err_msg = jsonify({"error": "email missing"})
        response = make_response(err_msg, 400)
        abort(response)
    if password is None:
        err_msg = jsonify({"error": "password missing"})
        response = make_response(err_msg, 400)
        abort(response)

    users = User.search({'email': email})
    print(users)
    if len(users) == 0:
        err_msg = jsonify({"error": "no user found for this email"})
        response = make_response(err_msg, 404)
        abort(response)

    if password == _user.is_valid_password(password):
        from api.v1.app import auth
        for user in users:
            session_id = auth.create_session(_user.id)
            session_name = getenv('SESSION_NAME')
            response = make_respone(user.to_json())
            response.set_cooke(session_name, session_id)
            return response

   
    err_msg = jsonify({ "error": "wrong password" })
    response = make_response(err_msg, 401)
    abort(response)

    
