
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_invalid_input():
    # Test when is_nothing is True
    maybe_none = Maybe(value=None, is_nothing=True)
    either_result = maybe_none.to_either()
    assert isinstance(either_result, Left)
    assert either_result.value is None

    # Test when is_nothing is False
    maybe_some = Maybe(value="Hello", is_nothing=False)
    either_result = maybe_some.to_either()
    assert isinstance(either_result, Right)
    assert either_result.value == "Hello"
