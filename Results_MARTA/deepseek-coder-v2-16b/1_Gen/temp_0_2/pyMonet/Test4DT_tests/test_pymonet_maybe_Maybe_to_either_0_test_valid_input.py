
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_valid_input():
    maybe_with_value = Maybe(10, False)
    either = maybe_with_value.to_either()
    
    assert isinstance(either, Right)
    assert either.value == 10
