
import pytest
from pymonet.semigroups import Semigroup

# Test valid input scenario
def test_valid_input():
    semigroup = Semigroup(5)
    result = semigroup.fold(lambda x: x + 1)
    assert result == 6, f"Expected fold to return 6 but got {result}"

# Test edge case with None as the initial value
def test_edge_case():
    semigroup = Semigroup(None)
    with pytest.raises(TypeError):
        semigroup.fold(lambda x: x + 1)

# Test invalid input by passing a non-callable object to fold method
def test_invalid_input():
    semigroup = Semigroup('hello')
    with pytest.raises(TypeError):
        semigroup.fold('not a callable')
