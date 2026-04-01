
import pytest
from superstring.superstring import SuperStringUpper

def test_invalid_input():
    # Test when base is not provided
    with pytest.raises(TypeError) as excinfo:
        SuperStringUpper()
    assert "missing 1 required positional argument" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringUpper___init___2_test_invalid_input
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper___init___2_test_invalid_input.py:8:8: E1120: No value for argument 'base' in constructor call (no-value-for-parameter)


"""