from flask import Flask

from service_app.url_manager import load_urls


app = Flask(__name__)

load_urls(app)
