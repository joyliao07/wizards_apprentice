from ..gvision import ProcessedImage
import pytest


@pytest.fixture
def green_car():
    return ProcessedImage('../../uploads/green_car.jpg')


@pytest.fixture
def red_chair():
    return ProcessedImage('../../uploads/red_chair.jpg')


@pytest.fixture
def black_laptop():
    return ProcessedImage('../../uploads/laptop.jpg')


@pytest.fixture
def red_teapot():
    return ProcessedImage('../../uploads/red_teapot.jpg')
