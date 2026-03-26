
import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy = Lazy("not_a_callable")  # Providing a non-callable argument
        lazy.to_either()  # This should raise a TypeError because "not_a_callable" is not callable
