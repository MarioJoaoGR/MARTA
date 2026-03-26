
import pytest
from pymonet.lazy import Lazy

def square(x):
    return x * x

class TestLazy:
    def test_edge_case_none(self):
        lazy = Lazy(square)
        with pytest.raises(TypeError):
            result = lazy.get(None)
