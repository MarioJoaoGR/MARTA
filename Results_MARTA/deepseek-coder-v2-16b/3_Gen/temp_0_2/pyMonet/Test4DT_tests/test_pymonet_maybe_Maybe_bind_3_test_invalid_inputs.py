
from pymonet.maybe import Maybe
import pytest

def test_invalid_inputs():
    # Test with a non-callable mapper function (should raise TypeError)
    maybe = Maybe(value=42, is_nothing=False)
    with pytest.raises(TypeError):
        maybe.bind("not a callable")  # This should fail because "not a callable" is not callable

    # Test with None as the mapper function (should raise TypeError)
    maybe = Maybe(value=42, is_nothing=False)
    with pytest.raises(TypeError):
        maybe.bind(None)  # This should fail because None is not a callable
