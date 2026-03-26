
import pytest
from flutes.iterator import Range

def test_valid_case_one_arg():
    r = Range(10)
    assert len(r) == 10

def test_valid_case_two_args():
    r = Range(1, 10 + 1)
    assert len(r) == 10

def test_valid_case_three_args():
    r = Range(1, 11, 2)
    assert len(r) == 5
