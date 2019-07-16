import os
import logging
from functools import wraps

from flask import abort

from service_app.domain.forms import FileUploadForm
from service_app.domain.files import get_file
from service_app.constants import UPLOAD_DIRECTORY, SUPPORTED_FORMATS


def upload_file(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        form = FileUploadForm(csrf_enabled=False)
        if form.file_upload.data:
            file_name = form.file_upload.data.filename
            extension = os.path.splitext(file_name)[1]
            if extension not in SUPPORTED_FORMATS:
                abort(400, f"File {file_name} has wrong format {extension}."
                           f" Supported formats are: .xlsx, .xlsm, .xltx, .xltm.")
            if not file_name:
                abort(400, f"File not upload")
            file_path = f"{UPLOAD_DIRECTORY}/{file_name}"
            try:
                form.file_upload.data.save(file_path)
            except Exception:
                abort(400, f"File {file_name} not saved")

        return f(request, file_name, file_path, *args, **kwargs)

    return wrapper


def remove_file(f):
    @wraps(f)
    def wrapper(request, file_name, *args, **kwargs):
        path = get_file(file_name)
        func = f(request, file_name, path, *args, **kwargs)
        os.remove(path)
        logging.info(f"File {file_name} removed from {path}.")
        return func
    return wrapper
