
import pytest
from string_utils.manipulation import __StringFormatter

def test_valid_input():
    # Test valid input
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

    # Test invalid input type, should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_0_test_valid_input.py:11:23: E0602: Undefined variable 'InvalidInputError' (undefined-variable)

"""