
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    lazy = Lazy(lambda x: x)  # Valid constructor function, but we will not pass any arguments to trigger TypeError
    with pytest.raises(TypeError):
        lazy.to_either()  # This should raise a TypeError because get method requires at least one argument
