from flask import render_template

from auth.models.user import User
from core.exceptions.base_error import BaseError
from core.manager.mail_manager import send_email
from core.manager.token_manager import generate_token, decode_token
from core.utils.password_utility import hash_password, compare_password

EMAIL_VERIFICATION = 'Email Verification'
EMAIL_KEY = 'email'
EMAIL_VERIFICATION_HTML = 'email_verification.html'


def create_user(user):
    db_user = User.find_by_email(user.email)
    if db_user: raise BaseError(message='User has already associated with this email',
                                code=409,
                                status='NON_UNIQUE_EMAIL')
    user.password = hash_password(user.password)
    user.save()
    # token = generate_token({EMAIL_KEY: user.email})
    # html = render_template(EMAIL_VERIFICATION_HTML, url=F'http://localhost.com/email-verification?token={token}')
    # send_email(recipients=[user.email],
    #            subject=EMAIL_VERIFICATION,
    #            body='Reset your password',
    #            html=html)
    return user


def verify_email(token):
    decoded_token = decode_token(token)
    user = User.find_by_email(decoded_token[EMAIL_KEY])
    if user is None: return
    user.email_verified = True
    user.commit()
    return user


def login(user):
    base_error = BaseError(message='Invalid username/password', code=400, status='BAD_CREDENTIAL')
    db_user = User.find_by_email(user.email)
    if not db_user: raise base_error
    if not compare_password(db_user.password, user.password): raise base_error
    return db_user
