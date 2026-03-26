
import pytest
from pymonet.semigroups import Semigroup

def test_edge_case():
    semigroup = Semigroup(None)
    
    with pytest.raises(TypeError):
        def add_one(x):
            return x + 1
        result = semigroup.fold(add_one)
