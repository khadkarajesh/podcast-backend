from core.alchemy.models.model import BaseModel
from extentions import db


class User(BaseModel):
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    email_verified = db.Column(db.Boolean(), default=False)
