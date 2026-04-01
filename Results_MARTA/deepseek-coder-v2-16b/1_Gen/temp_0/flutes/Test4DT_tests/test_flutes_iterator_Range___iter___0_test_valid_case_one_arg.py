
import pytest
from flutes.iterator import Range

def test_valid_case_one_arg():
    r = Range(10)
    assert isinstance(r, Range)
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
