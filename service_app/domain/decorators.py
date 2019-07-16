from functools import wraps

from flask import abort

from service_app.domain.forms import FileUploadForm
from service_app.constants import FILE_DIRECTORY


def upload_file(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        form = FileUploadForm(csrf_enabled=False)
        if form.file_upload.data:
            file_name = form.file_upload.data.filename
            if not file_name:
                raise abort(400, f"File not upload")
            file_path = f"{FILE_DIRECTORY}{file_name}"
            try:
                form.file_upload.data.save(file_path)
            except Exception:
                raise abort(400, f"File {file_name} not saved")

        return f(request, file_name, file_path, *args, **kwargs)

    return wrapper
