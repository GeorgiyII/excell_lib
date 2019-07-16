import logging

from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(Exception)
def handle_error(error):
    logging.error(f"{error}")
    errors = {
        "message": str(error)
    }
    return render_template("errors.html", errors=errors)
