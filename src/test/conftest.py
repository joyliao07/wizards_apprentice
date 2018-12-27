from ..gvision import ProcessedImage
import pytest


@pytest.fixture
def green_car():
    return ProcessedImage('./src/static/uploads/green_car.jpg')


@pytest.fixture
def red_chair():
    return ProcessedImage('./src/static/uploads/red_chair.jpg')
