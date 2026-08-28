
import pytest
from pymonet.semigroups import Semigroup

# Test valid input where a value is provided
def test_valid_input():
    semigroup = Semigroup(5)
    assert isinstance(semigroup, Semigroup), "Semigroup instance should be an instance of Semigroup"
    assert semigroup.value == 5, f"Expected value to be 5 but got {semigroup.value}"

# Test edge case where no input is provided (should raise TypeError)
def test_edge_case_none():
    with pytest.raises(TypeError):
        Semigroup()
