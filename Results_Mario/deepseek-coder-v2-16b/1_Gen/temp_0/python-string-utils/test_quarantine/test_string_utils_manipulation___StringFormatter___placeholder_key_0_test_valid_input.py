
from unittest.mock import patch
import pytest
from string_utils.formatter import __StringFormatter
from uuid import uuid4

def is_string(value):
    return isinstance(value, str)

class InvalidInputError(Exception):
    def __init__(self, value):
        self.message = f"Expected 'str', received '{type(value).__name__}'"
        super().__init__(self.message)

def test_valid_input():
    with patch('string_utils.formatter.__placeholder_key', return_value='$a1b2c3$'):
        formatter = __StringFormatter("valid string")
        assert formatter.input_string == "valid string"

def test_invalid_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(12345)
    assert str(excinfo.value) == "Expected 'str', received 'int'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py:4:0: E0401: Unable to import 'string_utils.formatter' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py:4:0: E0611: No name 'formatter' in module 'string_utils' (no-name-in-module)

"""