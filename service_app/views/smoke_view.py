from flask.views import MethodView


class SmokeView(MethodView):

    def get(self):
        return "Smoke"
