from core.alchemy.models.model import BaseModel
from extentions import db


class User(BaseModel):
    __tablename__ = 'users'
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    email_verified = db.Column(db.Boolean(), default=False)

    @classmethod
    def find_by_email(cls, email):
        return User.query.filter(User.email == email).first()
