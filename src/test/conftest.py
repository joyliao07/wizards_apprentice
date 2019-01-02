from ..gvision import ProcessedImage
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
