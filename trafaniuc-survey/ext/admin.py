from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla

from .database import db
# from ..models.user import User
# from ..models.survey import Survey

admin = Admin()

def init_app(app):
    admin.template_mode = 'bootstrap3'
    admin.init_app(app)
    # admin.add_view(sqla.ModelView(User, db.session))
    # admin.add_view(sqla.ModelView(Survey, db.session))