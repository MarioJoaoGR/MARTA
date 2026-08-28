
import pytest
from pymonet.maybe import Maybe

# Test valid input where Maybe is not nothing and has a valid value
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test edge case where Maybe is nothing (is_nothing is True)
def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # This should raise an AttributeError because the value does not exist

# Test invalid input where the type of value does not match T (should raise TypeError)
def test_invalid_input():
    try:
        Maybe('not a valid type', False)
    except TypeError as e:
        assert str(e) == "Expected type 'T' but got <class 'str'>"
