from flask import Flask

def format_datetime(date, fmt=None):
    if fmt:
        return date.strftime(fmt)
    else:
        return date.strftime('%d/%m/%Y')
        
def init_app(app: Flask):
    app.jinja_env.filters['datetime'] = format_datetime