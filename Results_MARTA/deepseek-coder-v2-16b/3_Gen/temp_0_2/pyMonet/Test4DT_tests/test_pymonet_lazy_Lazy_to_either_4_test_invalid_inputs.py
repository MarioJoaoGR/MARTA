
import pytest
from pymonet.lazy import Lazy

def test_invalid_inputs():
    # Test with None as constructor function
    lazy = Lazy(None)
    with pytest.raises(TypeError):
        lazy.get()
    
    # Test with a non-callable object (e.g., string) as constructor function
    lazy = Lazy("not_a_function")
    with pytest.raises(TypeError):
        lazy.get()
