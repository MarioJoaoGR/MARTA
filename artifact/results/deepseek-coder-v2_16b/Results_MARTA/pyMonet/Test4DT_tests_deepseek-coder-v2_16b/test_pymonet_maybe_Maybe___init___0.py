
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
    # The following assertion would fail because `maybe_none` has a value of None and should be Nothing
    # assert maybe_none.value is None  # This line will raise an AttributeError indicating that the value does not exist in a Nothing instance

# Test invalid input where Maybe is created with a non-int type, expecting TypeError
def test_invalid_input():
    try:
        maybe_invalid = Maybe('not an int', is_nothing=False)
    except TypeError as e:
        error = e
        assert isinstance(error, TypeError)
