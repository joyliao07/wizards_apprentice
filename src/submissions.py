PIXEL_PERCENTAGE = .2
COLOR_DETECTION_THRESHOLD = 1.2


def evaluate_submission(image, prompt):
    """Compare the ProcessedImage object to the prompts. Return

    input: image (ProcessedImage) the processed image submitted by the user
    input: prompt (tuple) adjective (color) and noun (object) to match
    return: (False, False) color and object not found
    return: (True, False) color found, object not found
    return: (False, True) color not found, object found
    return: (True, True) color and object found
    """
    object_found, color_found = False, False
    adjective, noun = prompt

    # Is the prompt object in this image?
    if noun in image.keywords:
        object_found = True

    # color_found = score_colors(image.colors, adjective)
    color_found = score_colors_highest_pixel_fractions(image.colors, adjective)
    return (color_found, object_found)


def score_colors(color_data, target_color):
    """Looks through all of the rgb value sets and returns True if any one of them has a higher
    value for the target color than the other two.
    """
    # Make a list of colors we don't want
    bad_colors = [c for c in ['red', 'green', 'blue'] if c != target_color]
    # import pdb; pdb.set_trace()
    # Iterate over all the rgb values found in the image
    for detected_rgb in color_data:
        # Compare each excluded color to the target color
        for bad_color in bad_colors:
            # If the target color value is less than one of the excluded, break
            if eval(f'detected_rgb.color.{ target_color }') <= eval(f'detected_rgb.color.{ bad_color }'):
                break
        else:
            # If we get here, at least one rgb was primarily our target color
            return True
    return False


def score_colors_highest_pixel_fractions(color_data, target_color):
    """Looks through all of the rgb value sets and returns True if any one of them has a higher
    value for the target color than the other two. Only checks the highest pixel ratios.
    """
    # import pdb; pdb.set_trace()
    # Sum all the pixel_fraction values
    pixel_fractions = sum([rgb.pixel_fraction for rgb in color_data])
    # Make a list of colors we don't want
    bad_colors = [c for c in ['red', 'green', 'blue'] if c != target_color]
    # Iterate over all the rgb values found in the image
    for detected_rgb in color_data:

        # Calculate the pixel percentage of this rgb
        pixels_percent = detected_rgb.pixel_fraction / pixel_fractions
        # import pdb; pdb.set_trace()
        if pixels_percent >= PIXEL_PERCENTAGE:
            # Compare each excluded color to the target color
            for bad_color in bad_colors:
                # If the target color value is less than one of the excluded, break
                if eval(f'detected_rgb.color.{ target_color }') / eval(f'detected_rgb.color.{ bad_color }') < COLOR_DETECTION_THRESHOLD:
                    break
            else:
                # If we get here, at least one rgb was primarily our target color
                print('Finding:', target_color)
                print(detected_rgb)
                return True
    return False
