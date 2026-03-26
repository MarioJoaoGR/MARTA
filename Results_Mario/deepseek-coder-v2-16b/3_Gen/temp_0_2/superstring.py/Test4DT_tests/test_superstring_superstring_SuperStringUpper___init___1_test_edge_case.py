
import pytest
from superstring.superstring import SuperStringUpper

def test_edge_case():
    instance = SuperStringUpper(None)
    assert instance._base is None
