# from ..ext.database import db
# from sqlalchemy_serializer import SerializerMixin


# class User(db.Model, SerializerMixin):
#     # pylint: disable=no-member
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(254), nullable=False)
#     name = db.Column(db.String(254), nullable=False)

from datetime import datetime
from ..ext.database import db, Doc


class User(Doc):
    def __init__(self, email: str, name: str, doc: dict = None):
        if doc:
            super().__init__(doc)
        else:
            super().__init__({
                'created_on': datetime.utcnow(),
                'email': email,
                'name': name
            })
