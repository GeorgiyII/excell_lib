from functools import wraps

from service_app.domain.forms import FileUploadForm
from service_app.constants import FILE_DIRECTORY


def upload_file(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        form = FileUploadForm(csrf_enabled=False)
        if form.file_upload.data:
            try:
                file_name = form.file_upload.data.filename
                file_path = FILE_DIRECTORY + file_name
                form.file_upload.data.save(file_path)
            except Exception as err:
                raise Exception(err)

        return f(request, file_name, file_path, *args, **kwargs)

    return wrapper
