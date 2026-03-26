
import pytest
from pymonet.box import Box

# Test cases for the Box class
def test_init():
    box = Box(123)
    assert box.value == 123

def test_str_init():
    box = Box("Hello, World!")
    assert box.value == "Hello, World!"

def test_map():
    box = Box(123)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box.value, str)
    assert mapped_box.value == "123"

def test_bind():
    box = Box(10)
    bound_value = box.bind(lambda x: x * 2)