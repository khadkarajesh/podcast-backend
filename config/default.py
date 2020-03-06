import os

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_DATABASE_URI = F"postgresql://{os.environ.get('USER_NAME')}:{os.environ.get('USER_PASSWORD')}@{os.environ.get('HOST')}/{os.environ.get('DATABASE_NAME')}"
SECRET_KEY = os.environ.get('SECRET_KEY')
SECURITY_SALT = os.environ.get('SECURITY_SALT')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['refresh', 'access']
BUNDLE_ERRORS = True

# email configuration
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')

# database configuration
DATABASE_NAME = os.environ.get('DATABASE_NAME')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
USER_NAME = os.environ.get('USER_NAME')
HOST = os.environ.get('HOST')
