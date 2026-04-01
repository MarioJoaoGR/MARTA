
import pytest
from pymonet.box import Box  # Assuming 'pymonet.box' is a valid module

def test_map():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box, Box)
    assert mapped_box.value == "123"

    box_str = Box("Hello, World!")
    mapped_box_str = box_str.map(lambda x: x.upper())
    assert isinstance(mapped_box_str, Box)
    assert mapped_box_str.value == "HELLO, WORLD!"
