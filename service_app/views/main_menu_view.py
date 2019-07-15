from flask.views import MethodView
from flask import render_template, send_file

from service_app.domain.forms import FileUploadForm, ConfigForm, DownloadForm
from service_app.domain.decorators import upload_file
from service_app.domain.table_executor import get_table_preview, modify_table
from service_app.domain.files import get_file


class MainMenuView(MethodView):

    def get(self):
        form = FileUploadForm(csrf_enabled=False)
        return render_template('file_upload.html', form=form, table=None)


class ConfigView(MethodView):

    def post(self, file_name):
        form = ConfigForm(csrf_enabled=False)
        file = get_file(file_name)
        sheet_name = form.sheet_name.data
        sheet_price_name = form.sheet_price_name.data
        row_number = form.row_number.data
        separate_symbol = form.separate_symbol.data
        table = modify_table(file, sheet_name, sheet_price_name, row_number, separate_symbol)
        file = {
            "name": file_name
        }
        table = {
            "table": table
        }
        download_form = DownloadForm(csrf_enabled=False)
        return render_template('file_download.html', table=table, file=file, form=download_form)


class FileUploadView(MethodView):

    @upload_file
    def post(self, file_name, file_path):
        table_preview = get_table_preview(file_path)
        form = ConfigForm(csrf_enabled=False)
        file = {
            "name": file_name
        }
        table = {
            "table": table_preview
        }
        return render_template('config.html', form=form, table=table, file=file)


class FileDownloadView(MethodView):

    def post(self, file_name):
        path = get_file(file_name)
        return send_file(path)
