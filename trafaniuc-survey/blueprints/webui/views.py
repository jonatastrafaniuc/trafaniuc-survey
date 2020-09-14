from flask import render_template
from ...models.survey import Survey

def index():
    return render_template('index.html', menu='home')

def draft_list():
    surveys = Survey.get_owner_drafts('jonatastrafaniuc@gmail.com', 0, 50)
    return render_template('draft_list.html', surveys=surveys, menu='draft')

def draft_add():
    return render_template('draft_detail.html', menu='draft', is_new=True)