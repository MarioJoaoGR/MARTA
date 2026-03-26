
import pytest
from pymonet.semigroups import Semigroup  # Assuming a hypothetical module 'pymonet' with a 'semigroups' submodule

def test_edge_case():
    s_none = Semigroup(None)
    s_empty_list = Semigroup([])
    
    assert s_none.value is None, "Expected value to be None"
    assert s_empty_list.value == [], "Expected value to be an empty list"
