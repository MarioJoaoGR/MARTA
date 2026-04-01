
import pytest
from superstring.superstring import SuperStringLower

def test_edge_case_none():
    obj = SuperStringLower(None)
    assert obj._base is None
