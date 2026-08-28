
# Module: pymonet.box
from pymonet.box import Box

def test_eq_same_type_and_value():
    box1 = Box(42)
    box2 = Box(42)
    assert box1 == box2, "Two boxes with the same integer value should be equal."

def test_eq_different_types():
    box_int = Box(42)
    box_str = Box("Hello")
    assert not (box_int == box_str), "Boxes with different types should not be equal."

def test_eq_same_type_different_value():
    box1 = Box(42)
    box2 = Box(50)
    assert not (box1 == box2), "Boxes with the same type but different values should not be equal."

def test_eq_none_type():
    box = Box(42)
    assert not (box == None), "A Box instance should not be considered equal to None."

def test_eq_other_object_type():
    box = Box(42)
    other_obj = {"value": 42}
    assert not (box == other_obj), "A Box instance should not be considered equal to an object of another type."
