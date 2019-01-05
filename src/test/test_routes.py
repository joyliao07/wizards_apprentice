import pytest
import io

# Login function


def login_for_test(app):
    """ this logs in test user """
    app.post('/login', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)


# test basics


def test_app_import(app):
    assert app


def test_bad_route(app):
    """ test 404 with bad route """
    rv = app.test_client().get('/fake')
    assert rv.status_code == 404
    assert b'Page not found' in rv.data


# Home route


def test_home_get_no_login(app):
    """ test login page for status code/correct message with no login """
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'You must be the new apprentice.' in rv.data


def test_home_get_with_login(app, db, session, account):
    """ test login page for status code/correct message with login """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/')

        assert rv.status_code == 200
        assert b'Welcome back, my apprentice' in rv.data


def test_home_bad_method(app):
    """ test home route with unimplemented method for correct status code """
    rv = app.test_client().delete('/')
    assert rv.status_code == 405
    assert b'Are you trying to pull a fast one' in rv.data


# Play route

def test_play_get_no_login(app):
    """ test that going to /play while not logged in redirects to login
    page """
    rv = app.test_client().get('/play', follow_redirects=True)
    assert b'You must be logged in' in rv.data
    assert rv.status_code == 200


def test_play_get_with_login(app, session, db, account):
    """ test that going to /play while logged in takes you to the prompt """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/play')

        assert rv.status_code == 200
        assert b'I seem to have forgotten what a'


def test_play_post_no_login(app):
    """ test that trying to post to /play with no login redirects to login """
    rv = app.test_client().post('/play', follow_redirects=True)

    assert rv.status_code == 200
    assert b'You must be logged in' in rv.data


def test_play_post_with_login(app, session, db, account):
    """ tests posting to play route (user making initial submission) """
    with app.test_client() as app:
        login_for_test(app)

        data = dict()
        data['file_upload'] = (io.BytesIO(b'hi'), 'test_no_match.jpg')

        rv = app.post(
            '/play',
            data=data,
            content_type='multipart/form-data',
            follow_redirects=True
        )

        assert rv.status_code == 200
        assert b'So, is this what a' in rv.data


def test_play_post_with_login_no_data(app, session, db, account):
    """ test that posting to /play with no data while logged in
    just serves the /play get page """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.post('/play')

        assert rv.status_code == 200
        assert b'I seem to have forgotten what a'


def test_play_bad_method(app):
    """ test home route with unimplemented method for correct status code """
    rv = app.test_client().delete('/play')
    assert rv.status_code == 405
    assert b'Are you trying to pull a fast one' in rv.data


# Submission route


def test_submission_get_no_login(app):
    """ tests that user is prompted to login when visiting submission page
    when not logged in """
    rv = app.test_client().get('/submission', follow_redirects=True)
    assert b'You must be logged in' in rv.data
    assert rv.status_code == 200


def test_submission_get_with_login_no_data(app, session, db, account):
    """ tests that 404 is received when going to /submission without
    submitting anything """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/submission', follow_redirects=True)

        assert rv.status_code == 404
        assert b'Page not found' in rv.data


def test_submission_get_with_login(app, db, session, account):
    """ tests that going to /submission route after submitting an image
    (but before confirming/finalizing submission) serves correct content """
    with app.test_client() as app:
        login_for_test(app)

        data = dict()
        data['file_upload'] = (io.BytesIO(b'hi'), 'test.jpg')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data'
        )

        rv = app.get('/submission')

        assert rv.status_code == 200
        assert b'So, is this what a' in rv.data


def test_submission_route_bad_method(app):
    """ test submission route with unimplemented method for correct
    status code """
    rv = app.test_client().delete('/submission')
    assert rv.status_code == 405
    assert b'Are you trying to pull a fast one' in rv.data


# Feedback route

def test_feedback_get_no_login(app):
    """ tests going to /feedback without being logged in to make sure
    user is prompted to log in """
    rv = app.test_client().get('/feedback', follow_redirects=True)

    assert rv.status_code == 200
    assert b'You must be logged in' in rv.data


def test_feedback_no_data(app, session, db, account):
    """ tests that 404 is received when going to /feedback without
    submitting anything """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/feedback', follow_redirects=True)

        assert rv.status_code == 404
        assert b'Page not found' in rv.data


def test_feedback_get_no_match(app, session, db, account, prompt):
    """ tests feedback text when user submits unmatching image """
    with app.test_client() as app:
        login_for_test(app)

        f = open('src/test/test_images/test_no_match.jpg', 'rb').read()

        data = dict()
        data['file_upload'] = (io.BytesIO(f), 'test.jpg')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data',
            follow_redirects=True
        )

        rv = app.get('/feedback')

        assert rv.status_code == 200
        assert b'This is not a' in rv.data
        assert b'It\'s not even' in rv.data


def test_feedback_get_color_only_match(app, session, db, account, prompt):
    """ tests feedback text when user submits image that matches color only """
    with app.test_client() as app:
        login_for_test(app)

        f = open('src/test/test_images/test_color_match.jpg', 'rb').read()

        data = dict()
        data['file_upload'] = (io.BytesIO(f), 'test.jpg')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data'
        )

        rv = app.get('/feedback')

        assert rv.status_code == 200
        assert b'Well... it\'s' in rv.data
        assert b'but it\'s not even a' in rv.data


def test_feedback_get_noun_only_match(app, session, db, account, prompt):
    """ tests feedback text when user submits image that matches object
    type only """
    with app.test_client() as app:
        login_for_test(app)

        f = open('src/test/test_images/test_noun_match.jpg', 'rb').read()

        data = dict()
        data['file_upload'] = (io.BytesIO(f), 'test.jpg')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data'
        )

        rv = app.get('/feedback')

        assert rv.status_code == 200
        assert b'That looks like a' in rv.data
        assert b'but it\'s not' in rv.data


def test_feedback_get_full_match(app, session, db, account, prompt):
    """ tests feedback text when user submits full match """
    with app.test_client() as app:
        login_for_test(app)

        f = open('src/test/test_images/test_full_match.png', 'rb').read()

        data = dict()
        data['file_upload'] = (io.BytesIO(f), 'test.png')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data'
        )

        rv = app.get('/feedback')

        assert rv.status_code == 200
        assert b'Yes, that\'s a' in rv.data


def test_feedback_route_bad_method(app):
    """ test feedback route with unimplemented method for correct ]
    status code """
    rv = app.test_client().delete('/feedback')
    assert rv.status_code == 405
    assert b'Are you trying to pull a fast one' in rv.data

# History route


def test_history_get_no_login(app):
    """ tests going to /history without being logged in to make sure user is
    redirected """
    rv = app.test_client().get('/history', follow_redirects=True)
    assert b'You must be logged in' in rv.data
    assert rv.status_code == 200


def test_history_get_no_submissions(app, session, db, account):
    """ tests going to /history when user hasn't submitted anything """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/history')

        assert rv.status_code == 200
        assert b'Apprentice, you have no submissions yet.' in rv.data


def test_history_get_with_submissions(app, session, db, account, prompt):
    """ tests that submission is present on history page """
    with app.test_client() as app:
        login_for_test(app)

        f = open('src/test/test_images/test_color_match.jpg', 'rb').read()

        data = dict()
        data['file_upload'] = (io.BytesIO(f), 'test.jpg')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data'
        )

        rv = app.get('/history')

        assert rv.status_code == 200
        assert b'Apprentice, your past submissions are below.'
        assert b'Blue Chair (Fail)' in rv.data


# Players route

def test_players_get_no_login(app):
    """ tests that going to /players when not logged in prompts user to log
    in """
    rv = app.test_client().get('/players', follow_redirects=True)
    assert b'You must be logged in' in rv.data
    assert rv.status_code == 200


def test_players_get_no_submissions(app, session, db, account, prompt):
    """ tests that going to /players with no submissions shows different
    message """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/players')

        assert rv.status_code == 200
        assert b'Apprentice, there are no successful submissions' in rv.data


def test_players_get_with_submissions(app, session, db, account, prompt):
    """ tests that going to /players shows a player's successful submission """
    with app.test_client() as app:
        login_for_test(app)

        f = open('src/test/test_images/test_full_match.png', 'rb').read()

        data = dict()
        data['file_upload'] = (io.BytesIO(f), 'test.png')

        app.post(
            '/play',
            data=data,
            content_type='multipart/form-data'
        )

        app.get('/feedback')

        rv = app.get('/players')

        assert rv.status_code == 200
        assert b'Other player\'s submissions are below.'
        assert b'Blue Chair' in rv.data
