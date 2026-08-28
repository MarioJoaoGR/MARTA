
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    assert maybe_none.to_either() == Left(None)

# Test invalid input error handling
def test_invalid_input_error_handling():
    with pytest.raises(TypeError):
        Maybe()  # This should raise a TypeError because the constructor requires two arguments: value and is_nothing
