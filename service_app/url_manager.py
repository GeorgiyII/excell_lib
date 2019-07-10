from flask import Blueprint, Flask
from service_app.views.smoke_view import SmokeView


def load_urls(app: Flask):
    app_v1 = Blueprint('v1', 'app_v1')

    app_v1.add_url_rule('/', view_func=SmokeView.as_view('app_v1'))

    app.register_blueprint(app_v1)
