
import pytest
from superstring.superstring import SuperString

def test_edge_case_none():
    s = SuperString(None)
    assert s._content is None
