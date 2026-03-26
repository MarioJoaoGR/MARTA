
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    lazy = Lazy('not_a_function')
    with pytest.raises(TypeError):
        lazy.to_validation()
