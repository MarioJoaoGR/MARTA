
import pytest
from pymonet.lazy import Lazy

def error_function():
    raise ValueError('Error')

def test_invalid_inputs():
    with pytest.raises(ValueError):
        lazy = Lazy(error_function)
        lazy.get()  # This should trigger the error in the constructor function
