import io
import os
import uuid
from google.cloud import vision
from google.cloud.vision import types


class ProcessedImage(object):
    def __init__(self, source):
        self.source = source
        self.labels = self.get_labels()
        self.keywords = self.get_keywords()
        self.image_properties = self.get_image_properties()
        self.filename = self.randomize_source_filename()
        self.colors = self.get_colors()

    def get_labels(self):
        """Query Vision API for image labels.

        input: source (string): path to the image file
        return labels:
        """
        client = vision.ImageAnnotatorClient()
        try:
            with io.open(self.source, 'rb') as image_file:
                content = image_file.read()
            image = types.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
        except FileNotFoundError:
            print('The image file was not found.')
        if labels:
            return labels

    def get_keywords(self):
        """Extract a list of keywords from the labels we got from Google Vision.

        returns: list of strings representing label descriptions
        """
        return [label.description for label in self.labels]

    def get_image_properties(self):
        """Get image properties. We're largely interested in dominant colors.
        """
        client = vision.ImageAnnotatorClient()
        try:
            with io.open(self.source, 'rb') as image_file:
                content = image_file.read()
            image = types.Image(content=content)
            response = client.image_properties(image=image)
            properties = response.image_properties_annotation
        except FileNotFoundError:
            print('The image file was not found.')
        if properties:
            return properties

    def randomize_source_filename(self):
        """Generate randomized filename for stored images.

        return: randomized string
        """
        ext = self.source.split('.')[-1]
        # TODO: rename source file
        return f'{ uuid.uuid4() }.{ ext }'

    def get_colors(self):
        """Extract color data from image_properties.

        return: (list) the color properties, sorted by pixel_fraction
        """
        colors = [color for color in self.image_properties.dominant_colors.colors]
        colors.sort(key=lambda x: x.pixel_fraction, reverse=True)
        return colors
