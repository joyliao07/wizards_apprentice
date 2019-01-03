from ..validate_image import get_image_timestamp, validate_image
import datetime
import os
import pytest


@pytest.fixture
def valid_image():
    base_path = os.path.split(__file__)[0]
    return os.path.join(base_path, 'test_images/laptop.jpg')


@pytest.fixture
def no_timestamp():
    base_path = os.path.split(__file__)[0]
    return os.path.join(base_path, 'test_images/blue_ball.jpg')


def test_imports():
    assert get_image_timestamp


def test_get_image_timestamp_returns_data(valid_image):
    assert get_image_timestamp(valid_image) < datetime.datetime.now()


def test_get_image_timestamp_returns_none(no_timestamp):
    assert get_image_timestamp(no_timestamp) is None


def test_validate_image_old(valid_image):
    if os.environ['WIZARD_APP_TESTING'] == 'False':
        assert validate_image(valid_image) is False


def test_validate_image_invalid(no_timestamp):
    if os.environ['WIZARD_APP_TESTING'] == 'False':
        assert validate_image(no_timestamp) is False
