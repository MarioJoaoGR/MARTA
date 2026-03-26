# Module: pymonet.box
# test_box.py
from pymonet.box import Box
import pytest

@pytest.fixture
def int_box():
    return Box(123)

@pytest.fixture
def str_box():
    return Box("Hello, World!")

def test_int_box_value(int_box):
    assert int_box.value == 123

def test_str_box_value(str_box):
    assert str_box.value == "Hello, World!"

def test_box_equality():
    box1 = Box(456)
    box2 = Box(456)
    assert box1 == box2

def test_box_inequality():
    box1 = Box(456)
    box2 = Box("Hello, World!")
    assert not (box1 == box2)
