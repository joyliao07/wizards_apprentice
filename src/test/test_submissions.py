from ..submissions import evaluate_submission
import pytest



def test_import():
    assert evaluate_submission


def test_evaluate_success(green_car, red_chair, red_teapot, blue_bird, green_sofa):
    # import pdb; pdb.set_trace()
    assert evaluate_submission(green_car, ('green', 'car')) == (True, True)
    assert evaluate_submission(red_chair, ('red', 'chair')) == (True, True)
    assert evaluate_submission(red_teapot, ('red', 'teapot')) == (True, True)
    assert evaluate_submission(blue_bird, ('blue', 'bird')) == (True, True)
    assert evaluate_submission(green_sofa, ('green', 'sofa')) == (True, True)


# @pytest.mark.skip(reason='These take a long time.')
def test_evaluate_failure(red_chair, green_car, black_laptop):
    assert evaluate_submission(red_chair, ('green', 'car')) == (False, False)
    assert evaluate_submission(green_car, ('green', 'horse')) == (True, False)
    assert evaluate_submission(black_laptop, ('red', 'car')) == (False, False)
