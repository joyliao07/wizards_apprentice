"""To add this function to routes.py."""
from .models import db, Submission


# @app.route('/players')
# @login_required
def players():
    """
    get: user views others' history
    """
    all = Submission.query.all()
    print(all)




    # return render_template('players.html')


players()






















