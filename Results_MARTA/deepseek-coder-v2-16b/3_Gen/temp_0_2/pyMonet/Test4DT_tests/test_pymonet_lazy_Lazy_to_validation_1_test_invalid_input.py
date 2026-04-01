
import pytest
from pymonet.lazy import Lazy

def test_invalid_input():
    with pytest.raises(TypeError):
        lazy = Lazy(lambda x: x)  # Valid constructor function
        lazy.to_validation()  # Should raise TypeError as it expects arguments
