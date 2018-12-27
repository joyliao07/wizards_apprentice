from flask import flash, render_template, redirect, url_for, session, g
from . import app
# from .forms import AuthForm
# from .models import Account, db
import functools


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.get('account') is None:
            flash('You must be logged in to visit this page.')
            return redirect(url_for('.login'))

        return view(**kwargs)

    return wrapped_view


@app.route('/login')
def login():
    """
    get: visit login page
    post: user tries to log in
    """
    return render_template('auth/login.html')


@app.route('/register')
def register():
    """
    get: visit register page
    post: user registers account
    """
    return render_template('auth/register.html')


@app.route('/logout')
def logout():
    """
    get: user logs out
    """
    return render_template('home.html')
