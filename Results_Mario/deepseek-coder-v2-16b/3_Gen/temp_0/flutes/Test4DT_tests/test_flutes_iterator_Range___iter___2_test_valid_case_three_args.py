
import pytest
from flutes.iterator import Range

def test_valid_case_three_args():
    r = Range(1, 11, 2)
    assert list(r) == [1, 3, 5, 7, 9]
