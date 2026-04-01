
import pytest
from string_utils.manipulation import asciify
from custom_exceptions import InvalidInputError

def test_invalid_input():
    # Test that a non-string input raises an InvalidInputError
    with pytest.raises(InvalidInputError):
        asciify(12345)  # Passing an integer to simulate invalid input

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_asciify_2_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_asciify_2_test_invalid_input.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""