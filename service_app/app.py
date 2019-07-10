from flask import Flask
from flask_bootstrap import Bootstrap

from service_app.url_manager import load_urls


app = Flask(__name__)
bootstrap = Bootstrap(app)

load_urls(app)
