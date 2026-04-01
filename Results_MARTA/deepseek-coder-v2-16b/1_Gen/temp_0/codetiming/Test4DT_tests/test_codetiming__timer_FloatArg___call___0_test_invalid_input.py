
import pytest
from codetiming._timer import FloatArg

def test_invalid_input():
    with pytest.raises(TypeError):
        instance = FloatArg()
        result = instance("not a float")  # This should raise a TypeError
