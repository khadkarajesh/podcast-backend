import os

from flask_mail import Message

from extentions import mail


def send_email(recipients, subject, body=None, html=None):
    with mail.connect() as connection:
        for recipient in recipients:
            message = body
            subject = subject
            msg = Message(recipients=[recipient],
                          body=message,
                          subject=subject,
                          sender=os.environ.get('MAIL_DEFAULT_SENDER'),
                          html=html)

            connection.send(msg)
