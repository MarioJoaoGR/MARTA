
import pytest
from superstring.superstring import SuperStringUpper

def test_edge_case_none():
    ssu = SuperStringUpper(None)
    assert ssu._base is None
