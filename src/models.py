from . import app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from passlib.hash import sha256_crypt

from datetime import datetime as dt


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Submission(db.Model):
    """ A single submission by a user.

    References one user (submitted_by) and one prompt (prompt_id) """
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(256), index=True, nullable=False, unique=True)
    prompt_id = db.Column(db.Integer, db.ForeignKey('prompts.id'))
    submitted_by = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    passes_prompt = db.Column(db.Boolean)

    submission_time = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return f'<Submission for prompt {self.prompt_id} by user>'


class Prompt(db.Model):
    """ A single prompt which users make submissions to.

    References many submissions (submissions) made by many users """
    __tablename__ = 'prompts'

    id = db.Column(db.Integer, primary_key=True)
    submissions = db.relationship('Submission', backref='prompts')
    adjective = db.Column(db.String(128))   # Color of the thing to find
    noun = db.Column(db.String(128))        # The thing to find

    def __repr__(self):
        return f'<Prompt adjective: {self.adjective} noun: {self.noun}>'


class Account(db.Model):
    """ A user account.

    References many submissions (submissions) to many prompts by this user """
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, nullable=False, unique=True)
    email = db.Column(db.String(256), index=True, nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    submissions = db.relationship('Submission', backref='accounts')

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return f'<Account email: {self.email}, username: {self.username}>'

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = sha256_crypt.hash(password)

    @classmethod
    def check_password_hash(cls, account, password):
        if account is not None:
            if sha256_crypt.verify(password, account.password):
                return True

        return False
