import logging

from flask.views import MethodView
from flask import render_template, send_file

from service_app.domain.forms import FileUploadForm, ConfigForm, DownloadForm, get_select_field_list
from service_app.domain.decorators import upload_file, remove_file
from service_app.domain.table_executor import get_table_preview, modify_table, get_sheets_list
from service_app.domain.files import get_file


class MainMenuView(MethodView):

    def get(self):
        form = FileUploadForm(csrf_enabled=False)
        return render_template('file_upload.html', form=form)


class ConfigView(MethodView):

    def post(self, file_name):
        form = ConfigForm(csrf_enabled=False)
        file_path = get_file(file_name)
        logging.info(f"File {file_name} have path: {file_path}")
        sheet_name = form.sheet_name.data
        sheet_price_name = form.sheet_price_name.data
        row_number = form.row_number.data
        separate_symbol = form.separate_symbol.data
        logging.info(f"Configs: sheet_name: {sheet_name}, sheet_price_name: {sheet_price_name},"
                     f" row_number: {row_number}, separate_symbol: {separate_symbol}")
        table = modify_table(file_path, sheet_name, sheet_price_name, row_number, separate_symbol)
        file = {
            "name": file_name
        }
        table_kwargs = {
            "table": table
        }
        logging.info(f"CONFIG:   Template file: {file}, table: {table_kwargs}")
        download_form = DownloadForm(csrf_enabled=False)
        return render_template('file_download.html', table=table_kwargs, file=file, form=download_form)


class FileUploadView(MethodView):

    @upload_file
    def post(self, file_name, file_path):
        sheets_names = get_sheets_list(file_path)
        sheets_list = get_select_field_list(sheets_names)
        table_preview = get_table_preview(file_path)
        row_list = get_select_field_list(table_preview)
        form = ConfigForm(csrf_enabled=False)
        form.row_number.choices = row_list
        form.sheet_name.choices = sheets_list
        form.sheet_price_name.choices = sheets_list
        file = {
            "name": file_name
        }
        table = {
            "table": table_preview
        }
        logging.info(f"FILE UPLOAD:  Template file: {file}, table: {table}")
        return render_template('config.html', form=form, table=table, file=file)


class FileDownloadView(MethodView):

    @remove_file
    def post(self, file_name, path):
        logging.info(f"FILE DOWNLOAD: download file: {file_name} from {path} ")
        return send_file(path)
