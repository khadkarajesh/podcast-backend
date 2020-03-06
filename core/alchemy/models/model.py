import uuid

from extentions import db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    created_by = db.Column(db.String())
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String())

    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)
        self.id = str(uuid.uuid4())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def commit(cls):
        db.session.commit()
