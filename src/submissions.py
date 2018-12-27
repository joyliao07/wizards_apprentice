def evaluate_submission(image, prompt):
    """Compare the ProcessedImage object to the prompts. Return

    input: image (ProcessedImage) the processed image submitted by the user
    input: prompt (tuple) adjective (color) and noun (object) to match
    return: (False, False) color and object not found
    return: (True, False) color found, object not found
    return: (False, True) color not found, object found
    return: (True, True) color and object found
    """
    result = (False, False)
    adjective, noun = prompt

    # Is the prompt object in this image?
    if noun in image.keywords:
        result = (result[0], True)

    # Make a list of colors we don't want
    bad_colors = [c for c in ['red', 'green', 'blue'] if c != adjective]
    # Iterate over all the rgb values found in the image
    for detected_rgb in image.colors:
        # Compare each excluded color to the target color
        for bad_color in bad_colors:
            # If the target color value is less than one of the excluded, break
            if eval(f'detected_rgb.color.{ adjective }') <= eval(f'detected_rgb.color.{ bad_color }'):
                break
        else:
            # If we get here, at least one rgb was primarily our target color
            result = (True, result[1])
            break

    return result
