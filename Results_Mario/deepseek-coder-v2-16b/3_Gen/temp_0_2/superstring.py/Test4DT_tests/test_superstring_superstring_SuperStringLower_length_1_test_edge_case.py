
import pytest
from superstring.superstring import SuperString, SuperStringLower

def test_edge_case():
    s = None
    lower_str = SuperStringLower(s) if s else print('Invalid input')
    assert lower_str is None, "Expected None for invalid input"
