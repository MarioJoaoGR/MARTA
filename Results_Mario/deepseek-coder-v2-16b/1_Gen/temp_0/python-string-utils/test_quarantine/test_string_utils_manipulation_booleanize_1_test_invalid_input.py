
import pytest
from string_utils.manipulation import booleanize
from string_utils.exceptions import InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        assert not booleanize("invalid input")
        assert not booleanize("")
        assert not booleanize("0")
        assert not booleanize("false")
        assert not booleanize("no")
        assert not booleanize("n")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation_booleanize_1_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_1_test_invalid_input.py:4:0: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_1_test_invalid_input.py:4:0: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)

"""