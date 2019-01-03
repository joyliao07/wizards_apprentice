from datetime import datetime
import os
from PIL import Image


def validate_image(file_path):
    """
    Determine if the submitted image is valid.

    :input file_path: modeled submission object
    :returns: True if image is valid
    :returns: False if image is invalid
    """
    if os.environ['WIZARD_APP_TESTING'] == 'False':
        img_time = get_image_timestamp(file_path)
        # No EXIF data
        if img_time is None:
            return False
        # Image older than 1 day
        if (datetime.now() - img_time).days > 0:
            return False
    return True


def get_image_timestamp(image_file):
    """
    Read an image timestamp by extracting EXIF data.

    :param image_file: full path to image file as string
    :returns: image file timestamp as datetime object
    """
    binary_image = Image.open(image_file)
    exif_data = binary_image._getexif()
    if exif_data:
        return datetime.strptime(exif_data[306], '%Y:%m:%d %I:%M:%S')
    return None
