from flask.views import MethodView
from flask import redirect, url_for


class SmokeView(MethodView):

    def get(self):
        return "Smoke"
