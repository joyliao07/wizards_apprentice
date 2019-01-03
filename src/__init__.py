from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    instance_relative_config=True
)

app.config.from_mapping(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    UPLOAD_FOLDER=os.getenv('UPLOAD_FOLDER'),
)

app.config.from_mapping(
    S3_BUCKET=os.environ.get("wizardphoto"),
    S3_LOCATION='http://{}.s3.amazonaws.com/'.format(os.environ.get("wizardphoto")),
    SECRET_KEY=os.urandom(32),
    DEBUG=True,
    PORT=5000
)

from . import routes, forms, models, exceptions, auth
