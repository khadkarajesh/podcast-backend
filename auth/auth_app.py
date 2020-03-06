from flask import Blueprint
from flask_restful import Api

from auth.resources.email_verification_resource import EmailVerificationResource
from auth.resources.signup_resource import SignupResource

auth_app = Blueprint('auth_app', __name__)
api = Api(auth_app)
api.add_resource(SignupResource, '/signup')
api.add_resource(EmailVerificationResource, '/email-verifications')
