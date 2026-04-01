
import pytest
from flutes.iterator import Range

def test_valid_case_two_args():
    r = Range(1, 10)
    assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    r = Range(1, 10, 2)
    assert list(r) == [1, 3, 5, 7, 9]
