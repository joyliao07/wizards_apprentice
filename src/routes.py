from flask import Flask, request, render_template, redirect, url_for, session, abort, flash, session

from .auth import login_required, logout_required

from . import app


@app.route('/')
def home():
    """
    get: user visits homepage
    """
    return render_template('home.html')


@app.route('/play', methods=['GET', 'POST'])
@login_required
def play():
    """
    get: visiting page to submit photo
    post: receiving submission form from user
    """
    return render_template('play.html')


@app.route('/submission', methods=['GET', 'POST'])
@login_required
def submission():
    """
    get: viewing submission and confirming
    post: user confirms submission for evaluation
    """
    return render_template('submission.html')


@app.route('/feedback')
@login_required
def feedback():
    """
    get: user sees whether submission passed/failed
    """
    return render_template('feedback.html')


@app.route('/history')
@login_required
def history():
    """
    get: user views their own history
    """
    return render_template('history.html')


@app.route('/players')
@login_required
def players():
    """
    get: user views others' history
    """
    return render_template('players.html')
