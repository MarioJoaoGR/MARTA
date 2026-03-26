
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Test that an instance of __StringFormatter can be created with a valid string input
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"

def test_invalid_input():
    # Test that creating an instance of __StringFormatter with an invalid type raises InvalidInputError
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___init___0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___0_test_valid_input.py:12:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)


"""