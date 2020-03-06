import os

from itsdangerous import URLSafeSerializer, BadSignature


def get_serializer():
    return URLSafeSerializer(os.environ.get('SECRET_KEY'))


def generate_token(identifier):
    return get_serializer().dumps(identifier)


def decode_token(token):
    try:
        return get_serializer().loads(token)
    except BadSignature as e:
        return {'status': 'BAD_SIGNATURE'}
