
import pytest
from pymonet.box import Box

def test_valid_input():
    box = Box(123)
    assert box.value == 123

    text_box = Box("Hello, World!")
    assert text_box.value == "Hello, World!"
