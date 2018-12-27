from uuid import uuid4
from os.path import splitext
from os.path import join as path_join

from flask import Flask, request, render_template, redirect, url_for, session, abort, flash, session

from werkzeug.utils import secure_filename

from .auth import login_required, logout_required
from .forms import SubmitForm

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
    form = SubmitForm()

    if form.validate_on_submit():
        allowed_filetypes = set(['.png', '.jpg', '.jpeg'])

        f = form.file_upload.data
        ext = splitext(f.filename)[1]

        if ext not in allowed_filetypes:
            flash('File must be a .png or a .jpg/.jpeg')
            return redirect(url_for('.play'))

        filename = secure_filename(str(uuid4()) + ext)
        file_path = path_join(app.root_path, app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        return redirect(url_for('.submission'))

    return render_template('play.html', form=form)


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
