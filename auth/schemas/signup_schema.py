import re

from marshmallow import fields, validates, ValidationError

from auth.models.user import User
from extentions import marshmallow

PASSWORD_REGEX = r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
PASSWORD_VALIDATION_MESSAGE = 'Password must be of minimum length 8, alphanumeric, special character, capital letter'


class SignupSchema(marshmallow.ModelSchema):
    email = fields.Email(required=True)

    class Meta:
        model = User
        dump_only = ('id',)
        include_fk = True

    @validates('password')
    def validate_password(self, password):
        if not re.match(PASSWORD_REGEX, password): raise ValidationError(PASSWORD_VALIDATION_MESSAGE)
