# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from flask_pymongo import PyMongo

db = PyMongo()


def init_app(app):
    db.init_app(app)


class Doc:
    def __init__(self, doc: dict = None):
        self.doc = doc

    def get_doc(self):
        return self.doc
