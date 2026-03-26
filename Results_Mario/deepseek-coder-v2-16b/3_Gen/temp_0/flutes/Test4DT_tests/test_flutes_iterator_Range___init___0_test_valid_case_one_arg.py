
import pytest
from flutes.iterator import Range

def test_valid_case_one_arg():
    r = Range(10)
    assert isinstance(r, Range)
    assert r.l == 0
    assert r.r == 10
    assert r.step == 1
    assert r.length == 10

    # Check indexing
    assert r[0] == 0
    assert r[9] == 9
