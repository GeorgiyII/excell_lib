from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired


class FileUploadForm(FlaskForm):
    file_upload = FileField('Выберите файл', validators=[DataRequired()])
    submit = SubmitField('Go')


class ConfigForm(FlaskForm):
    sheet_name = StringField('Страница с таблицей', validators=[DataRequired()])
    sheet_price_name = StringField('Страница с ценами', validators=[DataRequired()])
    row_number = SelectField('Строка с материалами', choices=[(1, 1), (2, 2), (3, 3)])
    separate_symbol = StringField('Символ разделитель', validators=[DataRequired()])
    submit = SubmitField('Go')


class DownloadForm(FlaskForm):
    submit = SubmitField('Download')
