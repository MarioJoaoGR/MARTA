
import pytest
from flutes.iterator import Range

def test_valid_case_two_args():
    r = Range(1, 10)
    assert len(r) == 9

    r = Range(5, 15)
    assert len(r) == 10

    r = Range(-3, 3)
    assert len(r) == 6
