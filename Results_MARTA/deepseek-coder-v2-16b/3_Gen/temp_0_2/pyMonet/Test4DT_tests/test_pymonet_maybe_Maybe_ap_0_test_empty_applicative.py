
from pymonet.maybe import Maybe
import pytest

def test_empty_applicative():
    # Create an empty Maybe instance
    maybe_empty = Maybe(value=None, is_nothing=True)
    
    # Try to apply a function (which we will mock as another Maybe with a value)
    result = maybe_empty.ap(Maybe(value="test", is_nothing=False))
    
    # Check that the result is still an empty Maybe instance
    assert isinstance(result, Maybe)
    assert result.is_nothing
