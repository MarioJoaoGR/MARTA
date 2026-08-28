
import pytest
from pymonet.box import Box

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Box()  # This should raise a TypeError because the constructor requires an argument
