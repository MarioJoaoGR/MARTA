
# Module: pymonet.either
# test_right.py
from pymonet.either import Right

def test_is_left():
    right_value = Right(None)  # Adding None as a value argument for the constructor call
    assert not right_value.is_left(), "Expected is_left to return False"

def test_is_right():
    right_value = Right(None)  # Adding None as a value argument for the constructor call
    assert right_value.is_right(), "Expected is_right to return True"
