
import pytest
from pymonet.semigroups import Semigroup

# Test edge case where Semigroup is initialized without a value
def test_edge_case():
    semigroup_none = Semigroup(None)
    assert semigroup_none.value is None

# Test invalid input where an argument is missing
def test_invalid_input():
    with pytest.raises(TypeError):
        Semigroup()
