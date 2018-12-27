from ..submissions import evaluate_submission
import pytest


def test_import():
    assert evaluate_submission


def test_evaluate_success(green_car):
    # import pdb; pdb.set_trace()
    assert evaluate_submission(green_car, ('green', 'car')) == (True, True)


def test_evaluate_failure(red_chair, green_car):
    assert evaluate_submission(red_chair, ('green', 'car')) == (False, False)
    assert evaluate_submission(green_car, ('green', 'horse')) == (True, False)
