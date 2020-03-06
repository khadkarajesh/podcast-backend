from flask_mail import Message

from extentions import mail


def send_email(recipients, subject, body):
    with mail.connect() as connection:
        for recipient in recipients:
            message = body
            subject = subject
            msg = Message(recipients=[recipient],
                          body=message,
                          subject=subject)

            connection.send(msg)
