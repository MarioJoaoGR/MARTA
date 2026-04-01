
import pytest
from pymonet.semigroups import Semigroup

def test_edge_case():
    # Test with None
    semigroup_none = Semigroup(None)
    assert semigroup_none.fold(lambda x: x) is None
    
    # Test with empty list
    semigroup_empty_list = Semigroup([])
    assert semigroup_empty_list.fold(lambda x: sum(x)) == 0
