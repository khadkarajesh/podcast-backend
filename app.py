from dotenv import load_dotenv
from flask import Flask, jsonify
from marshmallow import ValidationError

from auth.auth_app import auth_app
from extentions import db, migrate, marshmallow, mail

load_dotenv('.env')

app = Flask(__name__, template_folder='templates')
app.config.from_object('config.default')
app.config.from_envvar('CONFIGURATION_FILE')

app.register_blueprint(auth_app, url_prefix='/auth')

with app.test_request_context():
    db.init_app(app)
    db.create_all()
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    mail.init_app(app)


@app.errorhandler(ValidationError)
def validation_error(e):
    return e.messages


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
