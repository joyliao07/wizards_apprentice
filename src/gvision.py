import io
from google.cloud import vision
from google.cloud.vision import types


class ProcessedImage(object):
    """Model for images processed through the Google Vision API. Image files get
    label annotations and image property attributes that retain all of the
    data from the API. They keywords and colors attributes are a subset of the
    data scoped to the properties that we are most interested in.

    """

    def __init__(self, source):
        """
        input: source (string) path to the image file
        """
        self.filename = source
        self.labels = self.get_labels()
        self.keywords = self.get_keywords()
        self.image_properties = self.get_image_properties()
        self.colors = self.get_colors()

    def get_labels(self):
        """Query Vision API for image labels.

        input: source (string): path to the image file
        return labels:
        """
        client = vision.ImageAnnotatorClient()
        try:
            with io.open(self.filename, 'rb') as image_file:
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
            with io.open(self.filename, 'rb') as image_file:
                content = image_file.read()
            image = types.Image(content=content)
            response = client.image_properties(image=image)
            properties = response.image_properties_annotation
        except FileNotFoundError:
            print('The image file was not found.')
        if properties:
            return properties

    def get_colors(self):
        """Extract color data from image_properties.

        return: (list) the color properties, sorted by pixel_fraction
        """
        colors = [color for color in self.image_properties.dominant_colors.colors]
        colors.sort(key=lambda x: x.pixel_fraction, reverse=True)
        return colors
