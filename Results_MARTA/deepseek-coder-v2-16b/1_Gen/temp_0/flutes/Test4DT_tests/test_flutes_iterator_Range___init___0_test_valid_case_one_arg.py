
import pytest
from flutes.iterator import Range

def test_valid_case_one_arg():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4

    r = Range(1, 10 + 1)
    assert r[0] == 1
    assert r[2] == 3
    assert r[4] == 5

    r = Range(1, 11, 2)
    assert r[0] == 1
    assert r[2] == 5
    assert r[4] == 9
