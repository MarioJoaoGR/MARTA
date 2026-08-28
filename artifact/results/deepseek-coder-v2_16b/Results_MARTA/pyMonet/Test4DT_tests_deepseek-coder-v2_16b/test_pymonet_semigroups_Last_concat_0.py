
import pytest
from pymonet.semigroups import Last



def test_edge_case_none():
    with pytest.raises(TypeError):
        Last()

def test_invalid_input():
    with pytest.raises(TypeError):
        Last(is_nothing=False)