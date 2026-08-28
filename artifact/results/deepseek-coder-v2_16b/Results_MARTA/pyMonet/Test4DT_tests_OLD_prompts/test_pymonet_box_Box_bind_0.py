
import pytest
from pymonet.box import Box

def test_invalid_input():
    with pytest.raises(TypeError):
        Box()  # This should raise a TypeError because the constructor expects an argument

def test_bind_function():
    box = Box(5)
    mapped_value = box.bind(lambda x: Box(x * 2))
    assert isinstance(mapped_value, Box), "Expected a Box instance"
    assert mapped_value.value == 10, "Expected the value to be doubled"

def test_bind_with_different_type():
    box = Box("Hello")
    mapped_value = box.bind(lambda x: Box(x + " World!"))
    assert isinstance(mapped_value, Box), "Expected a Box instance"
    assert mapped_value.value == "Hello World!", "Expected the string to be appended"
