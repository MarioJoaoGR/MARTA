
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    lazy = Lazy(lambda x: x)  # Valid constructor function to avoid immediate evaluation
    with pytest.raises(TypeError):
        lazy.to_box()  # Calling to_box without arguments should raise a TypeError
