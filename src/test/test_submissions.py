from ..submissions import evaluate_submission
import pytest



def test_import():
    assert evaluate_submission


def test_evaluate_success(green_car, red_chair, red_teapot):
    # import pdb; pdb.set_trace()
    assert evaluate_submission(green_car, ('green', 'car')) == (True, True)
    assert evaluate_submission(red_chair, ('red', 'chair')) == (True, True)
    assert evaluate_submission(red_teapot, ('red', 'teapot')) == (True, True)


def test_evaluate_failure(red_chair, green_car, black_laptop):
    assert evaluate_submission(red_chair, ('green', 'car')) == (False, False)
    assert evaluate_submission(green_car, ('green', 'horse')) == (True, False)
    assert evaluate_submission(black_laptop, ('red', 'car')) == (False, False)
