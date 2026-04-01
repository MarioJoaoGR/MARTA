
from unittest.mock import patch
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from string_utils.errors import is_string

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter("not a valid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter_format_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_1_test_invalid_input.py:5:0: E0611: No name 'is_string' in module 'string_utils.errors' (no-name-in-module)


"""