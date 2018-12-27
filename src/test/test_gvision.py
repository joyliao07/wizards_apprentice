from ..gvision import ProcessedImage
import os


# TODO:
# test for files other than images
# test for image files with no features


def test_import():
    assert ProcessedImage


def test_instance():
    img_source = './uploads/green_car.jpg'
    assert ProcessedImage(img_source)


def test_labels():
    img_source = './uploads/green_car.jpg'
    image = ProcessedImage(img_source)
    assert 'car' in image.keywords
