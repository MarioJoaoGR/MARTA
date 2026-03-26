# Module: pymonet.either
# test_left.py
from pymonet.either import Left, Right

def test_left_initialization():
    left_value = Left("error message")
    assert isinstance(left_value, Left), "Expected an instance of Left"
    assert left_value.value == "error message", "Expected the value to be 'error message'"

def test_left_map():
    left_value = Left("error message")
    mapped_left = left_value.map(lambda x: str(x))
    assert isinstance(mapped_left, Left), "Mapping should return a new instance of Left"
    assert mapped_left.value == "error message", "Expected the value to remain unchanged after mapping"

def test_right_initialization():
    right_value = Right(42)
    assert isinstance(right_value, Right), "Expected an instance of Right"
    assert right_value.value == 42, "Expected the value to be 42"

def test_right_map():
    right_value = Right(42)
    mapped_right = right_value.map(lambda x: str(x))
    assert isinstance(mapped_right, Right), "Mapping should return a new instance of Right"
    assert mapped_right.value == "42", "Expected the value to be converted to string during mapping"
