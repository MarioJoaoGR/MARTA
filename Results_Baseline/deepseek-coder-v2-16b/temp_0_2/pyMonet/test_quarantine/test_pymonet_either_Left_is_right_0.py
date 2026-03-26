
# Module: pymonet.either
# test_either.py
from pymonet.either import Left, Right

def test_left_instance():
    left_error = Left("error message")
    assert not left_error.is_right(), "Expected is_right to return False for a Left instance"
    mapped_left = left_error.map(lambda x: f"Error: {x}")
    assert mapped_left.value == "Error: error message", "Expected the map method to transform the contained value correctly"
    assert left_error.is_left(), "Expected is_left to return True for a Left instance"
    assert not left_error.is_right(), "Expected is_right to return False after checking is_left"

def test_right_instance():
    right_success = Right(42)
    assert not right_success.is_left(), "Expected is_left to return False for a Right instance"
    assert right_success.is_right(), "Expected is_right to return True for a Right instance"
    def double_value(x):
        return x * 2
    mapped_value = right_success.map(double_value)
    assert mapped_value.value == 84, "Expected the map method to transform the contained value correctly"
    def add_one(x):
        return x + 1
    bound_value = right_success.bind(add_one)
    assert bound_value.value == 43, "Expected the bind method to apply a function to the contained value"

def test_either_class():
    left_value = Either(Left("error message"))
    assert not left_value.is_right(), "Expected is_right to return False for an Either with Left instance"
    right_value = Either(Right(42))
    assert right_value.is_right(), "Expected is_right to return True for an Either with Right instance"
    def error_handler(value):
        return f"Error: {value}"
    def success_handler(value):
        return value * 2
    assert left_value.case(error_handler, success_handler) == "Error: error message", "Expected the case method to handle Left correctly"
    assert right_value.case(error_handler, success_handler) == 84, "Expected the case method to handle Right correctly"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Left_is_right_0
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_right_0.py:28:17: E0602: Undefined variable 'Either' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_either_Left_is_right_0.py:30:18: E0602: Undefined variable 'Either' (undefined-variable)


"""