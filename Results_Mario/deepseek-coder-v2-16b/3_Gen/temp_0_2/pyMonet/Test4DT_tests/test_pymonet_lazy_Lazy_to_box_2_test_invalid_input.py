
import pytest
from pymonet.lazy import Lazy

def square(x):
    return x * x

# Test with invalid input type to check error handling
@pytest.mark.parametrize("invalid_input", [None, "string", [], {}])
def test_invalid_input(invalid_input):
    lazy = Lazy(square)
    with pytest.raises(TypeError):
        lazy.get(invalid_input)
