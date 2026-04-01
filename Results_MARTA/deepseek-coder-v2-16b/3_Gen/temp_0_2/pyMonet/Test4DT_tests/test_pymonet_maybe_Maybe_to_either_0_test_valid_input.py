
from pymonet.maybe import Maybe
from pymonet.either import Left, Right
import pytest

def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    maybe_none = Maybe(value=None, is_nothing=True)
    
    # Test when Maybe is not empty
    either_result_some = maybe_some.to_either()
    assert isinstance(either_result_some, Right)
    assert either_result_some.value == 42
    
    # Test when Maybe is empty
    either_result_none = maybe_none.to_either()
    assert isinstance(either_result_none, Left)
    assert either_result_none.value is None
