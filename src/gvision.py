import io
import os
from google.cloud import types
from google.cloud import vision


class AnnotatedImage(object):
    def __init__(self, source):
        self.source = source
        self.labels = get_labels(self.source)

    @classmethod
    def get_labels(source):
        client = vision.ImageAnnotatorClient()
        with io.open(source, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)


