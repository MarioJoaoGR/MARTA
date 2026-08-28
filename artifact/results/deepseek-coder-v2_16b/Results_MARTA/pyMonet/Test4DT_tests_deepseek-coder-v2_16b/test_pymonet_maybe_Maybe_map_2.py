
import pytest
from pymonet.maybe import Maybe

# Test valid input scenario
def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    assert not maybe_some.is_nothing
    assert maybe_some.value == 42

# Test edge case where input value is None and is_nothing should be set to True
def test_edge_case_none():
    maybe_none = Maybe(value=None, is_nothing=True)
    assert maybe_none.is_nothing
    with pytest.raises(AttributeError):
        print(maybe_none.value)  # This should raise an AttributeError because value should not be accessible when is_nothing is True

# Test invalid input where type of value does not match expected type T
def test_invalid_input():
    try:
        Maybe('not an acceptable type', is_nothing=False)
    except TypeError as e:
        assert str(e) == "Expected a value of type T, but got 'str'"
