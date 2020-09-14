from flask import Blueprint
from .views import index, draft_list, draft_add

bp = Blueprint('webui', __name__, template_folder="templates")
bp.add_url_rule('/', view_func=index)
bp.add_url_rule('/draft/list', view_func=draft_list)
bp.add_url_rule('/draft/add', view_func=draft_add)


def init_app(app):
    app.register_blueprint(bp)
