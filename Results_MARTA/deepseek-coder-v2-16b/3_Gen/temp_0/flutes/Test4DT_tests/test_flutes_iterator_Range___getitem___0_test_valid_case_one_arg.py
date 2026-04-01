
import pytest
from flutes.iterator import Range

def test_valid_case_one_arg():
    r = Range(10)
    assert r[0] == 0
    assert r[2] == 2
    assert r[4] == 4
