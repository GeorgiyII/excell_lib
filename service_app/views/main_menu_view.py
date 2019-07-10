from flask.views import MethodView
from flask import render_template


class MainMenuView(MethodView):

    def get(self):
        return render_template('index.html')

    def post(self):
        return "world"
