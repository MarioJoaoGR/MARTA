
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    lazy = Lazy(lambda x: x * x)
    with pytest.raises(TypeError):
        lazy.to_either('string')
