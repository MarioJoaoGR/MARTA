
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy = Lazy(lambda x: x + 1)
        lazy.to_maybe()  # This should raise TypeError because the lambda expects an argument but none is provided
