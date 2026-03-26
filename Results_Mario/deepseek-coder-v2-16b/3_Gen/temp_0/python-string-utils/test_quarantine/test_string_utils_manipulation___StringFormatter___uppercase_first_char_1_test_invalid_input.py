
from string_utils.manipulation import __StringFormatter
import pytest
from custom_exceptions import InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        formatter = __StringFormatter(12345)
    assert str(excinfo.value) == '12345 is not a valid input, please provide a string.'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_char_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_char_1_test_invalid_input.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""