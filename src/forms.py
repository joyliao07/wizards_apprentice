from flask import session

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, length


class SubmitForm(FlaskForm):
    file_upload = FileField('<span class="upload_label"><i class="fas fa-upload"></i> Upload File</span>', validators=[FileRequired()])


class AuthForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(max=16)])
    email = EmailField('E-mail', validators=[DataRequired(), length(max=128)])
    password = PasswordField('Password', validators=[DataRequired(), length(max=32)])


class ManualPromptForm(FlaskForm):
    adjective = StringField('Adjective', validators=[DataRequired()])
    noun = StringField('Noun', validators=[DataRequired()])
