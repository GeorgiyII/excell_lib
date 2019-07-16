from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired


class FileUploadForm(FlaskForm):
    file_upload = FileField('Выберите файл', validators=[DataRequired()])
    submit = SubmitField('Go')


class ConfigForm(FlaskForm):
    sheet_name = SelectField('Страница с таблицей', validators=[DataRequired()])
    sheet_price_name = SelectField('Страница с ценами', validators=[DataRequired()])
    row_number = SelectField('Строка с материалами', choices=[])
    separate_symbol = StringField('Символ разделитель', validators=[DataRequired()])
    submit = SubmitField('Go')


class DownloadForm(FlaskForm):
    submit = SubmitField('Download')


def get_select_field_list(data_list):
    if isinstance(data_list[0], list):
        result = [(i, i) for i in range(1, len(data_list) + 1)]
    else:
        result = [(i, i) for i in data_list]
    return result
