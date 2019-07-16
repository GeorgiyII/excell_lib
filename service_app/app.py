from flask import Flask
from flask_bootstrap import Bootstrap

from service_app.views.errors_view import errors
from service_app.url_manager import load_urls


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(errors)

load_urls(app)
