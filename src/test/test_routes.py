from .. import app


def test_app_import():
    assert app


def test_bad_route():
    rv = app.test_client().get('/fake')
    assert rv.status_code == 404


# Home route


def test_home_route_get():
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'Welcome to Wizard\'s Apprentice. Our wizard needs your help.' in rv.data


# Play route

def test_play_get_no_login():
    rv = app.test_client().get('/play', follow_redirects=True)
    assert b'<h2>Login:</h2>' in rv.data
    assert rv.status_code == 200


# Submission route

def test_submission_get_no_login():
    rv = app.test_client().get('/submission', follow_redirects=True)
    assert b'<h2>Login:</h2>' in rv.data
    assert rv.status_code == 200


# Feedback route

def test_feedback_get_no_login():
    rv = app.test_client().get('/feedback', follow_redirects=True)
    assert b'<h2>Login:</h2>' in rv.data
    assert rv.status_code == 200

# History route


def test_history_get_no_login():
    rv = app.test_client().get('/history', follow_redirects=True)
    assert b'<h2>Login:</h2>' in rv.data
    assert rv.status_code == 200


# Players route

def test_players_get_no_login():
    rv = app.test_client().get('/players', follow_redirects=True)
    assert b'<h2>Login:</h2>' in rv.data
    assert rv.status_code == 200
