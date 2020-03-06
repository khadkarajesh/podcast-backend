from flask import request
from flask_restful import Resource

from auth.manager.auth_manager import create_user
from auth.schemas.signup_schema import UserSchema

signup_schema = UserSchema()


class SignupResource(Resource):
    @classmethod
    def post(cls):
        user = signup_schema.load(request.json)
        return signup_schema.dump(create_user(user))
