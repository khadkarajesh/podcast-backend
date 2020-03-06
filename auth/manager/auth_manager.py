from flask import render_template

from auth.models.user import User
from core.manager.mail_manager import send_email
from core.manager.token_manager import generate_token, decode_token


def create_user(user):
    user.save()
    token = generate_token({'email': user.email})
    html = render_template('email_verification.html',
                           url=F'http://localhost.com/email-verification?token={token}')
    send_email(recipients=[user.email],
               subject='Email Verification',
               body='Reset your password',
               html=html)
    return user


def verify_email(token):
    decoded_token = decode_token(token)
    user = User.find_by_email(decoded_token['email'])
    if user is None: return
    user.email_verified = True
    user.commit()
    return user
