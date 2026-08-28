
# Module: pymonet.box
from pymonet.box import Box

def test_create_box_with_integer():
    box = Box(42)  # Creates a Box object containing the integer value 42.
    assert box.value == 42, "Box should contain the integer value 42."

def test_create_box_with_string():
    box_str = Box("Hello, World!")  # Creates a Box object containing the string "Hello, World!".
    assert box_str.value == "Hello, World!", "Box should contain the string 'Hello, World!'."

def test_map_function_to_transform_value():
    def add_one(x):
        return x + 1
    
    box = Box(42)
    mapped_box = box.map(add_one)
    assert mapped_box.value == 43, "Mapping function should transform the value by adding one."

def test_bind_function_to_transform_value():
    def double_value(x):
        return x * 2
    
    box = Box(5)
    bound_box = box.bind(double_value)