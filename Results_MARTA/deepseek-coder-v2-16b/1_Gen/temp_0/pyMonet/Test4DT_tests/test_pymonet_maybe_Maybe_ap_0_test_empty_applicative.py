
import pytest
from pymonet.maybe import Maybe

def test_empty_applicative():
    # Create an empty Maybe instance
    maybe_empty = Maybe(value=None, is_nothing=True)
    
    # Try to apply a function (which we mock as another Maybe with a value) to the empty Maybe
    result = maybe_empty.ap(Maybe(value="some_function", is_nothing=False))
    
    # Assert that the result is also an empty Maybe instance
    assert isinstance(result, Maybe)
    assert result.is_nothing
