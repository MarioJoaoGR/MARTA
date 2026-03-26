
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy = Lazy("not_a_function")  # Providing a non-callable argument
        lazy.to_maybe()  # This should raise an error because the provided constructor_fn is not callable
