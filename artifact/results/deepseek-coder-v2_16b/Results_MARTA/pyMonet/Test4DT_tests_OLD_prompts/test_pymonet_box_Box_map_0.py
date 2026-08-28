
import pytest
from pymonet.box import Box

def test_invalid_input():
    with pytest.raises(TypeError):
        # Attempt to create a Box instance without providing a value
        box = Box()
