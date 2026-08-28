
import pytest
from pymonet.maybe import Maybe

# Test valid input scenario
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test edge case with None value scenario
def test_edge_case():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    # Attempting to access the value should raise an AttributeError
    with pytest.raises(AttributeError):
        _ = maybe_none.value

# Test invalid input scenario
def test_invalid_input():
    try:
        Maybe('not a valid value', is_nothing=False)
    except TypeError as e:
        error = str(e)
        assert "expected type" in error  # Check if the error message contains expected content
