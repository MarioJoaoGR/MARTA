
import pytest
from string_utils.manipulation import camel_case_to_snake
from string_utils.exceptions import InvalidInputError

def test_invalid_input():
    # Test case for invalid input
    with pytest.raises(InvalidInputError):
        assert camel_case_to_snake("ThisIsACamelStringTest")  # This should raise an error because the function expects a string that is not in camel case format.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_camel_case_to_snake_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_1_test_invalid_input.py:4:0: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_1_test_invalid_input.py:4:0: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)


"""