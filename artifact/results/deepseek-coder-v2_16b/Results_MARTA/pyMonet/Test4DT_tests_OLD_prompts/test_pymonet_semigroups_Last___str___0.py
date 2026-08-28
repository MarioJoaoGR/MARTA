
import pytest
from pymonet.semigroups import Last, Semigroup

# Test for valid case
def test_valid_case():
    last_monoid = Last(42)  # Provide a value to the constructor
    assert str(last_monoid) == 'Last[value=42]'

# Test for edge case
def test_edge_case():
    with pytest.raises(TypeError):
        last_monoid = Last()  # Missing required argument should raise TypeError

# Test for error case
def test_error_case():
    with pytest.raises(TypeError):
        last_monoid = Last()  # Missing required argument should raise TypeError
