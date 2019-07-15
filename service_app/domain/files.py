from service_app.constants import UPLOAD_DIRECTORY
import os


def get_file(file_name):
    src = os.path.dirname(os.path.abspath(UPLOAD_DIRECTORY))
    file_path = f"{src}/{UPLOAD_DIRECTORY}/{file_name}"
    return file_path
