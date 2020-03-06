from flask import request
from flask_restful import Resource

from auth.manager.auth_manager import verify_email
from auth.schemas.signup_schema import UserSchema


class EmailVerificationResource(Resource):
    @classmethod
    def patch(cls):
        token = request.json['token']
        return UserSchema().dump(verify_email(token))
