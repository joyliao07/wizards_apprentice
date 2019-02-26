from ..gvision import ProcessedImage
import os


# TODO:
# test for files other than images
# test for image files with no features


def test_import(app):
    assert ProcessedImage


def test_instance(app):
    img_source = 'src/test/test_images/test_full_match.png'
    assert ProcessedImage(img_source)


def test_labels(app):
    img_source = 'src/test/test_images/test_full_match.png'
    image = ProcessedImage(img_source)
    assert 'Chair' in image.keywords
