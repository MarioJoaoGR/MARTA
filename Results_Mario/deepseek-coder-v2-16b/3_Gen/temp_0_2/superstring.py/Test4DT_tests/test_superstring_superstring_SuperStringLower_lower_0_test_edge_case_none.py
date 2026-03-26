
import pytest
from superstring.superstring import SuperStringLower

def test_edge_case_none():
    s = SuperStringLower(None)
    result = s.lower()
    assert result._base is None, "Expected _base to be None after calling lower()"
