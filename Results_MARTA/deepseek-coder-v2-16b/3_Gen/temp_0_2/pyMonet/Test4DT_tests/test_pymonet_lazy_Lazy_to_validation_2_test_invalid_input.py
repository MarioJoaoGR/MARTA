
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy = Lazy('not_a_function')
        lazy.to_validation()
