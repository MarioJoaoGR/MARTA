
import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

# Test for the basic functionality of to_either method in Maybe class
def test_Maybe_to_either_basic():
    # Create a Maybe instance with a value
    maybe_some = Maybe(value=42, is_nothing=False)
    
    # Call the to_either method and check if it returns the expected Right monad
    either_value = maybe_some.to_either()
    assert isinstance(either_value, Right)
    assert either_value.value == 42

    # Create a Maybe instance representing nothing
    maybe_none = Maybe(value=None, is_nothing=True)
    
    # Call the to_either method and check if it returns the expected Left monad
    either_value = maybe_none.to_either()
    assert isinstance(either_value, Left)
    assert either_value.value is None
