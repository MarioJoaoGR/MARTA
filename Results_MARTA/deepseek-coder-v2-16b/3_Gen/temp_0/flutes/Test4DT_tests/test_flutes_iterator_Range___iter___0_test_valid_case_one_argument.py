
import pytest
from flutes.iterator import Range

def test_valid_case_one_argument():
    r = Range(10)
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
