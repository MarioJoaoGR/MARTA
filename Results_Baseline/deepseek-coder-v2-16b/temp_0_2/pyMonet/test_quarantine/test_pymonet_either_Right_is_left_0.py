
# Module: pymonet.either
# test_right.py
from pymonet.either import Right

def test_is_left():
    right_value = Right()
    assert not right_value.is_left(), "Expected is_left to return False"

def test_is_right():
    right_value = Right()
    assert right_value.is_right(), "Expected is_right to return True"

def test_map_method():
    right_value = Right(42)
    def double_value(x):
        return x * 2
    mapped_value = right_value.map(double_value)
    assert mapped_value.value == 84, "Expected the value to be doubled"

def test_bind_method():
    right_value = Right(42)
    def add_one(x):
        return x + 1
    bound_value = right_value.bind(add_one)
    assert isinstance(bound_value, Right), "Expected the result to be a Right instance"
    assert bound_value.value == 43, "Expected the value to be incremented by one"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Right_is_left_0
pyMonet/Test4DT_tests/test_pymonet_either_Right_is_left_0.py:7:18: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)
pyMonet/Test4DT_tests/test_pymonet_either_Right_is_left_0.py:11:18: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""