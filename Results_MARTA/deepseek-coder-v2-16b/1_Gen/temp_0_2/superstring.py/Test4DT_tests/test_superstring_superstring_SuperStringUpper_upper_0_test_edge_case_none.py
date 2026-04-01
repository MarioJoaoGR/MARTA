
import pytest
from superstring.superstring import SuperStringUpper

def test_edge_case_none():
    str_upper = SuperStringUpper(None)
    result = str_upper.upper()
    assert result._base is None
