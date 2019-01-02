from ..gvision import ProcessedImage
from ..models import db as _db
from ..models import Account, Prompt
from .. import app as _app
import os
import pytest


base_path = os.path.split(__file__)[0]


@pytest.fixture
def green_car():
    print(__file__)
    return ProcessedImage(os.path.join(base_path, 'test_images/green_car.jpg'))


@pytest.fixture
def red_chair():
    return ProcessedImage(os.path.join(base_path, 'test_images/red_chair.jpg'))


@pytest.fixture
def black_laptop():
    return ProcessedImage(os.path.join(base_path, 'test_images/laptop.jpg'))


@pytest.fixture
def red_teapot():
    return ProcessedImage(os.path.join(base_path, 'test_images/red_teapot.jpg'))


@pytest.fixture
def blue_bird():
    return ProcessedImage(os.path.join(base_path, 'test_images/blue_bird.jpg'))


@pytest.fixture
def green_sofa():
    return ProcessedImage(os.path.join(base_path, 'test_images/green_sofa.jpg'))


# App, session, login fixtures


@pytest.fixture()
def app(request):
    """Session-wide Testable Flask Application
    """

    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False,
        UPLOAD_FOLDER='test/test_uploads/',
    )

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture()
def db(app, request):
    """Session-wide Test Database
    """
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture()
def session(db, request):
    """Creates a new database session for testing
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def account(app, session):
    """
    """
    account = Account(username='hannahtest', email='default@example.com', password='secret')

    session.add(account)
    session.commit()
    return account


@pytest.fixture()
def prompt(app, session):
    new_prompt = Prompt(adjective='blue', noun='chair')

    session.add(new_prompt)
    session.commit()
    return new_prompt
