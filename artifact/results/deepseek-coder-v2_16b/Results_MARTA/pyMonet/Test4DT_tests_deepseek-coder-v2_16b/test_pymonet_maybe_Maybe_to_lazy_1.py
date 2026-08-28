
import pytest
from pymonet.maybe import Maybe

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test edge case where Maybe is empty (is_nothing is True)
def test_edge_case():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        assert maybe_none.value  # This should raise an AttributeError because the value shouldn't be accessible when is_nothing is True

# Test invalid input where Maybe is not instantiated correctly (should raise TypeError)
def test_invalid_input():
    with pytest.raises(TypeError):
        Maybe()  # Instantiating Maybe without arguments should raise a TypeError
