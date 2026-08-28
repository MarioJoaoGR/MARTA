
import pytest
from pymonet.box import Box

def test_none_input():
    with pytest.raises(TypeError):
        Box()

def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_maybe()
