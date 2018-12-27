from flask import Flask, request, render_template, redirect, url_for, session, abort, flash, session

from . import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/play')
def play():
    """
    get: visiting page to submit photo
    post: receiving submission form from user
    """
    return render_template('play.html')


@app.route('/submission')
def submission():
    """
    get: viewing submission and confirming
    post: user confirms submission for evaluation
    """
    return render_template('submission.html')


@app.route('/feedback')
def feedback():
    """
    get: user sees whether submission passed/failed
    """
    return render_template('feedback.html')


@app.route('/history')
def history():
    """
    get: user views their own history
    """
    return render_template('history.html')


@app.route('/players')
def players():
    """
    get: user views others' history
    """
    return render_template('players.html')
