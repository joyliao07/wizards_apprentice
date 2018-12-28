from .. import app
import requests


def test_app_import():
    assert app


# Home route


def test_home_route_get():
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'Welcome to Wizard\'s Apprentice. Our wizard needs your help.' in rv.data


def test_bad_route():
    rv = app.test_client().get('/fake')
    assert rv.status_code == 404
