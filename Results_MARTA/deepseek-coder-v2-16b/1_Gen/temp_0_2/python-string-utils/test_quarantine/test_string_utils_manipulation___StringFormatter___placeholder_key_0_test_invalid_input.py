
from python_string_utils.manipulation import __StringFormatter, InvalidInputError  # Assuming this is the correct import path
import pytest
from unittest.mock import patch
import uuid

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)  # Providing an invalid input type (int)
    
    assert str(exc_info.value) == "Expected a string but got int"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_invalid_input.py:2:0: E0401: Unable to import 'python_string_utils.manipulation' (import-error)


"""