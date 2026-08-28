
import pytest
from unittest.mock import patch, MagicMock
from pymonet.maybe import Maybe

# Scenario 1: Test applying a function contained in another Maybe instance to a valid input.
def test_valid_input_applies_function():
    maybe_some = Maybe(value=lambda x: x + 1, is_nothing=False)
    applicative = Maybe(value=5, is_nothing=False)
    
    result = maybe_some.ap(applicative)
    assert not result.is_nothing
    assert result.value == 6

# Scenario 2: Test that an empty Maybe instance returns itself when attempting to apply a function.
def test_empty_applies_function():
    maybe_none = Maybe(value=None, is_nothing=True)
    applicative = Maybe(value=MagicMock(), is_nothing=False)
    
    result = maybe_none.ap(applicative)
    assert result.is_nothing

# Scenario 3: Test that the function raises an error when provided with invalid input types.
def test_invalid_input_raises_error():
    maybe_invalid = Maybe(value='not a function', is_nothing=False)
    applicative = Maybe(value=5, is_nothing=False)
    
    with pytest.raises(TypeError):
        result = maybe_invalid.ap(applicative)
