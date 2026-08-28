
import pytest
from unittest.mock import patch
from flutes.iterator import Range

def test_Range__get_idx_basic():
    r = Range(1, 11, 2)
    assert r._get_idx(0) == 1
    assert r._get_idx(1) == 3
    assert r._get_idx(2) == 5
    assert r._get_idx(3) == 7
    assert r._get_idx(4) == 9
