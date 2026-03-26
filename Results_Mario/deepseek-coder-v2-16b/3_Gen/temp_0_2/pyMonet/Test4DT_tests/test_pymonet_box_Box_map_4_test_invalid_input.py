
import pytest
from pymonet.box import Box

def test_invalid_input():
    box = Box(123)
    with pytest.raises(TypeError):
        mapped_box = box.map("not a callable")
