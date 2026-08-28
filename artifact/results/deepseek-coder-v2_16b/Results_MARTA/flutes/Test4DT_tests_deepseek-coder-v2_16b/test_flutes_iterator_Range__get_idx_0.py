
import pytest
from flutes.iterator import Range


def test_invalid_input_zero_args():
    with pytest.raises(ValueError):
        r = Range()

def test_invalid_input_more_than_three_args():
    with pytest.raises(ValueError):
        r = Range(1, 2, 3, 4)

def test_valid_input_one_arg():
    r = Range(10)
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_valid_input_three_args():
    r = Range(1, 11, 2)
    assert list(r) == [1, 3, 5, 7, 9]