
import pytest
from flutes.iterator import Range

def test_valid_case_three_arguments():
    r = Range(1, 10 + 1)  # (start, end)
    assert isinstance(r, Range)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

    r = Range(1, 11, 2)   # (start, end, step)
    assert isinstance(r, Range)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9
