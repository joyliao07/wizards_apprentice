from . import app
from flask import render_template


@app.errorhandler(404)
def not_found(error):
    """404 page"""
    return render_template('404_notfound.html', error=error), 404
