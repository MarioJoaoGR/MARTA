
from superstring.superstring import SuperStringConcatenation

def test_invalid_input():
    try:
        ssc = SuperStringConcatenation()
    except TypeError as e:
        assert str(e) == "__init__() missing 2 required positional arguments: 'left' and 'right'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation___init___0_test_invalid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation___init___0_test_invalid_input.py:6:14: E1120: No value for argument 'left' in constructor call (no-value-for-parameter)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation___init___0_test_invalid_input.py:6:14: E1120: No value for argument 'right' in constructor call (no-value-for-parameter)


"""