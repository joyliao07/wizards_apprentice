from flask import flash, render_template, redirect, url_for, session, g, abort
from sqlalchemy.exc import IntegrityError

from . import app
from .forms import AuthForm, RegisterForm, ManualPromptForm
from .models import Account, Prompt, db
from .prompt import random_generator

import functools
import os


# --- Helpers


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.get('user') is None:
            flash('You must be logged in to visit this page.')
            return redirect(url_for('.login'))

        return view(**kwargs)

    return wrapped_view


def logout_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.get('user') is not None:
            flash('You are already logged in')
            return redirect(url_for('.home'))

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_account():
    """ Get account id from session """
    account_id = session.get('account_id')

    if account_id is None:
        g.user = None
    else:
        g.user = Account.query.get(account_id)

        if session.get('admin') is True:
            g.admin = True


# --- Routes


@app.route('/login', methods=['GET', 'POST'])
@logout_required
def login():
    """
    get: visit login page
    post: user tries to log in
    """

    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        account = Account.query.filter_by(email=email).first()

        if account is None or not Account.check_password_hash(account, password):
            error = 'invalid username or password'

        if error is None:
            session.clear()
            session['account_id'] = account.id
            session['admin'] = False
            flash('You have logged in successfully')

            session['flash'] = 'off'

            if account.email == os.getenv('ADMIN_USER'):
                session['admin'] = True
                flash('admin login')

            return redirect(url_for('.home'))

        flash(error)

    return(render_template('auth/login.html', form=form))


@app.route('/register', methods=['GET', 'POST'])
@logout_required
def register():
    """
    get: visit register page
    post: user registers account
    """

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.data['username']
        email = form.data['email']
        password = form.data['password']
        error = None

        if Account.query.filter_by(email=email).first() is not None:
            error = f'{ email } has already been registered'

        elif len(password) > 32 or len(password) < 6:
            error = 'Password must be between 6 and 32 characters'

        elif len(username) > 16 or len(username) < 3:
            error = 'Username must be between 3 and 16 characters'

        elif error is None:
            try:
                account = Account(username=username, email=email, password=password)
                db.session.add(account)
                db.session.commit()

                flash('Registration complete')
                return redirect(url_for('.login'))
            except IntegrityError:
                error = 'There was an issue creating your account'

        flash(error)

    return render_template('auth/register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """
    get: user logs out
    """
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('.login'))


# --- Admin route


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """
    get: takes user to admin panel. they must be logged in to admin
    account
    post: update based on changes on admin panel
    """
    if session.get('admin') is True:
        form = ManualPromptForm()
        if form.validate_on_submit():
            adjective = form.data['adjective']
            noun = form.data['noun']
            prompt = Prompt(adjective=adjective, noun=noun)
            db.session.add(prompt)
            db.session.commit()
            flash(f'Prompt updated to { adjective } { noun }')

        return render_template('pages/admin.html', form=form)

    abort(404)


@app.route('/admin_new_prompt')
def admin_new_prompt():
    """
    get: resets prompt
    """
    if session.get('admin') is True:
        random_generator()
        flash('New random prompt generated')
        return redirect(url_for('.admin'))

    abort(404)
