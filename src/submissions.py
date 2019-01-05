PIXEL_PERCENTAGE = .2
COLOR_DETECTION_THRESHOLD = 20
RED_GREEN_THRESHOLD = 5


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
    for keyword in image.keywords:
        if noun in keyword:
            object_found = True
            break
    color_found = find_target_color(image.colors, adjective)
    return (color_found, object_found)


def find_target_color(color_data, target_color):
    """Looks through all of the rgb value sets and totals the proportion of pixels
    that are primarily the target color.

    input: color_data: color data extracted from image object, represented by rgb values
            and pixel_fraction
    input: target_color (string): the color we are trying to find
    return: True if proportion of target_color pixels > PIXEL_PERCENTAGE
    return: False if proportion of target_color pixels < PIXEL_PERCENTAGE
    """
    target_pixel_fraction = 0
    # import pdb; pdb.set_trace()
    # Sum all the pixel_fraction values
    pixel_fractions = sum([rgb.pixel_fraction for rgb in color_data])
    # Make a list of colors we don't want
    bad_colors = [c for c in ['red', 'green', 'blue'] if c != target_color]
    # Iterate over all the rgb values found in the image
    for detected_rgb in color_data:
        # Is this region majority target_color?
        for bad_color in bad_colors:
            color_diff = eval(f'detected_rgb.color.{ target_color }') - eval(f'detected_rgb.color.{ bad_color }')
            # If target_color is green, we need to be more lenient about the proportion of red
            if target_color == 'green' and bad_color == 'red':
                if abs(color_diff) < RED_GREEN_THRESHOLD:
                    break
            # If the target color value is less than one of the excluded, break
            elif color_diff < COLOR_DETECTION_THRESHOLD:
                break
        else:
            # If we get here, the region was majority target_color
            target_pixel_fraction += detected_rgb.pixel_fraction

    if target_pixel_fraction / pixel_fractions >= PIXEL_PERCENTAGE:
        return True
    return False
