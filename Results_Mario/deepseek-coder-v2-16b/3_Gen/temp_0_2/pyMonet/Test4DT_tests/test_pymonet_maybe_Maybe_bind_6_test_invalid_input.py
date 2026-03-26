
import pytest
from pymonet.maybe import Maybe

def test_invalid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    
    # Test when the mapper is not callable
    with pytest.raises(TypeError):
        result = maybe_some.bind("not a callable")
