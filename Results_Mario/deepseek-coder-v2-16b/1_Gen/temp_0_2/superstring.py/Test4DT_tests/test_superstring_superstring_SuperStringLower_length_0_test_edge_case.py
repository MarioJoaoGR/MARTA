
import pytest
from superstring.superstring import SuperStringBase, SuperStringLower

def test_edge_case():
    obj = SuperStringLower('')
    assert obj._base == ''
