from flask import render_template

from auth.models.user import User
from core.manager.mail_manager import send_email
from core.manager.token_manager import generate_token, decode_token

EMAIL_VERIFICATION = 'Email Verification'
EMAIL_KEY = 'email'
EMAIL_VERIFICATION_HTML = 'email_verification.html'


def create_user(user):
    user.save()
    token = generate_token({EMAIL_KEY: user.email})
    html = render_template(EMAIL_VERIFICATION_HTML, url=F'http://localhost.com/email-verification?token={token}')
    send_email(recipients=[user.email],
               subject=EMAIL_VERIFICATION,
               body='Reset your password',
               html=html)
    return user


def verify_email(token):
    decoded_token = decode_token(token)
    user = User.find_by_email(decoded_token[EMAIL_KEY])
    if user is None: return
    user.email_verified = True
    user.commit()
    return user
