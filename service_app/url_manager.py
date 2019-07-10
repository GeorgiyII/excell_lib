from flask import Blueprint, Flask
from service_app.views.smoke_view import SmokeView
from service_app.views.main_menu_view import MainMenuView


def load_urls(app: Flask):
    app_v1 = Blueprint('v1', 'app_v1')

    app_v1.add_url_rule('/smoke', view_func=SmokeView.as_view('smoke'))
    app_v1.add_url_rule('/', view_func=MainMenuView.as_view('main'))

    app.register_blueprint(app_v1)
