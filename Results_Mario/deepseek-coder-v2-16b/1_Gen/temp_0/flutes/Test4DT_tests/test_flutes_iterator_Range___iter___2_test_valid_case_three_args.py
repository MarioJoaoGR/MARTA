
from flutes.iterator import Range
import pytest

def test_valid_case_three_args():
    r = Range(1, 10, 2)
    assert list(r) == [1, 3, 5, 7, 9]
