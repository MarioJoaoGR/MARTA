
from pymonet.either import Either, Left, Right

def test_invalid_input():
    try:
        either = Either()  # Attempting to create an instance without providing a value
    except TypeError as e:
        assert str(e) == "Either.__init__() missing 1 required positional argument: 'value'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_is_right_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_invalid_input.py:6:17: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""