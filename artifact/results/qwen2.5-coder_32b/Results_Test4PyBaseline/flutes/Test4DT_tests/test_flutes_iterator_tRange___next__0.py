
import pytest
from flutes.iterator import Range

def test_range_single_argument():
    r = Range(10)
    assert list(r) == list(range(10))
    assert r[0] == 0