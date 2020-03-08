from flask import request
from flask_restful import Resource

from auth.manager.auth_manager import login
from auth.schemas.signup_schema import UserSchema


class LoginResource(Resource):
    @classmethod
    def post(cls):
        user = UserSchema(only=('email', 'password',)).load(request.json)
        return UserSchema(load_only=('password',)).dump(login(user))
