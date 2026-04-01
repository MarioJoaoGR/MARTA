
import pytest
from pymonet.lazy import Lazy

def square(x):
    return x * x

class TestLazy:
    def test_invalid_input(self):
        lazy = Lazy(square)
        with pytest.raises(TypeError):
            result = lazy.get('string')
