
import pytest
from pymonet.box import Box
from pymonet.either import Right

def test_valid_input():
    box = Box(42)
    either_box = box.to_either()
    assert isinstance(either_box, Right)
    assert either_box.value == 42

def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_either()
