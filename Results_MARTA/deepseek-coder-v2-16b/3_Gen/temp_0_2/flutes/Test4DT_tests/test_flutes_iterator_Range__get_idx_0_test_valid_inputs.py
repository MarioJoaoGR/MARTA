
import pytest
from flutes.iterator import Range

def test_valid_inputs():
    r = Range(1, 10, 2)
    assert r[0] == 1
    assert r[1] == 3
    assert r[2] == 5
    assert r[3] == 7
    assert r[4] == 9
