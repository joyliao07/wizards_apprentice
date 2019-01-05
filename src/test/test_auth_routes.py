import pytest


def login_for_test(app):
    """ this logs in test user """
    app.post('/login', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)


# login route


def test_login_get_no_login(app):
    """ test that going to /login without being logged in prompts user to log
    in """
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'Login' in rv.data


def test_login_get_already_logged_in(app, session, db, account):
    """ tests that going to /login when already logged in changes message """
    with app.test_client() as app:
            login_for_test(app)

            rv = app.get('/login', follow_redirects=True)

            assert rv.status_code == 200
            assert b'You are already logged in' in rv.data


def test_login_post_successful(app, session, db, account):
    """ tests successful login """
    with app.test_client() as app:
        rv = app.post('/login', data=dict(
            email='default@example.com',
            password='secret'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'You have logged in successfully' in rv.data


def test_login_post_user_not_found(app, session, db, account):
    """ tests failed login - user account doesn't exist """
    with app.test_client() as app:
        rv = app.post('/login', data=dict(
            email='defaulttttt@example.com',
            password='secret'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'invalid username or password' in rv.data


def test_login_post_bad_password(app, session, db, account):
    """ tests failed login - password is wrong """
    with app.test_client() as app:
        rv = app.post('/login', data=dict(
            email='default@example.com',
            password='secrettttt'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'invalid username or password' in rv.data


# register route


def test_register_get_no_login(app):
    """ tests going to register with no login - user should be prompted
    to register """
    rv = app.test_client().get('/register')

    assert rv.status_code == 200
    assert b'Register' in rv.data


def test_register_get_already_logged_in(app, session, db, account):
    """ tests that going to register when logged in tells user they're already
    logged in """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/register', follow_redirects=True)

        assert rv.status_code == 200
        assert b'You are already logged in' in rv.data


def test_register_post_successful(app, db, session):
    """ tests successful register """
    with app.test_client() as app:
        rv = app.post('/register', data=dict(
            username='hannah',
            email='default@example.com',
            password='secret'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'Registration complete' in rv.data


def test_register_post_already_registered(app, db, session, account):
    """ tests trying to register when an email is already registered """
    with app.test_client() as app:
        rv = app.post('/register', data=dict(
            username='hannah',
            email='default@example.com',
            password='secret'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'has already been registered' in rv.data


def test_register_post_bad_password(app, db, session):
    """ tests registration when password doesn't fit requirements """
    with app.test_client() as app:
        rv = app.post('/register', data=dict(
            username='hannah',
            email='default@example.com',
            password='s'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'Password must be between 6 and 32 characters' in rv.data


def test_register_post_bad_username(app, db, session):
    """ tests registration when username doesn't fit requirements """
    with app.test_client() as app:
        rv = app.post('/register', data=dict(
            username='h',
            email='default@example.com',
            password='secret'
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert b'Username must be between 3 and 16 characters' in rv.data


# logout route


def test_logout_get_successful(app, db, session, account):
    """ tests successful logout """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/logout', follow_redirects=True)

        assert rv.status_code == 200
        assert b'You have been logged out' in rv.data
        assert b'Login' in rv.data


def test_logout_route_no_login(app):
    """ tests logout when user is not logged in """
    rv = app.test_client().get('/logout', follow_redirects=True)

    assert rv.status_code == 200
    assert b'You must be logged in' in rv.data
