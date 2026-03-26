
import pytest
from pymonet.box import Box  # Assuming the module is named 'pymonet' and contains a 'box' submodule

def test_valid_input():
    box = Box(123)
    assert box.value == 123
    
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box, Box)
    assert mapped_box.value == "123"
